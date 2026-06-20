/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   routine.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 12:22:27 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/06/20 22:19:20 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	try_acquire_dongle(t_dongle *dongle, int coder_id, 
                                    long deadline, char *scheduler)
{
    t_request	*req;

    pthread_mutex_lock(&dongle->mutex);
    
    // Chequear cooldown
    if (get_time_ms() < dongle->cooldown_until)
    {
        pthread_mutex_unlock(&dongle->mutex);
        return (0);
    }
    
    if (ft_strcmp(scheduler, "fifo") == 0)
    {
        // FIFO: el mutex se encarga de serializar
        return (1);  // ← Mantener mutex bloqueado
    }
    else  // EDF
    {
        // Encolar siempre
        req = dongle->waitlist.head;
        while (req && req->coder_id != coder_id)
            req = req->next;
        if (!req)
        {
            req = create_request(coder_id, deadline);
            enqueue_request(&dongle->waitlist, req);
        }
        else
        {
            // Remover y re-encolar
            t_request *prev = dongle->waitlist.head;
            if (prev == req)
                dongle->waitlist.head = req->next;
            else
            {
                while (prev->next != req)
                    prev = prev->next;
                prev->next = req->next;
            }
            req->deadline = deadline;
            req->next = NULL;
            enqueue_request(&dongle->waitlist, req);
        }
        
        // Solo si somos primero
        if (dongle->waitlist.head->coder_id == coder_id)
        {
            dequeue_request(&dongle->waitlist);
            return (1);  // ← Mantener mutex bloqueado
        }
    }
    
    pthread_mutex_unlock(&dongle->mutex);
    return (0);
}

static void	compile(t_coder *coder)
{
    long	deadline;

    deadline = coder->last_compile + coder->data->time_to_burnout;
    if (coder->id % 2 == 0)
    {
        while (!try_acquire_dongle(coder->right, coder->id, deadline,
                                    coder->data->scheduler) 
            && !simulation_stopped(coder->data))
            ft_usleep(1);
        if (simulation_stopped(coder->data))
            return ;
        print_status(coder, "has taken a dongle");
        
        while (!try_acquire_dongle(coder->left, coder->id, deadline,
                                    coder->data->scheduler)
            && !simulation_stopped(coder->data))
            ft_usleep(1);
        if (simulation_stopped(coder->data))
        {
            pthread_mutex_unlock(&coder->right->mutex);
            return ;
        }
        print_status(coder, "has taken a dongle");
    }
    else
    {
        while (!try_acquire_dongle(coder->left, coder->id, deadline,
                                    coder->data->scheduler)
            && !simulation_stopped(coder->data))
            ft_usleep(1);
        if (simulation_stopped(coder->data))
            return ;
        print_status(coder, "has taken a dongle");
        
        while (!try_acquire_dongle(coder->right, coder->id, deadline,
                                    coder->data->scheduler)
            && !simulation_stopped(coder->data))
            ft_usleep(1);
        if (simulation_stopped(coder->data))
        {
            pthread_mutex_unlock(&coder->left->mutex);
            return ;
        }
        print_status(coder, "has taken a dongle");
    }
    coder->last_compile = get_time_ms();
    print_status(coder, "is compiling");
    ft_usleep(coder->data->time_to_compile);
    coder->compile_count++;
    coder->left->cooldown_until = get_time_ms() + coder->data->dongle_cooldown;
    pthread_mutex_unlock(&coder->left->mutex);
    coder->right->cooldown_until = get_time_ms() + coder->data->dongle_cooldown;
    pthread_mutex_unlock(&coder->right->mutex);
}

void	*coder_routine(void *arg)
{
	t_coder	*coder;

	coder = (t_coder *)arg;
	coder->last_compile = get_time_ms();
	while (!simulation_stopped(coder->data))
	{
		compile(coder);
		if (simulation_stopped(coder->data))
			break ;
		print_status(coder, "is debugging");
		ft_usleep(coder->data->time_to_debug);
		if (simulation_stopped(coder->data))
			break ;
		print_status(coder, "is refactoring");
		ft_usleep(coder->data->time_to_refactor);
	}
	return (NULL);
}
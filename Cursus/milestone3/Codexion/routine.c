/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   routine_new.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 12:22:27 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/06/25 18:13:39 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	can_acquire_dongle(t_dongle *dongle, int coder_id, char *scheduler)
{
	t_request	*head;

	if (get_time_ms() < dongle->cooldown_until)
		return (0);
	
	if (ft_strcmp(scheduler, "fifo") == 0)
		return (1);
	else
	{
		head = dongle->waitlist.head;
		if (!head || head->coder_id == coder_id)
			return (1);
	}
	return (0);
}

static void	add_to_queue_edf(t_dongle *dongle, int coder_id, long deadline)
{
	t_request	*req;

	req = dongle->waitlist.head;
	while (req && req->coder_id != coder_id)
		req = req->next;
	if (!req)
	{
		req = create_request(coder_id, deadline);
		enqueue_request(&dongle->waitlist, req);
	}
	else
		req->deadline = deadline;
}

static int	try_acquire_dongle(t_dongle *dongle, int coder_id, 
								long deadline, char *scheduler)
{
	int	acquired;

	acquired = 0;
	pthread_mutex_lock(&dongle->mutex);
	if (ft_strcmp(scheduler, "edf") == 0)
		add_to_queue_edf(dongle, coder_id, deadline);
	
	if (can_acquire_dongle(dongle, coder_id, scheduler))
	{
		if (ft_strcmp(scheduler, "edf") == 0)
			dequeue_request(&dongle->waitlist);
		acquired = 1;
	}
	
	if (!acquired)
		pthread_mutex_unlock(&dongle->mutex);
	return (acquired);
}

static void	release_dongle(t_dongle *dongle)
{
	dongle->cooldown_until = get_time_ms() + 50;
	pthread_mutex_unlock(&dongle->mutex);
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
			release_dongle(coder->right);
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
			release_dongle(coder->left);
			return ;
		}
		print_status(coder, "has taken a dongle");
	}
	
	coder->last_compile = get_time_ms();
	print_status(coder, "is compiling");
	ft_usleep(coder->data->time_to_compile);
	coder->compile_count++;
	
	release_dongle(coder->left);
	release_dongle(coder->right);
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

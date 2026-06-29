/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   routine.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 12:22:27 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/06/26 16:45:27 by pmarcos-         ###   ########.fr       */
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
			free(dequeue_request(&dongle->waitlist));
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
	int		left_acquired;
	int		right_acquired;

	deadline = coder->last_compile + coder->data->time_to_burnout;
	left_acquired = 0;
	right_acquired = 0;
	if (coder->data->num_coders == 1)
	{
		while (!try_acquire_dongle(coder->left, coder->id, deadline,
				coder->data->scheduler)
			&& !simulation_stopped(coder->data))
			ft_usleep(1);
		if (simulation_stopped(coder->data))
			return ;
		pthread_mutex_lock(&coder->mutex);
		coder->last_compile = get_time_ms();
		pthread_mutex_unlock(&coder->mutex);
		print_status(coder, "\033[32mhas taken a dongle\033[0m");
		left_acquired = 1;
		print_status(coder, "\033[33mis compiling\033[0m");
		ft_usleep(coder->data->time_to_compile);
		pthread_mutex_lock(&coder->mutex);
		coder->compile_count++;
		pthread_mutex_unlock(&coder->mutex);
		if (left_acquired)
			release_dongle(coder->left);
		return ;
	}
	if (coder->id % 2 == 0)
	{
		while (!try_acquire_dongle(coder->right, coder->id, deadline,
				coder->data->scheduler)
			&& !simulation_stopped(coder->data))
			ft_usleep(1);
		if (simulation_stopped(coder->data))
			return ;
		right_acquired = 1;
		print_status(coder, "\033[32mhas taken a dongle\033[0m");
		while (!try_acquire_dongle(coder->left, coder->id, deadline,
				coder->data->scheduler)
			&& !simulation_stopped(coder->data))
			ft_usleep(1);
		if (simulation_stopped(coder->data))
		{
			if (right_acquired)
				release_dongle(coder->right);
			return ;
		}
		left_acquired = 1;
		print_status(coder, "\033[32mhas taken a dongle\033[0m");
	}
	else
	{
		while (!try_acquire_dongle(coder->left, coder->id, deadline,
				coder->data->scheduler)
			&& !simulation_stopped(coder->data))
			ft_usleep(1);
		if (simulation_stopped(coder->data))
			return ;
		left_acquired = 1;
		print_status(coder, "\033[32mhas taken a dongle\033[0m");
		while (!try_acquire_dongle(coder->right, coder->id, deadline,
				coder->data->scheduler)
			&& !simulation_stopped(coder->data))
			ft_usleep(1);
		if (simulation_stopped(coder->data))
		{
			if (left_acquired)
				release_dongle(coder->left);
			return ;
		}
		right_acquired = 1;
		print_status(coder, "\033[32mhas taken a dongle\033[0m");
	}
	pthread_mutex_lock(&coder->mutex);
	coder->last_compile = get_time_ms();
	pthread_mutex_unlock(&coder->mutex);
	print_status(coder, "\033[33mis compiling\033[0m");
	ft_usleep(coder->data->time_to_compile);
	pthread_mutex_lock(&coder->mutex);
	coder->compile_count++;
	pthread_mutex_unlock(&coder->mutex);
	if (left_acquired)
		release_dongle(coder->left);
	if (right_acquired)
		release_dongle(coder->right);
}

void	*coder_routine(void *arg)
{
	t_coder	*coder;

	coder = (t_coder *)arg;
	pthread_mutex_lock(&coder->mutex);
	coder->last_compile = get_time_ms();
	pthread_mutex_unlock(&coder->mutex);
	while (!simulation_stopped(coder->data))
	{
		compile(coder);
		if (simulation_stopped(coder->data))
			break ;
		print_status(coder, "\033[34mis debugging\033[0m");
		ft_usleep(coder->data->time_to_debug);
		if (simulation_stopped(coder->data))
			break ;
		print_status(coder, "\033[35mis refactoring\033[0m");
		ft_usleep(coder->data->time_to_refactor);
	}
	return (NULL);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   routine.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 12:22:27 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/07/07 21:20:37 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	do_compile(t_coder *coder)
{
	pthread_mutex_lock(&coder->mutex);
	coder->last_compile = get_time_ms();
	pthread_mutex_unlock(&coder->mutex);
	print_status(coder, "\033[33mis compiling\033[0m");
	ft_usleep(coder->data->time_to_compile);
	pthread_mutex_lock(&coder->mutex);
	coder->compile_count++;
	pthread_mutex_unlock(&coder->mutex);
}

static void	compile(t_coder *coder)
{
	long		deadline;
	long		cooldown;
	t_dongle	*first;
	t_dongle	*second;

	deadline = coder->last_compile + coder->data->time_to_burnout;
	cooldown = coder->data->dongle_cooldown;
	if (coder->data->num_coders == 1)
	{
		if (!acquire_dongle(coder, coder->left, deadline))
			return ;
		do_compile(coder);
		release_dongle(coder->left, cooldown);
		return ;
	}
	if (coder->id % 2 == 0)
	{
		first = coder->right;
		second = coder->left;
	}
	else
	{
		first = coder->left;
		second = coder->right;
	}
	if (!acquire_dongle(coder, first, deadline))
		return ;
	if (!acquire_dongle(coder, second, deadline))
	{
		release_dongle(first, cooldown);
		return ;
	}
	do_compile(coder);
	release_dongle(first, cooldown);
	release_dongle(second, cooldown);
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

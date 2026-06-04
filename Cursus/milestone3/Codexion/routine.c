/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   routine.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 12:22:27 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/06/04 14:41:38 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	compile(t_coder *coder)
{
	if (coder -> id % 2 == 0)
	{
		pthread_mutex_lock(&coder -> right -> mutex);
		print_status(coder, "\33[94mhas taken a dongle\33[0m");
		pthread_mutex_lock(&coder -> left -> mutex);
		print_status(coder, "\33[94mhas taken a dongle\33[0m");
	}
	else
	{
		pthread_mutex_lock(&coder -> left -> mutex);
		print_status(coder, "\33[94mhas taken a dongle\33[0m");
		pthread_mutex_lock(&coder -> right -> mutex);
		print_status(coder, "\33[94mhas taken a dongle\33[0m");
	}
	coder -> last_compile = get_time_ms();
	print_status(coder, "\33[92mis compiling\33[0m");
	ft_usleep(coder -> data -> time_to_compile);
	coder -> compile_count++;
	pthread_mutex_unlock(&coder -> left -> mutex);
	pthread_mutex_unlock(&coder -> right -> mutex);
}

void	*coder_routine(void *arg)
{
	t_coder	*coder;

	coder = (t_coder *)arg;
	while (!simulation_stopped(coder->data))
	{
		compile(coder);

		if (simulation_stopped(coder->data))
			break ;

		print_status(coder, "\033[35mis debugging\33[0m");
		ft_usleep(coder->data->time_to_debug);

		if (simulation_stopped(coder->data))
			break ;

		print_status(coder, "\33[33mis refactoring\33[0m");
		ft_usleep(coder->data->time_to_refactor);
	}
	return (NULL);
}

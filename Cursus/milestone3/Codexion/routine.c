/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   routine.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 12:22:27 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/06/01 19:51:04 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	compile(t_coder *coder)
{
	if (coder -> id % 2 == 0)
	{
		pthread_mutex_lock(&coder -> right -> mutex);
		print_status(coder, "has taken a dongle");
		pthread_mutex_lock(&coder -> left -> mutex);
		print_status(coder, "has taken a dongle");
	}
	else
	{
		pthread_mutex_lock(&coder -> left -> mutex);
		print_status(coder, "has taken a dongle");
		pthread_mutex_lock(&coder -> right -> mutex);
		print_status(coder, "has taken a dongle");
	}
	coder -> last_compile = get_time_ms();
	print_status(coder, "is compiling");
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

		print_status(coder, "is debugging");
		ft_usleep(coder->data->time_to_debug);

		if (simulation_stopped(coder->data))
			break ;

		print_status(coder, "is refactoring");
		ft_usleep(coder->data->time_to_refactor);
	}
	return (NULL);
}

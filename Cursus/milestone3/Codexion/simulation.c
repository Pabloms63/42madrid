/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simulation.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 12:05:59 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/08/03 14:49:00 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	simulation_stopped(t_data *data)
{
	int	stop;

	pthread_mutex_lock(&data -> stop_mutex);
	stop = data -> stop;
	pthread_mutex_unlock(&data -> stop_mutex);
	return (stop);
}

void	stop_simulation(t_data *data)
{
	int	i;

	pthread_mutex_lock(&data -> stop_mutex);
	data -> stop = 1;
	pthread_mutex_unlock(&data -> stop_mutex);
	i = 0;
	while (i < data -> num_coders)
	{
		pthread_mutex_lock(&data -> dongles[i].mutex);
		pthread_cond_broadcast(&data -> dongles[i].cond);
		pthread_mutex_unlock(&data -> dongles[i].mutex);
		i++;
	}
}

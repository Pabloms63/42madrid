/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simulation.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 12:05:59 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/07/09 21:02:44 by pmarcos-         ###   ########.fr       */
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
	pthread_mutex_lock(&data -> stop_mutex);
	data -> stop = 1;
	pthread_mutex_unlock(&data -> stop_mutex);
}
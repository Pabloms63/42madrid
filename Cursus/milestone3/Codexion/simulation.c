/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simulation.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 12:05:59 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/05/25 12:08:42 by pmarcos-         ###   ########.fr       */
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

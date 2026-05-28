/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   monitor.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 13:08:52 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/05/28 14:12:37 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	all_finished(t_data *data)
{
	int	i;

	i = 0;
	while (i < data -> num_coders)
	{
		if (data -> coders[i].compile_count
			< data -> required_compiles)
			return (0);

		i++;
	}
	return (1);
}

void	*monitor_routine(void *arg)
{
	t_data	*data;
	int		i;

	data = (t_data *)arg;
	while (1)
	{
		i = 0;
		while (i < data -> num_coders)
		{
			if (get_time_ms() - data -> coders[i].last_compile
				> data -> time_to_burnout)
			{
				pthread_mutex_lock(&data -> stop_mutex);
				data -> stop = 1;
				pthread_mutex_unlock(&data -> stop_mutex);
				pthread_mutex_lock(&data -> log_mutex);
				printf("%ld %d burned out\n",
					get_time_ms() - data -> start_time,
					data -> coders[i].id);
				pthread_mutex_unlock(&data -> log_mutex);
				return (NULL);
			}
			i++;
		}
		if (all_finished(data))
		{
			pthread_mutex_lock(&data -> stop_mutex);
			data -> stop = 1;
			pthread_mutex_unlock(&data -> stop_mutex);
			return (NULL);
		}
		usleep(1000);
	}
	return (NULL);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   monitor.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 13:08:52 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/06/01 20:00:56 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	all_finished(t_data *data)
{
	int	i;

	i = 0;
	while (i < data->num_coders)
	{
		printf("Coder %d -> %d/%d\n",
			data->coders[i].id,
			data->coders[i].compile_count,
			data->required_compiles);

		if (data->coders[i].compile_count
			< data->required_compiles)
			return (0);
		i++;
	}
	printf("ALL FINISHED\n");
	return (1);
}

static void	stop_simulation(t_data *data)
{
	pthread_mutex_lock(&data -> stop_mutex);
	data -> stop = 1;
	pthread_mutex_unlock(&data -> stop_mutex);
}

void	*monitor_routine(void *arg)
{
	t_data	*data;
	int		i;

	data = (t_data *)arg;
	while (!simulation_stopped(data))
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
			stop_simulation(data);
			return (NULL);
		}
		usleep(1000);
	}
	return (NULL);
}

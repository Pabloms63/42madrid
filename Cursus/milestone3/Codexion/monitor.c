/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   monitor.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 13:08:52 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/06/26 16:29:57 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	all_finished(t_data *data)
{
	int	i;

	i = 0;
	while (i < data->num_coders)
	{
		if (data->coders[i].compile_count
			< data->required_compiles)
			return (0);
		i++;
	}
	usleep(1000);
	printf("\n\33[92mALL FINISHED\33[0m\n");
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
			pthread_mutex_lock(&data->coders[i].mutex);
			if (get_time_ms() - data -> coders[i].last_compile
				> data -> time_to_burnout)
			{
				pthread_mutex_unlock(&data->coders[i].mutex);
				pthread_mutex_lock(&data -> stop_mutex);
				data -> stop = 1;
				pthread_mutex_unlock(&data -> stop_mutex);
				pthread_mutex_lock(&data -> log_mutex);
				printf("%ld %d \033[31mburned out\033[0m\n",
					get_time_ms() - data -> start_time,
					data -> coders[i].id);
				pthread_mutex_unlock(&data -> log_mutex);
				return (NULL);
			}
			pthread_mutex_unlock(&data->coders[i].mutex);
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

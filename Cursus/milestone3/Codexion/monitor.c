/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   monitor.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 13:08:52 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/07/23 17:41:26 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	all_finished(t_data *data)
{
	int	i;
	int	count;

	i = 0;
	while (i < data->num_coders)
	{
		pthread_mutex_lock(&data->coders[i].mutex);
		count = data->coders[i].compile_count;
		pthread_mutex_unlock(&data->coders[i].mutex);
		if (count < data->required_compiles)
			return (0);
		i++;
	}
	usleep(1000);
	pthread_mutex_lock(&data->log_mutex);
	printf("\n\33[92mALL FINISHED\33[0m\n");
	pthread_mutex_unlock(&data->log_mutex);
	return (1);
}

static int	check_burnout(t_data *data, int i)
{
	pthread_mutex_lock(&data->coders[i].mutex);
	if (get_time_ms() - data -> coders[i].last_compile
		<= data -> time_to_burnout)
	{
		pthread_mutex_unlock(&data->coders[i].mutex);
		return (0);
	}
	pthread_mutex_unlock(&data->coders[i].mutex);
	pthread_mutex_lock(&data -> stop_mutex);
	data -> stop = 1;
	pthread_mutex_unlock(&data -> stop_mutex);
	pthread_mutex_lock(&data -> log_mutex);
	printf("%ld %d \033[31mburned out\033[0m\n",
		get_time_ms() - data -> start_time,
		data -> coders[i].id);
	pthread_mutex_unlock(&data -> log_mutex);
	return (1);
}

static int	check_all_coders(t_data *data)
{
	int	i;

	i = 0;
	while (i < data -> num_coders)
	{
		if (check_burnout(data, i))
			return (1);
		i++;
	}
	return (0);
}

void	*monitor_routine(void *arg)
{
	t_data	*data;

	data = (t_data *)arg;
	while (!simulation_stopped(data))
	{
		if (check_all_coders(data))
			return (NULL);
		if (all_finished(data))
		{
			stop_simulation(data);
			return (NULL);
		}
		usleep(1000);
	}
	return (NULL);
}

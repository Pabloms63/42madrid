/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 11:12:37 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/08/03 16:04:21 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	destroy_coders(t_data *data, int count)
{
	int	i;

	i = 0;
	while (i < count)
	{
		free_queue(&data->dongles[i].waitlist);
		pthread_cond_destroy(&data->dongles[i].cond);
		pthread_mutex_destroy(&data->dongles[i].mutex);
		pthread_mutex_destroy(&data->coders[i].mutex);
		i++;
	}
	pthread_mutex_destroy(&data->stop_mutex);
	pthread_mutex_destroy(&data->log_mutex);
	free(data->dongles);
	free(data->coders);
}

static void	init_one_coder(t_data *data, int i)
{
	data -> dongles[i].cooldown_until = 0;
	data -> dongles[i].available = 1;
	pthread_mutex_init(&data -> coders[i].mutex, NULL);
	data -> coders[i].id = i + 1;
	data -> coders[i].left = &data -> dongles[i];
	data -> coders[i].right
		= &data -> dongles[(i + 1) % data -> num_coders];
	data -> coders[i].last_compile = get_time_ms();
	data -> coders[i].compile_count = 0;
	data -> coders[i].data = data;
}

static int	alloc_arrays(t_data *data)
{
	data -> dongles = malloc(sizeof(t_dongle) * data -> num_coders);
	data -> coders = malloc(sizeof(t_coder) * data -> num_coders);
	if (!data -> dongles || !data -> coders)
	{
		free(data -> dongles);
		free(data -> coders);
		return (1);
	}
	return (0);
}

int	init_data(t_data *data)
{
	int	i;

	if (alloc_arrays(data))
		return (1);
	pthread_mutex_init(&data -> stop_mutex, NULL);
	pthread_mutex_init(&data -> log_mutex, NULL);
	i = 0;
	while (i < data -> num_coders)
	{
		pthread_mutex_init(&data -> dongles[i].mutex, NULL);
		pthread_cond_init(&data -> dongles[i].cond, NULL);
		if (queue_init(&data -> dongles[i].waitlist))
		{
			pthread_cond_destroy(&data -> dongles[i].cond);
			pthread_mutex_destroy(&data -> dongles[i].mutex);
			destroy_coders(data, i);
			return (1);
		}
		init_one_coder(data, i);
		i++;
	}
	return (0);
}

void	cleanup_data(t_data *data)
{
	destroy_coders(data, data -> num_coders);
}

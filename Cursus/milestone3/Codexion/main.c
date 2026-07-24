/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 14:12:19 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/07/23 17:42:17 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	init_threads(t_data *data, int *created)
{
	int	i;

	i = 0;
	while (i < data -> num_coders)
	{
		if (pthread_create(
				&data -> coders[i].thread,
				NULL,
				coder_routine,
				&data -> coders[i]))
		{
			*created = i;
			return (1);
		}
		i++;
	}
	*created = data -> num_coders;
	return (0);
}

static void	join_coders(t_data *data, int count)
{
	int	i;

	i = 0;
	while (i < count)
	{
		pthread_join(data -> coders[i].thread, NULL);
		i++;
	}
}

static int	start_coders(t_data *data)
{
	int	created;

	if (init_threads(data, &created))
	{
		printf("Error: coder thread creation failed\n");
		stop_simulation(data);
		join_coders(data, created);
		cleanup_data(data);
		return (1);
	}
	return (0);
}

static int	start_monitor(t_data *data)
{
	if (pthread_create(&data -> monitor, NULL, monitor_routine, data))
	{
		printf("Error: monitor thread creation failed\n");
		stop_simulation(data);
		join_coders(data, data -> num_coders);
		cleanup_data(data);
		return (1);
	}
	return (0);
}

int	main(int ac, char **av)
{
	t_data	data;

	if (ac != 9)
	{
		printf("Invalid arguments\n");
		return (1);
	}
	if (parse_args(&data, av))
	{
		printf("Error: invalid input\n");
		return (1);
	}
	if (init_data(&data))
	{
		printf("Init failed\n");
		cleanup_data(&data);
		return (1);
	}
	data.start_time = get_time_ms();
	if (start_coders(&data) || start_monitor(&data))
		return (1);
	join_coders(&data, data.num_coders);
	pthread_join(data.monitor, NULL);
	cleanup_data(&data);
	return (0);
}

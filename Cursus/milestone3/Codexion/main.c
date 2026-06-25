/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 14:12:19 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/06/25 18:29:38 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	main(int ac, char **av)
{
	t_data	data;
	int		i;

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
		return (1);
	}
	data.start_time = get_time_ms();
	if (init_threads(&data))
		return (1);
	pthread_create(&data.monitor,
		NULL,
		monitor_routine,
		&data);
	i = 0;
	while (i < data.num_coders)
	{
		pthread_join(data.coders[i].thread, NULL);
		i++;
	}
	pthread_join(data.monitor, NULL);
	cleanup_data(&data);
	return (0);
}

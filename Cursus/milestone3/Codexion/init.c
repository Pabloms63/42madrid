/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 11:12:37 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/06/20 22:21:05 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	init_data(t_data *data)
{
	int	i;

	data -> dongles = malloc(sizeof(t_dongle) * data -> num_coders);
	data -> coders = malloc(sizeof(t_coder) * data -> num_coders);
	if (!data -> dongles || !data -> coders)
		return (1);
	pthread_mutex_init(&data -> stop_mutex, NULL);
	pthread_mutex_init(&data -> log_mutex, NULL);
	i = 0;
	while (i < data -> num_coders)
	{
		pthread_mutex_init(&data -> dongles[i].mutex, NULL);
		data -> dongles[i].waitlist.head = NULL;
		data -> dongles[i].cooldown_until = 0;
		data -> coders[i].id = i + 1;
		data -> coders[i].left = &data -> dongles[i];
		data -> coders[i].right
			= &data -> dongles[(i + 1) % data -> num_coders];
		data -> coders[i].last_compile = get_time_ms();
		data -> coders[i].compile_count = 0;
		data -> coders[i].data = data;
		i++;
	}
	return (0);
}

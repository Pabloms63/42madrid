/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   threads.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 12:30:52 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/05/25 12:50:36 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	init_threads(t_data *data)
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
			return (1);
		i++;
	}
	return (0);
}


/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/24 18:09:53 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/05/25 11:13:07 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	validate_args(char **av)
{
	int	i;

	i = 1;
	while (i <= 7)
	{
		if (!is_number(av[i]))
			return (1);
		i++;
	}
	if (ft_strcmp(av[8], "fifo") != 0 && ft_strcmp(av[8], "edf") != 0)
		return (1);
	return (0);
}

int	parse_args(t_data *data, char **av)
{
	if (validate_args(av))
		return (1);
	data -> num_coders = ft_atol(av[1]);
	data -> time_to_burnout = ft_atol(av[2]);
	data -> time_to_compile = ft_atol(av[3]);
	data -> time_to_debug = ft_atol(av[4]);
	data -> time_to_refactor = ft_atol(av[5]);
	data -> required_compiles = ft_atol(av[6]);
	data -> dongle_cooldown = ft_atol(av[7]);
	data -> stop = 0;
	if (data -> num_coders <= 0
		|| data -> time_to_burnout <= 0
		|| data -> time_to_compile <= 0
		|| data -> time_to_debug <= 0
		|| data -> time_to_refactor <= 0
		|| data -> required_compiles <= 0
		|| data -> dongle_cooldown <= 0)
		return (1);
	return (0);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 14:12:19 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/05/24 20:52:40 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	main(int ac, char **av)
{
	t_data	data;

	printf("%ld\n", get_time_ms());
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
	return (0);
}

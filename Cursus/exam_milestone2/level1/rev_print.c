/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rev_print.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 01:01:52 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/22 01:16:32 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "unistd.h"

int	ft_strlen(char *str)
{
	int	cnt;

	cnt = 0;
	while (str[cnt])
		cnt++;
	return (cnt);
}

int	main(int argc, char **argv)
{
	int		a;

	a = ft_strlen(argv[1]) - 1;
	if (argc == 2)
	{
		while (a >= 0)
		{
			write (1, &argv[1][a], 1);
			a--;
		}
	}
	else
		return (write (1, "\n", 1));
}

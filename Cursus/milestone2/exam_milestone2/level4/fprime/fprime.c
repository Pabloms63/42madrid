/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fprime.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/23 13:46:59 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/23 14:00:57 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int	main(int argc, char **argv)
{
	if (argc == 2)
	{
		int num = atoi(argv[1]);
		int factor = 2;
		while (num > 1)
		{
			if (num % factor == 0)
			{
				num /= factor;
				printf("%d", factor);
				if (num != 1)
					printf("*");
			}
			else
				factor++;
		}
	}
	else
		return (printf("\n"), 0);
	printf("\n");
}

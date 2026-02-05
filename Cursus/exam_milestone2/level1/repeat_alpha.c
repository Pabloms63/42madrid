/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   repeat_alpha.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 01:00:04 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/22 19:13:56 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "unistd.h"

int	repeat_alpha(char letter)
{
	if (letter >= 'a' && letter <= 'z')
		return (letter - 'a' + 1);
	else if (letter >= 'A' && letter <= 'Z')
		return (letter - 'A' + 1);
	return (1);
}

int	main(int argc, char **argv)
{
	int	cnt;
	int	num;

	cnt = 0;
	num = 0;
	if (argc == 2)
	{
		while (argv[1][cnt] != '\0')
		{
			num = repeat_alpha(argv[1][cnt]);
			while (num > 0)
			{
				write(1, &argv[1][cnt], 1);
				num--;
			}
			cnt++;
		}
	}
	else
		write(1, "\n", 1);
}

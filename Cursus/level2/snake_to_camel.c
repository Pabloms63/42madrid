/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   snake_to_camel.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 18:54:43 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/28 19:08:11 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(int argc, char **argv)
{
	int		cnt;
	char	letter;

	cnt = 0;
	if (argc == 2)
	{
		while (argv[1][cnt] != '\0')
		{
			if (argv[1][cnt] == '_')
			{
				cnt++;
				letter = argv[1][cnt] - 32;
				write(1, &letter, 1);
			}
			else
				write (1, &argv[1][cnt], 1);
			cnt++;
		}
	}
}

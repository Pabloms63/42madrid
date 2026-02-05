/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   search_and_replace.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 20:04:08 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/22 20:45:07 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "unistd.h"

int	main(int argc, char **argv)
{
	char	word1;
	char	word2;
	int		cnt;

	cnt = 0;
	if (argc == 4 && argv[2][1] == '\0' && argv[3][1] == '\0')
	{
		word1 = argv[2][0];
		word2 = argv[3][0];
		while (argv[1][cnt] != '\0')
		{
			if (argv[1][cnt] == word1)
				argv[1][cnt] = word2;
			write(1, &argv[1][cnt], 1);
			cnt++;
		}
	}
	else
		write (1, "\n", 1);
}

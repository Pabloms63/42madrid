/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   first_word.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 22:04:30 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/21 22:04:30 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "unistd.h"

int	main(int argc, char **argv)
{
	int		cnt;
	char	word;

	cnt = 0;
	if (argc == 2)
	{
		while (argv[1][cnt] == 9 || argv[1][cnt] == 32)
			cnt++;
		while (argv[1][cnt] != 9 && argv[1][cnt] != 32)
		{
			word = argv[1][cnt];
			write(1, &word, 1);
			cnt++;
		}
	}
	write(1, "\n", 1);
	return (0);
}

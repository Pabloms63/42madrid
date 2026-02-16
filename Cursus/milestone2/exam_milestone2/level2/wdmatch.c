/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   wdmatch.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 18:25:57 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/16 20:16:30 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(int argc, char **argv)
{
	char *str1 = argv[1];
	char *str2 = argv[2];
	int	size = 0;
	int cnt = 0;

	if (argc != 3)
		write(1, "\n", 1);
	else if (argc == 3)
	{
		while (str1[size] != '\0')
			size++;
		while (cnt < size && *str2)
		{
			if (str1[cnt] == *str2++)
				cnt++;
		}
		if (cnt == size)
			write(1, str1, size);
	}
	write(1, "\n", 1);
}

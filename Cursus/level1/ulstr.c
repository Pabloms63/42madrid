/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ulstr.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 20:45:43 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/22 21:14:57 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "unistd.h"

void	ulstr(char *str)
{
	int		cnt;
	char	word;

	cnt = 0;
	while (str[cnt])
	{
		word = str[cnt];
		if (word >= 'a' && word <= 'z')
		{
			word -= 32;
			write(1, &word, 1);
		}
		else if (word >= 'A' && word <= 'Z')
		{
			word += 32;
			write(1, &word, 1);
		}
		else
			write(1, &word, 1);
		cnt++;
	}
}

int	main(int argc, char **argv)
{
	if (argc == 2)
		ulstr(argv[1]);
	write(1, "\n", 1);
	return (0);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotone.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 19:40:33 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/22 20:03:08 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "unistd.h"

void	rotone(char *str)
{
	int		cnt;
	char	word;

	cnt = 0;
	while (str[cnt] != '\0')
	{
		word = str[cnt];
		if (word == 'z' || word == 'Z')
			word -= 25;
		else if ((word >= 'a' && word <= 'y')
			|| (word >= 'A' && word <= 'Y'))
			word += 1;
		write(1, &word, 1);
		cnt++;
	}
}

int	main(int argc, char **argv)
{
	if (argc == 2)
		rotone(argv[1]);
	write(1, "\n", 1);
	return (0);
}

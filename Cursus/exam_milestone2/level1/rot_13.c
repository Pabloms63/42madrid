/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rot_13.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 19:07:52 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/22 19:41:52 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "unistd.h"

void	rot_13(char *str)
{
	int		cnt;
	char	word;

	cnt = 0;
	while (str[cnt] != '\0')
	{
		word = str[cnt];
		if ((word >= 65 && word <= 77)
			|| (word >= 97 && word <= 109))
			word += 13;
		else if ((word >= 78 && word <= 90)
			|| (word >= 110 && word <= 122))
			word -= 13;
		write(1, &word, 1);
		cnt++;
	}
}

int	main(int argc, char **argv)
{
	if (argc == 2)
		rot_13(argv[1]);
	write(1, "\n", 1);
	return (0);
}

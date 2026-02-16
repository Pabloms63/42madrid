/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   union.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 20:14:24 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/16 19:52:23 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	seen_before(char *str, int end, char c)
{
	int	i = 0;
	while (i < end)
	{
		if (str[i] == c)
			return (1);
		i++;
	}
	return (0);
}

int	main(int argc, char **argv)
{
	int		i;
	int		j;
	char	c;

	if (argc == 3)
	{
		j = 1;
		while (j <= 2)
		{
			i = 0;
			while (argv[j][i])
			{
				c = argv[j][i];
				if (!seen_before(argv[j], i, c))
				{
					if (j == 1 || !seen_before(argv[1], __INT_MAX__, c))
						write(1, &c, 1);
				}
				i++;
			}
			j++;
		}
	}
	write(1, "\n", 1);
	return (0);
}

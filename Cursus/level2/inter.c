/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   inter.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 02:03:50 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/28 17:38:46 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	already_written(char *s, char c, int pos)
{
	int	cnt;

	cnt = 0;
	while (cnt < pos)
	{
		if (s[cnt] == c)
			return (1);
		cnt++;
	}
	return (0);
}

void	inter(char *s1, char *s2)
{
	int	c1;
	int	c2;

	c1 = 0;
	while (s1[c1])
	{
		c2 = 0;
		while (s2[c2])
		{
			if (s1[c1] == s2[c2] && !already_written(s1, s1[c1], c1))
			{
				write(1, &s1[c1], 1);
				break ;
			}
			c2++;
		}
		c1++;
	}
}

int	main(void)
{
	inter("Hola", "Heollpaadiss");
	write(1, "\n", 1);
	return (0);
}

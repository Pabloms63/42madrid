/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   paramsum.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/22 21:23:37 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/22 22:00:41 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	putnbr(int n)
{
	if (n > 9)
		putnbr(n / 10);
	write(1, &"0123456789"[n % 10], 1);
}

int	main(int argc, char **argv)
{
	int cnt = 0;
	char c;

	if (argc > 1)
	{
		while (cnt < argc)
			cnt++;
		c = (cnt - 1) + '0';
		write(1, &c, 1);
		write(1, "\n", 1);
	}
	else
	{
		write(1, "0", 1);
		write(1, "\n", 1);
	}
}

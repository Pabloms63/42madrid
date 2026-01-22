/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fizz_buzz.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 00:16:02 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/22 00:28:52 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "unistd.h"

void	ft_putnbr(int i)
{
	if (i > 9)
		ft_putnbr(i / 10);
	write(1, &"0123456789"[i % 10], 1);
}

int	main(void)
{
	int		cnt;

	cnt = 1;
	while (cnt < 101)
	{
		if ((cnt % 3) == 0 && (cnt % 5) == 0)
			write(1, "fizzbuzz", 4);
		else if ((cnt % 3) == 0 && (cnt % 5) != 0)
			write(1, "fizz", 4);
		else if ((cnt % 3) != 0 && (cnt % 5) == 0)
			write(1, "buzz", 4);
		else
			ft_putnbr(cnt);
		write(1, "\n", 1);
		cnt++;
	}
}

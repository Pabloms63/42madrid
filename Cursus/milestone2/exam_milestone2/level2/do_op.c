/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   do_op.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/25 17:08:31 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/27 18:18:59 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

void	ft_putnbr(int i)
{
	if (i > 9)
		ft_putnbr(i / 10);
	write(1, &"0123456789"[i % 10], 1);
}

int	main(int argc, char **argv)
{
	int		cnt;
	int		num1;
	int		num2;

	cnt = 0;
	num1 = atoi(argv[1]);
	num2 = atoi(argv[3]);
	if (argc == 4)
	{
		if (argv[2][0] == '+')
			printf("%d\n", num1 + num2);
		else if (argv[2][0] == '-')
			printf("%d\n", num1 - num2);
		else if (argv[2][0] == '*')
			printf("%d\n", num1 * num2);
		else if (argv[2][0] == '/')
			printf("%d\n", num1 / num2);
	}
	return (0);
}

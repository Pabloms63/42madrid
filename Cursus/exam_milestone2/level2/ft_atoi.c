/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 17:57:33 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/27 18:18:39 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	is_space(int c)
{
	if (c == 32)
		return (1);
	return (0);
}

int	is_digit(int c)
{
	if (c >= 48 && c <= 57)
		return (1);
	return (0);
}

int	ft_atoi(const char *str)
{
	int	res;
	int	cnt;
	int	sign;

	cnt = 0;
	while (is_space(str[cnt]))
		cnt++;
	sign = 1;
	if (str[cnt] == '-')
	{
		sign = -1;
		cnt++;
	}
	res = 0;
	while (is_digit(str[cnt]))
	{
		res *= 10;
		res += str[cnt] - '0';
		cnt++;
	}
	return (res * sign);
}

int	main(void)
{
	printf("%d\n", ft_atoi("12345"));
}

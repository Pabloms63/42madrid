/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/23 12:04:20 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/23 12:18:19 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	val(char c)
{
	if (c >= '0' && c <= '9')
		return (c - '0');
	if (c >= 'a' && c <= 'f')
		return (c - 'a' + 10);
	if (c >= 'A' && c <= 'F')
		return (c - 'A' + 10);
	return (-1);
}

int	ft_atoi_base(const char *str, int str_base)
{
	int cnt = 0;
	int res = 0;
	int sign = 1;
	int v;
	while (str[cnt] == ' ' || str[cnt] == '\t')
		cnt++;
	if (str[cnt] == '-')
	{
		sign *= -1;
		cnt++;
	}
	while ((v = val(str[cnt])) >= 0 && v < str_base)
	{
		res = res * str_base + v;
		cnt++;
	}
	return (res * sign);
}

int main()
{
	printf("%d\n", ft_atoi_base("123", 10));
	printf("%d\n", ft_atoi_base("7B", 16));
	printf("%d\n", ft_atoi_base("-101", 2));
}
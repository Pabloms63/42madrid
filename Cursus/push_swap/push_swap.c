/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 17:35:25 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/12/29 19:38:59 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

size_t	ft_is_number(char *str)
{
	size_t	count;

	count = 0;
	if (str[count] == '-' || str[count] == '+')
		count++;
	if (!str[count])
		return (0);
	while (str[count] != '\0')
	{
		if (str[count] < '0' || str[count] > '9')
			return (0);
		count++;
	}
	return (1);
}

long	ft_atol(char *str)
{
	long	res;
	size_t	count;
	int		sign;

	count = 0;
	sign = 1;
	res = 0;
	if (str[count] == '+' || str[count] == '-')
	{
		if (str[count] == '-')
			sign = -1;
		count++;
	}
	while (str[count] != '\0')
	{
		if (str[count] >= '0' && str[count] <= '9')
			res = res * 10 + (str[count] - '0');
		if (res * sign > INT_MAX || res * sign < INT_MIN)
			return (LONG_MAX);
		count++;
	}
	return (res * sign);
}

int	main(int argc, char	*argv[])
{
	int	count;

	count = 1;
	if (argc <= 1)
		return (ft_printf("No hay argumentos"), 0);
	while (count < argc)
	{
		if (!ft_is_number(argv[count]))
			return (ft_printf("El argumento debe ser un número válido"), 0);
		ft_printf("%d\n", ft_atol(argv[count]));
		count++;
	}
}

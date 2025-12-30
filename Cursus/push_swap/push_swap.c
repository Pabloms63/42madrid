/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 17:35:25 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/12/30 20:51:11 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static size_t	ft_is_number(char *str)
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

static size_t	ft_is_duplicate_number(long *num, size_t size)
{
	size_t	a;
	size_t	b;

	a = 0;
	while (a < size)
	{
		b = a + 1;
		while (b < size)
		{
			if (num[a] == num[b])
				return (1);
			b++;
		}
		a++;
	}
	return (0);
}

static long	ft_atol(char *str)
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
	int		count;
	long	res;
	long	*nums;
	size_t	filled;

	count = 1;
	filled = 0;
	if (argc <= 1)
		return (ft_printf("No hay argumentos"), 0);
	nums = malloc((argc - 1) * sizeof(*nums));
	if (!nums)
		return (ft_printf("Error de memoria\n"), 1);
	while (count < argc)
	{
		if (!ft_is_number(argv[count]))
			return (free(nums), ft_printf("El argumento debe ser un número válido"), 0);
		res = ft_atol(argv[count]);
		nums[filled++] = res;
		if (ft_is_duplicate_number(nums, filled))
			return (free(nums), ft_printf("Los argumentos no pueden estar repetidos")
				, 0);
		ft_printf("%d\n", res);
		count++;
	}
	free(nums);
}

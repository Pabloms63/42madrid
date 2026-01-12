/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   validations.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/05 19:37:46 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/12 21:50:26 by pmarcos-         ###   ########.fr       */
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

size_t	ft_is_duplicate_number(long *num, size_t size)
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

int	parse_args(int argc, char *argv[])
{
	long	*nums;
	size_t	size;
	size_t	i;

	if (argc <= 1)
		return (0);
	if (has_quotes(argc, argv))
	{
		nums = nums_with_quotes(argv[1], &size);
		if (!nums)
			return (0);
	}
	else
	{
		size = argc - 1;
		nums = malloc(sizeof(long) * size);
		if (!nums)
			return (0);
		i = 0;
		while (i < size)
		{
			if (!ft_is_number(argv[i + 1]))
				return (free(nums), 0);
			nums[i] = ft_atol(argv[i + 1]);
			if (nums[i] == LONG_MAX)
				return (free(nums), 0);

			i++;
		}
	}
	if (ft_is_duplicate_number(nums, size))
		return (free(nums), 0);
	free(nums);
	return (1);
}

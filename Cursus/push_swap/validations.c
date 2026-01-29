/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   validations.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/05 19:37:46 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/29 14:09:46 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Check that the string is made up only of numbers.
 */
int	ft_is_number(char *str)
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

/**
 * @brief Check that no number is duplicated.
 */
int	ft_is_duplicate_number(int *num, size_t size)
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

/**
 * @brief Convert each character to long.
 */
int	ft_atoi2(char *str)
{
	int		res;
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
			return (INT_MAX);
		count++;
	}
	return (res * sign);
}

char	*join_args(int argc, char **argv)
{
	char	*res;
	char	*tmp;
	int		i;

	i = 1;
	res = ft_strdup("");
	while (i < argc)
	{
		tmp = ft_strjoin(res, argv[i]);
		free(res);
		if (!tmp)
			return (NULL);
		res = tmp;
		if (i + 1 < argc)
		{
			tmp = ft_strjoin(res, " ");
			free(res);
			if (!tmp)
				return (NULL);
			res = tmp;
		}
		i++;
	}
	return (res);
}

/**
 * @brief Check all validations
 */
int	parse_args(int argc, char **argv, int **out, size_t *size)
{
	char	*joined;
	char	**split;
	int		*nums;
	size_t	i;

	if (argc < 2)
		return (1);
	joined = join_args(argc, argv);
	if (!joined)
		return (1);
	split = ft_split(joined, ' ');
	free(joined);
	if (!split || !split[0])
		return (1);
	*size = split_len(split);
	nums = malloc(sizeof(int) * (*size));
	if (!nums)
		return (free_split(split), 1);
	i = 0;
	while (i < *size)
	{
		if (!ft_is_number(split[i]))
			return (free_split(split), free(nums), ft_printf("No es númerico\n"), 1);
		nums[i] = ft_atoi2(split[i]);
		if (nums[i] == INT_MAX)
			return (free_split(split), free(nums), ft_printf("Overflow\n"), 1);
		i++;
	}
	free_split(split);
	if (ft_is_duplicate_number(nums, *size))
		return (free(nums), ft_printf("Hay números duplicados\n"), 1);
	*out = nums;
	return (0);
}

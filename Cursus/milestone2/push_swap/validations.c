/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   validations.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/05 19:37:46 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/03 16:37:58 by pmarcos-         ###   ########.fr       */
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
long	ft_atoi2(char *str)
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

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   split_arg_quotes.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 20:53:02 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/12 21:53:55 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	split_len(char **str)
{
	int	cnt;

	cnt = 0;
	while (str[cnt])
		cnt++;
	return (cnt);
}

void	free_split(char **split)
{
	int	a;

	a = 0;
	while (split[a] != NULL)
		free(split[a++]);
	free(split);
}

int	has_quotes(int argc, char *argv[])
{
	int		cnt;

	cnt = 1;
	while (cnt < argc)
	{
		if (ft_strchr(argv[cnt], ' ') != NULL)
			return (1);
		cnt++;
	}
	return (0);
}

long	*nums_with_quotes(char *arg, size_t *len)
{
	char	**split;
	long	*nums;
	size_t	i;

	split = ft_split(arg, ' ');
	if (!split)
		return (NULL);

	*len = split_len(split);
	nums = malloc(sizeof(long) * (*len));
	if (!nums)
		return (NULL);

	i = 0;
	while (split[i])
	{
		if (!ft_is_number(split[i]))
			return (free_split(split), free(nums), NULL);
		nums[i] = ft_atol(split[i]);
		if (nums[i] == LONG_MAX)
			return (free_split(split), free(nums), NULL);
		i++;
	}
	free_split(split);
	return (nums);
}

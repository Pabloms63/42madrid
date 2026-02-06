/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_args.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/03 16:38:07 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/06 18:12:36 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	validate_and_convert(char **split, int **out, size_t size)
{
	int		*nums;
	size_t	i;
	long	val;

	nums = malloc(sizeof(int) * size);
	if (!nums)
		return (1);
	i = 0;
	while (i < size)
	{
		if (!ft_is_number(split[i]))
			return (free(nums), 1);
		val = ft_atoi2(split[i]);
		if (val > INT_MAX || val < INT_MIN)
			return (free(nums), 1);
		nums[i] = (int)val;
		i++;
	}
	if (ft_is_duplicate_number(nums, size))
		return (free(nums), 1);
	*out = nums;
	return (0);
}

/**
 * @brief Check all validations
 */
int	parse_args(int argc, char **argv, int **out, size_t *size)
{
	char	*joined;
	char	**split;
	int		result;

	joined = join_args(argc, argv);
	if (!joined)
		return (1);
	split = ft_split(joined, ' ');
	free(joined);
	if (!split || !split[0])
		return (1);
	*size = split_len(split);
	result = validate_and_convert(split, out, *size);
	free_split(split);
	return (result);
}

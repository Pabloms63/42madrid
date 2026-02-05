/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   indexing.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 13:46:39 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/29 13:58:37 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	sort_array(int *arr, size_t size)
{
	size_t	i;
	int		tmp;
	int		swapped;

	if (!arr)
		return ;
	while (1)
	{
		swapped = 0;
		i = 0;
		while (i < size - 1)
		{
			if (arr[i] > arr[i + 1])
			{
				tmp = arr[i];
				arr[i] = arr[i + 1];
				arr[i + 1] = tmp;
				swapped = 1;
			}
			i++;
		}
		if (!swapped)
			break ;
	}
}

int	get_index(int *arr, size_t size, int value)
{
	size_t	i;

	i = 0;
	while (i < size)
	{
		if (arr[i] == value)
			return ((int)i);
		i++;
	}
	return (-1);
}

int	max_bits(size_t size)
{
	int	bits;
	int	max;

	bits = 0;
	max = (int)size - 1;
	while ((max >> bits) != 0)
		bits++;
	return (bits);
}

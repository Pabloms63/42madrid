/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   radix.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/20 18:24:35 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/20 20:58:38 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

// void	assign_index(t_list **a)
// {
// 	t_list	*current;
// 	t_list	*compare;
// 	int		index;

// 	current = *a;
// 	while (current)
// 	{
// 		index = 0;
// 		compare = *a;
// 		while (compare)
// 		{
// 			if (current->content > compare->content)
// 				index++;
// 			compare = compare->next;
// 		}
// 		current->index = index;
// 		current = current->next;
// 	}
// }

void	radix(t_list **a, t_list **b)
{
	int	size;
	int	max_bits;
	int	x;
	int	y;

	size = ft_lstsize(*a);
	max_bits = get_max_bits(size);
	x = 0;			
	while (x < max_bits)
	{
		y = 0;
		while (y < size)
		{
			if (((*(int *)(*a)->content >> x) & 1))
				pb(a, b);
			else
				ra(a);
			y++;
		}
		while (*b)
			pa(a, b);
		x++;
	}
}

int	get_max_bits(int size)
{
	int	max_index;
	int	bits;

	bits = 0;
	max_index = size - 1;
	while (max_index > 0)
	{
		max_index >>= 1;
		bits++;
	}
	return (bits);
}

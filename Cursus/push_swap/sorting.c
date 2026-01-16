/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sorting.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/13 20:42:24 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/16 21:05:54 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Sort 2 numbers.
 */
void	sort_two(t_list **a)
{
	int	first;
	int	second;

	first = *(int *)(*a)-> content;
	second = *(int *)(*a)-> next -> content;
	if (first > second)
		sa(a);
}

void	sort_three(t_list **a)
{
	int	first;
	int	second;
	int	third;

	first = *(int *)(*a)-> content;
	second = *(int *)(*a)-> next -> content;
	third = *(int *)(*a)-> next -> next -> content;
	if (first > second && first < third)
		sa(a);
	else if (first > second && first > third && second < third)
		ra(a);
	else if (first > third && first < second)
		rra(a);
	else if (first < second && first < third && second > third)
	{
		sa(a);
		ra(a);
	}
	else if (first > second && first > third && second > third)
	{
		sa(a);
		rra(a);
	}
}

void	sort_five(t_list **a)
{
	ft_printf("por hacer");
}

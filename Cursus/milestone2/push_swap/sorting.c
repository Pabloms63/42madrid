/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sorting.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/13 20:42:24 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/03 14:46:15 by pmarcos-         ###   ########.fr       */
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

void	push_smallest_to_b(t_list **a, t_list **b)
{
	t_list	*tmp;
	int		min;
	int		pos;

	tmp = *a;
	min = *(int *)tmp->content;
	pos = 0;
	while (tmp)
	{
		if (*(int *)tmp->content < min)
		{
			min = *(int *)tmp->content;
			pos = 0;
		}
		tmp = tmp->next;
		pos++;
	}
	while (*(int *)(*a)->content != min)
	{
		if (pos <= ft_lstsize(*a) / 2)
			rra(a);
		else
			ra(a);
	}
	pb(a, b);
}

void	sort_five(t_list **a)
{
	t_list	*b;
	int		size;

	b = NULL;
	size = ft_lstsize(*a);
	if (size == 4)
	{
		push_smallest_to_b(a, &b);
		sort_three(a);
		pa(a, &b);
	}
	else if (size == 5)
	{
		push_smallest_to_b(a, &b);
		push_smallest_to_b(a, &b);
		sort_three(a);
		if (*(int *)(b->content) < *(int *)(b->next->content))
			sb(&b);
		pa(a, &b);
		pa(a, &b);
	}
}

void	radix_sort(t_list **a, int *nums, size_t size)
{
	t_list	*b;
	size_t	i;
	size_t	j;

	if (!a || !*a || size < 2)
		return ;
	b = NULL;
	sort_array(nums, size);
	i = 0;
	while (i < (size_t)max_bits(size))
	{
		j = 0;
		while (j < size)
		{
			if ((get_index(nums, size, *(int *)(*a)->content) >> i) & 1)
				ra(a);
			else
				pb(a, &b);
			j++;
		}
		while (b)
			pa(a, &b);
		i++;
	}
}

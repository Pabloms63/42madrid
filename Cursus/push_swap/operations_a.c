/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations_a.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 23:46:53 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/16 19:07:59 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Swap the first 2 elements at the top of stack a.
 */
void	sa(t_list **a)
{
	t_list	*first;
	t_list	*second;

	if (!a || !*a || !(*a)->next)
		return ;
	first = *a;
	second = first -> next;
	first -> next = second -> next;
	second -> next = first;
	*a = second;
	ft_printf("sa\n");
}

/**
 * @brief Take the first element at the top of b and put it at the top of a.
 */
void	pa(t_list **a, t_list **b)
{
	t_list	*first_b;

	if (!b || !*b)
		return ;
	first_b = *b;
	*b = first_b -> next;
	first_b -> next = *a;
	*a = first_b;
	ft_printf("pa\n");
}

/**
 * @brief The first element becomes the last one.
 */
void	ra(t_list **a)
{
	t_list	*first;
	t_list	*last;

	if (!a || !*a || !(*a)->next)
		return ;
	first = *a;
	last = ft_lstlast(*a);
	*a = first -> next;
	first -> next = NULL;
	last -> next = first;
	ft_printf("ra\n");
}

/**
 * @brief The last element becomes the first one.
 */
void	rra(t_list **a)
{
	t_list	*first;
	t_list	*last;
	t_list	*prev;

	if (!a || !*a || !(*a)->next)
		return ;
	first = *a;
	last = ft_lstlast(*a);
	prev = first;
	while (prev -> next != last)
		prev = prev -> next;
	prev -> next = NULL;
	last -> next = first;
	*a = last;
	ft_printf("rra\n");
}

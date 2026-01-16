/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations_b.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/08 19:12:43 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/16 19:08:29 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Swap the first 2 elements at the top of stack b.
 */
void	sb(t_list **b)
{
	t_list	*first;
	t_list	*second;

	if (!b || !*b || !(*b)-> next)
		return ;
	first = *b;
	second = first -> next;
	first -> next = second -> next;
	second -> next = first;
	*b = second;
	ft_printf("sb\n");
}

/**
 * @brief Take the first element at the top of a and put it at the top of b.
 */
void	pb(t_list **a, t_list **b)
{
	t_list	*first_a;

	if (!a || !*a)
		return ;
	first_a = *a;
	*a = first_a -> next;
	first_a -> next = *b;
	*b = first_a;
	ft_printf("pb\n");
}

/**
 * @brief The first element becomes the last one.
 */
void	rb(t_list **b)
{
	t_list	*first;
	t_list	*last;

	if (!b || !*b || !(*b)->next)
		return ;
	first = *b;
	last = ft_lstlast(*b);
	*b = first->next;
	first->next = NULL;
	last->next = first;
	ft_printf("rb\n");
}

/**
 * @brief The last element becomes the first one.
 */
void	rrb(t_list **b)
{
	t_list	*first;
	t_list	*last;
	t_list	*prev;

	if (!b || !*b || !(*b)-> next)
		return ;
	first = *b;
	last = ft_lstlast(*b);
	prev = first;
	while (prev -> next != last)
		prev = prev -> next;
	prev -> next = NULL;
	last -> next = first;
	*b = last;
	ft_printf("rrb\n");
}

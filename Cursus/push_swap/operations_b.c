/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations_b.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/08 19:12:43 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/08 23:40:30 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

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
}

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

void	pb(t_list **a, t_list **b)
{
	t_list	*first_a;

	if (!a || !*a)
		return ;
	first_a = *a;
	*a = first_a -> next;
	first_a -> next = *b;
	*b = first_a;
}

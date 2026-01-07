/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 23:46:53 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/07 23:58:51 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ra(t_list **a)
{
	t_list	*first;
	t_list	*last;

	if (!a || !*a || !(*a)->next)
		return ;

	first = *a;
	last = ft_lstlast(*a);

	*a = first->next;
	first->next = NULL;
	last->next = first;

	ft_printf("ra\n");
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


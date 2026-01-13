/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations_both.C                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/08 19:33:14 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/13 19:15:20 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief sa and sb at the same time.
 */
void ss(t_list **a, t_list *b)
{
	sa(a);
	sb(b);
}

/**
 * @brief ra and rb at the same time.
 */
void rr(t_list **a, t_list **b)
{
	ra(a);
	rb(b);
}

/**
 * rra and rrb at the same time.
 */
void rrr(t_list **a, t_list **b)
{
	rra(a);
	rrb(b);
}

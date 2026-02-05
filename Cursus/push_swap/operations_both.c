/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations_both.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/08 19:33:14 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/02 20:20:36 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief sa and sb at the same time.
 */
void	ss(t_list **a, t_list **b)
{
	sa(a);
	sb(b);
	ft_printf("ss\n");
}

/**
 * @brief ra and rb at the same time.
 */
void	rr(t_list **a, t_list **b)
{
	ra(a);
	rb(b);
	ft_printf("rr\n");
}

/**
 * rra and rrb at the same time.
 */
void	rrr(t_list **a, t_list **b)
{
	rra(a);
	rrb(b);
	ft_printf("rrr\n");
}

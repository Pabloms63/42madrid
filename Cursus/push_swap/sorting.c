/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sorting.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/13 20:42:24 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/13 20:52:42 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Sort 2 numbers.
 */
void	sort_two(t_list **a)
{
	if ((*(int *)(*a)-> content) > (*(int *)(*a)-> next -> content))
	{
		sa(a);
		ft_printf("sa\n");
	}
}

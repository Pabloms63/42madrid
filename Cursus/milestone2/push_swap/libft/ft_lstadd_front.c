/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 19:33:44 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/06 18:34:32 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * @brief Añada un nodo al principio de la lista enlazada.
 */
void	ft_lstadd_front(t_list **lst, t_list *new)
{
	if (!new)
		return ;
	new -> next = *lst;
	*lst = new;
}

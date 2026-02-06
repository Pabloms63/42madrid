/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 20:37:35 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/06 19:28:22 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * @brief Devuelve el último nodo de una lista enlazada.
 */
t_list	*ft_lstlast(t_list *lst)
{
	while (lst -> next != NULL)
	{
		lst = lst -> next;
	}
	return (lst);
}

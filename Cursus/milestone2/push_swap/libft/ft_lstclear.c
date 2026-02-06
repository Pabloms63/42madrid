/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 20:55:44 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/06 18:35:12 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * @brief Elimina y libera todos los nodos de una lista enlazada.
 */
void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*node;
	t_list	*temp;

	if (!lst || !del)
		return ;
	node = *lst;
	while (node != NULL)
	{
		temp = node -> next;
		del(node -> content);
		free (node);
		node = temp;
	}
	*lst = NULL;
}

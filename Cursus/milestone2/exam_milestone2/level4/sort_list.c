/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_list.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/23 18:25:34 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/23 18:35:16 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "list.h"
#include <unistd.h>

t_list	*sort_list(t_list* lst, int (*cmp)(int, int))
{
	int tmp;
	t_list *head;

	head = lst;
	while (lst != NULL && lst->next != NULL)
	{
		if (cmp(lst-> data, lst->next->data) == 0)
		{
			tmp = lst->data;
			lst->data = lst->next->data;
			lst -> next ->data = tmp;
			lst = head;
		}
		else
			lst = lst -> next;
	}
	return (head);
}

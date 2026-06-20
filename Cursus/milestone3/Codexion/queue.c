/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   queue.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/20 21:38:22 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/06/20 21:51:18 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"
#include <stdlib.h>

t_request	*create_request(int coder_id, long deadline)
{
	t_request	*req;

	req = malloc(sizeof(t_request));
	if (!req)
		return (NULL);
	req -> coder_id = coder_id;
	req -> deadline = deadline;
	req -> next = NULL;
	return (req);
}

void	enqueue_request(t_queue *queue, t_request *req)
{
	t_request	*current;

	if (!queue->head || queue -> head -> deadline > req -> deadline)
	{
		req -> next = queue -> head;
		queue -> head = req;
		return ;
	}
	current = queue -> head;
	while (current -> next && current -> next -> deadline <= req -> deadline)
		current = current -> next;
	req -> next = current -> next;
	current -> next = req;
}

t_request	*dequeue_request(t_queue *queue)
{
	t_request	*req;

	if (!queue->head)
		return (NULL);
	req = queue->head;
	queue->head = queue->head->next;
	return (req);
}

void	free_queue(t_queue *queue)
{
	t_request	*current;
	t_request	*next;

	current = queue->head;
	while (current)
	{
		next = current->next;
		free(current);
		current = next;
	}
	queue->head = NULL;
}
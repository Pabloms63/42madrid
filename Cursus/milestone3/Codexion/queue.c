/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   queue.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/20 21:38:22 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/07/25 19:51:20 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	queue_init(t_queue *queue)
{
	queue->nodes = malloc(sizeof(t_heap_node) * QUEUE_INIT_CAPACITY);
	if (!queue->nodes)
		return (1);
	queue->size = 0;
	queue->capacity = QUEUE_INIT_CAPACITY;
	queue->next_seq = 0;
	return (0);
}

int	enqueue_request(t_queue *queue, int coder_id, long key)
{
	if (queue->size == queue->capacity && heap_grow(queue))
		return (1);
	queue->nodes[queue->size].coder_id = coder_id;
	queue->nodes[queue->size].key = key;
	queue->size++;
	sift_up(queue, queue->size - 1);
	return (0);
}

int	dequeue_request(t_queue *queue, int *coder_id_out)
{
	if (queue->size == 0)
		return (1);
	*coder_id_out = queue->nodes[0].coder_id;
	queue->size--;
	queue->nodes[0] = queue->nodes[queue->size];
	sift_down(queue, 0);
	return (0);
}

void	free_queue(t_queue *queue)
{
	free(queue->nodes);
	queue->nodes = NULL;
	queue->size = 0;
	queue->capacity = 0;
}

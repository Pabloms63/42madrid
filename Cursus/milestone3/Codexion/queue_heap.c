/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   queue_heap.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/09 21:00:00 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/07/09 23:10:18 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

/*
** Mecanica interna del min-heap: intercambio de nodos, reordenacion
** (sift up/down) y crecimiento del array cuando se llena.
** Usadas por enqueue_request/dequeue_request en queue.c y por
** update_key en queue_utils.c.
*/

void	swap_nodes(t_heap_node *a, t_heap_node *b)
{
	t_heap_node	tmp;

	tmp = *a;
	*a = *b;
	*b = tmp;
}

void	sift_up(t_queue *queue, int i)
{
	int	parent;

	while (i > 0)
	{
		parent = (i - 1) / 2;
		if (queue->nodes[parent].key <= queue->nodes[i].key)
			break ;
		swap_nodes(&queue->nodes[parent], &queue->nodes[i]);
		i = parent;
	}
}

void	sift_down(t_queue *queue, int i)
{
	int	left;
	int	right;
	int	smallest;

	while (1)
	{
		left = 2 * i + 1;
		right = 2 * i + 2;
		smallest = i;
		if (left < queue->size
			&& queue->nodes[left].key < queue->nodes[smallest].key)
			smallest = left;
		if (right < queue->size
			&& queue->nodes[right].key < queue->nodes[smallest].key)
			smallest = right;
		if (smallest == i)
			break ;
		swap_nodes(&queue->nodes[i], &queue->nodes[smallest]);
		i = smallest;
	}
}

int	heap_grow(t_queue *queue)
{
	t_heap_node	*tmp;
	int			new_capacity;
	int			i;

	new_capacity = queue->capacity * 2;
	tmp = malloc(sizeof(t_heap_node) * new_capacity);
	if (!tmp)
		return (1);
	i = 0;
	while (i < queue->size)
	{
		tmp[i] = queue->nodes[i];
		i++;
	}
	free(queue->nodes);
	queue->nodes = tmp;
	queue->capacity = new_capacity;
	return (0);
}
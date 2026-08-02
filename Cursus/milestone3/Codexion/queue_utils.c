/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   queue_utils.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/09 21:00:00 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/07/28 19:32:54 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	heap_find(t_queue *queue, int coder_id)
{
	int	i;

	i = 0;
	while (i < queue->size)
	{
		if (queue->nodes[i].coder_id == coder_id)
			return (i);
		i++;
	}
	return (-1);
}

int	queue_contains(t_queue *queue, int coder_id)
{
	return (heap_find(queue, coder_id) >= 0);
}

void	update_key(t_queue *queue, int coder_id, long new_key)
{
	int		idx;
	long	old_key;

	idx = heap_find(queue, coder_id);
	if (idx < 0)
		return ;
	old_key = queue->nodes[idx].key;
	queue->nodes[idx].key = new_key;
	if (new_key < old_key)
		sift_up(queue, idx);
	else
		sift_down(queue, idx);
}

int	queue_peek(t_queue *queue)
{
	if (queue->size == 0)
		return (-1);
	return (queue->nodes[0].coder_id);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   dongle.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/07 21:20:39 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/07/07 21:21:55 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	can_acquire_dongle(t_dongle *dongle, int coder_id, char *scheduler)
{
	t_request	*head;

	if (get_time_ms() < dongle->cooldown_until)
		return (0);
	if (ft_strcmp(scheduler, "fifo") == 0)
		return (1);
	else
	{
		head = dongle->waitlist.head;
		if (!head || head->coder_id == coder_id)
			return (1);
	}
	return (0);
}

static void	add_to_queue_edf(t_dongle *dongle, int coder_id, long deadline)
{
	t_request	*req;

	req = dongle->waitlist.head;
	while (req && req->coder_id != coder_id)
		req = req->next;
	if (!req)
	{
		req = create_request(coder_id, deadline);
		enqueue_request(&dongle->waitlist, req);
	}
	else
		req->deadline = deadline;
}

int	try_acquire_dongle(t_dongle *dongle, int coder_id,
								long deadline, char *scheduler)
{
	int	acquired;

	acquired = 0;
	pthread_mutex_lock(&dongle->mutex);
	if (ft_strcmp(scheduler, "edf") == 0)
		add_to_queue_edf(dongle, coder_id, deadline);
	if (can_acquire_dongle(dongle, coder_id, scheduler))
	{
		if (ft_strcmp(scheduler, "edf") == 0)
			free(dequeue_request(&dongle->waitlist));
		acquired = 1;
	}
	if (!acquired)
		pthread_mutex_unlock(&dongle->mutex);
	return (acquired);
}

void	release_dongle(t_dongle *dongle, long cooldown)
{
	dongle->cooldown_until = get_time_ms() + cooldown;
	pthread_mutex_unlock(&dongle->mutex);
}

int	acquire_dongle(t_coder *coder, t_dongle *dongle, long deadline)
{
	while (!try_acquire_dongle(dongle, coder->id, deadline,
			coder->data->scheduler)
		&& !simulation_stopped(coder->data))
		ft_usleep(1);
	if (simulation_stopped(coder->data))
		return (0);
	print_status(coder, "\033[32mhas taken a dongle\033[0m");
	return (1);
}
/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   dongle.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/07 21:20:39 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/07/23 01:06:52 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	add_to_queue(t_dongle *dongle, int coder_id,
					long deadline, char *scheduler)
{
	long	key;

	if (queue_contains(&dongle->waitlist, coder_id))
	{
		if (ft_strcmp(scheduler, "edf") == 0)
			update_key(&dongle->waitlist, coder_id, deadline);
		return ;
	}
	if (ft_strcmp(scheduler, "edf") == 0)
		key = deadline;
	else
		key = dongle->waitlist.next_seq++;
	enqueue_request(&dongle->waitlist, coder_id, key);
}

static int	can_acquire_dongle(t_dongle *dongle, int coder_id)
{
	if (get_time_ms() < dongle->cooldown_until)
		return (0);
	return (queue_peek(&dongle->waitlist) == coder_id);
}

int	try_acquire_dongle(t_dongle *dongle, int coder_id,
								long deadline, char *scheduler)
{
	int	acquired;
	int	served_id;

	acquired = 0;
	pthread_mutex_lock(&dongle->mutex);
	add_to_queue(dongle, coder_id, deadline, scheduler);
	if (can_acquire_dongle(dongle, coder_id))
	{
		dequeue_request(&dongle->waitlist, &served_id);
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

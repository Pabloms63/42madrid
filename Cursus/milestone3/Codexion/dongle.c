/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   dongle.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/07 21:20:39 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/08/03 14:50:22 by pmarcos-         ###   ########.fr       */
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
	if (!dongle->available)
		return (0);
	if (get_time_ms() < dongle->cooldown_until)
		return (0);
	return (queue_peek(&dongle->waitlist) == coder_id);
}

static int	wait_for_turn(t_dongle *dongle, t_coder *coder)
{
	struct timespec	ts;
	long			wake;

	while (!can_acquire_dongle(dongle, coder->id)
		&& !simulation_stopped(coder->data))
	{
		wake = get_time_ms() + 5;
		if (dongle->cooldown_until > get_time_ms()
			&& dongle->cooldown_until < wake)
			wake = dongle->cooldown_until;
		ts.tv_sec = wake / 1000;
		ts.tv_nsec = (wake % 1000) * 1000000;
		pthread_cond_timedwait(&dongle->cond, &dongle->mutex, &ts);
	}
	if (simulation_stopped(coder->data))
	{
		queue_remove(&dongle->waitlist, coder->id);
		return (0);
	}
	return (1);
}

int	acquire_dongle(t_coder *coder, t_dongle *dongle, long deadline)
{
	int	served_id;

	pthread_mutex_lock(&dongle->mutex);
	add_to_queue(dongle, coder->id, deadline, coder->data->scheduler);
	if (!wait_for_turn(dongle, coder))
	{
		pthread_mutex_unlock(&dongle->mutex);
		return (0);
	}
	dequeue_request(&dongle->waitlist, &served_id);
	dongle->available = 0;
	pthread_mutex_unlock(&dongle->mutex);
	print_status(coder, "\033[32mhas taken a dongle\033[0m");
	return (1);
}

void	release_dongle(t_dongle *dongle, long cooldown)
{
	pthread_mutex_lock(&dongle->mutex);
	dongle->available = 1;
	dongle->cooldown_until = get_time_ms() + cooldown;
	pthread_cond_broadcast(&dongle->cond);
	pthread_mutex_unlock(&dongle->mutex);
}

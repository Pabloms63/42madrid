/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   log.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 11:45:18 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/05/25 11:51:42 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	print_status(t_coder *coder, char *msg)
{
	long	time;

	pthread_mutex_lock(&coder -> data -> log_mutex);
	pthread_mutex_lock(&coder -> data -> stop_mutex);
	if (coder -> data -> stop)
	{
		pthread_mutex_unlock(&coder -> data -> stop_mutex);
		pthread_mutex_unlock(&coder -> data -> log_mutex);
		return ;
	}
	pthread_mutex_unlock(&coder -> data -> stop_mutex);
	time = get_time_ms() - coder -> data -> start_time;
	printf("%ld %d %s\n", time, coder -> id, msg);
	pthread_mutex_unlock(&coder -> data -> log_mutex);
}

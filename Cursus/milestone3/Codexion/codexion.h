/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/19 14:15:03 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/05/19 14:15:03 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef CODEXION_H
# define CODEXION_H

# include <pthread.h>
# include <sys/time.h>
# include <unistd.h>
# include <stdlib.h>
# include <stdio.h>

typedef struct s_dongle
{
	pthread_mutex_t	mutex;
	int				available;
	long			cooldown_until;
}	t_dongle;

typedef struct s_data	t_data;

typedef struct s_coder
{
	int			id;
	pthread_t	thread;

	t_dongle	*left;
	t_dongle	*right;

	t_data		*data;
}	t_coder;

typedef struct s_data
{
	int				num_coders;

	long			time_to_burnout;
	long			time_to_compile;
	long			time_to_debug;
	long			time_to_refactor;

	int				stop;

	pthread_mutex_t	long_mutex;

	t_dongle		*dongles;
	t_coder			*coders;
}	t_data;

long	get_time_ms(void);

void	ft_usleep(long ms);

#endif
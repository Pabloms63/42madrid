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

	long		last_compile;
	int			compile_count;

	t_data		*data;
}	t_coder;

typedef struct s_data
{
	int				num_coders;

	long			time_to_burnout;
	long			time_to_compile;
	long			time_to_debug;
	long			time_to_refactor;
	long			dongle_cooldown;

	int				required_compiles;

	int				stop;

	long			start_time;

	pthread_t		monitor;

	pthread_mutex_t	stop_mutex;
	pthread_mutex_t	log_mutex;

	t_dongle		*dongles;
	t_coder			*coders;
}	t_data;

/* UTILS */
int		is_digit(char c);
int		is_number(char *str);
int		ft_strcmp(const char *s1, const char *s2);
long	ft_atol(char *str);

/* TIME */
long	get_time_ms(void);
void	ft_usleep(long ms);

/* PARSE */
int		parse_args(t_data *data, char **av);

/* INIT */
int		init_data(t_data *data);
int		init_threads(t_data *data);

/* ROUTINE */
void	*coder_routine(void *arg);

/* LOG */
void	print_status(t_coder *coder, char *msg);

/* SIMULATION */
int		simulation_stopped(t_data *data);

/* MONITOR */
void	*monitor_routine(void *arg);

#endif
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
# include <limits.h>

# define QUEUE_INIT_CAPACITY 4

typedef struct s_heap_node
{
	int		coder_id;
	long	key;
}	t_heap_node;

typedef struct s_data	t_data;

typedef struct s_queue
{
	t_heap_node	*nodes;
	int			size;
	int			capacity;
	long		next_seq;
}	t_queue;


typedef struct s_dongle
{
	pthread_mutex_t	mutex;
	long			cooldown_until;
	t_queue			waitlist;
}	t_dongle;


typedef struct s_coder
{
	int				id;
	pthread_t		thread;
	pthread_mutex_t	mutex;

	t_dongle		*left;
	t_dongle		*right;

	long			last_compile;
	int				compile_count;

	t_data			*data;
}	t_coder;

typedef struct s_data
{
	long			num_coders;

	long			time_to_burnout;
	long			time_to_compile;
	long			time_to_debug;
	long			time_to_refactor;
	long			dongle_cooldown;

	long			required_compiles;

	int				stop;

	long			start_time;

	char			*scheduler;

	pthread_t		monitor;

	pthread_mutex_t	stop_mutex;
	pthread_mutex_t	log_mutex;

	t_dongle		*dongles;
	t_coder			*coders;
}	t_data;


/* UTILS */
int			is_digit(char c);
int			is_number(char *str);
int			ft_strcmp(const char *s1, const char *s2);
long		ft_atol(char *str);

/* TIME */
long		get_time_ms(void);
void		ft_usleep(long ms);

/* PARSE */
int			parse_args(t_data *data, char **av);

/* INIT */
int			init_data(t_data *data);
int			init_threads(t_data *data, int *created);
void		cleanup_data(t_data *data);

/* QUEUE (heap) - queue.c */
int			queue_init(t_queue *queue);
int			enqueue_request(t_queue *queue, int coder_id, long key);
int			dequeue_request(t_queue *queue, int *coder_id_out);
void		free_queue(t_queue *queue);

/* QUEUE (heap) - queue_heap.c */
void		swap_nodes(t_heap_node *a, t_heap_node *b);
void		sift_up(t_queue *queue, int i);
void		sift_down(t_queue *queue, int i);
int			heap_grow(t_queue *queue);

/* QUEUE (heap) - queue_utils.c */
int			queue_contains(t_queue *queue, int coder_id);
void		update_key(t_queue *queue, int coder_id, long new_key);
int			queue_peek(t_queue *queue);

/* DONGLE */
int			try_acquire_dongle(t_dongle *dongle, int coder_id,
				long deadline, char *scheduler);
void		release_dongle(t_dongle *dongle, long cooldown);
int			acquire_dongle(t_coder *coder, t_dongle *dongle, long deadline);

/* ROUTINE */
void		*coder_routine(void *arg);

/* LOG */
void		print_status(t_coder *coder, char *msg);

/* SIMULATION */
int			simulation_stopped(t_data *data);
void		stop_simulation(t_data *data);

/* MONITOR */
void		*monitor_routine(void *arg);

#endif
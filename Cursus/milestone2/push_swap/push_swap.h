/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 17:48:03 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/03 16:39:40 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "ft_printf/ft_printf.h"
# include "libft/libft.h"
# include <stdarg.h>
# include <unistd.h>
# include <stdint.h>
# include <stddef.h>
# include <stdlib.h>
# include <limits.h>

//Validaciones
int		ft_is_number(char *str);
int		ft_is_duplicate_number(int *num, size_t size);
long	ft_atoi2(char *str);
int		parse_args(int argc, char **argv, int **out, size_t *size);
int		split_len(char **str);
void	free_split(char **split);
char	*join_args(int argc, char **argv);
int		validate_and_convert(char **split, int **out, size_t size);

//Ordenamiento
void	sort_two(t_list **a);
void	sort_three(t_list **a);
void	sort_five(t_list **a);
void	push_smallest_to_b(t_list **a, t_list **b);
void	radix_sort(t_list **a, int *nums, size_t size);

//Indexing
void	sort_array(int *arr, size_t size);
int		get_index(int *arr, size_t size, int value);
int		max_bits(size_t size);

//Operaciones de pila A
void	ra(t_list **a);
void	pa(t_list **a, t_list **b);
void	sa(t_list **a);
void	rra(t_list **a);

//Operaciones de pila B
void	rb(t_list **b);
void	pb(t_list **a, t_list **b);
void	sb(t_list **b);
void	rrb(t_list **b);

//Operaciones de ambas pilas
void	ss(t_list **a, t_list **b);
void	rr(t_list **a, t_list **b);
void	rrr(t_list **a, t_list **b);
int		sort_nums(t_list *a);

#endif

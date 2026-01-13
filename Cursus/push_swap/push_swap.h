/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 17:48:03 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/13 20:27:57 by pmarcos-         ###   ########.fr       */
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
int		ft_is_duplicate_number(long *num, size_t size);
long	ft_atol(char *str);
int		parse_args(int argc, char **argv, long **out, size_t *size);
int		split_len(char **str);
void	free_split(char **split);
char	*join_args(int argc, char **argv);

//Operaciones de pila A
void	ra(t_list **a);
void	sa(t_list **a);

//Operaciones de pila B
void	rb(t_list **b);
void	sb(t_list **b);

//Operaciones de ambas pilas
void	ss(t_list **a, t_list *b);

#endif

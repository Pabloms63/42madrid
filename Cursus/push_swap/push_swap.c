/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 17:35:25 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/07 23:17:42 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	add_args_pila_a(t_list **a, int argc, char *argv[])
{
	t_list	*new;
	int		count;
	int		num;
	int		*value;

	count = 1;
	while (count < argc)
	{
		num = ft_atol(argv[count]);
		value = malloc(sizeof(int));
		*value = num;
		new = ft_lstnew(value);
		ft_lstadd_back(a, new);
		count++;
	}
}

static int	is_sorted(t_list *a)
{
	int	current;
	int	next;

	if (!a || !a -> next)
		return (1);
	while (a -> next)
	{
		current = *(int *)a -> content;
		next = *(int *)a -> next -> content;
		if (current > next)
			return (0);
		a = a -> next;
	}
	return (1);
}

int	main(int argc, char	*argv[])
{
	t_list	*a;

	a = NULL;
	if (!parse_args(argc, argv))
	{
		ft_printf("\nError\n");
		return (1);
	}
	add_args_pila_a(&a, argc, argv);
	if (is_sorted(a))
	{
		ft_lstclear(&a, free);
		return (0);
	}
	ft_lstclear(&a, free);
	return (0);
}

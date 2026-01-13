/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 17:35:25 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/13 20:09:35 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	add_nums_to_stack(t_list **a, long *nums, size_t size)
{
	size_t	i;
	int		*value;
	t_list	*new;

	i = 0;
	while (i < size)
	{
		value = malloc(sizeof(int));
		if (!value)
			return ;
		*value = (int)nums[i];
		new = ft_lstnew(value);
		ft_lstadd_back(a, new);
		i++;
	}
}

static int	sort_nums(t_list *a)
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

int	main(int argc, char **argv)
{
	t_list	*a;
	long	*nums;
	size_t	size;

	a = NULL;
	if (parse_args(argc, argv, &nums, &size))
		return (write(2, "Error\n", 6), 1);
	add_nums_to_stack(&a, nums, size);
	free(nums);
	if (sort_nums(a))
		return (ft_lstclear(&a, free), 0);
	ft_lstclear(&a, free);
	return (0);
}


/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   split_arg_quotes.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 20:53:02 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/13 20:33:07 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Returns the length of the string to split.
 */
int	split_len(char **str)
{
	int	cnt;

	cnt = 0;
	while (str[cnt])
		cnt++;
	return (cnt);
}

/**
 * @brief Free all the split.
 */
void	free_split(char **split)
{
	int	a;

	a = 0;
	while (split[a] != NULL)
		free(split[a++]);
	free(split);
}

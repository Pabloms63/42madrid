/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 11:24:15 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/12/29 18:23:57 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @param s El string a convertir
 * @param size
 */
void	ft_bzero(void *s, size_t size)
{
	unsigned char	*str;
	size_t			count;

	count = 0;
	str = (unsigned char *)s;
	while (count < size)
	{
		str[count] = 0;
		count++;
	}
}

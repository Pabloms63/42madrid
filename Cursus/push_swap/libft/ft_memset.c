/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/29 17:13:54 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/12/29 18:25:08 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	*ft_memset(void *s, int c, size_t size)
{
	unsigned char	*str;
	size_t			count;

	count = 0;
	str = s;
	while (count < size)
	{
		str[count] = (unsigned char)c;
		count++;
	}
	return (s);
}

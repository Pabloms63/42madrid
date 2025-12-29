/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 12:10:41 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/12/29 18:25:14 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	*ft_memmove(void *dest, const void *src, size_t size)
{
	char		*str_dest;
	const char	*str_src;
	size_t		count;

	str_dest = (char *)dest;
	str_src = (const char *)src;
	count = 0;
	if (str_dest < str_src)
	{
		while (count < size)
		{
			str_dest[count] = str_src[count];
			count++;
		}
	}
	else if (str_dest > str_src)
	{
		while (size > 0)
		{
			str_dest[size - 1] = str_src[size - 1];
			size--;
		}
	}
	return (dest);
}

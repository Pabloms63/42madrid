/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/30 14:58:25 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/12/29 18:26:31 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_strlcat(char *dest, const char *src, size_t size)
{
	size_t		size_dest;
	size_t		size_src;
	size_t		count_src;

	size_dest = 0;
	while (dest[size_dest] && size_dest < size)
		size_dest++;
	size_src = 0;
	while (src[size_src])
		size_src++;
	if (size <= size_dest)
		return (size + size_src);
	count_src = 0;
	while (src[count_src] && (size_dest + count_src) < size - 1)
	{
		dest[size_dest + count_src] = src[count_src];
		count_src++;
	}
	dest[size_dest + count_src] = '\0';
	return (size_src + size_dest);
}

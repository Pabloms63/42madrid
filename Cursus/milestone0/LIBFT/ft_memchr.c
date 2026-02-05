/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 17:21:15 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/17 17:10:09 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	size_t				count;
	const unsigned char	*str;

	count = 0;
	str = s;
	while (count < n && str[count] != (unsigned char)c)
	{
		count++;
	}
	if (count == n)
		return (NULL);
	return ((void *)(str + count));
}

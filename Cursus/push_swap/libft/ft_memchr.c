/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 17:21:15 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/12/29 18:24:52 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	const unsigned char	*str;
	size_t				cnt;

	str = s;
	cnt = 0;
	while (cnt < n)
	{
		if (str[cnt] == (unsigned char)c)
			return ((void *) str + cnt);
		cnt++;
	}
	return (NULL);
}

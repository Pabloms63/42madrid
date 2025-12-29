/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 19:05:26 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/12/29 18:26:17 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

char	*ft_strchr(const char *s, int c)
{
	size_t		count;

	count = 0;
	while (s[count])
	{
		if (s[count] == (unsigned char)c)
			return ((char *)s + count);
		count++;
	}
	if ((unsigned char)c == '\0')
		return ((char *)s + count);
	return (NULL);
}

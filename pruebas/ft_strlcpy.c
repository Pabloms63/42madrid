/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 14:33:16 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/16 14:47:45 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

size_t	strlcpy(char *dst, const char *src, size_t dstsize){
	size_t a;

	a = 0;
	if (dstsize > 0)
	{
		while (src[a] && a < dstsize - 1)
		{
			dst[a] = src[a];
			a++;	
		}
		dst[a] = '\0';
	}
	return (ft_strlen(src));
}

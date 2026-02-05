/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/29 18:24:53 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/02 18:20:42 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * @param dest String destino.
 * @param src Sring origen.
 * @param size Número de bytes.
 * @return Devuelve el tamaño del string de origen.
 */
size_t	ft_strlcpy(char *dest, const char *src, size_t size)
{
	size_t	count;
	size_t	len;

	len = ft_strlen(src);
	if (size < 1)
		return (len);
	count = 0;
	while (src[count] != '\0' && (count < size - 1))
	{
		dest[count] = src[count];
		count++;
	}
	dest[count] = '\0';
	return (len);
}

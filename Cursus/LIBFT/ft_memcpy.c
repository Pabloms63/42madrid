/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 11:40:46 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/20 15:44:59 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * Copia el contenido del puntero de memoria origen
 * en el puntero memoria destino.
 * @param dest Puntero de memoria de destino.
 * @param src Puntero de memoria de origen.
 * @param size Nímero de bytes a copiar.
 * @return Devuelve el puntero de memoria de destino.
 */
void	*ft_memcpy(void *dest, const void *src, size_t size)
{
	unsigned char		*str_dest;
	unsigned const char	*str_src;
	size_t				count;

	str_dest = (unsigned char *)dest;
	str_src = (unsigned const char *)src;
	count = 0;
	if (!dest && !src)
		return (NULL);
	while (count < size)
	{
		str_dest[count] = str_src[count];
		count++;
	}
	return (dest);
}

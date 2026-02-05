/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/29 17:13:54 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/20 15:45:03 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * Sustituye el contenido del puntero por el caracter 'c'
 * un número 'size' de veces.
 * @param s Puntero de memoria.
 * @param c Caracter.
 * @param size Número de bytes.
 * @return Devuelve el puntero de memoria.
 */
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

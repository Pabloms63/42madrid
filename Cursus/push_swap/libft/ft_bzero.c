/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 11:24:15 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/13 20:57:59 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/** 
 * Convierte un número de caracteres del string en ceros.
 * @param s Puntero al string.
 * @param size Número de caracteres a convertir.
*/
void	ft_bzero(void *s, size_t size)
{
	unsigned char	*str;
	size_t			count;

	count = 0;
	str = (unsigned char *)s;
	while (count < size)
	{
		str[count] = 0;
		count++;
	}
}

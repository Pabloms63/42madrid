/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 19:59:06 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/17 20:56:32 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * @brief  Busca la última aparición de un carácter en un string.
 *
 * Recorre la cadena 's' desde el final hacia el inicio buscando el carácter 'c'.
 * Si lo encuentra, devuelve un puntero a esa 
 * posición dentro de la cadena original.
 * Si no lo encuentra, devuelve NULL.
 *
 * @param s  La cadena de caracteres donde se busca.
 * @param c  El carácter que se desea encontrar (convertido a unsigned char).
 * @return   Un puntero a la última aparición de 
 * 'c' en 's', o NULL si no se encuentra.
 */
char	*ft_strrchr(const char *s, int c)
{
	int		len;

	len = ft_strlen(s);
	while (len >= 0)
	{
		if (s[len] == (unsigned char)c)
			return ((char *)s + len);
		len--;
	}
	return (NULL);
}

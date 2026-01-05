/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 19:05:26 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/17 20:59:23 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * @param s String constante.
 * @param c Caracter.
 * @return Devuelve el string desde la primera coincidencia
 *  hasta el fin, o null si no hay coincidencia.
 */
char	*ft_strchr(const char *s, int c)
{
	int		count;

	count = 0;
	while (s[count] != '\0')
	{
		if (s[count] == (unsigned char)c)
			return ((char *)s + count);
		count++;
	}
	if ((unsigned char)c == '\0')
		return ((char *)s + count);
	return (NULL);
}

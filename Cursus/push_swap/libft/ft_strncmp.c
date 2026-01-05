/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 16:06:17 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/02 18:27:09 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * @param s1 String 1.
 * @param s2 String 2.
 * @param n Número de bytes.
 * @return Devuelve la diferencia entre caracteres comparados.
 */
int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	size_t	count;

	if (n < 1)
		return (0);
	count = 0;
	while ((s1[count] != '\0' || s2[count] != '\0') && count < n)
	{
		if (s1[count] != s2[count])
			return ((unsigned char)s1[count] - (unsigned char)s2[count]);
		count++;
	}
	return (0);
}

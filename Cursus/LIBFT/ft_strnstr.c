/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 18:59:20 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/17 12:45:57 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * @param big String donde buscar.
 * @param little String a buscar.
 * @param len Número de bytes máximo que se deben buscar.
 * @return Devuelve un puntero desde el inicio de la subcadena
 * al final de la cadena. O null si la subcadena no se encuentra en la cadena.
 */
char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t		cnt_big;
	size_t		cnt_little;

	cnt_big = 0;
	cnt_little = 0;
	if (little[cnt_little] == '\0')
		return ((char *)big);
	while ((cnt_big < len) && (big[cnt_big] != '\0'))
	{
		cnt_little = 0;
		while (little[cnt_little] != '\0'
			&& big[cnt_big + cnt_little] != '\0'
			&& (cnt_big + cnt_little) < len
			&& big[cnt_big + cnt_little] == little[cnt_little])
		{
			cnt_little++;
		}
		if (little[cnt_little] == '\0')
			return ((char *) big + cnt_big);
		cnt_big++;
	}
	return (NULL);
}

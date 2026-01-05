/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/29 16:28:34 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/02 18:25:32 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * @param str String.
 * @return Devuelve el tamaño del String.
 */
int	ft_strlen(const char *str)
{
	int		count;

	count = 0;
	while (str[count] != '\0')
		count++;
	return (count);
}

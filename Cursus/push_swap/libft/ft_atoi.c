/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/30 16:38:59 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/12/29 18:23:52 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Convierte un string de caracters a entero.
 * @param nptr El string de caracteres
 * @return El entero resultante.
 */
int	ft_atoi(const char *nptr)
{
	int		count;
	int		sign;
	int		res;

	res = 0;
	count = 0;
	sign = 1;
	while ((nptr[count] == 32) || (nptr[count] >= 9 && nptr[count] <= 13))
		count++;
	if (nptr[count] == '-' || nptr[count] == '+')
	{
		if (nptr[count] == '-')
			sign = -1;
		count++;
	}
	while (nptr[count] >= '0' && nptr[count] <= '9')
	{
		res = res * 10 + (nptr[count] - '0');
		count++;
	}
	return (res * sign);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/30 16:38:59 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/17 17:25:50 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * @brief Convierte un string en un número entero (int).
 *
 * Analiza el string 'nptr' y devuelve su valor numérico como un entero.
 * Ignora espacios en blanco iniciales, admite signos '+' o '-' y convierte 
 * la secuencia numérica consecutiva.
 *
 * @param nptr  El string que representa un número
 * (puede incluir espacios y signo).
 * @return      El número entero resultante de la conversión.
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

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/03 18:47:08 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/10 13:32:59 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * @brief Reserva memoria e inicializa a cero
 *
 * ft_calloc reserva suficiente memoria para almacenar 'count'
 * elementos de tamaño 'size' y establece todos los bytes a cero.
 *
 * @param count Número de elementos a reservar.
 * @param size Tamaño en bytes de cada elemento.
 * @return void* Puntero a la memoria reservada e inicializada a cero.
 *               Devuelve NULL si la reserva falla.
 */
void	*ft_calloc(size_t nmeb, size_t size)
{
	size_t	total;
	void	*ptr;

	total = nmeb * size;
	ptr = malloc(total);
	ft_bzero(ptr, total);
	return (ptr);
}

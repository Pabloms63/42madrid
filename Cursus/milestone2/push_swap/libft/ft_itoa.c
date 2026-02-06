/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 16:07:09 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/06 18:32:03 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * @brief Cuenta todos los dígitos de un número entero
 */
int	ft_cnt_digits(int n)
{
	int		len;
	long	num;

	len = 0;
	num = (long)n;
	if (num <= 0)
	{
		num = -num;
		len++;
	}
	while (num > 0)
	{
		num /= 10;
		len++;
	}
	return (len);
}

/**
 * @brief Convierte un entero en un string.
 */
char	*ft_itoa(int n)
{
	int		len;
	long	num;
	char	*str;

	num = (long)n;
	len = ft_cnt_digits(num);
	str = malloc(sizeof(char) * (len + 1));
	if (!str)
		return (NULL);
	str[len] = '\0';
	if (num == 0)
		str[0] = '0';
	if (num < 0)
	{
		str[0] = '-';
		num *= -1;
	}
	while (num > 0)
	{
		len--;
		str[len] = (num % 10) + '0';
		num /= 10;
	}
	return (str);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils2.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/02 16:30:07 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/11/03 16:52:36 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_puthexlower_fd(unsigned long long n, int fd)
{
	char	digit;
	int		count;

	digit = 0;
	count = 0;
	if (n >= 16)
	{
		count += ft_puthexlower_fd(n / 16, fd);
	}
	if ((n % 16) > 9)
		digit = (n % 16) + 'a' - 10;
	else
		digit = (n % 16) + '0';
	write(fd, &digit, 1);
	return (count + 1);
}

int	ft_puthexupper_fd(unsigned long long n, int fd)
{
	char	digit;
	int		mayus;
	int		count;

	digit = 0;
	count = 0;
	if (n >= 16)
	{
		count += ft_puthexupper_fd(n / 16, fd);
	}
	if ((n % 16) > 9)
		digit = (n % 16) + 'a' - 10;
	else
		digit = (n % 16) + '0';
	mayus = (char)ft_toupper((int)digit);
	write(fd, &mayus, 1);
	return (count + 1);
}

int	ft_putnbr_unsigned_fd(unsigned int n, int fd)
{
	int	count;

	count = 0;
	if (n >= 10)
		count += ft_putnbr_unsigned_fd(n / 10, fd);
	ft_putchar_fd((n % 10) + '0', fd);
	return (count + 1);
}

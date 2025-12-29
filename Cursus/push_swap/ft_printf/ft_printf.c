/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 20:09:56 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/12/29 18:31:15 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	handle_str(int count, va_list args)
{
	char	*str;

	str = va_arg(args, char *);
	if (!str)
		count += ft_putstr_fd_printf("(null)", 1);
	else
		count += ft_putstr_fd_printf(str, 1);
	return (count);
}

int	handle_ptr(int count, va_list args)
{
	void	*ptr;

	ptr = va_arg(args, void *);
	if (!ptr)
		count += ft_putstr_fd_printf("(nil)", 1);
	else
	{
		count += ft_putstr_fd_printf("0x", 1);
		count += ft_puthexlower_fd((unsigned long long)ptr, 1);
	}
	return (count);
}

int	handle_formats(char format, va_list args)
{
	int		count;

	count = 0;
	if (format == 'c')
		count += ft_putchar_fd_printf(va_arg(args, int), 1);
	else if (format == 's')
		count += handle_str(count, args);
	else if (format == 'p')
		count += handle_ptr(count, args);
	else if (format == 'd' || format == 'i')
		count += ft_putnbr_fd_printf(va_arg(args, int), 1);
	else if (format == 'u')
		count += ft_putnbr_unsigned_fd(va_arg(args, unsigned int), 1);
	else if (format == 'x')
		count += ft_puthexlower_fd
			((unsigned long long)va_arg(args, unsigned int), 1);
	else if (format == 'X')
		count += ft_puthexupper_fd
			((unsigned long long)va_arg(args, unsigned int), 1);
	return (count);
}

int	ft_printf(const char *format, ...)
{
	va_list	args;
	int		count;

	count = 0;
	if (!format)
		return (-1);
	va_start(args, format);
	while (*format)
	{
		if (*format == '%')
		{
			format++;
			if (*format == '%')
				count += ft_putchar_fd_printf('%', 1);
			else
				count += handle_formats(*format, args);
		}
		else
			count += ft_putchar_fd_printf(*format, 1);
		format++;
	}
	va_end(args);
	return (count);
}

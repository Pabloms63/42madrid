/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/02 16:23:03 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/12/29 18:31:39 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_putchar_fd_printf(char c, int fd)
{
	write(fd, &c, 1);
	return (1);
}

int	ft_putstr_fd_printf(char *s, int fd)
{
	int	len;

	if (!s)
		return (ft_putstr_fd_printf("(null)", fd));
	len = ft_strlen(s);
	if (len == 0)
		return (0);
	write(fd, s, len);
	return (len);
}

int	ft_putnbr_fd_printf(int n, int fd)
{
	long	num;
	char	digit;
	int		count;

	count = 0;
	num = (long)n;
	if (num < 0)
	{
		write(fd, "-", 1);
		num = -num;
		count++;
	}
	if (num == 0)
	{
		write(fd, "0", 1);
		return (1);
	}
	if (num >= 10)
		count += ft_putnbr_fd_printf(num / 10, fd);
	digit = (num % 10) + '0';
	write(fd, &digit, 1);
	return (count + 1);
}

int	ft_strlen(const char *str)
{
	int		count;

	if (!str)
		return (0);
	count = 0;
	while (str[count] != '\0')
		count++;
	return (count);
}

int	ft_toupper(int c)
{
	if (c >= 97 && c <= 122)
		c = c - 32;
	return (c);
}

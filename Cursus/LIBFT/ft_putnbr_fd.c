/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 21:03:11 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/17 20:50:57 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	long	num;
	char	c;
	char	minus;

	minus = '-';
	num = (long)n;
	if (num < 0)
	{
		write(fd, &minus, 1);
		num *= -1;
	}
	if (num >= 10)
		ft_putnbr_fd((num / 10), fd);
	c = num % 10 + '0';
	write(fd, &c, 1);
}

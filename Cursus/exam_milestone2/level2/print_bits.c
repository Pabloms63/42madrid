/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_bits.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 17:49:48 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/28 20:59:54 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	print_bits(unsigned char octet)
{
	int		cnt;
	char	bit;

	cnt = 7;
	while (cnt >= 0)
	{
		bit = ((octet >> cnt) & 1) + '0';
		write (1, &bit, 1);
		cnt--;
	}
}

int	main(void)
{
	print_bits('c');
	write(1, "\n", 1);
	return (0);
}

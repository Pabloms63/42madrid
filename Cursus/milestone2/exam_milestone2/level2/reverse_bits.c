/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   reverse_bits.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 20:54:47 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/29 12:18:05 by pmarcos-         ###   ########.fr       */
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

unsigned char	reverse_bits(unsigned char octet)
{
	unsigned char	reversed;
	int				cnt;

	reversed = 0;
	cnt = 8;
	while (cnt--)
	{
		reversed = (reversed << 1) | (octet & 1);
		octet = octet >> 1;
	}
	return (reversed);
}

int	main(void)
{
	unsigned char	c;
	unsigned char	rev;

	c = 'c';
	rev = reverse_bits(c);
	print_bits(rev);
}

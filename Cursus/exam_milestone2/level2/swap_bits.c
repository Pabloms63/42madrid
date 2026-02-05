/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap_bits.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 20:14:11 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/29 12:15:34 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


unsigned char	swap_bits(unsigned char octet)
{
	return ((octet >> 4 || octet << 4));
}

int	main(void)
{
	swap_bits('c');
	return (0);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   lcm.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/23 18:01:13 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/23 18:24:13 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

unsigned int    lcm(unsigned int a, unsigned int b)
{
	unsigned int x = a;
	unsigned int y = b;
	unsigned int r;

	if ((int)a <= 0 || (int)b <= 0)
		return (0);
	while (y != 0)
	{
		r = x % y;
		x = y;
		y = r;
	}
	return ((a / x) * b);
}

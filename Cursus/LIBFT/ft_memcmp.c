/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 18:58:54 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/03 19:47:38 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	size_t				count;
	const unsigned char	*s1_char;
	const unsigned char	*s2_char;

	s1_char = s1;
	s2_char = s2;
	count = 0;
	while (count < n)
	{
		if (s1_char[count] != s2_char[count])
			return (s1_char[count] - s2_char[count]);
		count++;
	}
	return (0);
}

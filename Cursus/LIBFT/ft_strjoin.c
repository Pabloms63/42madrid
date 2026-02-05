/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 18:20:38 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/17 13:13:21 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * @param
 * @param
 * @return
 */
char	*ft_strjoin(char const *s1, char const *s2)
{
	int		a;
	int		b;
	char	*s3;

	s3 = malloc(ft_strlen(s1) + ft_strlen(s2) + 1);
	if (!s3)
		return (NULL);
	a = 0;
	while (s1[a] != '\0')
	{
		s3[a] = s1[a];
		a++;
	}
	b = 0;
	while (s2[b] != '\0')
	{
		s3[a + b] = s2[b];
		b++;
	}
	s3[a + b] = '\0';
	return (s3);
}

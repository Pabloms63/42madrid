/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strspn.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 23:53:29 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/28 00:16:21 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

size_t	ft_strspn(const char *s, const char *charset)
{
	size_t	i;
	size_t	j;
	int		found;

	i = 0;
	while (s[i] != '\0')
	{
		found = 0;
		j = 0;
		while (charset[j] != '\0')
		{
			if (s[i] == charset[j])
			{
				found = 1;
				break ;
			}
			j++;
		}
		if (found == 0)
			return (i);
		i++;
	}
	return (i);
}


int	main(void)
{
	printf("%ld\n", ft_strspn("1234hola", "0123456789"));

	return (0);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrev.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 00:30:59 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/28 02:03:35 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	cnt;

	cnt = 0;
	while (str[cnt])
		cnt++;
	return (cnt);
}

char	*ft_strrev(char *str)
{
	char	*s_def;
	int		c1;
	int		c2;
	int		len;

	len = ft_strlen(str);
	c1 = len - 1;
	c2 = 0;
	s_def = malloc(c1 + 1);
	if (!s_def)
		return (NULL);
	while (c1 >= 0)
	{
		s_def[c2] = str[c1];
		c1--;
		c2++;
	}
	s_def[c2] = '\0';
	return (s_def);
}

int	main(void)
{
	char	*str;
	char	*rev;

	str = "Hola";
	rev = ft_strrev(str);
	printf("%s\n", rev);
	free(rev);
	return (0);
}

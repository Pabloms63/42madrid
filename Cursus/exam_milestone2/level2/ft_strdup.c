/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 20:46:39 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/27 23:16:08 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	cnt;

	cnt = 0;
	while (str[cnt])
		cnt++;
	return (cnt);
}

char	*ft_strdup(char *src)
{
	int		cnt;
	char	*str;
	int		len;

	cnt = 0;
	len = ft_strlen(src);
	str = malloc(len + 1);
	if (!str)
		return (NULL);
	while (src[cnt])
	{
		str[cnt] = src[cnt];
		cnt++;
	}
	str[cnt] = '\0';
	return (str);
}

int	main(void)
{
	printf("%s\n", ft_strdup("Holaa que tal"));
	return (0);
}

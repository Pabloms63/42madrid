/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 15:43:21 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/11/05 17:12:20 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

int	ft_strlen(const char *str)
{
	int		count;

	if (!str)
		return (0);
	count = 0;
	while (str[count] != '\0')
		count++;
	return (count);
}

char	*ft_strjoin(char const *s1, char const *s2)
{
	int		a;
	int		b;
	char	*s3;

	if (!s1)
		return (ft_strdup(s2));
	if (!s2)
		return (ft_strdup(s1));
	s3 = malloc(ft_strlen(s1) + ft_strlen(s2) + 1);
	if (!s3 || (!s1 && !s2))
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

char	*ft_strchr(const char *s, int c)
{
	size_t		count;

	count = 0;
	while (s[count])
	{
		if (s[count] == (unsigned char)c)
			return ((char *)s + count);
		count++;
	}
	if ((unsigned char)c == '\0')
		return ((char *)s + count);
	return (NULL);
}

char	*ft_strdup(const char *s)
{
	char	*new_s;
	int		count;
	size_t	len;

	len = ft_strlen(s);
	new_s = malloc(sizeof(char) * (len + 1));
	if (!new_s)
		return (NULL);
	count = 0;
	while (s[count] != '\0')
	{
		new_s[count] = s[count];
		count++;
	}
	new_s[count] = '\0';
	return (new_s);
}

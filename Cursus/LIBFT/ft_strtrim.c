/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 19:59:05 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/17 18:33:24 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	is_in_set(char c, const char *set)
{
	int	a;

	a = 0;
	while (set[a] != '\0')
	{
		if (set[a] == c)
			return (1);
		a++;
	}
	return (0);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	int		start;
	int		end;
	int		len_new;
	char	*shorted;

	if (!s1 || !set)
		return (NULL);
	start = 0;
	while (is_in_set(s1[start], set))
	{
		start++;
	}
	end = (ft_strlen(s1) - 1);
	while (end > start && is_in_set(s1[end], set))
	{
		end --;
	}
	len_new = end - start + 1;
	shorted = malloc(sizeof(char) * (len_new + 1));
	ft_strlcpy(shorted, s1 + start, len_new + 1);
	return (shorted);
}

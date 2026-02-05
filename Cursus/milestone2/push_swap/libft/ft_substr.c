/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/03 20:17:13 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/17 13:18:02 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * @param 
 * @param
 * @param
 * @return
 */
char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	size_t	a;
	size_t	s_len;
	char	*new_s;

	if (!s)
		return (NULL);
	s_len = ft_strlen(s);
	if (start >= s_len)
		return (ft_strdup(""));
	if (len > s_len - start)
		len = s_len - start;
	new_s = malloc(len + 1);
	if (!new_s)
		return (NULL);
	a = 0;
	while (a < len && s[start + a])
	{
		new_s[a] = s[start + a];
		a++;
	}
	new_s[a] = '\0';
	return (new_s);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/03 19:49:48 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/03 20:14:19 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	char	*new_s;
	int		count;

	if (!s)
		return (NULL);
	new_s = malloc(ft_strlen(s) + 1);
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

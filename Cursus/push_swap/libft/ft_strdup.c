/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/03 19:49:48 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/12/29 18:26:19 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

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

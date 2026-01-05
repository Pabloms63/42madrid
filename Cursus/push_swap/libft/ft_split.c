/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/08 20:11:36 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/17 18:44:21 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_cnt_wrds(const char *s, char c)
{
	int	a;
	int	new_word;

	a = 0;
	new_word = 0;
	while (s[a])
	{
		while (s[a] == c)
			a++;
		if (s[a] && s[a] != c)
		{
			new_word++;
			while (s[a] && s[a] != c)
				a++;
		}
	}
	return (new_word);
}

int	*ft_size_wrds(const char *s, char c, int num_wrds)
{
	int	a;
	int	b;
	int	start;
	int	len;
	int	*size_wrds;

	size_wrds = malloc(sizeof(int) * num_wrds);
	if (!size_wrds)
		return (NULL);
	a = 0;
	b = 0;
	while (s[a] && b < num_wrds)
	{
		while (s[a] == c)
			a++;
		start = a;
		while (s[a] != c && s[a])
			a++;
		len = a - start;
		size_wrds[b] = len;
		b++;
	}
	return (size_wrds);
}

char	**ft_fill_split(const char *s, char c, int num_wrds, int *size_wrd)
{
	int		a;
	int		b;
	int		z;
	char	**str_def;

	str_def = malloc(sizeof(char *) * (num_wrds + 1));
	if (!str_def)
		return (NULL);
	a = 0;
	b = 0;
	while (s[a] && b < num_wrds)
	{
		while (s[a] == c)
			a++;
		str_def[b] = malloc(sizeof(char) * (size_wrd[b] + 1));
		if (!str_def[b])
			return (NULL);
		z = 0;
		while (s[a] != c && s[a])
			str_def[b][z++] = s[a++];
		str_def[b][z] = '\0';
		b++;
	}
	str_def[b] = NULL;
	return (str_def);
}

char	**ft_split(const char *s, char c)
{
	int		num_wrds;
	int		*len_wrds;
	char	**str_def;

	num_wrds = ft_cnt_wrds(s, c);
	len_wrds = ft_size_wrds(s, c, num_wrds);
	if (!len_wrds)
		return (NULL);
	str_def = ft_fill_split(s, c, num_wrds, len_wrds);
	free(len_wrds);
	return (str_def);
}

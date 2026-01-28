/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   last_word.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 02:06:33 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/28 02:28:43 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	ft_strlen(char *str)
{
	int	cnt;

	cnt = 0;
	while (str[cnt])
		cnt++;
	return (cnt);
}

int	main(int argc, char **argv)
{
	int	len;
	int	end;

	if (argc == 2)
	{
		len = ft_strlen(argv[1]) - 1;
		while (len >= 0 && (argv[1][len] == ' ' || argv[1][len] == '\t'))
			len--;
		end = len;
		while (len >= 0 && (argv[1][len] != ' ' && argv[1][len] != '\t'))
			len--;
		write(1, &argv[1][len + 1], end - len);
	}
	write(1, "\n", 1);
	return (0);
}

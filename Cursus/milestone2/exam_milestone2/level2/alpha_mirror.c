/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   alpha_mirror.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 21:17:30 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/25 17:07:49 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(int argc, char **argv)
{
	int		cnt;
	char	word;

	cnt = 0;
	if (argc == 2)
	{
		while (argv[1][cnt])
		{
			word = argv[1][cnt];
			if (word >= 65 && word <= 90)
				word = 90 - word + 65;
			else if (word >= 97 && word <= 122)
				word = 122 - word + 97;
			write(1, &word, 1);
			cnt++;
		}
	}
	write(1, "\n", 1);
}

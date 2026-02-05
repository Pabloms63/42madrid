/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   camel_to_snake.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/25 16:52:41 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/25 17:07:41 by pmarcos-         ###   ########.fr       */
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
			if ((word >= 65 && word <= 90) || (word >= 97 && word <= 122))
			{
				if (word >= 97 && word <= 122)
					write (1, &word, 1);
				else if (word >= 65 && word <= 90)
				{
					write(1, "_", 1);
					word += 32;
					write(1, &word, 1);
				}
			}
			cnt++;
		}
	}
}

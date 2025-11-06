/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 15:43:33 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/11/06 14:11:53 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*extract_line(char *str_og)
{
	int		count;
	char	*str2;

	if (!str_og)
		return (NULL);
	count = 0;
	while (str_og[count] && str_og[count] != '\n')
		count++;
	if (str_og[count] == '\n')
		count++;
	str2 = malloc(count + 1);
	if (!str2)
		return (NULL);
	count = 0;
	while (str_og[count] && str_og[count] != '\n')
	{
		str2[count] = str_og[count];
		count++;
	}
	if (str_og[count] == '\n')
		str2[count++] = '\n';
	str2[count] = '\0';
	return (str2);
}

char	*update_line(char *str_og)
{
	int		count_og;
	int		count_str2;
	int		len;
	char	*str2;

	count_og = 0;
	len = ft_strlen(str_og);
	while (str_og[count_og] && str_og[count_og] != '\n')
		count_og++;
	if (str_og[count_og] == '\n')
		count_og ++;
	str2 = malloc((len - count_og) + 1);
	if (!str2)
		return (NULL);
	count_str2 = 0;
	while (str_og[count_og])
	{
		str2[count_str2] = str_og[count_og];
		count_og++;
		count_str2++;
	}
	str2[count_str2] = '\0';
	free(str_og);
	return (str2);
}

char	*exceptios_and_malloc_buffer(int fd)
{
	char	*buffer;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	buffer = malloc(BUFFER_SIZE + 1);
	if (!buffer)
		return (NULL);
	return (buffer);
}

char	*get_next_line(int fd)
{
	static char	*saved;
	char		*temp;
	char		*buffer;
	char		*line;
	int			bytes_read;

	buffer = exceptios_and_malloc_buffer(fd);
	bytes_read = 1;
	while ((!saved || !ft_strchr(saved, '\n')) && bytes_read > 0)
	{
		bytes_read = read(fd, buffer, BUFFER_SIZE);
		if (bytes_read > 0)
		{
			buffer[bytes_read] = '\0';
			temp = saved;
			saved = ft_strjoin(saved, buffer);
			free(temp);
		}
	}
	free(buffer);
	if (!saved || !*saved)
		return (NULL);
	line = extract_line(saved);
	saved = update_line(saved);
	return (line);
}

int	main(void)
{
	int		fd;
	char	*line;

	fd = open("test.txt", O_RDONLY);
	if (fd == -1)
	{
		printf("Error al abrir archivo\n");
		return (1);
	}
	while ((line = get_next_line(fd)))
	{
		printf("%s", line);
		free(line);
	}
	close(fd);
	return (0);
}

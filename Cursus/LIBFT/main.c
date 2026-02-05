/* ************************************************************************** */

/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/29 17:27:58 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/10/03 20:37:01 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int		main(void)
{
	//Variables para bzero:
	char str_bz[50] = "texto para bzero";
	size_t n_bz = 12;
	//Variables para calloc:
	size_t n_meb = 5;
	size_t size_calloc = 8;
	//Variables para memchr:
	const char *str_mchr = "texto para memchr";
	int c_mchr = 'r';
	size_t n_mchr = 12;
	//Variables para memcmp:
	const char *s1_memcmp = "texto 1 para memcmp";
	const char *s2_memcmp = "texto 2 para memcmp";
	size_t n_memcmp = 13;
	//Variables para memcpy:
	char	dest_mc[50];
	const char	*src_mc = "texto para memcpy";
	//Variables para memmove:
	char	dest_mm[50];
	const char	*src_mm = "texto para memmove";
	size_t	n_mm = 12;
	//Variables para memset:
	char	str_ms[] = "texto para memset";
	int		c_ms = '$';
	size_t	n_ms = 10;
	//Variables para strchr:
	const char *cc_sc = "texto para strchr";
	int	c_sc = 'a';
	//Variables para strdup:
	const char *str_strdup = "texto para strdup";
	//Variables para strlcat:
	char dest_slcat[] = "texto 1";
	const char *src_slcat = " + texto 2 strlcat";
	size_t n_slcat = 15;
	//Variables para strlcpy:
	char dest_slcpy[] = "txt1";
	const char *src_slcpy = "texto_definito1";
	size_t n_slcpy = 8;
	//Variables para strncmp:
	const char *str_scmp1 = "texto 1 de strcpy";
	const char *str_scmp2 = "texto 2 de strcpy";
	size_t n_scmp = 7;
	//Variables para strrchr:
	const char *cc_srrc = "texto para strrchr";
	int c_srrchr = 'p';
	//Variables para strnstr:
	const char *big_strnstr = "texto 1 para strnstr";
	const char *little_strnstr = "para";
	size_t n_strnstr = 12; 
	//Variables para substr:
	const char *str_substr = "texto para substr";
	unsigned int n_substr = 8;
	size_t len_substr = 9;
	//Variables para split:
	const char *str_split = "Hola a todos";
	char c_split = ' ';

	printf("ft_atoi: %d\n", ft_atoi("433543"));
	printf("ft_bzero antes: %s\n", str_bz);
	ft_bzero(str_bz, n_bz);
	printf("ft_bzero después: %s\n", str_bz);
	printf("ft_calloc: %p\n", ft_calloc(n_meb, size_calloc));
	printf("ft_isalnum: %d\n", ft_isalnum('h'));
	printf("ft_isalpha: %d\n", ft_isalpha('h'));
	printf("ft_isascii: %d\n", ft_isascii('h'));
	printf("ft_isdigit: %d\n", ft_isdigit('h'));
	printf("ft_isprint: %d\n", ft_isprint('h'));
	printf("ft_memchr: %p\n", ft_memchr(str_mchr, c_mchr, n_mchr));
	ft_memcpy(dest_mc, src_mc, 12);
	printf("ft_memcmp: %d\n", ft_memcmp(s1_memcmp, s2_memcmp, n_memcmp));
	printf("ft_memcpy: %s\n", dest_mc);
	ft_memmove(dest_mm, src_mm, n_mm);
	printf("ft_memmove: %s\n", dest_mm);
	ft_memset(str_ms, c_ms, n_ms);
	printf("ft_memset: %s\n", str_ms);
	char **matriz_split = ft_split(str_split, c_split);
	int i = 0;
	while (matriz_split[i] != NULL)
	{
		printf("%s\n", matriz_split[i]);
		i++;
	}
	ft_putchar_fd('h', 2);
	ft_putendl_fd("texto de ft_putendl!!!", 2);
	ft_putnbr_fd(7, 1);
	ft_putstr_fd("texto de ft_putstr!!!", 1);
	printf("ft_strchr: %s\n", ft_strchr(cc_sc, c_sc));
	printf("ft_strdup: %s\n", ft_strdup(str_strdup));
	printf("ft_strlcat: %d\n", ft_strlcat(dest_slcat, src_slcat, n_slcat));
	printf("ft_strlcpy: %ld\n", ft_strlcpy(dest_slcpy, src_slcpy, n_slcpy));
	printf("ft_strlen: %d\n", ft_strlen("holaaaa"));
	printf("ft_strncmp: %d\n", ft_strncmp(str_scmp1, str_scmp2, n_scmp));
	printf("ft_strnstr: %s\n",
		ft_strnstr(big_strnstr, little_strnstr, n_strnstr));
	printf("ft_strrchr: %s\n", ft_strrchr(cc_srrc, c_srrchr));
	printf("ft_substr: %s\n", ft_substr(str_substr, n_substr, len_substr));
	printf("ft_tolower: %c\n", ft_tolower('H'));
	printf("ft_toupper: %c\n", ft_toupper('h'));
	return (0);
}

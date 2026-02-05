/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/02 16:29:33 by pmarcos-          #+#    #+#             */
/*   Updated: 2025/11/02 19:40:09 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <stdio.h>
# include <unistd.h>

int		ft_puthexlower_fd(unsigned long long n, int fd);
int		ft_putchar_fd(char c, int fd);
int		ft_putstr_fd(char *s, int fd);
int		ft_putnbr_fd(int n, int fd);
int		ft_putnbr_unsigned_fd(unsigned int n, int fd);
int		ft_puthexupper_fd(unsigned long long n, int fd);
int		ft_strlen(const char *str);
int		ft_toupper(int c);
int		ft_printf(const char *format, ...);
int		handle_formats(char format, va_list args);

#endif

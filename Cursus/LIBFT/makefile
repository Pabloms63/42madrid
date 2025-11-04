# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/20 21:26:53 by pmarcos-          #+#    #+#              #
#    Updated: 2025/10/20 22:01:10 by pmarcos-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC = gcc
CFLAGS = -Wall -Wextra -Werror

NAME = libft.a

# Archivos fuente obligatorios
SRC = $(filter-out ft_lst%.c,$(wildcard *.c))   
BONUS = $(wildcard ft_lst*.c)                   
OBJ = $(SRC:.c=.o)
BONUS_OBJ = $(BONUS:.c=.o)


# **************************************************************************** #
#                               REGLAS PRINCIPALES                              #
# **************************************************************************** #

all: $(NAME)

$(NAME): $(OBJ)
	ar rcs $(NAME) $(OBJ)
	ranlib $(NAME)

# Target para compilar bonus
bonus: $(NAME) $(BONUS_OBJ)
	ar rcs $(NAME) $(OBJ) $(BONUS_OBJ)
	ranlib $(NAME)


# Compilación genérica de .c a .o
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Limpiar archivos .o
clean:
	rm -f $(OBJ) $(BONUS_OBJ)

# Limpiar .o y la librería
fclean: clean
	rm -f $(NAME)

# Recompilar todo
re: fclean all

# **************************************************************************** #
#                                  PRUEBAS                                     #
# **************************************************************************** #
test: $(NAME) main.c
	$(CC) $(CFLAGS) main.c -L. -lft -o test_prog
	./test_prog
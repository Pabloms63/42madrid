# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/02 18:22:42 by pmarcos-          #+#    #+#              #
#    Updated: 2026/02/03 16:40:19 by pmarcos-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC = cc
CFLAGS = -Wall -Werror -Wextra
RM = rm -f

NAME = push_swap

# Source files
SRCS = push_swap.c \
		operations_a.c \
		operations_b.c \
		operations_both.c \
		sorting.c \
		validations.c \
		split_utils.c \
		indexing.c \
		parse_args.c

# Object files
OBJS = $(SRCS:.c=.o)

# Libft
LIBFT_DIR = libft
LIBFT = $(LIBFT_DIR)/libft.a

# ft_printf
PRINTF_DIR = ft_printf
PRINTF = $(PRINTF_DIR)/libftprintf.a

# Header
HEADER = push_swap.h

# Colors
GREEN = \033[0;32m
RED = \033[0;31m
RESET = \033[0m

all: $(NAME)

$(NAME): $(LIBFT) $(PRINTF) $(OBJS)
	@$(CC) $(CFLAGS) $(OBJS) $(PRINTF) $(LIBFT) -o $(NAME)
	@echo "$(GREEN)✓ push_swap compilado correctamente$(RESET)"

%.o: %.c $(HEADER)
	@$(CC) $(CFLAGS) -c $< -o $@
	@echo "$(GREEN)✓ Compilado: $<$(RESET)"

$(LIBFT):
	@make -C $(LIBFT_DIR)
	@make bonus -C $(LIBFT_DIR)

$(PRINTF):
	@make -C $(PRINTF_DIR)

clean:
	@$(RM) $(OBJS)
	@make -C $(LIBFT_DIR) clean
	@make -C $(PRINTF_DIR) clean
	@echo "$(RED)✗ Archivos objeto eliminados$(RESET)"

fclean: clean
	@$(RM) $(NAME)
	@make -C $(LIBFT_DIR) fclean
	@make -C $(PRINTF_DIR) fclean
	@echo "$(RED)✗ Ejecutable eliminado$(RESET)"

re: fclean all

.PHONY: all clean fclean re
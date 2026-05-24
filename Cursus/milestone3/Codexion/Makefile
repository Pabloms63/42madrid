NAME = codexion

CC = cc
CFLAGS = -Wall -Wextra -Werror -pthread

SRC = main.c \
	time.c \
	parser.c \
	utils.c \
	init.c \
	log.c \
	routine.c

OBJ = $(SRC:.c=.o)

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $(NAME)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all
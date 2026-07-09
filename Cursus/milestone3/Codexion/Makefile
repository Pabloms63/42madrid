NAME = codexion

CC = cc
CFLAGS = -Wall -Wextra -Werror -pthread
RM = rm -f

SRC = main.c \
	time.c \
	parser.c \
	utils.c \
	init.c \
	log.c \
	routine.c \
	simulation.c \
	dongle.c \
	monitor.c \
	queue.c \
	queue_heap.c \
	queue_utils.c

OBJ = $(SRC:.c=.o)

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $(NAME)


.PHONY: all clean fclean re

clean:
	$(RM) $(OBJ)

fclean: clean
	$(RM) $(NAME)

re: fclean all
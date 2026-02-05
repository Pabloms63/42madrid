all: clean executable execute

executable: main.o ft_putchar.o ft_putstr.o ft_strcmp.o ft_strlen.o
	gcc -Wall -Wextra -Werror main.o ft_putchar.o ft_putstr.o ft_strcmp.o ft_strlen.o -o executable	

main.o: main.c
	gcc -Wall -Wextra -Werror -c main.c

ft_putchar.o: ft_putchar.c
	gcc -Wall -Wextra -Werror -c ft_putchar.c

ft_putstr.o: ft_putstr.c
	gcc -Wall -Wextra -Werror -c ft_putstr.c

ft_strcmp.o: ft_strcmp.c
	gcc -Wall -Wextra -Werror -c ft_strcmp.c

ft_strlen.o: ft_strlen.c
	gcc -Wall -Wextra -Werror -c ft_strlen.c

execute:
	./executable

clean:
	rm -f *.o executable


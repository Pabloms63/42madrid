#include <unistd.h>

void ft_putstr(char *str){
    int count = 0;
    while(str[count] != '\0'){
        char c = str[count];
        write(1, &c, 1);
        count++;
    }
}

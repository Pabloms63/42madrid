#include <stdio.h>

int ft_strlen(char *str){
    int count = 0;
    while(str[count] != '\0'){
        count++;
    }
    return (count);
}

int main(void){
    printf("Tamaño del string: %d\n", ft_strlen("Hola que tal, buenos días"));
    return (0);
}
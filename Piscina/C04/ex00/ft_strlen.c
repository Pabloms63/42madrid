#include <stdio.h>

int ft_strlen(char *str){
    int count = 0;
    while(str[count] != '\0'){
        count++;
    }

    return count;
}

int main(){
    char str[] = "Cadena de caracteres de ejemplo";

    printf("%d\n", ft_strlen(str));
    return (0);
}
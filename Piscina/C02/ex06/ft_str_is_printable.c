#include <stdio.h>

int ft_str_is_printable(char *str){
    int count = 0;
    while(str[count] != '\0'){
        if(!(str[count] >= 32 && str[count] <= 176))
            return (0);
        count++;
    }
    return (1);
}

int main(void){
    char str[] = "HOLA";
    printf("%d\n", ft_str_is_printable(str));
    return (0);
}
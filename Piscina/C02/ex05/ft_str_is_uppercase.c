#include <stdio.h>

int ft_str_is_uppercase(char *str){
    int count = 0;
    while(str[count] != '\0'){
        if(!(str[count] >= 65 && str[count] <= 90))
            return (0);
        count++;
    }
    return (1);
}

int main(void){
    char str[] = "HOLA";
    printf("%d\n", ft_str_is_uppercase(str));
    return (0);
}
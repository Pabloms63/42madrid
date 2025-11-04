#include <stdio.h>

int ft_str_is_lowercase(char *str){
    int count = 0;
    while(str[count] != '\0'){
        if(!(str[count] >= 97 && str[count] <= 122))
            return (0);
        count++;
    }
    return (1);
}

int main(void){
    char str[] = "holaaa";
    printf("%d\n", ft_str_is_lowercase(str));
    return (0);
}
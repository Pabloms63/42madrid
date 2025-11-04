#include <stdio.h>

int ft_str_is_alpha(char *str){
    int count = 0;
    while(str[count] != '\0'){
        if(!((str[count] >= 97 && str[count] <= 122) || (str[count] >= 65 && str[count] <= 90))){
            return (0);
        }
        count++;
    }
    return (1);
}

int main(void){
    char str[] = "Holaaaa6578aaaaaaa";
    printf("%d\n", ft_str_is_alpha(str));
    return (0);
}
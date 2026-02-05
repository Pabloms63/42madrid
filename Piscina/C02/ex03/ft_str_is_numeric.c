#include <stdio.h>

int ft_str_is_numeric(char *str){
    int count = 0;
    while(str[count] != '\0'){
        if(!(str[count] >= '0' && str[count] <= '9')){
            return (0);
        }
        count++;
    }
    return (1);
}

int main(void){
    char str[] = "1234234";
    printf("%d\n", ft_str_is_numeric(str));
    return (0);
}
#include <stdio.h>

int ft_atoi(char  *str){
    int count = 0;
    int sign = 1;
    int result = 0;

    while(str[count] != '\0'){
        if(str[count] == ' '){
            count++;
        }
        else
            break;
    }

    while(str[count] != '\0'){
        if(str[count] == '-' || str[count] == '+'){
            if(str[count] == '-'){
                sign = -sign;
            }
            count++;
        }
        else
            break;
    }

    while(str[count] != '\0'){
        if(str[count] >= '0' && str[count] <= '9'){
            result = result * 10 + (str[count] - '0');
            count++;
        }else
            break;
    }

    return (result * sign);
}

int main(){
    printf("Número convertido: %d\n", ft_atoi(" +--+++-8989645"));
    return (0);
}
#include <unistd.h>

char *ft_strupcase(char *str){
    int count = 0;
    while(str[count] != '\0'){
        if(str[count] >= 97 && str[count] <= 122)
            str[count] = str[count] - 32;
        count++;
    }
    return (str);
}

int main(void){
    char str[] = "hola";
    ft_strupcase(str);
    int count = 0;
    while(str[count] != '\0'){
        write(1, &str[count], 1);
        count++;
    }

    write(1, "\n", 1);
    return (0);
}
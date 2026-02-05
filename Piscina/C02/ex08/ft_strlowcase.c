#include <unistd.h>

char *ft_strlowcase(char *str){
    int count = 0;
    while(str[count] != '\0'){
        if(str[count] >= 65 && str[count] <= 90)
            str[count] = str[count] + 32;
        count++;
    }
    return (str);
}

int main(void){
    char str[] = "HOLA";
    ft_strlowcase(str);
    int count = 0;
    while(str[count] != '\0'){
        write(1, &str[count], 1);
        count++;
    }

    write(1, "\n", 1);
    return (0);
}
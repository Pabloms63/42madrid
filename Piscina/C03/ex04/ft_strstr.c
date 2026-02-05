#include <stdio.h>

char *ft_strstr(char *str, char *to_find){
    int count = 0;
    int count_tf = 0;

    if (to_find[0] == '\0') 
            return str;

    while(str[count] != '\0'){
        while (str[count + count_tf] == to_find[count_tf] && to_find[count_tf] != '\0') {
            count_tf++;
        }
        if (to_find[count_tf] == '\0') 
            return &str[count];

        count_tf = 0;
        count++;
    }

    return 0;
}

int main(){
    char *resultado = ft_strstr("Hola esto es un ejemplo a ver que tal.", "ejemplo");

    if (resultado)
        printf("Subcadena encontrada: %s\n", resultado);
    else
        printf("Subcadena no encontrada.\n");

    return 0;
}
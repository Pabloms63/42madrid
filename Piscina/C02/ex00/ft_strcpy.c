#include <unistd.h>

char *ft_strcpy(char *dest, char *src){
    int count = 0;
    while(src[count] != '\0'){
        dest[count] = src[count];
        count++;
    }
    dest[count] = '\0';
    return (dest);
}

int main(void){
    char src[] = "Copia esto";
    char dest[11];
    ft_strcpy(dest, src);

    int count = 0;
    while(dest[count] != '\0'){
        write(1, &dest[count], 1);
        count++;
    }

    write(1, "\n", 1);
    return (0);
}
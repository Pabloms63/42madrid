#include <unistd.h>

char *ft_strncpy(char *dest, char *src, unsigned int n){
    unsigned int count = 0;
    while(src[count] != '\0' && count < n){
        dest[count] = src[count];
        count++;
    }
    while (count < n) {
        dest[count] = '\0';
        count++;
    }
    return (dest);
}

int main(void){
    char src[] = "Copia esto";
    char dest[sizeof(src)];
    unsigned int size = 5;

    ft_strncpy(dest, src, size);
    dest[size] = '\0';

    int count = 0;
    while(dest[count] != '\0'){
        write(1, &dest[count], 1);
        count++;
    }

    write(1, "\n", 1);
    return (0);
}
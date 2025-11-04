#include <stdio.h>

char *ft_strcat(char *dest, char *src){
    int count_dest = 0;
    int count_src = 0;
    while(dest[count_dest] != '\0'){
        count_dest++;
    }
    while(src[count_src] != '\0'){
        dest[count_dest] = src[count_src];
        count_src++;
        count_dest++;
    }
    
    dest[count_dest] = '\0';

    return dest;
}

int main(){
    char dest[50] = "Esto se debe ";
    char src[] = "concatenar.";

    printf("%s\n", ft_strcat(dest, src));
    return (0);
}
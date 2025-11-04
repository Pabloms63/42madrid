#include <stdio.h>

char *ft_strncat(char *dest, char *src, unsigned int nb){
    int count_dest = 0;
    unsigned int count_src = 0;

    while(dest[count_dest] != '\0')
        count_dest++;

    while(src[count_src] != '\0' && count_src < nb){
        dest[count_dest] = src[count_src];
        count_src++;
        count_dest++;
    }
    
    dest[count_dest] = '\0';

    return (dest);
}

int main(){
    char dest[50] = "Este es el contenido original. ";
    char src[] = "Y este el añadido.";
 
    printf("%s\n", ft_strncat(dest, src, 19));

    return (0);
}
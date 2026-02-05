#include <stdlib.h>
#include <stdio.h>

char *ft_strdup(char *src){
    int count = 0;
    char *copia;

    // calcular la longitud
    while (src[count] != '\0') {
        count++;
    }

    // reservar memoria (+1 para '\0')      
    copia = (char*)malloc((count+ 1) * sizeof(char));
    
    if(!copia){
        return (NULL);
    }

    int a = 0;

    while(a < count){
        copia[a] = src[a];
        a++;
    }

    copia[count] = '\0';

    return (copia);
}

int main() {
    const char *src = "Hola mundo";
    
    // Duplicar la cadena
    char *copia = ft_strdup(src);

    printf("Original: %s\n", src);
    printf("Copia   : %s\n", copia);

    // Liberar la memoria reservada
    free(copia);

    return 0;
}
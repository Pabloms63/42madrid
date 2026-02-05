#include <stdio.h>

unsigned int ft_strlen(char *str) {
    unsigned int len = 0;
    while (str[len])
        len++;
    return len;
}

unsigned int ft_strlcat(char *dest, char *src, unsigned int size) {
    unsigned int dest_len = ft_strlen(dest);
    unsigned int src_len = ft_strlen(src);
    unsigned int i = 0;

    // Si el tamaño total es menor o igual al tamaño actual de dest, no hay espacio para concatenar
    if (size <= dest_len)
        return size + src_len;

    // Concatenar mientras haya espacio en el buffer (size - dest_len - 1 para el '\0')
    while (src[i] && dest_len + i < size - 1) {
        dest[dest_len + i] = src[i];
        i++;
    }

    // Asegurarse de que la cadena resultante esté terminada en '\0'
    dest[dest_len + i] = '\0';

    // Retornar la longitud total que intentó crear
    return dest_len + src_len;
}

int main(void) {
    char dest[64] = "Frase del primer array.";  // Espacio suficiente para concatenar
    char src[] = " Frase concatenada.";

    unsigned int result = ft_strlcat(dest, src, 16);

    printf("Resultado: %s\n", dest);
    printf("Longitud que intentó crear: %u\n", result);

    return 0;
}
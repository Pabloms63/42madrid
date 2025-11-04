#include "ft.h"
#include <stdio.h>

int main(void){
    //Primer metodo
    int a = 96;
    int b = 69;
    ft_putchar('h');
    printf("\n");

    //Segundo método
    ft_swap(&a, &b);
    printf("Antes: %d %d\n", a, b);
    ft_swap(&a, &b);
    printf("Después: %d %d\n", a, b);
    ft_putchar('\n');

    //Tercer método
    char *str1 = "Ejemplo de string";
    ft_putstr(str1);
    fflush(stdout);
    ft_putchar('\n');

    //Cuarto método
    char *str2 = "Devuelve el tamaño de este string";
    printf("%d", ft_strlen(str2));
    fflush(stdout);
    ft_putchar('\n');

    //Quinto elemento
    char *str3 = "a";
    char *str4 = "b";
    printf("%d\n", ft_strcmp(str3, str4));

    return (0);
}
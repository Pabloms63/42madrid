#include <stdio.h>

void ft_ft(int *nbr){
    *nbr = 42;
}

int main(void){
    int num = 98;
    int *nbr = &num;
    printf("Antes de la conversión: %d\n", *nbr);
    ft_ft(nbr);
    printf("Después de la conversión: %d\n", *nbr);
    return (0);
}
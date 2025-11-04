#include <stdio.h>

void ft_ultimate_div_mod(int *a, int *b){
    int div = *a / *b;
    int mod = *a % *b;

    *a = div;
    *b = mod;
}

int main(void){
    int a = 89;
    int b = 9;

    ft_ultimate_div_mod(&a, &b);
    printf("División: %d\nMódulo: %d\n", a, b);
    return (0);
}
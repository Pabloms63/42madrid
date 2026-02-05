#include <stdio.h>

void ft_div_mod(int a, int b, int *div, int *mod){
    *div = a / b;
    *mod = a % b;
}

int main(void){
    int a = 18;
    int b = 6;
    int div, mod;
    ft_div_mod(a, b, &div, &mod);
    printf("Division: %d Modulo: %d\n", div, mod);
    return (0);
}
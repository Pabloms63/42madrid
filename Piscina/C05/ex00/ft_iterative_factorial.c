#include <stdio.h>

int ft_iterative_factorial(int nb){
    int result;

    if(nb < 0)
        return (0);

    result = 1;

    while(nb > 0){
        result *= nb;
        nb--;
    }

    return (result);
}

int main(void){
    printf("Factorial de 5 -> %d\n", ft_iterative_factorial(5));
    printf("Factorial de 7 -> %d\n", ft_iterative_factorial(7));
    printf("Factorial de 10 -> %d\n", ft_iterative_factorial(10));

    return (0);
}
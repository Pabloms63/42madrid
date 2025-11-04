#include <stdio.h>

int ft_is_prime(int nb){
    int count = 0;

    if (nb <= 1)
        return (0);

    count = 2;

    while (count <= nb / count) 
    {
        if (nb % count == 0)
            return (0);
        count++;
    }
    return (1);
}

int ft_find_next_prime(int nb){
    if(nb <= 1)
        return (2);
    
    while(!ft_is_prime(nb)){
        nb++;
    }

    return (nb);
}

int main(void){
    printf("%d\n", ft_find_next_prime(8));
    return (0);
}
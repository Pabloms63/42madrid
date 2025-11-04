#include <stdio.h>

int ft_sqrt(int nb){
    int count = 0;

    if(nb <= 0)
        return (0);

    while(count < nb){
        if(count * count == nb){
            return (count);
        }
        count++;
    }
    return (0);
}

int main(void){
    printf("%d\n", ft_sqrt(9));
    return (0);
}
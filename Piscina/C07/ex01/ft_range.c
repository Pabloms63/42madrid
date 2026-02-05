#include <stdio.h>
#include <stdlib.h>

int *ft_range(int min, int max){
    int *tab;
    int count = 0;
    int size = max - min;

    if(min >= max){
        return (NULL);
    }

    //malloc
    tab = (int *)malloc(size * sizeof(int));

    while(min < max){
        tab[count] = min;
        min++;
        count++;
    }
    return(tab);
}

int main(){
    int *array = ft_range(1, 7);
    
    int size = 7 - 1;
    int count = 0;

    while(count < size){
        printf("%d", array[count]);
        
        if(count < size - 1){
            printf(", ");
        }
        count++;
    }

    return (0);
}
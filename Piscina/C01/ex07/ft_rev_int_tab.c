#include <stdio.h>

void ft_rev_int_tab(int *tab, int size){
    int count = 0;
    int temp;
    while(count < tab[size / 2]){
        temp = tab[count];
        tab[count] = tab[size - 1 - count];
        tab[size - 1 - count] = temp;
        count++;
    }
}

int main(void){
    int tab[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int size = 9;

    printf("Antes de invertir: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", tab[i]);
    }
    printf("\n");

    ft_rev_int_tab(tab, size);

    printf("Después de invertir: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", tab[i]);
    }
    printf("\n");
    return (0);
}
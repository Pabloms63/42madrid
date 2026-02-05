#include <stdio.h>

void ft_swap(int *a, int *b){
    int support = 0;
    support = *a;
    *a = *b;
    *b = support;
}
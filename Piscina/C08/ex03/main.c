#include "ft_point.h"
#include <stdio.h>

int main(void){
    t_point p;
    p.x = 12;
    p.y = 34;

    printf("Plano cartesiano: x = %d, y = %d\n", p.x, p.y);
    return (0);
}
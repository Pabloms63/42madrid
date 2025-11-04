#include <unistd.h>

char ft_is_negative(int num){
    char neg = 'N';
    char pos = 'P';
    if(num < 0)
        write(1, &neg, 1);
    else
        write(1, &pos, 1);
}

int main(void){
    ft_is_negative(-9);
    return (0);
}
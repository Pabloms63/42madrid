#include <unistd.h>

char *ft_putnbr(int num){
    long n = num;
    if (n < 0){
        write(1, "-", 1);
        n = -n;
    }
    if(n >= 10){
        ft_putnbr(n / 10);
    }
    char c_n = n % 10 + '0';
    write(1, &c_n, 1);
}

int main(void){
    ft_putnbr(789);
    return (0);
}
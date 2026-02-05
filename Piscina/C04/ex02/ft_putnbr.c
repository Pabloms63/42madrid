#include <unistd.h>

void ft_putnbr(int nb){
    long n = nb;
    if(n < 0){
        char neg = '-';
        write(1, &neg, 1);
        n = -n;
    }

    if(n > 9){
        ft_putnbr(n / 10);
    }

    char c = (n % 10) + '0';
    write(1, &c, 1);
}

int main(void)
{
    ft_putnbr(789);
    write(1, "\n", 1);

    ft_putnbr(-42);
    write(1, "\n", 1);

    ft_putnbr(0);
    write(1, "\n", 1);

    ft_putnbr(-2147483648);
    write(1, "\n", 1);

    return (0);
}

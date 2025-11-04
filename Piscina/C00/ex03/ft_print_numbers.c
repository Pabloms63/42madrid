#include <unistd.h>

char *ft_print_numbers(){
    int number = 0;

    while(number <= 9){
        char char_num = number + '0';
        write(1, &char_num, 1);
        number++;
    }
}

int main(void){
    ft_print_numbers();
    return (0);
}
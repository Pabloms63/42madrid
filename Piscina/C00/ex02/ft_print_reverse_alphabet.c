#include <unistd.h>

char *ft_print_reverse_alphabet(){
    char letra = 'z';
    while(letra >= 'a'){
        write(1, &letra, 1);
        letra--;
    }
}

int main(void){
    ft_print_reverse_alphabet();
    return (0);
}
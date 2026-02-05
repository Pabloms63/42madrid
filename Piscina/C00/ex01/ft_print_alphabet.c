#include <unistd.h>

char	*ft_print_alphabet(){
    char letra = 'a';
    while(letra <= 'z'){
        write(1, &letra, 1);
        letra++;
    }
}

int main(void){
    ft_print_alphabet();
    return (0);
}
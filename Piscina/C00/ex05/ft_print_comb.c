#include <unistd.h>

char ft_print_comb(){
    int count1 = 0;
    while(count1 <= 7){
        int count2 = count1 + 1;
        while(count2 <= 8){
            int count3 = count2 + 1;
            while(count3 <= 9){
                char num1 = count1 + '0';
                char num2 = count2 + '0';
                char num3 = count3 + '0';
                char coma = ',';
                char espacio = ' ';

                write(1, &num1, 1);
                write(1, &num2, 1);
                write(1, &num3, 1);

                if(count1 != 7){
                    write(1, &coma, 1);
                    write(1, &espacio, 1);
                }
                count3++;
            }
            count2++;
        }
        count1++;
    }
}

int main(void){
    ft_print_comb();
    return (0);
}
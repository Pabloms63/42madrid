#include <unistd.h>

char ft_print_comb2(){
    int count1 = 0;
    while(count1 <= 98){
        int count2 = count1 + 1;
        while(count2 <= 99){
            char c1[2] = {count1 / 10 + '0', count1 % 10 + '0'};
            char c2[2] = {count2 / 10 + '0', count2 % 10 + '0'};

            write(1, &c1[0], 1);
            write(1, &c1[1], 1);
            write(1, " ", 1);
            write(1, &c2[0], 1);
            write(1, &c2[1], 1);

            if(count1 != 98){
                write(1, ",", 1);
                write(1, " ", 1);
            }

            count2++;
        }
        count1++;
    }
}

int main(void){
    ft_print_comb2();
    return (0);
}
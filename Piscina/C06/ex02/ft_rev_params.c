#include <unistd.h>

int main(int argc, char *argv[]){
    int count1 = argc - 1;
    int count2;

    while(count1 > 0){
        count2 = 0;
        while(argv[count1][count2] != '\0'){
            write(1, &argv[count1][count2], 1);
            count2++;
        }
        write(1, "\n", 1);
        count1--;
    }
    return (0);
}
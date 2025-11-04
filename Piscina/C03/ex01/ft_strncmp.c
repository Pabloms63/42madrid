#include <stdio.h>

int ft_strncmp(char *s1, char *s2, unsigned int n) {
    unsigned int count = 0;
    while (count < n) {
        if (s1[count] != s2[count] || s1[count] == '\0' || s2[count] == '\0') {
            return (s1[count] - s2[count]);
        }
        count++;
    }
    return 0;
}

int main(){
    printf("%d\n", ft_strncmp("Holae", "Holax", 5));
    return (0);
}
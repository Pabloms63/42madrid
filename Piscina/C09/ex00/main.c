#include <stdio.h>

void ft_putstr(char *str);
int  ft_strlen(char *str);

int main(void)
{
    ft_putstr("Hola, libft!\n");
    int len = ft_strlen("Hola, libft!");
    printf("%d", len);
    return 0;
}


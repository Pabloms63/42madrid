#include <stdio.h>

int ft_strlen(char *str){
    int count = 0;

    while(str[count] != '\0'){
        count++;
    }

    return (count);
}

char *ft_strjoin(int size, char **strs, char *sep){
    int total_len = 0;
    int sep_len = ft_strlen(sep);
    int a, b, c;
    char *result;

    if(size == 0){
        result = (char *)malloc(a);
        if(result){
            result[0] = '\0';
        return (result);
        }
    }

    //Calcular longitrud total
    int count = 0;

    while(count < size){
        total_len += ft_strlen(strs[count]);
        count++;
    }

    total_len += sep_len * (size - 1);

    //Reservar memoria
    result = (char *)malloc(total_len + 1);
    if(!result){
        return (NULL);
    }

    //Copiar cadenas + separadores
    c = 0;
    while(a < size){
        b = 0;
        while(strs[a][b]){
            result[c++] = strs[a][b++];
        }
        if(a < size - 1){
            b = 0;
            while(sep[b]){
                result[c++] = sep[b++];
            }
        }
    }
    result[k] = '\0';
    return (result);
}

int main(void){
    char *arr[] = {"Hola", "mundo", "en", "C"};
    char *res = ft_strjoin(4, arr, " - ");

    printf("%s\n", res); // "Hola - mundo - en - C"

    free(res);
    return 0;
}
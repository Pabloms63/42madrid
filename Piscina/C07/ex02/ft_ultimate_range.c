#include <stdio.h>
#include <stdlib.h>

int		ft_ultimate_range (int **range, int min, int max)
{
	int count = 0;
	int size = max -min;

	if (min >= max)
    {
        *range = NULL;
        return 0;
    }

	*range = malloc(size * sizeof(int));
    if (!*range)
        return -1;

	while(min < max){
		(*range)[count] = min;
		min++;
		count++;
	}

	return (size);
}

int		main (void)
{
	int count = 0;
	int *array;
	int size;

	size = ft_ultimate_range(&array, 2, 9);

	while(count < size){
		printf("%d ", array[count]);
		count++;
	}

	return (0);
}
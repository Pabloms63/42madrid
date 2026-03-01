#include <stdlib.h>

int	*ft_rrange(int start, int end)
{
	int		len;
	int		*arr;
	int		i = 0;

	if (start <= end)
		len = end - start + 1;
	else
		len = start - end + 1;

	arr = (int *)malloc(sizeof(int) * len);
	if (!arr)
		return (NULL);

	while (i < len)
	{
		arr[i] = end;
		if (end > start)
			end--;
		else
			end++;
		i++;
	}
	return (arr);
}

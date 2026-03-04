#include <stdlib.h>

int count_digits (int n)
{
	int num = (long)n;
	int len = 0;

	if (num < 0)
	{
		num = -num;
		len++;
	}
	if (num == 0)
	{
		len++;
		return (len);
	}
	while (num > 0)
	{
		num /= 10;
		len++;
	}
	return (len);
}

char	*ft_itoa(int nbr)
{
	int len = 0;
	int num = (long)nbr;
	char *str;

	len = count_digits(nbr);
	str = malloc(sizeof(char) * (len + 1));
	str[len] = '\0';
	if (num == 0)
		str[0] = '0';
	if (num < 0)
	{
		str[0] = '-';
		num = -num;
	}
	while (num > 0)
	{
		len--;
		str[len] = (num % 10) + '0';
		num /= 10;
	}
	return (str);
}

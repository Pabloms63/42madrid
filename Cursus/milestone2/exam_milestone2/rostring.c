#include <unistd.h>

int main (int argc, char **argv)
{
	if (argc == 2)
	{
		int cnt = 0;
		int end;
		int start;
		while (argv[1][cnt] && argv[1][cnt] == 32)
			cnt++;
		start = cnt;
		while (argv[1][cnt] && argv[1][cnt] != 32)
			cnt++;
		end = cnt;
		while (argv[1][cnt] && argv[1][cnt] == 32)
			cnt++;
		while (argv[1][cnt])
		{
			write(1, &argv[1][cnt], 1);
			cnt++;
		}
		while (start < end)
		{
			write(1, &argv[1][start], 1);
			start++;
		}
	}
	write(1, "\n", 1);
}

#include <unistd.h>

int main (int argc, char **argv)
{
	if (argc >= 2)
	{
		int c = 1;
		while (argv[c])
		{
			int cnt = 0;
			while (argv[c][cnt])
			{
				while (argv[c][cnt] && argv[c][cnt] == 32)
				{
					write(1, &argv[c][cnt], 1);
					cnt++;
				}
				if (argv[c][cnt] && argv[c][cnt] != 32)
				{
					if (argv[c][cnt] >= 97 && argv[c][cnt] <= 122)
						argv[c][cnt] -= 32;
					write(1, &argv[c][cnt], 1);
					cnt++;
				}
				while (argv[c][cnt] && argv[c][cnt] != 32)
				{
					if (argv[c][cnt] && (argv[c][cnt] >= 65 && argv[c][cnt] <= 90))
					{
						argv[c][cnt] += 32;
						write(1, &argv[c][cnt], 1);
						cnt++;
					}
					else
					{
						write(1, &argv[c][cnt], 1);
						cnt++;
					}
				}
			}
			write(1, "\n", 1);
			c++;
		}
	}
	else
		write(1, "\n", 1);
}

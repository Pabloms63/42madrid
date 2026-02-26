#include <unistd.h>

int main (int argc, char **argv)
{
	if (argc >= 2)
	{
		int cnt1 = 1;
		while (argv[cnt1])
		{
			int cnt2 = 0;
			while(argv[cnt1][cnt2])
			{
				while (argv[cnt1][cnt2] && argv[cnt1][cnt2] == 32)
				{
					write(1, &argv[cnt1][cnt2], 1);
					cnt2++;
				}
				if (argv[cnt1][cnt2] && argv[cnt1][cnt2] != 32)
				{
					if (argv[cnt1][cnt2] && (argv[cnt1][cnt2] >= 97 && (argv[cnt1][cnt2] <= 122)))
						argv[cnt1][cnt2] -= 32;
					write(1, &argv[cnt1][cnt2], 1);
					cnt2++;
				}
				while (argv[cnt1][cnt2] && argv[cnt1][cnt2] != 32)
				{
					if (argv[cnt1][cnt2] && (argv[cnt1][cnt2] >= 65 && (argv[cnt1][cnt2] <= 90)))
						argv[cnt1][cnt2] += 32;
					write(1, &argv[cnt1][cnt2], 1);
					cnt2++;
				}
			}
			write(1, "\n", 1);
			cnt1++;
		}
	}
	else
		write(1, "\n", 1);
}

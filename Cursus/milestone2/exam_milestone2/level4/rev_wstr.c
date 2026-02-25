#include <unistd.h>

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        int cnt = 0;
        while (argv[1][cnt])
            cnt++;
        cnt--;

        while (cnt >= 0)
        {
            while (cnt >= 0 && argv[1][cnt] == ' ')
                cnt--;

            int end = cnt;

            while (cnt >= 0 && argv[1][cnt] != ' ')
                cnt--;

            int start = cnt + 1;

            while (start <= end)
                write(1, &argv[1][start++], 1);

            if (cnt >= 0)
                write(1, " ", 1);
        }
    }
    write(1, "\n", 1);
    return 0;
}

#include <stdio.h>
#include <unistd.h>

int main()
{
    char buf[0x100];
    printf("give me something: ");
    fflush(stdout);
    read(0, buf, 0x100);
    ((void (*)())buf)();
}
// #include <stdio.h>

// int main(void)
// {
//   char *array1[2] = {'Good morning', 'C language'};
//   printf('%s\n', array1[0] + 5);
//   printf('%c\n', *(array1[1] + 6));
// }

// #include <stdio.h>

// int main(void)
// {
//   int n = 50;
//   int *p = &n;
//   printf("%p\n", p);
//   printf("%i\n", *p);
// }

#include <stdio.h>
int main()
{
  char *s = "EMMA";
  printf("%p\n", &s[0]);
  printf("%p\n", &s[1]);
  printf("%p\n", &s[2]);
  printf("%p\n", &s[3]);
  printf("%p\n", &s[4]);
  printf("%p\n", s[0]);
  printf("%p\n", s[1]);
  printf("%p\n", s[2]);
  printf("%p\n", s[3]);
  printf("%p\n", s[4]);
}
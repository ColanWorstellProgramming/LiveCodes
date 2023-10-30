#include "main.h"

/**
 * printAnimal - | Prototype For Main Function
 * @format: Var
 * Return: Void
 */

int main(void)
{
    const char *format1 = "cdf";
    const char *format2 = "%c%d%f";

    printAnimal(format1);
    _putchar('\n');
    printAnimal(format2);

    return 0;
}

void printAnimal(const char *format, ...)
{

    char *str = NULL;
    int i;


    /* Check If Format Exists */

    if (format == NULL)
    {
        exit(98);
    }

    /* Check For Null Byte*/

    while (*format != '\0')
    {

        /* Check For % To Initiate Format */

        if (*format == '%')
        {

            format++;

            /* Check For Format Specifier */

            switch (*format)
            {
                case 'c': /* C for Cat */
                    str = "Meow";
                    break;
                case 'd': /* D for Dog */
                    str = "Bark";
                    break;
                default: /* What Does The Fox Say? */
                    str = "Who Knows?";
                    break;
            }

        /* What If No %? */

        } else if (*format != '%')

        {
            str = "N/A";
        }

        /* Print String */

        for (i = 0; str[i] != '\0'; i++)
        {
            _putchar(str[i]);
        }

        /* Iterate */

        _putchar('\n');
        format++;

    }
}
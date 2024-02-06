#ifndef MORSE_H
#define MORSE_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ENCODED_LENGTH 256
// Функція для конвертації тексту в код Морзе та повернення його у вигляді масива
char* morseCode(char* message);

#endif // MORSE_H

#include <stdio.h>
#include <string.h>

void textToMorse(char text[], int size) {
    char morseCode[26][5] = {
        "01",    // A
        "1000",  // B
        "1010",  // C
        "100",   // D
        "0",     // E

        "0010",  // F
        "110",   // G
        "0000",  // H
        "00",    // I
        "1011",  // J

        "1100",  // K
        "101",   // L
        "1111",  // M
        "10",    // N
        "111",   // O

        "0110",  // P
        "1101",  // Q
        "0100",  // R
        "000",   // S
        "1",     // T

        "001",   // U
        "0001",  // V
        "011",   // W
        "1001",  // X
        "1011",  // Y

        "1100",  // Z

       
    };

    for (int i = 0; i < size; i++) {
        if (text[i] >= 'A' && text[i] <= 'Z') {
            int index = text[i] - 'A';
            printf("%s", morseCode[index]);
        }
        else if (text[i] >= 'a' && text[i] <= 'z') {
            int index = text[i] - 'a';
            printf("%s", morseCode[index]);
        }
        
    }
}

int main() {
    char inputText[] = "Hello World";
    int textSize = strlen(inputText);

    textToMorse(inputText, textSize);

    return 0;
}

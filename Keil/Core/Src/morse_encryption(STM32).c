const char* textToMorse(char text[], int size) {
   
    static char morseCode[26][5] = {
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

    // Статична змінна для зберігання результату
    static char result[100]; 
    // Індекс для відстеження позиції у рядку
    int resultIndex = 0;

    
    for (int i = 0; i < size; i++) {
        
        if (text[i] == ' ') {
            // Додавання пробілу між словами
            result[resultIndex++] = '3';
        }
        else {
            // Перевірка, чи символ є великою літерою
            if (text[i] >= 'A' && text[i] <= 'Z') {
                int index = text[i] - 'A';
                strcpy_s(&result[resultIndex], sizeof(result) - resultIndex, morseCode[index]);
                resultIndex += strlen(morseCode[index]);

                // Цифра '2' як роздільник між кодами Морзе
                result[resultIndex++] = '2';
            }
            else if (text[i] >= 'a' && text[i] <= 'z') {
                // Розрахунок індексу у масиві morseCode для малої літери
                int index = text[i] - 'a';
                // Додавання коду Морзе у рядок результату
                strcpy_s(&result[resultIndex], sizeof(result) - resultIndex, morseCode[index]);
                // Оновлення resultIndex на основі доданого коду Морзе
                resultIndex += strlen(morseCode[index]);

                result[resultIndex++] = '2';
            }
        }
    }

    // Завершення рядка нульовим символом
    result[resultIndex] = '\0';

    return result;
}
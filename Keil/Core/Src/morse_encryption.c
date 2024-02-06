char* morseCode(char* message) {
    static char encoded[MAX_ENCODED_LENGTH];
    size_t length = strlen(message);

    encoded[0] = '\0';

    const char* morseTable[256] = {
        ['A'] = "10",     ['B'] = "0111",   ['C'] = "0101",   ['D'] = "011",
        ['E'] = "1",      ['F'] = "1101",   ['G'] = "001",    ['H'] = "1111",
        ['I'] = "11",     ['J'] = "1000",   ['K'] = "010",    ['L'] = "1011",
        ['M'] = "00",     ['N'] = "01",     ['O'] = "000",    ['P'] = "1001",
        ['Q'] = "0010",   ['R'] = "101",    ['S'] = "111",    ['T'] = "0",
        ['U'] = "110",    ['V'] = "1110",   ['W'] = "100",    ['X'] = "0110",
        ['Y'] = "0100",   ['Z'] = "0011",   ['1'] = "10000",  ['2'] = "11000",
        ['3'] = "11100",  ['4'] = "11110",  ['5'] = "11111",  ['6'] = "01111",
        ['7'] = "00111",  ['8'] = "00011",  ['9'] = "00001",  ['0'] = "00000",
        [' '] = "3"
    };

    size_t encoded_length = 0;

    for (size_t i = 0; i < length; i++) {
        char x = toupper(message[i]);
        const char* code = morseTable[x];

        if (code) {
            size_t code_length = strlen(code);

            if (encoded_length + code_length >= MAX_ENCODED_LENGTH - 1) {

                return NULL;
            }
            strcat(encoded, code);
            encoded_length += code_length;
            // Add separators only if there's enough space in the buffer
            if (i < length - 1 && x != ' ' && toupper(message[i + 1]) != ' ' && encoded_length < MAX_ENCODED_LENGTH - 1) {
                strcat(encoded, "2");
                encoded_length++;
            }
        } else {

            return NULL;
        }
    }

    return encoded;
}

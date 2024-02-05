char* morseCode(char* message) {
    size_t length = strlen(message);
    char* encoded = (char*)malloc(5 * length);  // Assuming each character is at most 5 Morse code characters long

    // Set the first character to '\0' to initialize an empty string
    encoded[0] = '\0';

    for (size_t i = 0; i < length; i++) {
        char x = message[i];

        switch (x) {
            case 'a':
        case 'A':
            strcat(encoded, "10");
            break;
        case 'b':
        case 'B':
            strcat(encoded, "0111");
            break;
        case 'c':
        case 'C':
            strcat(encoded, "0101");
            break;
        case 'd':
        case 'D':
            strcat(encoded, "011");
            break;
        case 'e':
        case 'E':
            strcat(encoded, "1");
            break;
        case 'f':
        case 'F':
            strcat(encoded, "1101");
            break;
        case 'g':
        case 'G':
            strcat(encoded, "001");
            break;
        case 'h':
        case 'H':
            strcat(encoded, "1111");
            break;
        case 'i':
        case 'I':
            strcat(encoded, "11");
            break;
        case 'j':
        case 'J':
            strcat(encoded, "1000");
            break;
        case 'k':
        case 'K':
            strcat(encoded, "010");
            break;
        case 'l':
        case 'L':
            strcat(encoded, "1011");
            break;
        case 'm':
        case 'M':
            strcat(encoded, "00");
            break;
        case 'n':
        case 'N':
            strcat(encoded, "01");
            break;
        case 'o':
        case 'O':
            strcat(encoded, "000");
            break;
        case 'p':
        case 'P':
            strcat(encoded, "1001");
            break;
        case 'q':
        case 'Q':
            strcat(encoded, "0010");
            break;
        case 'r':
        case 'R':
            strcat(encoded, "101");
            break;
        case 's':
        case 'S':
            strcat(encoded, "111");
            break;
        case 't':
        case 'T':
            strcat(encoded, "0");
            break;
        case 'u':
        case 'U':
            strcat(encoded, "110");
            break;
        case 'v':
        case 'V':
            strcat(encoded, "1110");
            break;
        case 'w':
        case 'W':
            strcat(encoded, "100");
            break;
        case 'x':
        case 'X':
            strcat(encoded, "0110");
            break;
        case 'y':
        case 'Y':
            strcat(encoded, "0100");
            break;
        case 'z':
        case 'Z':
            strcat(encoded, "0011");
            break;
        case '1':
            strcat(encoded, "10000");
            break;
        case '2':
            strcat(encoded, "11000");
            break;
        case '3':
            strcat(encoded, "11100");
            break;
        case '4':
            strcat(encoded, "11110");
            break;
        case '5':
            strcat(encoded, "11111");
            break;
        case '6':
            strcat(encoded, "01111");
            break;
        case '7':
            strcat(encoded, "00111");
            break;
        case '8':
            strcat(encoded, "00011");
            break;
        case '9':
            strcat(encoded, "00001");
            break;
        case '0':
            strcat(encoded, "00000");
            break;
        case ' ':
                strcat(encoded, "3");  // 3 для пробілів
                break;

            default:
                fprintf(stderr, "Found invalid character: %c\n", x);
                exit(EXIT_FAILURE);
        }

        if (i < length - 1 && x != ' ' && message[i + 1] != ' ')
            strcat(encoded, "2");  // 2 для розділу букв
    }

    return encoded;
}

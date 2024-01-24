#include <stdio.h>

unsigned char BCC(const char* data, size_t length) {
    unsigned char calculated_bcc = 0;

    // Iterate through each byte in the data
    for (size_t i = 0; i < length; ++i) {
        // XOR each byte with the current calculated BCC value
        calculated_bcc ^= data[i];
    }

    return calculated_bcc;
}

int main() {
    // Example
    char data[] = { 'A', 'B', 'C', 'D', '1' };

    unsigned char calculated_bcc = BCC(data, sizeof(data) / sizeof(data[0]));

    printf("Calculated BCC: 0x%02X\n", calculated_bcc);

    return 0;
}


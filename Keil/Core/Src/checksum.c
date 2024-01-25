
unsigned short calculateCRC16(const unsigned char* data, int length) {
    unsigned short crc = 0xFFFF;

    for (int i = 0; i < length; i++) {
        crc ^= (unsigned short)data[i];
        for (int j = 0; j < 8; j++) {
            crc = (crc & 1) ? ((crc >> 1) ^ 0xA001) : (crc >> 1);
        }
    }

    return crc;
}
def calculate_crc16(data):
    crc = 0xFFFF

    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1

    return crc & 0xFFFF
def main():
    data = [0x1, 0x77]
    checksum = calculate_crc16(data)

    print(f"CRC-16 Checksum: {checksum:04X} (hex)")
    print(f"CRC-16 Checksum: {checksum} (dec)")
    print("CRC-16 Checksum:", bin(checksum)[2:].zfill(16), "(bin)")

if __name__ == "__main__":
    main()
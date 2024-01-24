# Morse Decoder Communication Protocol

This document outlines the communication protocol for the Morse decoder project, facilitating interaction between the PC frontend and STM backend applications.

## 1. PC to STM Request for STM_ID

- **Message Structure:**
  - Command Code: `0x01` (1 byte)
  - Empty: `0x00` (1 byte)
  - Checksum: `0xBCC` (2 bytes)

- **Example Byte Sequence:** `0x01 0x00 0xBCC` (hexadecimal)

## 2. STM to PC Response with STM_ID

- **Message Structure:**
  - Command Code: `0x01` (1 byte, in response to the `0x01` command)
  - STM ID: `0x77` (example STM ID, 1 byte)
  - Checksum: `0xBCC` (2 bytes)

- **Example Byte Sequence:** `0x01 0x77 0xBCC` (hexadecimal)

## 3. PC to STM Encrypt Request with Data

- **Message Structure:**
  - Command Code: `0x02` (1 byte, for example)
  - Block Size: `{block_size}` (4 bytes, specifying the block size for encryption)
  - Data: `{data}` (variable size, the data to be encrypted)
  - Checksum: `0xBCC` (2 bytes)

- **Example Byte Sequence:** `0x02 {block_size} {data} 0xBCC` (hexadecimal)

## 4. STM to PC Response with Converted Data

- **Message Structure:**
  - Command Code: `0x02` (1 byte, in response to the `0x02` command)
  - Block Size: `{block_size}` (4 bytes, specifying the block size for converted data)
  - Converted Data: `{converted_data}` (variable size, representing the actual converted data)
  - Checksum: `0xBCC` (2 bytes)

- **Example Byte Sequence:** `0x02 {block_size} {converted_data} 0xBCC` (hexadecimal)

## 5. PC to STM Request for Max Message Size

- **Message Structure:**
  - Command Code: `0x03` (1 byte, for example)
  - Empty: `0x00` (1 byte)
  - Checksum: `0xBCC` (2 bytes)

- **Example Byte Sequence:** `0x03 0x00 0xBCC` (hexadecimal)

## 6. STM to PC Response with Max Message Size

- **Message Structure:**
  - Command Code: `0x03` (1 byte, in response to the `0x03` command)
  - Max Message Size: `{max_size}` (4 bytes, defining the size as needed)
  - Checksum: `0xBCC` (2 bytes)

- **Example Byte Sequence:** `0x03 {max_size} 0xBCC` (hexadecimal)

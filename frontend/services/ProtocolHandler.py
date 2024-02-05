import binascii

from frontend.services.Command import Command
from frontend.services.CommandConstants import CommandConstants
from frontend.services.checksum import calculate_crc16
from frontend.services.uart_communication import UARTCommunication


class PCtoSTMRequestSTMID(Command):
    def execute(self, input_data, uart_communication):
        print("Invoked PCtoSTMRequestSTMID")

        # Expected message structure
        expected_command_code = CommandConstants.PC_TO_STM_REQUEST_STM_ID
        expected_stm_id = CommandConstants.STM_ID
        empty_byte = 0x00
        expected_checksum = calculate_crc16([expected_command_code] + [empty_byte])

        # Byte Sequence
        byte_sequence = bytes([expected_command_code, empty_byte]) + expected_checksum.to_bytes(2, 'big')

        # Send data
        uart_communication.send_data(byte_sequence)

        # Receive data
        received_data = uart_communication.receive_data()

        return self.validate_received_data(received_data, expected_command_code, expected_stm_id)

    def validate_received_data(self, received_data, expected_command_code, expected_stm_id):
        if len(received_data) == 5:  # Ensure correct length
            received_command_code = received_data[0]
            received_stm_id = received_data[1]
            received_checksum = received_data[2]

            if (received_command_code == expected_command_code and
                    received_stm_id == expected_stm_id):
                # Validate checksum
                calculated_checksum = calculate_crc16(list(received_data[:-2]))
                if calculated_checksum == received_checksum:
                    print("Received STM Id:", received_stm_id)
                    return True
                else:
                    print("Checksum error")
            else:
                print("Mismatch in command code or STM ID")
        else:
            print("Invalid data length")

        return False


class PCtoSTMEncryptRequest(Command):
    def execute(self, input_data, uart_communication):
        print("Invoked PCtoSTMEncryptRequest")

        command_code = CommandConstants.PC_TO_STM_ENCRYPT_REQUEST

        input_data_bytes = input_data.encode('utf-8')  # Encode input_data to bytes
        block_size = len(input_data_bytes).to_bytes(4, 'big')  # Convert block size to bytes
        checksum = calculate_crc16(command_code.to_bytes() + input_data_bytes + block_size)

        # Create byte sequence
        byte_sequence = bytes([command_code]) + block_size + input_data_bytes + checksum.to_bytes(2, 'big')

        # Send data
        uart_communication.send_data(byte_sequence)

        # Receive response
        received_data = uart_communication.receive_data()

        # Process the response
        if received_data:
            return self.process_response(received_data)
        else:
            print("No response received")
            return None

    def process_response(self, received_data):
        """
        Process the response received from the STM.

        Parameters:
        - received_data: The data received from the STM.

        Returns:
        - The converted data if the response is valid, None otherwise.
        """
        # Validate the response message structure
        if len(received_data) >= 7:  # Ensure minimum length
            received_command_code = received_data[0]
            received_block_size = int.from_bytes(received_data[1:5], 'big')
            received_converted_data = received_data[5:-2]  # Extract converted data
            received_checksum = int.from_bytes(received_data[-2:], 'big')

            # Validate checksum
            calculated_checksum = calculate_crc16(list(received_data[:-2]))
            if calculated_checksum == received_checksum:
                print("Received converted data:", received_converted_data.decode('utf-8'))  # Convert bytes to string
                return received_converted_data.decode('utf-8')  # Return converted data as string
            else:
                print("Checksum error in received data")
        else:
            print("Invalid response data length")

        return None  # Return None if response is not valid


class PCtoSTMRequestMaxMessageSize(Command):
    def execute(self, input_data, uart_communication):
        print("Invoked PCtoSTMRequestMaxMessageSize")

        # Message Structure
        command_code = CommandConstants.PC_TO_STM_REQUEST_MAX_MESSAGE_SIZE
        empty_byte = 0x00

        # Byte Sequence
        checksum = calculate_crc16([command_code] + [empty_byte])

        byte_sequence = bytes([command_code, empty_byte]) + checksum.to_bytes(2, 'big')

        # Send data
        uart_communication.send_data(byte_sequence)

        # Receive response
        received_data = uart_communication.receive_data()

        # Process the response
        max_message_size = self.process_response(received_data)
        return max_message_size

    def process_response(self, received_data):
        """
        Process the response received from the STM.

        Parameters:
        - received_data: The response data received from the STM.

        Returns:
        - The maximum message size as an integer if the response is valid, None otherwise.
        """
        if received_data:
            # Validate the response message structure
            if len(received_data) == 7:  # Ensure correct length
                received_command_code = received_data[0]
                received_max_size = int.from_bytes(received_data[1:5], 'big')
                received_checksum = int.from_bytes(received_data[-2:], 'big')

                # Validate checksum
                calculated_checksum = calculate_crc16(list(received_data[:-2]))
                if calculated_checksum == received_checksum:
                    print("Received Max Message Size:", received_max_size)
                    return received_max_size  # Return maximum message size
                else:
                    print("Checksum error in received data")
            else:
                print("Invalid response data length")
        else:
            print("No response received")

        return None  # Return None if response is not valid


class ProtocolHandler:
    def __init__(self):
        """
        Initializes a ProtocolHandler instance.
        """
        # A dictionary to store registered commands
        self.commands = {}

        # Registers default commands upon initialization
        self.register_default_commands()

    def register_command(self, command_code, command):
        """
        Registers a command with the given command code.

        Parameters:
        - command_code: The unique identifier for the command.
        - command: An instance of the Command class
        """
        self.commands[command_code] = command

    def process_command(self, command_code, input_data, uart_communication):
        """
        Processes a command with the given command code and input data.

        Parameters:
        - command_code: The command code indicating the type of command to be executed.
        - input_data: The input data required for executing the command.

        Returns:
        - The result of executing the command or "Invalid command" if the command is not found.
        """
        # Retrieve the command associated with the command code
        command = self.commands.get(command_code)

        # If the command exists, execute it with the provided input data
        if command:
            return command.execute(input_data, uart_communication)
        else:
            # Return "Invalid command" if the command is not found
            return "Invalid command"

    def register_default_commands(self):
        """
        Registers default commands used in the protocol.

        Default commands are registered with their corresponding command codes.
        """
        # Register default commands using their command codes and corresponding command objects
        self.register_command(CommandConstants.PC_TO_STM_REQUEST_STM_ID,
                              PCtoSTMRequestSTMID(CommandConstants.PC_TO_STM_REQUEST_STM_ID))
        self.register_command(CommandConstants.PC_TO_STM_ENCRYPT_REQUEST,
                              PCtoSTMEncryptRequest(CommandConstants.PC_TO_STM_ENCRYPT_REQUEST))
        self.register_command(CommandConstants.PC_TO_STM_REQUEST_MAX_MESSAGE_SIZE,
                              PCtoSTMRequestMaxMessageSize(CommandConstants.PC_TO_STM_REQUEST_MAX_MESSAGE_SIZE))


def main():
    # Create an instance of the ProtocolHandler
    protocol_handler = ProtocolHandler()

    COM_PORT = 'COM4'
    BAUD_RATE = 9600

    # Create an instance of the UARTCommunication (assuming it's properly implemented)
    uart_communication = UARTCommunication(COM_PORT, BAUD_RATE)
    uart_communication.open_port()

    # Test PCtoSTMRequestSTMID command
    print("Testing PCtoSTMRequestSTMID command:")
    boolean_result = protocol_handler.process_command(CommandConstants.PC_TO_STM_REQUEST_STM_ID, None,
                                                      uart_communication)
    print(boolean_result)

    # Test PCtoSTMEncryptRequest command
    print("Testing PCtoSTMEncryptRequest command:")
    input_data = b"Test data"
    encrypt_data = protocol_handler.process_command(CommandConstants.PC_TO_STM_ENCRYPT_REQUEST, input_data,
                                                    uart_communication)
    print(encrypt_data)

    # Test PCtoSTMRequestMaxMessageSize command
    print("Testing PCtoSTMRequestMaxMessageSize command:")
    received_size = protocol_handler.process_command(CommandConstants.PC_TO_STM_REQUEST_MAX_MESSAGE_SIZE, None,
                                                     uart_communication)
    print(received_size)


if __name__ == "__main__":
    main()

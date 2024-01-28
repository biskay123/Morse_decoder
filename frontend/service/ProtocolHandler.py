from service.Command import Command
from service.CommandConstants import CommandConstants as Constants


class PCtoSTMRequestSTMID(Command):
    def execute(self, input_data):
        print("Invoked PCtoSTMRequestSTMID")
        # Implement logic for PC to STM Request for STM_ID (Command Code: 0x01)
        return input_data


class PCtoSTMEncryptRequest(Command):
    def execute(self, input_data):
        print("Invoked PCtoSTMEncryptRequest")
        # Implement logic for PC to STM Encrypt Request with Data (Command Code: 0x02)
        return input_data


class PCtoSTMRequestMaxMessageSize(Command):
    def execute(self, input_data):
        print("Invoked PCtoSTMRequestMaxMessageSize")
        # Implement logic for PC to STM Request for Max Message Size (Command Code: 0x03)
        return input_data


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

    def process_command(self, command_code, input_data):
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
            return command.execute(input_data)
        else:
            # Return "Invalid command" if the command is not found
            return "Invalid command"

    def register_default_commands(self):
        """
        Registers default commands used in the protocol.

        Default commands are registered with their corresponding command codes.
        """
        # Register default commands using their command codes and corresponding command objects
        self.register_command(Constants.PC_TO_STM_REQUEST_STM_ID,
                              PCtoSTMRequestSTMID(Constants.PC_TO_STM_REQUEST_STM_ID))
        self.register_command(Constants.PC_TO_STM_ENCRYPT_REQUEST,
                              PCtoSTMEncryptRequest(Constants.PC_TO_STM_ENCRYPT_REQUEST))
        self.register_command(Constants.PC_TO_STM_REQUEST_MAX_MESSAGE_SIZE,
                              PCtoSTMRequestMaxMessageSize(Constants.PC_TO_STM_REQUEST_MAX_MESSAGE_SIZE))


"""
if __name__ == '__main__':
    processor = ProtocolHandler()
    command = 0x02
    input_data = "Some data"
    result = processor.process_command(command, input_data)
    print(result)
"""

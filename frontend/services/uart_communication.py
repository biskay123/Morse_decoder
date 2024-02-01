import serial
import time

class UARTCommunication:
    def __init__(self, port, baud_rate):
        """
        Initializes a UARTCommunication instance.

        Parameters:
        - port: The COM port (e.g., 'COM1' or '/dev/ttyUSB0').
        - baud_rate: The baud rate for the UART communication.
        """
        self.serial_port = serial.Serial(port, baud_rate, timeout=1)

    def open_port(self):
        """
        Opens the COM port for UART communication.
        """
        if not self.serial_port.is_open:
            self.serial_port.open()
            print(f"COM port {self.serial_port.name} opened.")
        else:
            print(f"COM port {self.serial_port.name} is already open.")

    def close_port(self):
        """
        Closes the COM port.
        """
        if self.serial_port.is_open:
            self.serial_port.close()
            print(f"COM port {self.serial_port.name} closed.")

    def send_data(self, data):
        """
        Sends data over UART.

        Parameters:
        - data: The data to be sent.
        """
        if self.serial_port.is_open:
            self.serial_port.write(data.encode())
            print(f"Sent data: {data}")

    def receive_data(self):
        """
        Receives data from UART.

        Returns:
        - The received data.
        """
        if self.serial_port.is_open:
            received_data = self.serial_port.readline().decode().strip()
            print(f"Received data: {received_data}")
            return received_data
        
def get_available_com_ports():
    """
    Returns a list of available COM ports.
    """
    return serial.tools.list_ports.comports()


if __name__ == '__main__':
    # Set your COM port and baud rate
    com_port = 'COM4'
    baud_rate = 9600

    # Create an instance of UARTCommunication
    uart_communication = UARTCommunication(com_port, baud_rate)

    try:
        # Open the COM port
        uart_communication.open_port()

        # Example: Send data
        command_code = 0x02
        input_data = "Some data"
        data_to_send = f"{hex(command_code)} {input_data}"
        uart_communication.send_data(data_to_send)

        # Example: Receive data
        received_data = uart_communication.receive_data()

    finally:
        # Close the COM port when done
        uart_communication.close_port()

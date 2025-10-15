import sys
from src.formatter import format_file_size

def main():
    """
    Main entry point for the script.
    Reads a file size in bytes from the command-line argument,
    formats it using format_file_size, and prints the result.

    Usage:
        python main.py <size_in_bytes>

    If no argument or an invalid argument is provided, prints an error message.
    """
    if len(sys.argv) >= 2:
        try:
            size_bytes = int(sys.argv[1])
            formatted_size = format_file_size(size_bytes)
            print(formatted_size)
        except ValueError:
            print("Please provide a valid file size in bytes as a command-line argument.")
    else:
        print("Please provide the file size in bytes as a command-line argument.")

if __name__ == "__main__":
    main() # Dummy

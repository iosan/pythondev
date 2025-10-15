import math

def format_file_size(size_bytes):
    """
    Convert a file size in bytes to a human-readable string.

    Args:
        size_bytes (int): The file size in bytes.

    Returns:
        str: The formatted file size (e.g., '1.23 MB').

    Raises:
        ValueError: If size_bytes is negative.
    """
    if size_bytes < 0:
        raise ValueError("Size cannot be negative")
    if size_bytes == 0:
        return "0B"

    size_units = ["B", "KB", "MB", "GB", "TB"]
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = "{:.2f}".format(size_bytes / p)
    return f"{s} {size_units[i]}"
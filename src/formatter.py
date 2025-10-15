import math


def format_file_size(size_bytes):
    if size_bytes < 0:
        raise ValueError("Size cannot be negative")

    elif size_bytes == 0:
        return "0B"

    size_name = ["B", "KB", "MB", "GB", "TB"]
    i = int(math.floor(math.log(size_bytes) / math.log(1024)))
    p = math.pow(1024, i)
    s = "{:.2f}".format(size_bytes / p)
    return f"{s} {size_name[i]}"

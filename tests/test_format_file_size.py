from formatter import format_file_size


def test_format_file_size_returns_GB_format():
    """
    Test that format_file_size returns the correct string for 1 GB.
    1024**3 bytes should be formatted as '1.00 GB'.
    """
    assert format_file_size(1024**3) == "1.00 GB"

import os
from datetime import datetime
from typing import Any

from src.date_parser import (
    compare_timestamps,
    find_files_with_timestamps,
    parse_timestamp,
    parse_timestamp_from_filename,
    unify_timestamps,
)


def test_parse_timestamp_iso():
    """
    Test parsing an ISO formatted timestamp string.
    """
    ts = "2024-10-15T12:34:56"
    dt = parse_timestamp(ts)
    assert isinstance(dt, datetime)
    assert dt.year == 2024 and dt.month == 10 and dt.day == 15


def test_parse_timestamp_unix():
    """
    Test parsing a Unix timestamp.
    """
    ts = 1728995696  # Unix timestamp for 2024-10-15T12:34:56 UTC
    dt = parse_timestamp(ts)
    assert isinstance(dt, datetime)
    assert dt.year == 2024 and dt.month == 10 and dt.day == 15


def test_unify_timestamps_mixed_formats():
    """
    Test unifying a list of mixed-format timestamps.
    """
    timestamps = ["2024-10-15T12:34:56", 1728995696, "15 Oct 2024 12:34:56", "invalid"]
    results = unify_timestamps(timestamps)
    assert isinstance(results[0], datetime)
    assert isinstance(results[1], datetime)
    assert isinstance(results[2], datetime)
    assert results[3] is None


def test_compare_timestamps():
    """
    Test comparing timestamps in different formats.
    """
    ts1 = "2024-10-15T12:34:56Z"
    ts2 = 1728995696
    assert compare_timestamps(ts1, ts2) == 0
    assert compare_timestamps(ts1, "2024-10-15T12:34:57Z") == -1
    assert compare_timestamps("2024-10-15T12:34:58Z", ts2) == 1
    assert compare_timestamps(ts1, "invalid") is None


def test_parse_timestamp_from_filename():
    """
    Test extracting and parsing timestamps from filenames.
    """
    fname1 = "report_2024_10_15_12_34_56.txt"
    fname2 = "backup_15_10_2024_12_34_56.log"
    dt1 = parse_timestamp_from_filename(fname1)
    dt2 = parse_timestamp_from_filename(fname2)
    assert isinstance(dt1, datetime)
    assert dt1.year == 2024 and dt1.month == 10 and dt1.day == 15 and dt1.hour == 12
    assert isinstance(dt2, datetime)
    assert dt2.year == 2024 and dt2.month == 10 and dt2.day == 15 and dt2.hour == 12


def test_find_files_with_timestamps(tmp_path: Any):
    """
    Test finding files with timestamp substrings in a directory tree.
    """
    filenames = [
        "data_2024_10_15_12_34_56.csv",
        "log_15_10_2024_12_34_56.txt",
        "no_timestamp.txt",
    ]
    subfolder = tmp_path / "sub"
    subfolder.mkdir()
    for fname in filenames:
        (subfolder / fname).write_text("sample")
    found_files = find_files_with_timestamps(str(tmp_path))
    assert any("2024_10_15_12_34_56" in f for f in found_files)
    assert any("15_10_2024_12_34_56" in f for f in found_files)
    assert all("no_timestamp.txt" not in f for f in found_files)


def test_dummy_files_in_data_folder():
    """
    Test using dummy files in the data folder for timestamp extraction and matching.
    """
    data_folder = os.path.join(os.path.dirname(__file__), "..", "data")
    files = find_files_with_timestamps(data_folder)
    if not files:
        # Skip test if no dummy files exist
        return
    timestamps = [parse_timestamp_from_filename(os.path.basename(f)) for f in files]
    timestamps = [ts for ts in timestamps if ts is not None]
    assert len(timestamps) > 0
    # Check that files with the same timestamp are found in different subfolders
    timestamp_to_files = {}
    for f in files:
        ts = parse_timestamp_from_filename(os.path.basename(f))
        if ts:
            timestamp_to_files.setdefault(ts, []).append(f)
    for ts, file_list in timestamp_to_files.items():
        if len(file_list) > 1:
            # There should be at least one matching file for this timestamp in a different subfolder
            assert any(
                os.path.dirname(f1) != os.path.dirname(f2)
                for f1 in file_list
                for f2 in file_list
                if f1 != f2
            )

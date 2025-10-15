import os
import re
from datetime import UTC, datetime
from typing import Dict, List, Optional, Union

import dateutil.parser


def parse_timestamp(timestamp: Union[str, int, float]) -> Optional[datetime]:
    """
    Parse a timestamp in various formats (ISO, RFC, Unix epoch, etc.) and return a naive UTC datetime object.

    Args:
        timestamp (str | int | float): The timestamp to parse.

    Returns:
        Optional[datetime]: The parsed datetime object in UTC, or None if parsing fails.
    """
    if isinstance(timestamp, (int, float)):
        try:
            dt = datetime.fromtimestamp(float(timestamp), UTC)
            return dt.replace(tzinfo=None)
        except Exception:
            return None
    if isinstance(timestamp, str):
        try:
            dt = dateutil.parser.parse(timestamp)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=UTC)
            dt = dt.astimezone(UTC).replace(tzinfo=None)
            return dt
        except Exception:
            try:
                dt = datetime.fromtimestamp(float(timestamp), UTC)
                return dt.replace(tzinfo=None)
            except Exception:
                return None
    return None


def parse_timestamp_from_filename(filename: str) -> Optional[datetime]:
    """
    Extract and parse a timestamp from a filename.
    Supports formats:
      - 'YYYY_MM_DD_HH_MM_SS'
      - 'DD_MM_YYYY_HH_MM_SS'

    Args:
        filename (str): The filename containing a timestamp.

    Returns:
        Optional[datetime]: The parsed datetime object in UTC, or None if not found/invalid.
    """
    match = re.search(r"(\d{4})_(\d{2})_(\d{2})_(\d{2})_(\d{2})_(\d{2})", filename)
    if match:
        try:
            dt = datetime(
                int(match.group(1)),
                int(match.group(2)),
                int(match.group(3)),
                int(match.group(4)),
                int(match.group(5)),
                int(match.group(6)),
                tzinfo=UTC,
            )
            return dt.replace(tzinfo=None)
        except Exception:
            return None
    match = re.search(r"(\d{2})_(\d{2})_(\d{4})_(\d{2})_(\d{2})_(\d{2})", filename)
    if match:
        try:
            dt = datetime(
                int(match.group(3)),
                int(match.group(2)),
                int(match.group(1)),
                int(match.group(4)),
                int(match.group(5)),
                int(match.group(6)),
                tzinfo=UTC,
            )
            return dt.replace(tzinfo=None)
        except Exception:
            return None
    return None


def find_files_with_timestamps(base_folder: str) -> List[str]:
    """
    Recursively find files in subfolders of base_folder that contain a timestamp substring
    in the format 'YYYY_MM_DD_HH_MM_SS' or 'DD_MM_YYYY_HH_MM_SS'.

    Args:
        base_folder (str): The base directory to search.

    Returns:
        List[str]: List of file paths containing a timestamp substring.
    """
    files_with_timestamps = []
    for root, _, files in os.walk(base_folder):
        for file in files:
            if re.search(r"\d{4}_\d{2}_\d{2}_\d{2}_\d{2}_\d{2}", file) or re.search(
                r"\d{2}_\d{2}_\d{4}_\d{2}_\d{2}_\d{2}", file
            ):
                files_with_timestamps.append(os.path.join(root, file))
    return files_with_timestamps


def unify_timestamps(
    timestamps: List[Union[str, int, float]],
) -> List[Optional[datetime]]:
    """
    Convert a list of timestamps to unified datetime objects.

    Args:
        timestamps (List[str | int | float]): List of timestamps in various formats.

    Returns:
        List[Optional[datetime]]: List of datetime objects (or None for failed parses).
    """
    return [parse_timestamp(ts) for ts in timestamps]


def compare_timestamps(
    ts1: Union[str, int, float], ts2: Union[str, int, float]
) -> Optional[int]:
    """
    Compare two timestamps after unifying their formats.

    Args:
        ts1 (str | int | float): First timestamp.
        ts2 (str | int | float): Second timestamp.

    Returns:
        Optional[int]: -1 if ts1 < ts2, 0 if equal, 1 if ts1 > ts2, None if either can't be parsed.
    """
    dt1 = parse_timestamp(ts1)
    dt2 = parse_timestamp(ts2)
    if dt1 is None or dt2 is None:
        return None
    if dt1 < dt2:
        return -1
    elif dt1 > dt2:
        return 1
    else:
        return 0


if __name__ == "__main__":
    """
    If run as a script, find files with timestamp substrings in the data folder,
    print their parsed timestamps, and show matches in other subdirectories.
    """
    data_folder = os.path.join(os.path.dirname(__file__), "..", "data")
    files = find_files_with_timestamps(data_folder)
    if files:
        print("Found files with timestamp substrings:")
        # Build a mapping from timestamp to file
        timestamp_to_files: Dict[datetime, List[str]] = {}
        for f in files:
            ts = parse_timestamp_from_filename(os.path.basename(f))
            if ts:
                timestamp_to_files.setdefault(ts, []).append(f)
        # For each file, try to find a matching file in other subdirs
        for ts, file_list in timestamp_to_files.items():
            for file in file_list:
                print(f"File: {file}")
                print(f"  Parsed timestamp: {ts}")
                # Find matches in other subdirs
                matches = [
                    f
                    for f in files
                    if f != file
                    and parse_timestamp_from_filename(os.path.basename(f)) == ts
                ]
                if matches:
                    print("  Matching files in other subdirs:")
                    for match in matches:
                        print(f"    {match}")
                else:
                    print("  No matching files found in other subdirs.")
    else:
        print("No files with timestamp substrings found in the data folder.")

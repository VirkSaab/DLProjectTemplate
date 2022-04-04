import os
import time
import subprocess
from pathlib import Path
from typing import Union, Callable, Any

__all__ = [
    # Functions
    'manage_log_files', 'get_recent_githash',

    # Decorators
    'show_exec_time',

]

# ============================= FUNCTIONS ==============================


def get_recent_githash():
    """Get the recent commit git hash"""
    proc = subprocess.Popen(["git", "rev-parse", "HEAD"],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.stdout.read().strip().decode('ascii')


def manage_log_files(logs_dir: Union[str, Path],
                     keep_n_recent_logs: int = 5,
                     file_ext: str = '.log') -> None:
    """Log files rotation handler

    Args:
        logs_dir: Folder path where the logs will be saved.
        keep_n_recent_logs: Number of files with same name to save.
            Oldest file will be deleted first.
        file_ext: file extension to filter out relevant files.
    """
    # Get log files paths
    log_filespaths = list(Path(logs_dir).glob(f"*{file_ext}"))
    # Function to split the timestamp from filepath

    def get_time_from_filename(x):
        try:
            return float(x.stem.split('@')[-1])
        except ValueError:
            return None

    # Sort timestamps
    timestamps = sorted(
        filter(
            lambda x: False if x is None else True,
            list(map(get_time_from_filename, log_filespaths))
        ),
        reverse=True)
    # Keep only n recent files
    timestamps = timestamps[: keep_n_recent_logs]
    # Remove old files
    for fp in log_filespaths:
        if get_time_from_filename(fp) not in timestamps:
            os.remove(fp)


# ============================= CLASSES ==============================


# ============================== DECORATORS ==============================
def show_exec_time(func: Callable) -> Any:
    """Display the execution time of a function.

        This decorator is suited to large programs that takes
            more than a second to run.

        Example:

            .. code-block:: python

                @show_exec_time
                def take_a_break(timeout=10):
                    time.sleep(timeout)

                >>> take_a_break()
                >>> >> Completed in 00h:00m:10s <<
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()

        # Run the given function
        results = func(*args, **kwargs)

        end_time = time.time()

        hrs = (end_time - start_time) // 3600
        rem = (end_time - start_time) % 3600
        mins = rem // 60
        secs = rem % 60

        hrs = str(round(hrs)).zfill(2)
        mins = str(round(mins)).zfill(2)
        secs = str(round(secs)).zfill(2)

        print(f"\n>> Completed in {hrs}h:{mins}m:{secs}s <<\n")

        return results
    return wrapper

import datetime


def timestamp():
    """Return current timestamp string."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log_info(message: str):
    """Print informational logs with timestamp."""
    print(f"[INFO] {timestamp()} - {message}")


def log_error(message: str):
    """Print error logs with timestamp."""
    print(f"[ERROR] {timestamp()} - {message}")

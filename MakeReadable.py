"""MakeReadable.py."""
import time


def human_readable(epoch_time=0):
    """Function to convert epoch time to a human-readable format."""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time))

print(human_readable(1347517370))
print(human_readable())

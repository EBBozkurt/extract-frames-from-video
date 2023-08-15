import sys


def progress_inditacor(count, total, status=''):
    """
    Display a progress bar with percentage completion.

    Args:
        count (int): Current count or progress value. \n
        total (int): Total count or progress value. \n
        status (str): Optional status message to display after the progress bar.

    Returns:
        None

    """

    # Set the length of the progress bar to 60 characters
    bar_len = 60

    # Calculate the number of filled characters in the progress bar
    filled_len = int(round(bar_len * count / total))

    # Calculate the percentage completion
    percents = round(100.0 * count / total, 1)

    # Create the progress bar with filled and empty characters
    bar = '*' * filled_len + '-' * (bar_len - filled_len)

    # Write the progress bar and percentage completion to the console
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))

    # Flush the output to the console to ensure it is immediately displayed
    sys.stdout.flush()

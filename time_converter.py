SECONDS_PER_MINUTE = 60

def seconds_to_minutes(seconds: float) -> float:
    """
    Converts time from seconds to minutes.

    :param seconds: Time duration in seconds.
    :return: Equivalent duration in minutes.
    """
    return seconds / SECONDS_PER_MINUTE

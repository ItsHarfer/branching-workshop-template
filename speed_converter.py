MPS_TO_KPH = 3.6

def mps_to_kph(speed_mps: float) -> float:
    """
    Converts speed from meters per second (m/s) to kilometers per hour (km/h).

    :param speed_mps: Speed in meters per second.
    :return: Equivalent speed in kilometers per hour.
    """
    return speed_mps * MPS_TO_KPH
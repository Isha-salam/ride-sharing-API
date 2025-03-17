from .models import Driver
import random

def find_best_driver(pickup_location):
    available_drivers = Driver.objects.filter(is_available=True)

    if not available_drivers.exists():
        return None

    sorted_drivers = sorted(available_drivers, key=lambda d: d.rating, reverse=True)


    best_driver = sorted_drivers[0]

    return best_driver

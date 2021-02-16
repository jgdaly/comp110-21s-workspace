"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730356913"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: a: int = int(input("days_to_target"())
    # TODO 4: b: str = str(future_date())
    # TODO 5: print("a", which falls on "b")


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    population2: int = (100)
    doses2: int = (50)
    doses_per_day2: int = (2)
    target2: int = (50)
    return("We will reach 50% vaccination in 25 days")
    Population1: int = (330000000)
    Doses1: int = (32780860)
    Doses_per_Day1: int = (1319981)
    Target_percent1: int = (80)
    return("We will reach 80% vaccination in 375 days")
    Population3: int = (30000)
    Doses3: int = (1234)
    Doses_per_Day3: int = (4321)
    Target_percent3: int = (100)
    return("We will reach 100% vaccination in 14 days")
    days_to_target()

# TODO 3: Define future_date function


def future_date(days_into_future: int) -> str:
    today: datetime = datetime.today()
    one_day: timedelta = timedelta(1)
    tomorrow: datetime = today + one_day
    fortnight: timedelta = timedelta(7 + 7)
    future_date: datetime = today + fortnight
    return(future_date.strftime("%B %d, %Y"))
    


if __name__ == "__main__":
    main()

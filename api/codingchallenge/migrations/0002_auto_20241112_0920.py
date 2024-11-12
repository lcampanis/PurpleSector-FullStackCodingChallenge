from django.db import migrations


def forwards_func(apps, schema_editor):
    data = {
        "VER": {
            "1": 99.019,
            "2": 97.974,
            "3": 98.006,
            "4": 97.976,
            "5": 98.035,
            "6": 97.986,
            "7": 98.021,
            "8": 98.154,
        },
        "GAS": {
            "1": 100.438,
            "2": 100.643,
            "3": 100.894,
            "4": 100.818,
            "5": 101.11,
            "6": 101.134,
            "7": 101.173,
            "8": 98.762,
        },
        "PER": {
            "1": 101.063,
            "2": 98.862,
            "3": 98.83,
            "4": 98.758,
            "5": 98.404,
            "6": 98.718,
            "7": 98.804,
            "8": 99.172,
        },
        "ALO": {
            "1": 99.792,
            "2": 99.1,
            "3": 99.548,
            "4": 99.662,
            "5": 99.674,
            "6": 99.729,
            "7": 99.959,
            "8": 100.275,
        },
        "LEC": {
            "1": 100.23,
            "2": 98.75,
            "3": 98.658,
            "4": 98.825,
            "5": 98.664,
            "6": 98.572,
            "7": 98.691,
            "8": 98.614,
        },
        "STR": {
            "1": 99.892,
            "2": 99.625,
            "3": 99.745,
            "4": 99.144,
            "5": 99.714,
            "6": 99.945,
            "7": 99.801,
            "8": 100.106,
        },
        "SAR": {
            "1": 100.467,
            "2": 100.349,
            "3": 100.644,
            "4": 100.902,
            "5": 100.791,
            "6": 100.892,
            "7": 100.868,
            "8": 100.908,
        },
        "MAG": {
            "1": 101.521,
            "2": 101.978,
            "3": 100.773,
            "4": 101.34,
            "5": 101.125,
            "6": 101.526,
            "7": 101.283,
            "8": 101.278,
        },
        "RIC": {
            "1": 101.289,
            "2": 100.914,
            "3": 100.373,
            "4": 100.63,
            "5": 101.125,
            "6": 101.166,
            "7": 101.23,
            "8": 101.573,
        },
        "TSU": {
            "1": 100.837,
            "2": 100.243,
            "3": 99.95,
            "4": 101.131,
            "5": 100.886,
            "6": 100.952,
            "7": 100.846,
            "8": 101.01,
        },
        "ALB": {
            "1": 100.43,
            "2": 100.143,
            "3": 99.761,
            "4": 100.606,
            "5": 100.744,
            "6": 100.646,
            "7": 100.918,
            "8": 100.969,
        },
        "ZHO": {
            "1": 99.33,
            "2": 99.229,
            "3": 98.998,
            "4": 99.143,
            "5": 98.873,
            "6": 98.794,
            "7": 98.896,
            "8": 98.888,
        },
        "HUL": {
            "1": 100.72,
            "2": 100.484,
            "3": 101.004,
            "4": 101.002,
            "5": 101.002,
            "6": 101.148,
            "7": 101.249,
            "8": 101.615,
        },
        "OCO": {
            "1": 100.408,
            "2": 99.948,
            "3": 99.543,
            "4": 100.281,
            "5": 100.331,
            "6": 100.488,
            "7": 100.562,
            "8": 100.866,
        },
        "NOR": {
            "1": 100.433,
            "2": 99.777,
            "3": 100.664,
            "4": 100.814,
            "5": 100.726,
            "6": 100.857,
            "7": 100.783,
            "8": 99.314,
        },
        "HAM": {
            "1": 102.288,
            "2": 99.166,
            "3": 99.22,
            "4": 99.198,
            "5": 99.335,
            "6": 99.756,
            "7": 99.757,
            "8": 100.267,
        },
        "SAI": {
            "1": 101.659,
            "2": 98.933,
            "3": 99.042,
            "4": 98.985,
            "5": 99.128,
            "6": 99.474,
            "7": 99.502,
            "8": 99.779,
        },
        "RUS": {
            "1": 102.662,
            "2": 99.59,
            "3": 99.093,
            "4": 99.261,
            "5": 99.549,
            "6": 99.493,
            "7": 100.056,
            "8": 100.31,
        },
        "BOT": {
            "1": 104.154,
            "2": 99.956,
            "3": 99.397,
            "4": 99.823,
            "5": 101.033,
            "6": 100.265,
            "7": 100.564,
            "8": 100.387,
        },
        "PIA": {
            "1": 100.83,
            "2": 100.691,
            "3": 100.718,
            "4": 100.862,
            "5": 101.111,
            "6": 101.167,
            "7": 101.295,
            "8": 101.534,
        },
    }
    driver = apps.get_model("codingchallenge", "Driver")
    event = apps.get_model("codingchallenge", "Event")
    race = apps.get_model("codingchallenge", "Race")
    e = event.objects.create(name="Monaco Grand Prix")
    drivers = driver.objects.bulk_create(
        [
            driver(**i)
            for i in [
                {"name": "Kevin Magnussen", "tla": "MAG"},
                {"name": "Oscar Piastri", "tla": "PIA"},
                {"name": "Alex Albon", "tla": "ALB"},
                {"name": "Nico Hulkenberg", "tla": "HUL"},
                {"name": "Logan Sargeant", "tla": "SAR"},
                {"name": "Lewis Hamilton", "tla": "HAM"},
                {"name": "Pierre Gasly", "tla": "GAS"},
                {"name": "Daniel Ricciardo", "tla": "RIC"},
                {"name": "Lance Stroll", "tla": "STR"},
                {"name": "Sergio Perez", "tla": "PER"},
                {"name": "Valtteri Bottas", "tla": "BOT"},
                {"name": "Fernando Alonso", "tla": "ALO"},
                {"name": "Yuki Tsunoda", "tla": "TSU"},
                {"name": "Esteban Ocon", "tla": "OCO"},
                {"name": "Guanyu Zhou", "tla": "ZHO"},
                {"name": "George Russell", "tla": "RUS"},
                {"name": "Carlos Sainz", "tla": "SAI"},
                {"name": "Lando Norris", "tla": "NOR"},
                {"name": "Charles Leclerc", "tla": "LEC"},
                {"name": "Max Verstappen", "tla": "VER"},
            ]
        ]
    )
    driver_dict = {d.tla: d for d in drivers}
    laps_obj = []
    for tla, laps in data.items():
        for lap_number, lap_time in laps.items():
            laps_obj.append(
                race(
                    driver=driver_dict[tla],
                    event=e,
                    lap_number=lap_number,
                    lap_time=lap_time,
                )
            )
    race.objects.bulk_create(laps_obj)


def reverse_func(apps, schema_editor):
    driver = apps.get_model("codingchallenge", "Driver")
    event = apps.get_model("codingchallenge", "Event")
    race = apps.get_model("codingchallenge", "Race")
    driver.objects.all().delete()
    event.objects.all().delete()
    race.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("codingchallenge", "0001_initial"),
    ]

    operations = [migrations.RunPython(forwards_func, reverse_func)]

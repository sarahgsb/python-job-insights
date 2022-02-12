from functools import lru_cache

import csv


@lru_cache
def read(path):
    with open(path, "r") as file:
        items = []
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in jobs_reader:
            items.append(row)

    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    return items


# print(read("src/jobs.csv"))

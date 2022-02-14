from src.jobs import read
from src.insights import get_min_salary
from src.sorting import sort_by


def test_sort_by_criteria():
    job = read("src/jobs.csv")
    sort_by(job, "min_salary")
    sort = job[0]["min_salary"]
    assert type(job) is list
    assert sort == str(get_min_salary("src/jobs.csv"))
    pass

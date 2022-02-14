from src.jobs import read


def get_unique_job_types(path):
    unique_job_types = set()
    job = read(path)
    for job_types in job:
        unique_job_types.add(job_types["job_type"])

    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """

    return unique_job_types


# print(read("src/jobs.csv"))


def filter_by_job_type(jobs, job_type):
    filter_by_job = list()
    for job in jobs:
        if job["job_type"] == job_type:
            filter_by_job.append(job)
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return filter_by_job


def get_unique_industries(path):
    unique_industries = set()
    jobs = read(path)
    for industries in jobs:
        if industries["industry"] != "":
            unique_industries.add(industries["industry"])

    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    return unique_industries


def filter_by_industry(jobs, industry):
    filter_industry = list()
    for job in jobs:
        if job["industry"] == industry:
            filter_industry.append(job)
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return filter_industry


def get_max_salary(path):
    max_salary = set()
    job = read(path)
    for salary in job:
        if salary["max_salary"].isnumeric():
            max_salary.add(int(salary["max_salary"]))
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    return max(max_salary)


def get_min_salary(path):
    min_salary = set()
    job = read(path)
    for salary in job:
        if salary["min_salary"].isnumeric():
            min_salary.add(int(salary["min_salary"]))
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    return min(min_salary)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    filter_salary = list()
    for job in jobs:
        if job["job_type"] == salary:
            filter_salary.append(job)
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return filter_salary

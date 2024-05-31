from unittest import TestCase

time_constraints = [5, 5, 10, 10, 15, 15, 20, 20] # [very easy, very easy, easy, easy, medium, medium, hard, hard]


def interview(times, total_time):
    result = 'qualified';

    if (len(times) != len(time_constraints)) or (total_time > 120):
        result = 'disqualified'
    else:
        for time, max_time in zip(times, time_constraints):
            if time > max_time:
                result = 'disqualified'
                break

    print(result)

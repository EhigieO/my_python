def get_length(list_numbers):
    counter = 0
    for _ in list_numbers:
        counter += 1
    return counter


def get_sum(list_numbers):
    sum_of_numbers = 0
    count = 0
    for _ in list_numbers:
        sum_of_numbers += list_numbers
        count += 1
    return sum_of_numbers


def get_mean(list_numbers):
    mean = get_sum(list_numbers)/get_length(list_numbers)
    return mean

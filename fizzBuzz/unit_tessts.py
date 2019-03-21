from fizz_buzz import get_sum_figs, is_divisible_by_five, is_divisible_by_three, process_input_data, main
import functools
import json


def test_function(func):
    file_name = func.__name__ + ".json"
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with open(file_name, "r") as f:
            test_data = json.load(f)
        if "process_input_data" in func.__name__:
            exp_list = []
            input_list = []
            for key in test_data:
                exp_list.append(test_data[key])
                input_list.append(key)
            result_list = func(input_list)
            assert result_list == exp_list
            return
        for key in test_data:
            result = func(key)
            expectation = test_data[key]
            if "is" in func.__name__:
                assert result == expectation
            else:
                assert result == expectation
    return wrapper

@test_function
def test_get_sum_figs(*args, **kwargs):
    return get_sum_figs(*args, **kwargs)


@test_function
def test_is_divisible_by_five(*args, **kwargs):
    return is_divisible_by_five(*args, **kwargs)


@test_function
def test_is_divisible_by_three(*args, **kwargs):
    return is_divisible_by_three(*args, **kwargs)


@test_function
def test_process_input_data(*args, **kwargs):
    return process_input_data(*args, **kwargs)


def run_test_suite():
    test_get_sum_figs()
    test_is_divisible_by_five()
    test_is_divisible_by_three()
    test_process_input_data()

run_test_suite()
import numpy as np
import datetime

def task1():
    vector = np.linspace(10,49,40)
    print(vector)
    vector_reversed = np.flip(vector)
    print(vector_reversed)

def task2():
    random_array = np.random.random((5, 5))
    print(random_array)
    return random_array

def task3():
    random_array = random_array = np.random.random((5,5))
    mean = np.mean(random_array)
    standard_deviation = np.std(random_array)
    normalized_array = (random_array - mean) / standard_deviation
    print(normalized_array)

def task4():
    m5by3 = np.random.random((5, 3))
    m3b2 = np.random.random((3, 2))
    print(np.dot(m5by3, m3b2))

def task5():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    next_month = tomorrow + datetime.timedelta(days=26)
    print(yesterday)
    print(today)
    print(tomorrow)
    print(next_month)

def task6():
    random_array = 2 * np.random.random((5, 5))
    integer_rounded_down = np.floor(random_array)
    integer_rounded_up = np.ceil(integer_rounded_down)
    integer_rounded = np.round(integer_rounded_up)
    integer_truncated = np.trunc(integer_rounded)
    print(integer_rounded)
    print(integer_rounded_down)
    print(integer_rounded_up)
    print(integer_truncated)
    print(random_array.astype(int))

def task7():
    struct = [
        ("pos", [("x",int),("y",int)]),
        ("color", [("r",int),("g",int),("b",int)])
    ]
    empty_struct = np.zeros(2,dtype = struct)
    print(empty_struct)

def generator_function():
    for x in range(10):
        yield 10 - x

def task8():
    array_from_generator = np.array(list(generator_function()))
    print(array_from_generator)

def task9():
    random_one = np.random.randint(0,2,2)
    random_two = np.random.randint(0,2,2)
    print(np.array_equal(random_one, random_two))

def task10():
    random_x = np.random.random((100,2))

def main():
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    # task8()
    task9()


if __name__ == "__main__":
    main()
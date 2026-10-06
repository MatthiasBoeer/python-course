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
    random = np.random.random((100,2))
    X = np.atleast_2d(random[:,0])
    Y = np.atleast_2d(random[:,1])
    distance = np.sqrt((X-X.T)**2 + (Y-Y.T)**2)
    print(distance)

def task11():
    A = np.random.randint(-5,5,25).reshape(5,5)
    print(A)
    B = A - A.mean(axis=1)[:,np.newaxis]
    print(B)

def task12():
    A = np.random.randint(-5,5,(5,5))
    print(A)
    B = A.argsort()
    print(B)

def task13():
    A = np.random.randint(-5,5,(5,5))
    print(A)
    rank = np.linalg.matrix_rank(A)
    print(rank)

def task14():
    A = np.random.randint(-5,5,(16,16))
    print("A= ", A)
    B = A.reshape(4,4,4,4)
    print("B= ", B)
    C = B.sum(axis=(1,3))
    print("C= ", C)

def main():
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    # task8()
    # task9()
    # task10()
    # task11()
    # task12()
    # task13()
    task14()


if __name__ == "__main__":
    main()
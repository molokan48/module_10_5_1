import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    file_start_time = time.time()
    with open(name) as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()
    file_read_time = time.time()
    print(f'Файл {str(name[2::])} прочитан за {round(file_read_time - file_start_time, 4)}')


def linear_read(filenames):
    start_time = time.time()
    for name in filenames:
        read_info(name)
    stop_time = time.time()
    print(f'Линейный вызов: {round(stop_time - start_time, 4)}')


def parallel_read(filenames):

    start_time = time.time()
    x= 0
    pool_name = []

    for name in filenames:
        x+= 1
        pool_name.append(name)

    with Pool(processes= x) as pool:
        pool.map(read_info, pool_name,)
        stop_time = time.time()
        print(f'Многопроцессный вызов: {round(stop_time - start_time, 4)}')



if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    parallel_read(filenames)
    linear_read(filenames)
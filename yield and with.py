
# def generators(a):
#     for n in range(a):
#         yield n ** 2
# for generator in generators(1000):
#     print(generator)

# my_list = [x**2 for x in range(1,1000)]
# print(my_list)















# import contextlib

# with open('test.txt', 'w') as file:
#     file.write('It is new text...')
#     print(file.closed)

# print(file.closed)

# @contextlib.contextmanager
# def str_reverse(my_str):
#     print('Входим в контекстный менеджер:')
#     yield my_str[::-1]
#     print('Вышли из контекствного менеджера.')


# with str_reverse('Привет, мир!') as reverse:
#     print(reverse)








from course import get_course
import contextlib

@contextlib.contextmanager
def get_course_info(my_str):
    try:
        print('Входим в контекстный менеджер:')
        yield my_str
    except OSError:
        print("error!")
    finally:
        print('Вышли из контекствного менеджера.')


with get_course_info(f'{get_course(input("Введите ID валюты: "))}') as currency:
    print(f'(1 шт.) {input("Введите название валюты: ")}  стоит(ят)', currency)
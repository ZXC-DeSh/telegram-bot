# import time

# class RunningCodeJudge:
#     def __init__(self):
#         self.start = None
    
#     def __enter__(self):
#         self.start = time.time()
#         return 15

#     def __exit__(self,exc_type, exc_val, exc_tb):
#         print(f'Время: {time.time() - self.start}')
        
#         if exc_type is TypeError:
#             return True

# with RunningCodeJudge():
#     my_list = [x for x in range(1, 100_000_001)]
#     my_list -= 'str'







# my_list = [1, 2, 3, 4]
# list_iterator = iter(my_list)
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))

# for i in list_iterator:
# print(i)






import random


class RandomIter:
    def __init__(self, limit):
        self.limit = limit
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.limit == 0:
            raise StopIteration
        self.limit -= 1
        return random.randint(1, 100)
 
rand_iter = RandomIter(0)

for i in rand_iter:
    print(i)
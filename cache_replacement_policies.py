import random


def cache_replacement_policies():
    print('cache hit rate with belady\'s algorithm (optimal) replacement policy: ' + str(optimal_policy))
    print('cache hit rate with random replacement policy: ' + str(random_policy))
    print('cache hit rate with first-in-first-out replacement policy: ' + str(fifo_policy))
    print('cache hit rate with least-recently-used replacement policy: ' + str(lru_policy))

cache_replacement_policies(2000)

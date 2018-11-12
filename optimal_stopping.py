import random


def optimal_stopping(sample_size, iterations):
    global_optimal = sample_size
    optimal_hits = 0
    threshold = int(sample_size * .369)

    for i in range(iterations):
        values = random.sample(range(1, sample_size + 1), sample_size)
        explore = (x for x in values[:threshold + 1])
        exploit = (x for x in values[threshold:])

        explore_optimal = max(explore)
        exploit_next_best = next((x for x in exploit if x > explore_optimal), 0)

        if exploit_next_best == global_optimal:
            optimal_hits += 1

    percentage = (1.0 * optimal_hits / iterations) * 100
    print("optimal hit rate: " + str(percentage) + "%")

optimal_stopping(100, 1000)

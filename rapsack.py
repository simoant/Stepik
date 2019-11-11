import sys
import heapq


def fractional_knapsack(capacity, values_and_weights):
    order = [(-v / w, w) for v, w in values_and_weights]
    heapq.heapify(order)
    # print(order)
    acc = 0
    while order and capacity:
        v_per_w, w = heapq.heappop(order)
        can_take = min(w, capacity)
        acc += -v_per_w * can_take
        capacity -= can_take

    return acc


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, capacity = next(reader)
    # print ( n, capacity)
    values_and_weights = list(reader)
    # print (values_and_weights)
    assert(len(values_and_weights) == n)
    opt_value = fractional_knapsack(capacity, values_and_weights)
    print ("{:.3f}".format(opt_value))

def test():
    from random import randint
    from timing import timed

    for attemps in range(100):
        n = randint(0, 1000)
        capacity = randint(0, 2 * 10 ** 6)
        values_and_weights = []
        for i in range(n):
            values_and_weights.append((randint(0, 2 * 10**6), randint(1, 2 * 10**6)))
        t = timed(fractional_knapsack, capacity, values_and_weights)
        assert t < 5
        print("{:.10f}".format(t))

if __name__ == '__main__':
    test()
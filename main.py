from time import perf_counter


def timer(func):

    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        func(*args, **kwargs)
        end_time = perf_counter()
        total_time = end_time - start_time
        print(f'execution time is: {total_time:.4f}')

    return wrapper


@timer
def main():
    t = {}
    for _ in range(int(input())):
        w = input().lower()

        s = tuple(sorted(w))
        if s not in t:
            t[s] = [w]
        elif w not in t[s]:
            t[s].append(w)

    for val in t.values():
        if len(val) != 1:
            print(*val)


main()


# 0.00007780

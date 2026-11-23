from functools import reduce
def main():
    sets_list = [
        set(map(int, input(": ").split())),
        set(map(int, input(": ").split())),
        set(map(int, input(": ").split())),
    ]
    result = reduce(lambda a, b: a | b, sets_list)
    print("各集合:", sets_list)
    print("并集:", result)
if __name__ == "__main__":
    main()
# Demonstrate basic generator works


def skip1(start, stop):
    # generator function
    # yield returns value then pauses execution
    # can be resumed any time later
    for i in range(start, stop + 1, 2):
        yield i


def main():
    # produces generator DOES NOT RUN
    # when generator function called returns a generator instance from "generator" class
    g1 = skip1(3, 25)
    # Need to invoke with built-in next() function
    i = next(g1)
    print(i)
    # Now do a bunch
    for _ in range(11):
        i = next(g1)
        print(i)

    # This would exhaust the generator and raise StopIteration exception
    # i = next(g1)

    g2 = skip1(6, 15)

    # can pass generator into a list function or tuple function
    list_g2 = list(g2)
    print(list_g2)

    g3 = skip1(1, 9)
    # can iterate over since generator is also an iterator
    for i in g3:
        print(i)

    # can use in list comprehension
    vals = [num for num in skip1(3, 15)]
    print(vals)


if __name__ == "__main__":
    main()

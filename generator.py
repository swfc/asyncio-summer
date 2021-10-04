"""Module docstring."""
from typing import Generator


def odds(start: int, stop: int) -> Generator:
    """Every generator is an itorator.

    You can pass it to next().
    Think of as a producer.

    Args:
        start (int): [description]
        stop (int): [description]

    Yields:
        Generator: [description]
    """
    for odd in range(start, stop + 1, 2):
        yield odd


def main():
    print(type(odds(3, 15)))
    g1 = odds(3, 15)
    g2 = odds(7, 21)
    g3 = odds(21, 33)
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))
    # another next call would cause StopIteration exception

    list_using_for = [odd for odd in odds(7, 21)]
    print(list_using_for)

    list_from_gen = list(g2)
    print(list_from_gen)

    tup_from_gen = tuple(g3)
    print(tup_from_gen)

    my_list = [1, 2, 3, 4, 5]
    # my_list is iterable but not an iterator
    # use iter to make an iterable an iterator
    iterable_list = iter(my_list)
    # now iterable_list has a __next__ method
    print(next(iterable_list))
    print(next(iterable_list))
    print(next(iterable_list))
    print(next(iterable_list))
    print(next(iterable_list))


if __name__ == "__main__":
    main()

from typing import List, Tuple

"""
4
8 2
300 100 300 300 200 100 800 500
5 3
100 100 100 100 3
7 3
10 20 40 10 10 30 30
10 2
30 30 60 60 90 90 60 60 30 30
"""


def read_input():
    pass


def num_req(k: int, lst: List[int]) -> int:

    t_processed = lst_to_tup(lst)

    if t_processed[0] - 1 <= k:
        return 0
    else:
        calc_req(k, t_processed)


def lst_to_tup(lst: List[int]) -> Tuple[int, List[tuple]]:
    """

    >>> lst = [300, 100, 300, 300, 200, 100, 800, 500]
    >>> lst_to_tup(lst)
    (7, [(1, 300), (1, 100), (2, 300), (1, 200), (1, 100), (1, 800), (1, 500)])
    """
    tup_lst = []
    count = 1
    num = lst[0]
    tup_count = 0

    for i in (range(1, len(lst))):

        if lst[i] != lst[i-1]:
            tup_lst.append((count, num))
            tup_count += 1
            count = 1
            num = lst[i]
        else:
            count += 1

    tup_lst.append((count, num))    # add on complete
    tup_count += 1

    return tup_count, tup_lst


def calc_req(k: int, t_processed: Tuple[int, List[tuple]]) -> int:
    pass


# UNUSED

# def num_changes(lst: List[int]) -> int:
#     """
#
#     >>> lst = [300, 100, 300, 300, 200, 100, 800, 500]
#     >>> num_changes(lst)
#     6
#     """
#
#     changes = 0
#     for i in (range(1, len(lst))):
#         if lst[i] != lst[i-1]:
#             changes += 1
#
#     return changes

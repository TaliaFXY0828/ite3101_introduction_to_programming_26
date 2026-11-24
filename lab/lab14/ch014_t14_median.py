
from typing import List


def median(lst:List[int]) -> float:
    sorted_lst = sorted(lst)
    if len(sorted_lst) % 2==0:
        index_1 = length // 2 -1
        index_2 = length // 2
        return (sorted_lst[index_1] + sorted_lst[index_2]) / 2.0
    index = length // 2
    return sorted_lst[index]
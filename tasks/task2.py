
def func2(ids: dict) -> list:
    all_lst = []
    for i in ids.values():
        all_lst += i

    return list(set(all_lst))
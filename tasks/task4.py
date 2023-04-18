
def func4(stats:dict) -> str:
    name, maxlen = None, 0
    for i in stats.keys():
        if name == None or stats[i] > maxlen:
            name, maxlen = i, stats[i]

    return name
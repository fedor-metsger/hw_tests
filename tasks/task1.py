
def func1(geo_logs: list) -> list:
    rus_logs = []
    for i in geo_logs:
        for j in i.values():
            if "Россия" == j[1]:
                rus_logs.append(i)
                break

    return rus_logs
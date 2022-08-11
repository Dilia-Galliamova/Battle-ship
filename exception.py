class NotNumber(Exception):
    pass


class OutOfRange(Exception):
    pass


def trigger_exception(index):
    if str(index).isdigit() is False:
        raise NotNumber()
    elif not (int(index) // 10 in [1, 2, 3, 4, 5, 6] and int(index) % 10 in [1, 2, 3, 4, 5, 6]):
        raise OutOfRange()

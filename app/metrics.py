def conversion_rate(visitors, buyers):

    if visitors == 0:
        return 0

    return round(
        buyers / visitors * 100,
        2
    )
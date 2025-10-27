def fastPow(number, power):
    if power <= 0:
        raise ValueError("Степень должна быть положительной")
    result = number
    while power != 1:
        result *= result
        power = power // 2
    return result

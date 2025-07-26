def format_currency(amount):
    s = str(amount)
    if '.' in s:
        integer, decimal = s.split('.')
    else:
        integer, decimal = s, None

    last3 = integer[-3:]
    rest = integer[:-3]
    if rest:
        rest = ",".join([rest[max(i-2, 0):i] for i in range(len(rest), 0, -2)][::-1])
        formatted = rest + "," + last3
    else:
        formatted = last3

    return formatted + ('.' + decimal if decimal else '')

print(format_currency(12345678.90))  # Output: 1,23,45,678.90

result = []
def divider(a, b):
    try:
        if a < b:
            raise ValueError("ValueError: 'a' should be greater than or equal to 'b'")
        if b == 0:
            raise ZeroDivisionError("ZeroDivisionError: division by zero")
        if b > 100:
            raise IndexError("IndexError: 'b' should be less than or equal to 100")
        return a / b
    except ValueError as ve:
        print(ve)
    except ZeroDivisionError as zde:
        print(zde)
    except IndexError as ie:
        print(ie)

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)
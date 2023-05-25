def calc(func):
    def wrapper(*args, **kwargs):
        print("Calculating...")
        result = func(*args, **kwargs)
        print("Finished Calculating!")

        return result

    return wrapper


@calc
def add(x, y):
    return x + y


print(add(5, 5))

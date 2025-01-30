def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Invalid operand types.")
        return None

# This will produce the 'uncommon' error because the list element isn't a number
my_list = [10, 0, 'a']
result = function_with_uncommon_error(my_list[0], my_list[2])
print(result)
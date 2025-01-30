def function_with_uncommon_error(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a / b
            return result
        else:
            print("Error: Invalid operand types. Both operands must be numbers.")
            return None
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

my_list = [10, 0, 'a', 5, 2]
result1 = function_with_uncommon_error(my_list[0], my_list[3])
print(result1)
result2 = function_with_uncommon_error(my_list[0], my_list[2])
print(result2)
result3 = function_with_uncommon_error(my_list[3], my_list[4])
print(result3) 
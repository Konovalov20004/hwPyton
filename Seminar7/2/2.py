def print_operation_table(operation, num_rows, num_columns):
    for i in range(num_rows):
            b = list(map(lambda x: x * (i + 1), operation(num_columns)))
            print(b)

def operation(numnum_columns):
    a = [a + 1 for a in range(num_columns)]
    return a
    print(a)

num_columns = int(input())
num_rows = int(input())
print_operation_table(operation, num_rows, num_columns)
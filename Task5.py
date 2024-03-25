def read_numbers(file_name):
    with open(file_name, 'r') as f:
        numbers = [int(line.strip()) for line in f.readlines()]
    return numbers

def format_number(n):
    return "{:,.2f}".format(n)

numbers = read_numbers("input.txt")
total = sum(numbers)
print(format_number(total))
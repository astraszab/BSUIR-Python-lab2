import string


def numbers_from_file(fname):
    """Generator for numbers in a file
    """
    with open(fname, 'r') as file:
        number = ''
        while True:
            character = file.read(1)
            if character == '':
                if number:
                    yield int(number)
                break
            elif character in string.digits + '-':
                number += character
            elif character == ' ' or character == '\n':
                if number:
                    yield int(number)
                number = ''
            else:
                raise ValueError('Not a number in a file.')


def external_sort(input_file_name, block_size, output_file_name=None):
    """External sort of a file with integer numbers (separated by spaces).
    """
    if output_file_name is None:
        output_file_name = input_file_name


def main():
    ls = []
    for num in numbers_from_file('input_data/short_numbers.txt'):
        ls.append(num)
    print(ls)


if __name__ == '__main__':
    main()

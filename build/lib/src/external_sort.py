import string
from math import inf
from tempfile import TemporaryDirectory
from os.path import join


BLOCK_FILE_NAME = 'block_{}.dat'


class ExternalSort:
    """External sort of a file with integer numbers (separated by spaces).
    """
    def __init__(self, input_file_name, block_size, output_file_name):
        if block_size < 2:
            raise ValueError('Block size should be integer greater than one.')
        self.input_file_name = input_file_name
        self.block_size = block_size
        self.output_file_name = output_file_name
        self.tempdir = TemporaryDirectory()

    def run(self):
        """Run algorithm of external sort.
        """
        first_index, last_index = \
            self.get_initial_blocks()
        while last_index - first_index > self.block_size:
            first_index, last_index = \
                self.join_blocks(first_index, last_index)
        self.merge_blocks(self.output_file_name, first_index, last_index)

    def get_initial_blocks(self):
        """Create files with sorted blocks from fname.
        Return indeces of saved blocks.
        """
        block = []
        index = 0
        for number in self.numbers_from_file(self.input_file_name):
            block.append(number)
            if len(block) == self.block_size:
                block.sort()
                self.write_block(index, block)
                block = []
                index += 1
        else:
            if block:
                block.sort()
                self.write_block(index, block)
                index += 1
        return 0, index

    def numbers_from_file(self, fname):
        """Generator for numbers in a file.
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

    def write_block(self, index, block):
        """Write the block to a file with given index.
        """
        writer = self.numbers_to_file(
            join(self.tempdir.name, BLOCK_FILE_NAME.format(index)))
        next(writer)
        for number in block:
            writer.send(number)
        writer.close()

    def numbers_to_file(self, fname):
        """Coroutine that saves numbers to a file.
        """
        with open(fname, 'w') as output_file:
            empty = True
            while True:
                number = (yield)
                if not empty:
                    output_file.write(' ')
                output_file.write(str(number))
                empty = False

    def join_blocks(self, first_index, last_index):
        """Join blocks into bigger ones and return their indices.
        """
        index = last_index
        for i in range(first_index, last_index, self.block_size):
            if i + self.block_size <= last_index:
                self.merge_blocks(
                    join(self.tempdir.name, BLOCK_FILE_NAME.format(index)),
                    i, i+self.block_size)
            else:
                self.merge_blocks(
                    join(self.tempdir.name, BLOCK_FILE_NAME.format(index)),
                    i, last_index)
            index += 1
        return last_index, index

    def merge_blocks(self, fname, first_index, last_index):
        """Merge blocks into one and save to a file with given name.
        """
        number_generators = [self.numbers_from_file(
            join(self.tempdir.name, BLOCK_FILE_NAME.format(index)))
            for index in range(first_index, last_index)]
        numbers = [next(number_generator)
                   for number_generator in number_generators]
        writer = self.numbers_to_file(fname)
        next(writer)
        while True:
            minvalue, minindex = self.argmin(numbers)
            if minindex is None:
                break
            writer.send(minvalue)
            try:
                numbers[minindex] = next(number_generators[minindex])
            except StopIteration:
                numbers[minindex] = inf
        writer.close()

    def argmin(self, array):
        """Find minimum value and its index.
        """
        minvalue = inf
        minindex = None
        for i in range(len(array)):
            if array[i] < minvalue:
                minvalue = array[i]
                minindex = i
        return minvalue, minindex


def external_sort(input_file_name, block_size, output_file_name=None):
    """External sort of a file with integer numbers (separated by spaces).
    """
    if output_file_name is None:
        output_file_name = input_file_name
    sorter = ExternalSort(input_file_name, block_size, output_file_name)
    sorter.run()

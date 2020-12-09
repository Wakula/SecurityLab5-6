from key_manager import generate_random_key
import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception("File name is required.")
    file = sys.argv[1]
    with(open(file, 'w')) as f:
        f.write(generate_random_key())

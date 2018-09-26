import re
import sys


def get_address(port):
    f = open('./1.txt')

    while True:
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        if not data:
            return"NOT FOUND THE PORT"

        try:
            PORT = re.match(r'\S+', data).group()
        except Exception as e:
            print(e)
            continue

        if port == PORT:
            # pattern = r'address is (\w{4}\.\w{4}\.\w{4})'
            pattern = r'address is ((\d{1,3}\.){3}\d{1,3}/\d+|Unknown)'
            addr = re.search(pattern, data).group(1)
            return addr


if __name__ == '__main__':
    port = sys.argv[1]
    print(get_address(port))

    # parrent = r'\A\r\n\r\n\Z'
    # regex = re.compile(parrent)
    # s = regex.search(data).group()
    # print(s)

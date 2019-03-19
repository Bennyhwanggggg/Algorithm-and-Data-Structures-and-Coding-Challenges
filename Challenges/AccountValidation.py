def main(input):

    if len(input) != 8:
        return 'INVALID'

    try:
        num = int(input[0:6], 16)
        check = int(input[6:], 16)
    except:
        return 'INVALID'

    num = list(map(int, str(num)))
    return 'INVALID' if sum(num) != check else 'VALID'



if __name__ == '__main__':
    print(main('8BADF00D'))
    print(main('C0FFEE1C'))
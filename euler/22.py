def read_names(path):
    with open(path, 'r') as f:
        return f.read()
    
def parse_names(names):
    return [n[1:-1] for n in names.split(',')]

def name_score(name):
    total = 0
    for n in name:
        total += ord(n) - ord('A') + 1
    return total

def main():
    name_list = sorted(parse_names(read_names('names.txt')))
    total = 0
    for i, name in enumerate(name_list):
        total += name_score(name) * (i+1)
    print(total)

if __name__ == '__main__':
    main()
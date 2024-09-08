class HashTable:
    def __init__(self, size):
        self.size = size
        self.arr = [[] for _ in range(self.size)]

    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        return h % self.size

    def __getitem__(self, key):
        h = self.get_hash(key)
        existing_items = self.arr[h]
        for k, v in existing_items:
            if k == key:
                return v


    def __setitem__(self, key, value):
        h = self.get_hash(key)
        existing_items = self.arr[h]
        for idx, elm in enumerate(existing_items):
            if elm[0] == key:
                existing_items[idx][1] = value
                return

        existing_items.append((key, value))


    def __delitem__(self, key):
        h = self.get_hash(key)
        existing_items = self.arr[h]
        for idx, elm in enumerate(existing_items):
            if elm[0] == key:
                del existing_items[idx]

def load_csv_to_ht(filename):
    ht = HashTable(100)
    with open(filename, newline='') as csvfile:
        _ = csvfile.readline()
        line = csvfile.readline()
        while line:
            line = line.strip()
            line = line.split(',')
            ht[line[0]] = int(line[1])
            line = csvfile.readline()
    return ht

def avg_tmp_first_week(data):
    res = 0
    for i in range(1, 8):
        key = f'Jan {i}'
        res += data[key]
    return res / 7

def max_tmp_in_ten_days(data):
    tmps = []
    for i in range(1, 11):
        key = f'Jan {i}'
        tmps.append(data[key])
    return max(tmps)

def tmp_on_jan9_and_jan4(data):
    print(data['Jan 9'])
    print(data['Jan 4'])

data = load_csv_to_ht('nyc_weather.csv')
print(avg_tmp_first_week(data))
print(max_tmp_in_ten_days(data))
tmp_on_jan9_and_jan4(data)

def poem_repeated_words():
    ht = {}
    ignored_chars = ['!', ',', ';', ':']

    with open('poem.txt', 'r') as poems:
        line = poems.readline()
        while line:
            line = line.strip()
            line = line.split(' ')
            for word in line:
                if word in ignored_chars:
                    continue
                if ht.get(word) is not None:
                    ht[word] += 1
                else:
                    ht[word] = 1
            line = poems.readline()

    print(ht)

poem_repeated_words()

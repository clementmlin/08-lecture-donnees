'''
on import ce qu'il faut
'''
#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    '''
    on import ce qu'il faut
    '''
    data = []
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            line = line.strip()
            if ';' in line:
                parts = line.split(';')
            elif ',' in line:
                parts = line.split(',')
            else:
                parts = line.split()
            nums = []
            for p in parts:
                p = p.strip()
                nums.append(int(p))
            if nums:
                data.append(nums)
    return data

def get_list_k(data, k):
    '''
    on import ce qu'il faut
    '''
    l=data[k]
    return l

def get_first(l):
    '''
on import ce qu'il faut
'''
    return l[0]

def get_last(l):
    '''
on import ce qu'il faut
'''
    return l[-1]

def get_max(l):
    '''
on import ce qu'il faut
'''
    maximum=l[0]
    for i in l[1:]:
        if i>maximum:
            maximum=i
    return maximum

def get_min(l):
    '''
on import ce qu'il faut
'''
    minimum=l[0]
    for i in l[1:]:
        if i<minimum:
            minimum=i
    return minimum

def get_sum(l):
    '''
on import ce qu'il faut
'''
    s=0
    for i in range(len(l)):
        s+=l[i]
    return s


#### Fonction principale


def main():
    '''
on import ce qu'il faut
'''
    pass
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()

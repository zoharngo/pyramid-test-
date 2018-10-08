from collections import Counter

def paths_lookup_count(tri):
    steps = 2
    _slice = 1
    while len(tri) > 1:     
        row_0 = tri.pop()
        row_1 = tri.pop()
        temp = []
        
        for t in row_1:
            for j in range(0,steps):
                node1 = row_0[j] + t
                temp.append(node1)
            row_0 = row_0[_slice:]
        j = 0
        tri.append(temp)
        steps*=2
        _slice+=1 
    
    res = Counter(tri[0]).items() 

    return sorted(res, key = lambda x: x[1])
 
 
data ="""   55
            94 48
            95 30 96
            77 71 26 67
            97 13 76 38 45"""
 

        
if __name__ == '__main__':
    data = []
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]

    data = [map(int, row.split()) for row in lines]
    print paths_lookup_count(data)


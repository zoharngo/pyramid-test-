from collections import Counter

def paths_lookup_count(tri):
    size = len(tri)
 
    while len(tri) > 1: 
        
        if len(tri) == size :
            steps = 2
            _offset = 1
        else:
            _offset = steps
            steps *= 2
            
        temp = []
        row_0 = tri.pop()
        row_1 = tri.pop()

        if len(row_1) == 1 :
            steps = len(row_0)

        for t in row_1:
            for j in range(0,steps):
                node1 = row_0[j] + t
                temp.append(node1)
            row_0 = row_0[_offset:]
        j = 0
        tri.append(temp)

    res = Counter(tri[0]).items() 

    return sorted(res, key = lambda x: x[1])
 
 
data ="""55
        94 48
        95 30 96
        77 71 26 67
        97 13 76 38 45
        07 36 79 16 37 68
        48 07 09 18 70 26 06"""


        
if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]

    data = [map(int, row.split()) for row in lines]
    print paths_lookup_count(data)


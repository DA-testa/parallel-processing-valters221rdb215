# python3

def parallel_processing(n, m, data):
    output = []
    threadnr = [0] * n
    
    for i in range(m):
        nextthrd = 0
        for v in range(1, n):
            if threadnr[v] < threadnr[nextthrd]:
                nextthrd = v
        sakums = threadnr[nextthrd]
        beigas = sakums + data[i]
        
        threadnr[nextthrd] = beigas
        output.append((nextthrd, sakums))
    
    return output


def main():
 
    n, m = map(int, input().split())
    if not (1 <= n <= 10**5):
        raise ValueError("n should be between 1 and 10^5")
    if not (1 <= m <= 10**5):
        raise ValueError("m should be between 1 and 10^5")
    data = list(map(int, input().split()))
    if len(data) != m:
        raise ValueError("the length of data should be equal to m")
    for i in range(m):
        if not (0 <= data[i] <= 10**9):
            raise ValueError("each element in data should be between 0 and 10^9")

    result = parallel_processing(n, m, data)
    

    for pair in result:
        print(pair[0], pair[1])


if __name__ == "__main__":
    main()

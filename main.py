# python3

def parallel_processing(n, m, data):
    output = []
    threadnr = [0] *n
    
    for i in range(m):
        nextthrd = threadnr.index(min(threadnr))
        sakums = threadnr[nextthrd]
        beigas = sakums + data[i]
        
        threadnr[nextthrd] = beigas
        output.append((nextthrd, sakums))
    
    return output


def main():
 
    n, m = map(int, input().split())
    if not (1 <= n <= 10**5):
        raise ValueError("Error - n isnt between 1 and 10^5")
    if not (1 <= m <= 10**5):
        raise ValueError("Error: m isnt between 1 and 10^5")
    data = list(map(int, input().split()))
    if len(data) != m:
        raise ValueError("Error: the length of data isnt equal to m")
    for i in range(m):
        if not (0 <= data[i] <= 10**9):
            raise ValueError("Error: each element in data isnt between 0 and 10^9")

    result = parallel_processing(n, m, data)
    

    for pair in result:
        print(pair[0], pair[1])


if __name__ == "__main__":
    main()

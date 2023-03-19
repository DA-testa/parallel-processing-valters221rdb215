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
   
    data = list(map(int, input().split()))
   

    result = parallel_processing(n, m, data)
    

    for pair in result:
        print(pair[0], pair[1])


if __name__ == "__main__":
    main()

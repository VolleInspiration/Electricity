import numpy as np

def std_difference(data):
    avg = average(data)
    N = len(data)

    return (data-avg) / std_diviation(data, avg, N)

def std_diviation(data, avg, N):
    return np.sqrt( np.sum((data - avg) ** 2 / ( N - 1 )) ) 

def average(data):
    return np.sum(data) / len(data)

def main():
    data = [1,2,3,4,5,6,7,300]
    print("Average:", average(data) )
    print("Diviation:", std_diviation(data, average(data), len(data)) )
    print("Difference:", std_difference(data) )

if __name__ == "__main__":
    main()
def sum_if(data, condition):
    return sum([i for i in data if condition(i)])

if __name__ == '__main__':
    
    data = list(range(20))
    result = sum_if(data, lambda x: x > 10)

    print(result)

def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a = 0
    for i in data:
        if  i in ('123456790'):
            a+=int(i)

    return a 

f = open('data/data03.txt')
data = f.read() 
f.close()

print(main(data))
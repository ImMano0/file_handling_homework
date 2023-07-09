def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a = []
    for i in data:
        if i.isdigit():
            a.append(i)

    return a 

f = open('data/data03.txt')
data = f.read() 
f.close()

print(main(data))
#Rread file and convert to list
def read_file(filename: str) -> list[int]:
    """
    Reads a file and returns a list of integers.

    Args:
        filename (str): The name of the file to read.
    Returns:
        data (list): A list of integers from the file.
    """
    # Open the file
    # Read the file
    f=open("data.txt",mode='r')
    s=f.readline()
    return   list(map(lambda x:int(x),filter(lambda x: x.isdigit(),s)))  #list(filter(lambda x: x.isdigit(),s))
print(read_file('data.txt'))

#Print list from file

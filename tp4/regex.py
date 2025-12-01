def readTheBook(fileName : str) -> str:
    """ Read and return the file content 
        Arguments:
            fileName : str : the name of the file to read
        Returns:
            content : str : the content of the file
    """
    try:
        with open(fileName,'r') as file :
            content = file.read();
            print(content)
            return content
    except :
        print("file not found")
        return ""

if __name__ == "__main__":
    readTheBook('tp4/the-prince.txt')

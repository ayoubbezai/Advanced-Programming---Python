from typing import List
import re
def readTheBook(fileName : str) -> str:
    """ 
    Read and return the file content 
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
    
    
def extractYears(content : str) -> List[str] :
    """
    Extract years from the book 
        Arguments : 
            content : str : the text after read it int string
        Return :
            years : List[str] : return all the years as  list of strings 
        Exemple 
            years = extractYears(content)
            print(years)
            //output
            [2012,1039]
    """
    pattren = r"\d{4}"
    years = re.findall(pattren,content)
    return years
    



if __name__ == "__main__":
    content = readTheBook('tp4/the-prince.txt')
    years = extractYears(content)
    print(years)

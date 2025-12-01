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

def extractCapitilized(content : str) -> List[str] :
    """
    Extract or the word that are capitalized (firs letter is uppercase)
        Arguments : 
            content : str : the text after read it int string
        Return :
            capitilized : List[str] : return all the capitilized words as  list of strings 
        Exemple 
            capitilized = extractCapitilized(content)
            print(capitilized)
            //output
            ['Gutenberg', 'Literary', 'Archive', 'Foundation']
    """
    pattren = r"\b[A-Z][a-z]+\b"
    capitilized = re.findall(pattren,content);
    return capitilized

def extractFullNames(content : str) -> List[str] :
    """
    Extract or the full names words that are capitalized (first letter is uppercase twice)
        Arguments : 
            content : str : the text after read it int string
        Return :
            names : List[str] : return all the names words as  list of strings 
        Exemple 
            names = extractFullNames(content)
            print(names)
            //output
            ['Gutenberg', 'Literary', 'Archive', 'Foundation']
    """
    pattren = r"\b[A-Z][a-z]\b\s+\b[A-Z][a-z]+\b"
    names = re.findall(pattren,content);
    return names

def extractDilogs(content : str) -> List[str] :
    """
    Extract all dialogs senteces which are insde quoates 
        Arguments : 
            content : str : the text after read it int string
        Return :
            dilogs : List[str] : return all the dilogs  as  list of strings 
        Exemple 
            dilogs = extractDilogs(content)
            print(dilogs)
            //output
            [ 'Of Mixed', 'Of New', 'Of New', 'Of Ecclesiastical', 'Of Auxiliary', 'Of Liberality', 'Of Cruelty', 'If France', 'As Pertinax']
    """
    pattern = r'["\'`].+?["\'`]'
    dilogs = re.findall(pattern,content);
    return dilogs

if __name__ == "__main__":
    content = readTheBook('tp4/the-prince.txt')
    years = extractYears(content)
    print(years)
    capitilized = extractCapitilized(content);
    print(capitilized)
    names = extractFullNames(content);
    print(names)
    dilogs = extractDilogs(content);
    print(dilogs)

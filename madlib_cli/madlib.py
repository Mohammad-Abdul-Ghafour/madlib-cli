import re

def read_template(path):
    """
    A function that read a file
    and return the content of the file
    and takes the path of file as input

    input : 
        path_of_file/name_of_file.extention
    """
    with open(path , "r" ) as f:
        content = f.read()
        return content

def parse_template(content):
    """
    A function takes in a string as input
    and return an array

    input :
        "any {string} with {}"

    output :
        [the string,tuple(string)]
    """
    file = content
    arrayOfWords = re.findall('[^{]+(?=})',file)
    tupleOfWords = tuple(arrayOfWords)
    stringOfText = re.sub('[^{]+(?=})',"",file)
    return stringOfText , tupleOfWords




def merge(stringOfText,tupleOfWords):
    """
    A function takes in a string and tuple
    and return new file with the modified string
    from the user input

    input :
        1. a sring
        2. a tuple

    output :
        a new file
    """

    try:
        new_file = stringOfText
        for i,val in enumerate(tupleOfWords):
            new_file = new_file.replace("{}",tupleOfWords[i],1)
        with open("madlib_cli/assets/text_test_copy.txt" , "w") as f:
            f.write(new_file)
        return read_template("madlib_cli/assets/text_test_copy.txt")
    except FileNotFoundError:
        return "error"

if __name__ == "__main__":
    print("Welcome to guessing game ..!")
    content = read_template("madlib_cli/assets/text.txt")
    tupleOfWords = parse_template(content)[1]
    stringOfText = parse_template(content)[0]
    print(tupleOfWords)
    array = [*tupleOfWords]

    for indx,item in enumerate(array):
        userInput= input( f"Please enter {item} : > ")
        array[indx] = userInput

    tupleArray = tuple(array)
    print(merge(stringOfText,tupleArray))

    




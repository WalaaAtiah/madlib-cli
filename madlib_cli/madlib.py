from logging import exception
import re

#test function
def read_template(x):
    try:
        file = open(x)
        read = file.read()
        file.close()
        # print(read)
        return read
    except FileNotFoundError as err:
        raise FileNotFoundError


def parse_template(x):
    read=x
    pattern = r"{\w{0,}}"
    parts =re.findall(pattern, read)
    # print(parts)

    for i, char in enumerate(parts):
        parts[i] = re.sub("{", "", char)
        parts[i] = re.sub("}", "", parts[i])
        read = re.sub(parts[i], "", read)

    print(tuple(parts))
    print(read)
    return read,tuple(parts)
    


def merge(x,y):
    
    return x.format(*y)


# read_template("assets/dark_and_stormy_night_template.txt")
# parse_template("It was a {Adjective} and {Adjective} {Noun}.")
# merge("It was a {} and {} {}.", ("dark", "stormy", "night"))


#demo lap 

def welcam():
    welcam_text ="""
    #######################################################
    ###                                                 ###
    ###             Welcome to Madlibs                  ###
    ###           Mad Libs is a word game               ###
    ###      You can create your own funny story        ###
    ###                                                 ###
    ### By filling in the blanks with adjectives,nouns  ###
    ### colors, numbers and more...                     ### 
    ###                                                 ###
    ### These words are inserted into the blanks        ###
    ### and the story is complete.                      ###
    ###                                                 ###
    ### There are no winners and no losers, just laughs.###
    ###      Just add your words and press enter        ###
    ###                                                 ###
    #######################################################
    """
    print(welcam_text)


def parse_template_story(x):
    # Number_1-50 A_Girl's_Name
    read=x
    pattern = r"{\w{0,}}|{\w{0,}\d-\d{0,3}}|{\w{0,}'\w{0,}}"
    parts =re.findall(pattern, read)
    # print(parts)
    # print(len(parts))

    for i, char in enumerate(parts):
        parts[i] = re.sub("{", "", char)
        parts[i] = re.sub("}", "", parts[i])
        read = re.sub(parts[i], "", read)

    return read,tuple(parts)
    
def add_words(x):
    # print(x)
    words=[]
    for i in x:
        y=input(i+" ===> ")
        words.append(y)
    return tuple(words)

def write_story(x):
    with open("assets/response.txt","w") as file:
        file.write(x)
    





if __name__=="__main__":
    # a=('Clever',"genius","Walaa","ate","Mazen","bags","cute","angry","dogs","elephant","ante","Bayan","smoll","pins","big","water","45","yahya","488","books","888")
    welcam()
    read=read_template("assets/story.txt")

    # print (read)
    stripped,parts=parse_template_story(read)
    # print(parts)
    # print(stripped)
    words=add_words(parts)
    # print(words)
    story=merge(stripped,words)
    write_story(story)
    print(story)
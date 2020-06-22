from leveldata import *


def returnstorycount():
    with open('src/save.txt','r') as file:
        for line in file:
            storycount = int(line.strip('[]'))
            return storycount


def save(storycount):
    with open('src/save.txt', 'w') as file:
        file.write(str(storycount))


def getlevel(storycount):
    #array = leveldata[storycount]
    #return array

#hier kommt die ganzen komischen Storydinger :(
    if storycount == 1:
        array = leveldata1
        return array
    if storycount == 2:
        array = leveldata2
        return array
    if storycount == 3:
        array = leveldata3
        return array
    if storycount == 4:
        array = leveldata4
        return array
    if storycount == 5:
        array = leveldata5
        return array
    if storycount == 6:
        array = leveldata6
        return array
    if storycount == 7:
        array = leveldata7
        return array
    if storycount == 8:
        array = leveldata8
        return array
    if storycount == 9:
        array = leveldata9
        return array
    if storycount == 10:
        array = leveldata10
        return array
    if storycount == 11:
        array = leveldata11
        return array

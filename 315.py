import sys
templist = []
with open("test.txt",encoding='UTF-8') as f:
    lines=f.readlines()
    for i in lines:
        templist.append(i.strip("\n"))
html = []
# image = []
# sound = []
# video = []
# formatlist = []
# dynamic = []
# other = []
def findtype(string):
    htmltype = ["html","htm", "shtml","map"]
    # imagetype = ["gif", "jpeg", "jpg", "xbm", "bmp", "rgb", "xpm"]
    # soundtype = ["au", "snd", "wav", "mid", "midi", "lha", "aif", "aif"]
    # videotype = ["mov", "movie", "avi", "qt", "mpeg", "mpg"]
    # formattype = ["ps", "eps", "doc", "dvi", "txt"]
    # dynamictype = ["cgi", "pl", "cgi-bin"]
    for i in htmltype:
        i = "." + i
        if (string.find(i) != -1):
            return "htmltype"
    # for i in imagetype:
    #     if (string.find(i) != -1):
    #         return "imagetype"
    # for i in soundtype:
    #     if (string.find(i) != -1):
    #         return "soundtype"
    # for i in videotype:
    #     if (string.find(i) != -1):
    #         return "videotype"
    # for i in formattype:
    #     if (string.find(i) != -1):
    #         return "formattype"
    # for i in dynamictype:
    #     if (string.find(i) != -1):
    #         return "dynamictype"
    # return "else"
htmlvalue = []
for x in templist:
    if(findtype(x) == "htmltype"):
        if (len(x) >= 43):
            htmlindex = x.rfind('"')
            htmlvalue.append(x[htmlindex+2:].split())
    # elif(findtype(x) == "imagetype"):
    #     image.append(x)
    # elif(findtype(x) == "soundtype"):
    #     sound.append(x)
    # elif(findtype(x) == "videotype"):
    #     video.append(x)
    # elif(findtype(x) == "formattype"):
    #     formatlist.append(x)
    # elif(findtype(x) == "dynamictype"):
    #     dynamic.append(x)
    # else:
    #     other.append(x)
htmlnum = 0
for x in htmlvalue:
    if(x[1] != "-"):
        htmlnum += int(x[1])
print(htmlnum)

 



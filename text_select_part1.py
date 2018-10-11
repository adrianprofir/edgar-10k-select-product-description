import os
import re

text = """ ITEM 1 First match

ITEM 2.


 2321ITEMS 1.2112
    AND 2.  
BUSINESS AND PROPERTIES

ITEM 1A.
ITEM 1 Second match

ITEM 2.

ITEM 1 Third match

ITEM 2. """


# path from where to get the txt files
saved_path = "E:/Thesis stuff/10k abbot/python/10ktxt/"

#path to where to save the txt
selected_path = "E:/Thesis stuff/10k abbot/python/Multiple 10k/10k_select/"

#path for 10ks with ITEM1
item1_path = "E:/Thesis stuff/10k abbot/python/10kcap/"

list_txt = os.listdir(selected_path)

def allindices(text, sub, listindex=[]):
    i = text.find(sub)
    while i >= 0:
        listindex.append(i)
        i = text.find(sub, i+1)
    return listindex


item1_begin = 'ITEM 1.'
item1a = 'ITEM 1A.'
item2_begin = 'ITEM 2.'
item3_begin = 'ITEM 3.'

counter1 = 0
counter2 = 0
counter3 = 0

for text in list_txt:
    file_path = selected_path + text #the path must be united with each item from the list
    file = open(file_path, "r+", encoding="utf-8") #opens the txt document and encodes it with utf-8
    file_read = file.read() #reads the opened file
    begin = allindices(file_read, item1_begin, listindex=[])
    end = allindices(file_read, item2_begin, listindex=[])
    # try to see if the index returns errors
    # if the index returns errors, print to console, count and continue the code further
    try:
        save_txt = file_read[begin[0]:end[0]].strip()
    except IndexError:
        print("Error in 1 " + text)
        counter1 += 1
        #print("error in 1 " + text)
        continue

    # if the above try function returns no errors, then continue to this:
    if len(save_txt) >= 2000:
        saved_file = open(item1_path + text, "w+", encoding="utf-8")  # save the file with the complete names
        saved_file.write(save_txt)  # write to the new text files the selected text
        saved_file.close()  # close the file
        #print("1' works for " + text)
    else:

        try:
            save_txt = file_read[begin[1]:end[1]].strip()
        except IndexError:
            print("Error in 2 " + text)
            counter2 += 1
            #print("error in 2 " + text)
            continue
        if len(save_txt) >= 2000:
            saved_file = open(item1_path + text, "w+", encoding="utf-8")  # save the file with the complete names
            saved_file.write(save_txt)  # write to the new text files the selected text
            saved_file.close()  # close the file
            #print("2' works for " + text)
        else:
            print("not working " + text)
    file.close()

"""
begin = allindices(text, item1_begin, listindex=[])
end = allindices(text, item2_begin, listindex=[])
int_begin = begin[1]
int_end = end[1]

text3 = text[int_begin:int_end].strip()
print(text3)


for item1 in item1_begin:
    begin = text.find(item1)
    print(begin)

for item2 in item2_begin:
    end =  text.find(item2)
    print(end)

text2 = text[begin:end].strip()
print(text2)

# look for instances of ITEM 1 in the text provided
for item1 in item1_begin:
    begin = text.find(item1)
    print(begin)
    if begin != -1:
        break

# the beginning of the parsing is found
if begin != -1:  # Begin found
    for item1A in item1_ends:
        end = text.find(item1A, begin + 1)
        print(end)
        if end != -1:
            break

    if end == -1:  # ITEM 1A does not exist
        for item2 in item2_begin:
            end = text.find(item2, begin + 1)
            print(end)
            if end != -1:
                break
    text2 = text[begin:end].strip()
    print(text2)"""

"""
for text in list_txt:
    file_path = selected_path + text #the path must be united with each item from the list
    file = open(file_path, "r+", encoding="utf-8") #opens the txt document and encodes it with utf-8
    file_read = file.read() #reads the opened file
    is_item1_here = file_read.find("ITEM 1A")
    whole_list = []
    if is_item1_here != -1:
        whole_list.append(text)
        for each in whole_list:
            i = 1
            while i == 1:
                text1a = open("item1a.txt", "a", encoding="utf-8")
                text1a.write("\n" + text)
                text1a.close()
                i += 1
            break

only_item1 = open("item1a.txt", "r+", encoding="utf-8")
read_only_item1 =  only_item1.read()
print(read_only_item1)
final_list = [item for item in read_only_item1 if item not in list_txt]
only_item1.close()
"""
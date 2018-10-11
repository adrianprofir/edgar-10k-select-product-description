import os

# path from where to get the txt files
saved_path = "E:/Thesis stuff/10k abbot/python/10ktxt/"

#path to where to save the txt
selected_path = "E:/Thesis stuff/10k abbot/python/Multiple 10k/10k_select/"

#path for 10ks with ITEM1
item1_path = "E:/Thesis stuff/10k abbot/python/10kcap/"

list_txt = os.listdir(selected_path)

saved_txt = os.listdir(item1_path)

def allindices(text, sub, listindex=[]):
    i = text.find(sub)
    while i >= 0:
        listindex.append(i)
        i = text.find(sub, i+1)
    return listindex


item1_begin = 'ITEM XX.'
item3_begin = 'ITEM 3.'

for text in list_txt:
        # the path must be united with each item from the list
        file_path = selected_path + text

        # opens the txt document and encodes it with utf-8
        file = open(file_path, "r+", encoding="utf-8")

        # reads the opened file
        file_read = file.read()

        # point to the beginning and the end of text we want to select
        begin = allindices(file_read, item1_begin, listindex=[])
        end = allindices(file_read, item3_begin, listindex=[])
        try:
            save_txt = file_read[begin[0]:end[0]].strip()
        except IndexError:
            continue
        if len(save_txt) >= 2000:
            saved_file = open(item1_path + text, "w+", encoding="utf-8")  # save the file with the complete names
            saved_file.write(save_txt)  # write to the new text files the selected text
            saved_file.close()  # close the file
            print("1 works for " + text)
        else:
            try:
                save_txt = file_read[begin[1]:end[1]].strip()
            except IndexError:
                continue
            if len(save_txt) >= 2000:
                saved_file = open(item1_path + text, "w+", encoding="utf-8")  # save the file with the complete names
                saved_file.write(save_txt)  # write to the new text files the selected text
                saved_file.close()  # close the file
                print("2 works for " + text)
            else:
                print("not here " + text)
        file.close()

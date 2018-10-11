import os
import re
import unicodedata

from bs4 import BeautifulSoup

# path from where to get the txt files E:\Thesis stuff\10k_files\10k
tenk_path = "E:/Thesis stuff/10k_files/10k/"

# path to where to save the parsed html code in the txt files
save_path = "E:/Thesis stuff/10k_files/10ktxt/"

# get a list of all the items in that specific folder and put it in a variable
arr = os.listdir(tenk_path)

def _process_text(text):
    """
        Preprocess Text
    """
    text = unicodedata.normalize("NFKD", text)  # Normalize
    text = '\n'.join(text.splitlines())  # Let python take care of unicode break lines

    # Convert to upper
    text = text.upper()  # Convert to upper

    # Take care of breaklines & whitespaces combinations due to beautifulsoup parsing
    text = re.sub(r'[ ]+\n', '\n', text)
    text = re.sub(r'\n[ ]+', '\n', text)
    text = re.sub(r'\n+', '\n', text)

    # To find MDA section, reformat item headers
    text = text.replace('\n.\n', '.\n')  # Move Period to beginning

    text = text.replace('\nI\nTEM', '\nITEM')
    text = text.replace('\nITEM\n', '\nITEM ')
    text = text.replace('\nITEM  ', '\nITEM ')

    text = text.replace(':\n', '.\n')

    # Math symbols for clearer looks
    text = text.replace('$\n', '$')
    text = text.replace('\n%', '%')

    # Reformat
    text = text.replace('\n', '\n\n')  # Reformat by additional breakline

    soup = BeautifulSoup(inside_txt_content, "html.parser")
    text = soup.get_text("\n")

    text = text.replace("ITEM ONE", "ITEM 1.")
    text = text.replace("ITEM TWO", "ITEM 2.")

    # make the ITEM 1 and ITEM 2 standard, meaning with a "."
    text = re.sub("(ITEM\s1\W)", "ITEM 1.", text)
    text = re.sub("(ITEM\s2\W)", "ITEM 2.", text)

    # some 10k-s group together ITEM 1 and 2, therefore: change the keyword to something different
    text = re.sub("(ITEM\s3\W)", "ITEM 3.", text)
    text = re.sub("(ITEMS\s1\W)", "ITEM XX.", text)

    return text

#loop that does the opening, parsing and saving
for name in arr:
    inside_txt = open(tenk_path + name ,"r+", encoding="utf-8")                    #open each txt file found in the folder tenk_path
    inside_txt_content = inside_txt.read()
    inside_cleaned = _process_text(inside_txt_content)
    inside_txt.close()                                               #close the initial 10k after it has been opened and read and parsed
    completeName = os.path.join(save_path + name)                #use the save path plus the name of the 10k to save to the new location
    print(name)                                                      #print to console the current file it is working one
    saved_file = open(completeName + ".txt","w+", encoding="utf-8")   #save the file with the complete namas
    saved_file.write(inside_cleaned)                     #write to the new text files the parsed html code
    saved_file.close()                              #close the file
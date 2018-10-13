import os
import re
import unicodedata

from bs4 import BeautifulSoup

# path from where to get the txt files D:\10Ks\2 download
tenk_path = "D:/10Ks/2 download/"

# path to where to save the parsed html code in the txt files
save_path = "D:/10Ks/2_download/"

# get a list of all the items in that specific folder and put it in a variable
list_10k = os.listdir(tenk_path)

def _process_text(text):
    """
        Pre-process Text
    """
    text = unicodedata.normalize("NFKD", text)  # Normalize
    text = '\n'.join(text.splitlines())  # Let python take care of unicode break lines

    # Take care of breaklines & whitespaces combinations due to beautifulsoup parsing
    text = re.sub(r'[ ]+\n', '\n', text)
    text = re.sub(r'\n[ ]+', '\n', text)
    text = re.sub(r'\n+', '\n', text)

    # Reformat item headers
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

    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text("\n")

    # Convert to upper
    text = text.upper()  # Convert to upper

    text = re.sub(r'(\.)', '', text)

    # remove empty lines
    text = re.sub(r'(\n\s)', '', text)

    # make the ITEM 1A end with a dot:
    text = text.replace("ITEM 1A", " ITEM 1A. ")
    text = re.sub(r'(ITEM\s1A)', 'ITEM 1A. ', text)

    # Some 10ks number their items with "ONE", "TWO" etc, replace that so we get consistency
    text = text.replace("ITEM ONE", " ITEM 1. ")
    text = text.replace("ITEM TWO", " ITEM 2. ")

    # Some 10ks number the items with roman numbers
    text = text.replace("ITEM I", "ITEM 1.")
    text = text.replace("ITEM II", "ITEM 2.")
    text = text.replace("ITEM III", "ITEM 3.")

    # make the ITEM 1 and ITEM 2 standard, meaning with a "."
    text = re.sub("(ITEM\s1\W)", " ITEM 1. ", text)
    text = re.sub("(ITEM\s2\W)", " ITEM 2. ", text)

    # some 10ks group together ITEM 1 and 2, therefore: change the keyword to something different
    text = re.sub("(ITEM\s3\W)", " ITEM 3. ", text)
    text = re.sub("(ITEMS\s1\W)", " ITEM XX. ", text)

    return text


# loop that does the opening, parsing and saving
for name in list_10k:

    # open each txt file found in the folder tenk_path
    inside_txt = open(tenk_path + name ,"r+", encoding="utf-8")
    inside_txt_content = inside_txt.read()

    # In case the files are too big and python has a memory error: continue and print to console for which one
    try:
        inside_cleaned = _process_text(inside_txt_content)
    except MemoryError:
        error_log = open("error_log.txt", "a", encoding='utf-8')
        error_log.write("\n" + name)
        error_log.close()
        print("ERROR IN " + name)
        continue
    inside_txt.close()

    # use the save path plus the name of the 10k to save to the new location
    completeName = os.path.join(save_path + name)
    print(name)
    saved_file = open(completeName + ".txt","w+", encoding="utf-8")
    saved_file.write(inside_cleaned)
    saved_file.close()

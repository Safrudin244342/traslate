import os
from textblob import TextBlob
import time

# function built in
def translate_file(file):
    print(file)

# membaca semua doc yang ada di folder doc
list_file = os.listdir("doc")

for file in list_file:
    file_read = open("doc/" + file, 'r')
    text_save = []
    for baris in file_read:
        text_asal = TextBlob(baris)
        text_translate = text_asal.translate(to="en")
        text_save.append(str(text_translate) + "\n")

    file_write = open("doc_translate/" + file, 'w')
    file_write.writelines(text_save)

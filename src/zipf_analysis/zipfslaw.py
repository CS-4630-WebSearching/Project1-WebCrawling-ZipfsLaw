import os
import re
import collections
import csv

TOTAL_WORDS = 0


def order_text(directory):
    """
    :return: text without punctuation or numbers
    """

    text = ""

    for i in os.listdir(directory):
        text = text + " "
        if i.endswith(".txt"):
            f = open(os.path.join(directory, i), 'r', encoding="utf-8")
            text = text + f.read()
            f.close()

    clean = re.compile('<.*?>')
    remove = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789«»–·"

    text = re.sub(clean, '', text)
    tr = str.maketrans("", "", remove)
    text = text.lower()

    return text.translate(tr)


def top_word_frequencies(text, top):
    """
    :param text: refined text from web crawl free from punctuation and numbers
    :param top: number of top word frequencies to return
    :return: a list of tuples with the most frequent words and their frequencies in descending order
    """

    words = text.split()
    global TOTAL_WORDS
    TOTAL_WORDS = len(words)
    word_frequencies = collections.Counter(words)
    top_words = word_frequencies.most_common(top)

    return top_words


def generate_zipf_data(frequencies):
    """
    :param frequencies: ordered list of tuples containing the word and frequency
    :return:
    """
    zipf_data = []

    for i in frequencies:
        if isinstance(i[0], str):
            probability = i[1] / TOTAL_WORDS

            zipf_data.append({"word": i[0],
                              "frequency": i[1],
                              "probability of occurrence": probability})
    
    return zipf_data


def print_data(zip_file, file_name):
    with open(file_name, "w", encoding="utf-8") as outfile:
        for entries in zip_file:
            for key in entries.keys():
                outfile.write("%s," % (entries[key]))
            outfile.write("\n")


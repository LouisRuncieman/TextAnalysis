import nltk
import os
from pandasgui import show

from text_analysis.summary_of_text_analysers import SummaryOfTextAnalysers
from text_analysis.text_analyser import TextAnalyser


def create_text_analysers_from_directory(directory):
    valid_file_formats = ('.txt')
    tokens_to_remmove = get_tokens_to_remove()

    text_analysers = {}
    for filename in os.listdir(directory):
        if filename.endswith(valid_file_formats):
            text_analysers[filename] = create_text_analyser_from_file(directory + filename, tokens_to_remmove)
    return text_analysers


def get_tokens_to_remove():
    stopwords = nltk.corpus.stopwords.words("english")
    tokens_to_remove = stopwords + get_uninteresting_words("uninteresting_words.csv")
    return tokens_to_remove


def get_uninteresting_words(filename):
    raw = file_import(filename)
    temp = raw.split(",")
    return temp


def file_import(filename):
    f = open(filename, 'r')
    raw = f.read()
    raw = raw.rstrip('\n')
    return raw


def create_text_analyser_from_file(filename, tokens_to_remove):

    text_body = file_import(filename)
    text_analyser = TextAnalyser(text_body)
    text_analyser.expand_contractions_in_tokens()
    text_analyser.normalise_tokens()
    # text_analyser.porter_stem_tokens()
    # text_analyser.lemmatize_tokens()
    text_analyser.remove_tokens(tokens_to_remove)

    return text_analyser


if __name__ == '__main__':

    relative_directory_path = "test_docs/"
    text_analysers = create_text_analysers_from_directory(relative_directory_path)
    summary_of_text_analysers = SummaryOfTextAnalysers(text_analysers)
    df = summary_of_text_analysers.create_dataframe()
    show(df[df["Total occurrences"] >= 20])

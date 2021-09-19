import nltk
import os
from pandasgui import show

from text_analysis.summarise_text_analysers import SummaryOfTextAnalysers
from text_analysis.text_analyser import TextAnalyser


def create_text_analysers_from_directory(directory):
    valid_file_formats = ('.txt')

    text_analysers = {}
    for filename in os.listdir(directory):
        if filename.endswith(valid_file_formats):
            text_analysers[filename] = create_text_analyser_from_file(directory + filename)
    return text_analysers


def create_text_analyser_from_file(filename):
    stopwords = nltk.corpus.stopwords.words("english")
    tokens_to_remove = stopwords + ["let", "us", "one", "also", "need", "must", "many", "enough"]

    text_body = file_import(filename)
    text_analyser = TextAnalyser(text_body)
    text_analyser.expand_contractions_in_tokens()
    text_analyser.normalise_tokens()
    # interesting_word_analyser.porter_stem_tokens()
    # interesting_word_analyser.lemmatize_tokens()
    text_analyser.remove_tokens(tokens_to_remove)

    return text_analyser


def file_import(filename):
    f = open(filename, 'r')
    raw = f.read()
    return raw


if __name__ == '__main__':

    relative_directory_path = "test_docs/"
    text_analysers = create_text_analysers_from_directory(relative_directory_path)
    summary_of_text_analysers = SummaryOfTextAnalysers(text_analysers)
    df = summary_of_text_analysers.create_dataframe()
    show(df[df["Total occurrences"] > 20])

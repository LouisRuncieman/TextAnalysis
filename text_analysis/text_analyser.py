import nltk
import contractions
import re


class TextAnalyser:

    def __init__(self, text_body):
        self.text_body = text_body
        self.word_tokens = []
        self.sentence_tokens = []
        self._text_body_to_tokens()
        self._text_body_to_sentence_tokens()

    def _text_body_to_tokens(self):
        self.word_tokens = nltk.word_tokenize(self.text_body)

    def _text_body_to_sentence_tokens(self):
        self.sentence_tokens = nltk.sent_tokenize(self.text_body)

    def expand_contractions_in_tokens(self):
        self.word_tokens = [contractions.fix(word) for word in self.word_tokens]

    def normalise_tokens(self):
        self.word_tokens = [word.lower() for word in self.word_tokens if word.isalpha()]

    def porter_stem_tokens(self):
        porter_stemmer = nltk.PorterStemmer()
        self.word_tokens = [porter_stemmer.stem(word) for word in self.word_tokens]

    def lemmatize_tokens(self):
        lemmatizer = nltk.WordNetLemmatizer()
        self.word_tokens = [lemmatizer.lemmatize(word) for word in self.word_tokens]

    def remove_tokens(self, tokens_to_remove):
        self.word_tokens = [word for word in self.word_tokens if word not in tokens_to_remove]

    def get_freq_dist(self):
        freq_dist = nltk.FreqDist(self.word_tokens)
        return freq_dist

    def get_sentence_tokens_by_word(self, word):
        sentence_tokens = []
        if word in self.word_tokens:
            for sentence_token in self.sentence_tokens:
                if re.search(r'\b' + word + r'\b', sentence_token, flags=re.IGNORECASE):
                    sentence_tokens.append(sentence_token)
        return sentence_tokens

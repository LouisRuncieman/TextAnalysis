import pandas as pd


class SummaryOfTextAnalysers:

    def __init__(self, text_analysers):
        self.text_analysers = text_analysers
        self.all_word_tokens = set()
        self.summary = {}
        self._get_all_word_tokens()
        self._get_summary()

    def _get_all_word_tokens(self):
        all_word_tokens = set()
        for raw_analyser in self.text_analysers.values():
            all_word_tokens.update(raw_analyser.word_tokens)
        self.all_word_tokens = all_word_tokens

    def _get_summary(self):
        summary = {}
        for word in self.all_word_tokens:
            summary[word] = {}
            for text_analyser in self.text_analysers:
                fd = self.text_analysers[text_analyser]
                summary[word].update({text_analyser: fd.get_sentence_tokens_by_word(word)})
        self.summary = summary

    def create_dataframe(self):
        TOTAL_OCCURRENCES = "Total occurrences"
        OCCURRENCES_IN = "Occurrences in "
        EXTRACTS_IN = "Extracts in "
        WORD = 'Word'

        occurrences = {}
        extracts = {}
        text_analyser_names = sorted(list(self.text_analysers.keys()))

        for text_analyser in text_analyser_names:
            occurrences[OCCURRENCES_IN + text_analyser] = []
            extracts[EXTRACTS_IN + text_analyser] = []
            for word in self.all_word_tokens:
                count = len(self.summary[word][text_analyser])
                occurrences[OCCURRENCES_IN + text_analyser].append(count)
                extracts[EXTRACTS_IN + text_analyser].append(self.summary[word][text_analyser])

        d = {WORD: list(self.all_word_tokens)}
        d.update(occurrences)
        d.update(extracts)
        df = pd.DataFrame(data=d)

        total_occurrences = df[[OCCURRENCES_IN + name for name in text_analyser_names]].sum(axis=1)
        df.insert(loc=1, column=TOTAL_OCCURRENCES, value=total_occurrences)
        df.sort_values(by=TOTAL_OCCURRENCES, ascending=False, inplace=True)
        return df

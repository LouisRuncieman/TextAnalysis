# Text Analysis

Given a plain text file (or a directory of files), produce the following summary: 
* Interesting\* words used (and occurrences);
* the files in which they appear (and occurrences);
* The sentences in which they are used.

\*Interesting words are defined as any word other than stopwords (defined by the NLTK Corpora Stopwords list) or any words appearing in `uninteresting_words.csv` which can updated over time.

## `TextAnalyser`

This class takes a raw text body (as a string) and generates word tokens and sentence tokens upon initilisation. Once created, sentence tokens remain unchanged. Word tokens, however, have a number of methods to manipulate their content inplace. 

#### `expand_contractions_in_tokens`

Using the `contractions` package, expand contractions in every word token. For example, "let's" is expanded to two tokens, "let" and "us".

#### `normalise_tokens`

Remove non-alphabetic characters from word tokens, such as punctionation. Make all word tokens lower case.

#### `porter_stem_tokens`

Convert word tokens into their stem (root). This is done by removing affixes from the word token (such as de-, bi-, ,-es, -ing, -s). Done via the Porter Algorithm (other algorithms avaiable). 
Note that stemming a word or sentence may result in words that are not actual words (for example universe is stemmed to univers).

#### `lemmatize_tokens`

Cnvert word tokens into their lemma (base). Lemmatization considers the context and converts the word to its meaningful base form, avoiding spelling mistakens seen in stemming. For example, "run", "ran", "running" all have lemma "run". "Better", "great" and "good" have lemma "good".

#### `remove_tokens`

Remove word tokens given a list of word tokens to remove.

#### `get_freq_dist`

Generate a frequency distribution of word tokens in the raw text body.

#### `get_sentence_tokens_by_word`

Given a word to search for, return a list of sentence tokens in which it was used.

## `SummaryOfTextAnalysers`

Given a dictionary with `filename` keys and `TextAnalyser` values, create a condensed text analysis summary upon initialisation. 
The summary is indexed by interesting word and provides all sentence tokens in which the interesting word is used for each `filename`. E.g.:

```
{
  "power": {
    "doc1.txt": ["We the people have the power.", "Social media is power.", ...],
    "doc2.txt": ["Electricity is the primary form of power in the modern world.", "The power produced by batteries was not sufficient."],
    "doc3.txt": [],
    ...
  },
  "think": { ... },
  ....
}
```
This summary contains sufficient information to determine occurrences of word tokens across all documents in unique sentences.

#### `create_dataframe`

Generate a pandas dataframe from the `summary`. Essentially a non-condensed form of `summary`, with headers: Word, Total occurrences, Occurrences in \<filename\>, Extracts in \<filename\>.
This dataframe can be visualised using `show` from the `pandasgui` package.

## Example

By running `main.py` display a summary dataframe from the plain text files in `test_docs/`, generated using `SummaryOfTextAnalysers`. Note that occurrences count the number of unique sentences the wor was used in, not the total number of occurrences across the entire text.
Token manipulation done:
* word tokens have had contractions expanded,
* word tokens are normalised,
* stopwords and words in `uninteresting_words.csv` removed.

Finally, results are filtered to only those with Total Occurrences >= 20.

![image](https://user-images.githubusercontent.com/44169061/133929024-f58eb50c-65fb-4f2c-bc3f-2ca4ecbd7f05.png)


  

import nltk
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt

nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Read the Moby Dick file from the Gutenberg dataset
from nltk.corpus import gutenberg
moby_dick = gutenberg.raw('melville-moby_dick.txt')

# Tokenization
tokens = word_tokenize(moby_dick)

# Stopword Filtering
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Part-of-Speech Tagging
tagged_tokens = nltk.pos_tag(filtered_tokens)

# POS Frequency
pos_freq = FreqDist(tagged_tokens)
pos_freq.plot(5, title='Top 5 POS Frequencies')

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word, pos=get_wordnet_pos(pos)) for word, pos in tagged_tokens]

# Plot Frequency Distribution
lemmatized_freq = FreqDist(lemmatized_tokens)
lemmatized_freq.plot(20, title='Top 20 Lemmatized Tokens')

# Get WordNet tag for POS
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return 'a'  # Adjective
    elif treebank_tag.startswith('V'):
        return 'v'  # Verb
    elif treebank_tag.startswith('N'):
        return 'n'  # Noun
    elif treebank_tag.startswith('R'):
        return 'r'  # Adverb
    else:
        return 'n'  # Default to Noun

plt.show()

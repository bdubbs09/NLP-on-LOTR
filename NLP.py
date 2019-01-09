import urllib2
from bs4 import BeautifulSoup
import nltk
from nltk import tokenize
from nltk.corpus import stopwords
from nltk.book import *


class Explore_LOTR:
    def __init__(self):
        self.url = "http://ae-lib.org.ua/texts-c/tolkien__the_lord_of_the_rings_2__en.htm"

    def scrape(self):
        page = urllib2.urlopen(self.url)
        soup = BeautifulSoup(page, "html.parser")
        book = []

        for tag in soup.find_all('p'):
            book.append(tag.text)

        sub_book = book[100:120]
        encode = [x.encode('UTF8') for x in sub_book]
        snip = ''.join(map(str, encode))
        return snip


    def parse(self, passage):
        from nltk.tokenize import TweetTokenizer, sent_tokenize
        parsed_passage = tokenize.sent_tokenize(passage)
        for x, sent in enumerate(parsed_passage):
            sent = sent.replace("\n", " ")
            parsed_passage[x] = sent

        tokenizer_words = TweetTokenizer()
        tokens_sents = [tokenizer_words.tokenize(t) for t in parsed_passage]
        tagged_sents = [nltk.pos_tag(s) for s in tokens_sents]
        return tagged_sents

    def expand(self, p_sent):
        from nltk.stem import WordNetLemmatizer
        wordnet_lemmatizer = WordNetLemmatizer()
        lemma_sent = [wordnet_lemmatizer.lemmatize(x) for x,_ in p_sent]
        return lemma_sent

    def dependency_tree(self, exp_sent):
        tree = []

        return tree


    def reduced_sent(self, word_tokens):
        stop_words = set(stopwords.words('english'))
        filtered_sentence = [w for w in word_tokens if not w in stop_words]

        filtered_sentence = []

        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)

        return filtered_sentence
    
    # Getting relevant stats on passage.
    # Looking at word frequency.
    # Needs to be finished.
    def passage_stats(self, passage):
        
        dist = FreqDist(passage)

        return dist["Aragon"]

def main():
    book = Explore_LOTR()
    passage = book.scrape()
    parsed_sents = book.parse(passage)
    ex_sent = parsed_sents[15]
    expanded_sent = book.expand(ex_sent)
    reduced_sent = book.reduced_sent(expanded_sent)
    print(reduced_sent)

if __name__ == "__main__":
    main()

import nltk
from textblob import TextBlob
from newspaper import Article

url = input("Please Enter a URL:\n")
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(f"\n{text}")

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1

def outcome(sentiment):
    if sentiment < -0.3:
        return "negative"
    elif sentiment > -0.3 and sentiment < 0.3:
        return "neutral"
    else:
        return "positive"
    
outcome = outcome(sentiment)

print(f"\nThis article is {outcome} ({sentiment}).")
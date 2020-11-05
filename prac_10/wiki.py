import wikipedia

phrase = input(str("Phrase: "))
while phrase != "":
    try:
        article = wikipedia.page(phrase)
        print(article.title)
        print(article.summary)
        print(article.url)
        phrase = input(str("Phrase: "))
    except wikipedia.DisambiguationError:
        print("There was an error with your search")
        phrase = input(str("Phrase: "))
import requests
from bs4 import BeautifulSoup
import wikipedia


# Adapted from https://www.freecodecamp.org/news/scraping-wikipedia-articles-with-python/

def firstParagraph(term, number):
    numSentences = wikipedia.summary(term, sentences=number)
    return numSentences


def byId(term, id):

    urlScrape = 'https://en.wikipedia.org/wiki/' + term

    response = requests.get(
        url=urlScrape
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    output = soup.find(id=id).get_text()

    return output


def firstXParagraphs(term, number):
    count = number
    urlScrape = 'https://en.wikipedia.org/wiki/' + term

    response = requests.get(
        url=urlScrape
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    list_output = []

    while number > 0:
        for p in soup.find_all('p'):
            list_output.append(p.get_text())
            number -= 1

    return list_output


def textUnderHTwo(term, hTwo, numSentence):

    count = numSentence

    urlScrape = 'https://en.wikipedia.org/wiki/' + term

    response = requests.get(
        url=urlScrape
    )

    soup = BeautifulSoup(response.content, 'html.parser')
    id_object = soup.find_all('h2')

    list_output = []

    for h in id_object:
        if hTwo in h.get_text():
            para = h.find_next_siblings('p')
            for p in para:
                if count > 0:
                    list_output.append(p.get_text())
                count -= 1

    return list_output





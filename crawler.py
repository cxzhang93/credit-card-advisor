from bs4 import BeautifulSoup
import requests

# get soup from inserted url
def getSoup(url):
	r = requests.get(url)
	html_content = r.text
	soup = BeautifulSoup(html_content, "html.parser")
	return soup

# find the nth character in a string
# imported from http://stackoverflow.com/questions/1883980/find-the-nth-occurrence-of-substring-in-a-string
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

soup = getSoup('http://www.moneysmart.sg')

# Initialize the list of credit card information page
creditCardPageList = []

# Crawl for credit card information page
for link in soup.find_all('a'):
	hyperlink = str(link.get('href'))
	# if hyperlinks contains 'credit-card', then record the hyperlink
	if 'credit-cards/' in hyperlink: 
		if hyperlink not in creditCardPageList:
			creditCardPageList.append(hyperlink)

# Initialize the list of all the credit card array
i = 0
cardList = [[]]

# Get URL for every category of cards
for categoryUrl in creditCardPageList: 
	soup = getSoup(categoryUrl) # get html code for every category of credit card
	for link in soup.find_all('a'): 
		hyperlink = str(link.get('href')) # get hyper link appeared in the page
		if 'credit-cards/' in hyperlink: 
			endingPosition = find_nth(hyperlink, '/', 5) # get correct url for credit card page. Filtered url of apply and other sub pages
			if endingPosition == -1: 
				if hyperlink not in cardList[i]:
					if hyperlink not in creditCardPageList:
						cardList[i].append(hyperlink)
						print(hyperlink)

	break

#find_nth



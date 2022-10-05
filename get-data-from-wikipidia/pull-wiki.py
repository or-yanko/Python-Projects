import wikipedia
import time
import sys
from random import uniform
from termcolor import colored


def slowprint(s, col='green', slow=1./100, isChangeSpeed=False):
    """Print slower"""
    if isChangeSpeed == False:
        for c in s + '\n':
            sys.stdout.write(colored(c, col))
            sys.stdout.flush()
            time.sleep(slow)
    else:
        for c in s + '\n':
            sys.stdout.write(colored(c, col))
            sys.stdout.flush()
            a = uniform(1./25, 0.6)
            time.sleep(a)


language = "en"
wikipedia.set_lang(language)

slowprint("which subject whould you like to search on wikipidia?")
a = input()

result = wikipedia.search(a)
slowprint(f"Result search of '{a}':")
i = 1
for b in result:
    slowprint(f"{i}.\t'{b}'")
    i += 1

slowprint("which search result do you choose? enter num of search result")
c = int(input())
page = wikipedia.page(result[c-1])

slowprint("what whould you like to see? enter letters like the ex 'c t r':")
slowprint("c\tfor Page content")
slowprint("t \tfor Page title")
slowprint("ct \tfor Categories")
slowprint("l \tfor Links")
slowprint("r \tfor References")
slowprint("s \tfor Summary")
lst = input().lower().split(" ")
if 'c' in lst:
    content = page.content
    slowprint("Page content:\n" + content + "\n", 'white', 1./1000)
if 't' in lst:
    title = page.title
    slowprint("Page title:\n" + title + "\n", 'white', 1./1000)
if 'ct' in lst:
    categories = page.categories
    output = ""
    i = 1
    for d in categories:
        output += f"{i}.\t{d}\n"
        i += 1
    slowprint("Categories:\n" + output + "\n", 'white', 1./1000)
if 'l' in lst:
    links = page.links
    output = ""
    i = 1
    for d in links:
        output += f"{i}.\t{d}\n"
        i += 1
    slowprint("Links:\n" + output + "\n", 'white', 1./1000)
if 'r' in lst:
    references = page.references
    output = ""
    i = 1
    for d in references:
        output += f"{i}.\t{d}\n"
        i += 1
    slowprint("References:\n" + output + "\n", 'white', 1./1000)
if 's' in lst:
    summary = page.summary
    slowprint("Summary:\n" + summary + "\n", 'white', 1./1000)

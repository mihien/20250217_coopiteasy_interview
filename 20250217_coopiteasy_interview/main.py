import time
import validators
from html_parser import html_parser

def main():
    url = ""
    while not validators.url(url):
        url = input("Please enter the url from which the html files will be downloaded: \n")
        if not validators.url(url):
            print("Invalid url.")

    html_parser(url)

    print("Done parsing.")
    time.sleep(1)

if __name__ == "__main__":
    main()
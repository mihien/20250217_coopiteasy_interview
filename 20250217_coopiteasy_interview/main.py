import time
import os
import shutil
import validators
from html_parser import html_parser

def main():
    if os.path.exists('output'):
        shutil.rmtree('output')
    os.makedirs('output')

    url = ""
    while not validators.url(url):
        url = input("Please enter the url from which the html files will be downloaded: \n")
        if not validators.url(url):
            print("\nInvalid url.")

    html_parser(url)

    print("Done parsing.")
    time.sleep(1)

if __name__ == "__main__":
    main()
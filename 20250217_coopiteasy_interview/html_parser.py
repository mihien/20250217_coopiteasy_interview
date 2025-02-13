import requests
import validators
from bs4 import BeautifulSoup

def html_parser(target_url: str) -> None:
    target_domain_name = target_url.split('/')[2]

    urls_to_visit = [ target_url ]
    urls_found = [ target_url ]

    while urls_to_visit:
        current_url = urls_to_visit.pop()
        response = requests.get(current_url)
        parsed_html = BeautifulSoup(response.text, 'html5lib')
        output_file = "output/" + parsed_html.find('title').string
        with open(output_file, "w") as text_file:
            print(current_url)
            text_file.write(response.text)

        for a_tag in parsed_html.body.find_all('a', href=True):
            href = a_tag['href']
            if not validators.url(href):
                continue
            href_domain_name = href.split('/')[2]
            if href_domain_name != target_domain_name:
                continue
            elif href in urls_found:
                continue

            urls_found.append(href)
            urls_to_visit.append(href)
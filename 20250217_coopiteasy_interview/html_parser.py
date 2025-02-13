import requests
import validators
import networkx as nx
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

def html_parser(target_url: str) -> None:
    target_domain_name = target_url.split('/')[2]

    urls_to_visit = [ target_url ]
    urls_to_node_dict = { target_url:0 }
    node_count = 0
    G = nx.Graph()
    G.add_node(node_count)

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
            if href not in urls_to_node_dict:
                node_count += 1
                G.add_node(node_count)
                urls_to_node_dict[href] = node_count
                urls_to_visit.append(href)
            
            G.add_edge(
                urls_to_node_dict[current_url],
                urls_to_node_dict[href]
            )
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.savefig("output/graph.png")
    

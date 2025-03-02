Wikipedia Dataset Scraper

This project allows you to automatically fetch Wikipedia articles based on specified titles and save them in a JSON file format. It uses the wikipediaapi package to retrieve the text of Wikipedia articles.
Prerequisites

To install all the required dependencies for this project, simply run the following command:

pip install -r requirements.txt

How to Use
There are two main functions in this project:

get_wikipedia_text(title, lang="fa")
This function retrieves the text of a Wikipedia article based on its title. You can specify the language of the article using the lang parameter (default is set to Persian).

title: The title of the Wikipedia article (e.g., "Artificial_Intelligence").
lang: The language of the article (default is "fa" for Persian, but you can also use "en" for English, etc.).
The function returns a dictionary containing the article's title and text.

create_wikipedia_dataset(titles, output_file="dataset.json", lang="fa")
This function is used to fetch multiple articles and store them in a JSON file. You need to pass a list of article titles to this function, and you can specify the output file name (default is "dataset.json").

titles: A list of Wikipedia article titles you want to fetch.
output_file: The name of the output file where the data will be saved.
lang: The language of the articles (default is "fa").


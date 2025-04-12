import wikipedia

SEARCH_PROMPT = "Enter page title: "

def main():
    user_search = input(SEARCH_PROMPT).strip()
    while user_search != "":
        try:
            page_result = wikipedia.page(user_search, auto_suggest = False)
            print(f"\n{page_result.title}")
            print(f"{wikipedia.summary(user_search, sentences=4)}")
            print(f"{page_result.url}\n")

        except wikipedia.DisambiguationError as i:
            print(f"\nWe need a more specific title. Try one of the following, or a new search:")
            print(f"{i.options[:5] + ['...']}\n")
"""
Word Occurrence
Estimate = 20 Minutes
Actual =
"""

def main():
    user_text = input("Input Text: ")
    texts = user_text.split()
    word_counter = {}
    for counter in texts:
        if counter in word_counter:
            word_counter[counter] += 1
        else:
            word_counter[counter] = 1

    # for counter in texts:
    #     counter.lower()
    #     if counter in word_counter:
    #         word_counter[counter] += 1
    #     else:
    #         word_counter[counter] = 1
    # for word, count in word_counter.items():
    #     print(f"{word} : {count}")

main()
"""
Wimbledon
Estimate: 30 Minutes
Actual: 1 Hour
"""
import csv

FILENAME = "wimbledon.csv"

def main():
    champions_data = read_data_file(FILENAME)
    champions_count = count_winnings(champions_data)
    list_of_countries = extract_countries(champions_data)

    print("Wimbledon Champions: ")
    for champions, count in champions_count.items():
        print(f"{champions} {count}")

    countries = list_of_countries.split(", ")
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(list_of_countries)

def read_data_file(file):
    data = []
    with open(file, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            category = line.split(",")
            countries = category[1]
            champions = category[2]
            data.append((countries,champions))
    return data

def count_winnings(data):
    champion_counter = {}
    for countries, champions in data:
        if champions in champion_counter:
            champion_counter[champions] += 1
        else:
            champion_counter[champions] = 1
    return champion_counter

def extract_countries(data):
    countries_list = []
    for country, champions in data:
        if country not in countries_list:
            countries_list.append(country)
    countries_list.sort()
    countries_string = ", ".join(countries_list)
    return countries_string

main()
"""
Wimbledon
Estimate: 30 Minutes
Actual:
"""
import csv

FILENAME = "wimbledon.csv"

def main():
    champions_data = read_data_file(FILENAME)
    champions_count = count_winnings(champions_data)

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

main()
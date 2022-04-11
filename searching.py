import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    if field in set(data.keys()):
        return data[field]

def linear_search(unordered_numbers, searched_number):
    positions = []
    count = 0
    for position, number in enumerate(unordered_numbers):
        if number == searched_number:
            positions.append(position)
            count += 1

    output = dict()
    output["positions"] = positions
    output["count"] = count
    return output

def patter_search(sequence, hledany_vzor):
    positions = []
    for index in range(len(sequence) - len(hledany_vzor) + 1):
        subsequence = sequence[index:(index + len(hledany_vzor))]
        same = True
        for letter_subsequence, letter_hledany_vzor in zip(subsequence, hledany_vzor):
            if letter_subsequence != letter_hledany_vzor:
                same = False
                break
        if same:
            positions.append(index)

    return positions


def binary_search(seznam_cisel, hledane_cislo):




def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    dna_sequence = read_data("sequential.json", "dna_sequence")
    ordered_numbers = read_data("sequential.json", "ordered_numbers")

    search_output_dict = linear_search(unordered_numbers, 0)
    print(search_output_dict)

    search_output_mnoz = patter_search(dna_sequence, "ATA")
    print(search_output_mnoz)

    #search_output_number = binary_search(ordered_numbers, )
    #print(search_output_number)

if __name__ == '__main__':
    main()
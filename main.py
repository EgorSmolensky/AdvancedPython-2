from pprint import pprint
import re
import csv


def read_csv_file():
    with open("phonebook_raw.csv", encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",")
        return list(rows)


def write_csv_file(contacts):
    with open("phonebook.csv", mode="w", encoding='UTF-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts)


def right_name(person_info):
    fullname = ' '.join(person_info[:3]).split()
    if len(fullname) == 2:
        fullname.append('')
    return fullname


def right_phone_number(person_info):
    pattern = re.compile(r"(8|\+7)[- ]?\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{2})[- ]?(\d{2})(( ?)\(?(доб\.) ?(\d+))?\)?")
    return pattern.sub(r'+7(\2)\3-\4-\5\7\8\9', person_info[5])


def merge_duplicates(contacts_list, person_info):
    names = [' '.join(info[:2]) for info in contacts_list]
    person_name = ' '.join(person_info[:2])
    if person_name in names:
        index = names.index(person_name)
        for i in range(len(contacts_list[0])):
            if contacts_list[index][i] == '':
                contacts_list[index][i] = person_info[i]
    else:
        contacts_list.append(person_info)


if __name__ == '__main__':
    contacts_list = read_csv_file()
    new_contacts_list = []

    for person_info in contacts_list:
        new_person = list(person_info)

        new_person[:3] = right_name(person_info)
        new_person[5] = right_phone_number(person_info)
        merge_duplicates(new_contacts_list, new_person)

    pprint(new_contacts_list)
    write_csv_file(new_contacts_list)

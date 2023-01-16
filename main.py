from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8', newline='') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)


def address_book():
    n = len(contacts_list)
    for i in range(n):
        words = contacts_list[i][0].split()
        if len(words) == 3:
            contacts_list[i][0] = words[0]
            contacts_list[i][1] = words[1]
            contacts_list[i][2] = words[2]
        elif len(words) == 2:
            contacts_list[i][0] = words[0]
            contacts_list[i][1] = words[1]
        elif len(words) == 1:
            words2 = contacts_list[i][1].split()
            if len(words2) == 2:
                contacts_list[i][1] = words2[0]
                contacts_list[i][2] = words2[1]

    pattern = r'(\+7|7|8)?\s?\(?(\d{3})\)?[\s-]?(\d{3})-?(\d{2})-?(\d{2})(\s?\(?доб\.\s?(\d{4})\)?)?'
    new_list = []
    for contact in contacts_list:
        a = ','.join(contact)
        new_list.append(a)
    text = ','.join(new_list)
    repl = r'+7(\2)\3-\4-\5\6'
    new_text = re.sub(pattern, repl, text, flags=0)
    new_list2 = new_text.split(',')
    my_list = []
    for i in range(n):
        my_list.append(new_list2[0:7])
        del new_list2[0:7]

    updated_contacts_list = []
    contacts_dict = {}
    for contact in my_list:
        name_tuple = (contact[0], contact[1])
        if name_tuple in contacts_dict:
            number = contacts_dict[name_tuple]
            for i in range(3, 7):
                if updated_contacts_list[number][i] == '':
                    updated_contacts_list[number][i] = contact[i]
        else:
            updated_contacts_list.append(contact)
            number = len(updated_contacts_list) - 1
            contacts_dict[name_tuple] = number

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(updated_contacts_list)


if __name__ == '__main__':
    address_book()

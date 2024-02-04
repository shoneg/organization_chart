import math
import urllib.parse

import numpy as np
import yaml


def generate_v_card(first_name: str, last_name: str, position: str, position_lines: int, email: str, phone: str, address: str, organization: str, website: str, img_url: str, add_width: int, relative_x=0, relative_y=0) -> str:
    template: str
    with open('v_card.svg', 'r', encoding='utf-8') as v_card_file:
        template = v_card_file.read()

    blank_lines = 0
    for l in [email, address, phone]:
        if l.strip() == '':
            blank_lines += 1

    current = template.replace('first_name', first_name.lower())
    current = current.replace('First_Name', first_name)

    current = current.replace('Position', position)

    current = current.replace('last_name', last_name.lower())
    current = current.replace('Last_Name', last_name)

    current = current.replace('email_address', urllib.parse.quote(email))
    current = current.replace('Email_Address', email)

    current = current.replace('phone_address', phone.translate(
        str.maketrans('', '', ' -._:/')))
    current = current.replace('Phone_Address', phone)

    current = current.replace('office_address', urllib.parse.quote(address))
    current = current.replace('Office_Address', address)

    current = current.replace('organization', urllib.parse.quote(organization))

    current = current.replace('web_address', urllib.parse.quote(website))

    current = current.replace('image_address', img_url)

    current = current.replace(
        'pre_mail', '<!--' if email.strip() == '' else '')
    current = current.replace(
        'post_mail', '-->' if email.strip() == '' else '')
    current = current.replace(
        'pre_phone', '<!--' if phone.strip() == '' else '')
    current = current.replace(
        'post_phone', '-->' if phone.strip() == '' else '')
    current = current.replace(
        'pre_address', '<!--' if address.strip() == '' else '')
    current = current.replace(
        'post_address', '-->' if address.strip() == '' else '')

    current = current.replace('full_width', str(380 + add_width))
    current = current.replace('full_height', str(260 + position_lines*35))
    current = current.replace('position_width', str(210 + add_width))
    current = current.replace('address_x', str(356 + add_width + relative_x))
    current = current.replace('address_y', str(
        209 + relative_y - blank_lines * 20))
    current = current.replace('name_x', str(14 + relative_x))
    current = current.replace('name_y', str(14 + relative_y))
    current = current.replace('img_x', str(23 + relative_x))
    current = current.replace('img_y', str(
        27 + relative_y + position_lines*35))
    current = current.replace('qr_x', str(249 + add_width + relative_x))
    current = current.replace('qr_y', str(9 + relative_y))
    current = current.replace('rel_x', str(relative_x))
    current = current.replace('rel_y', str(relative_y))

    return current


def generate_organization_field(name: str, width: int, height: int, v_cards: list[str]) -> str:
    template: str
    with open('organization.svg', 'r', encoding='utf-8') as org_file:
        template = org_file.read()

    current = template.replace('org_width', str(width))
    current = current.replace('org_height', str(height))
    current = current.replace('org_height_minus_two', str(width - 4))

    current = current.replace('v_cards', '\n'.join(v_cards))

    current = current.replace('org_name', name)

    return current


def read_config(file_name) -> dict[str, list[dict[str, str]]]:
    config: dict
    with open(file_name, 'r', encoding='utf-8') as config_file:
        config = yaml.safe_load(config_file)

    better_config = {}
    for first_level_entry in config:
        group = list(first_level_entry.keys())[0]
        content = list(first_level_entry.values())[0]
        better_config[group] = []
        current_list = [list(c.values())[0] for c in content]
        for index, entry_list in enumerate(current_list):
            better_config[group].append({})
            for second_level_entry in entry_list:
                better_config[group][index][list(second_level_entry.keys())[
                    0]] = list(second_level_entry.values())[0]

    return better_config


def pre(
    width, height): return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="{width}px" height="{height}" viewBox="-0.5 -0.5 {width} {height}">'


def post(): return '</svg>'


def v_card_width(add_width): return 342 + add_width


def persons_add_width(person: dict[str, str]) -> int:
    max_length = max(
        len(person['Mail'] if 'Mail' in person else ''),
        len(person['Adresse'] if 'Adresse' in person else ''),
        len(person['Telefon'] if 'Telefon' in person else ''),
        len(person['Vorname']) + len(person['Nachname']) + 1
    )

    a = -9.9
    b = -0.022
    c = 15
    r = a * np.exp(b * max_length) + c
    return max_length * r


def v_card_height(position_lines): return 207 + position_lines*35


def field_dimensions(card_num: int) -> list[int]:
    ret: list[int] = []
    root = math.sqrt(card_num)
    rows = math.ceil(root)
    for i in range(rows):
        ret.append(math.floor((card_num+i) / rows))
    ret.reverse()
    return ret


if __name__ == "__main__":

    better_config = read_config('config.yml')
    vertical_padding = 120
    top_padding = 200
    margin = 80

    for organization, persons in better_config.items():
        v_cards: list[str] = []
        dimensions = field_dimensions(len(persons))
        max_width = max([v_card_width(persons_add_width(p)) for p in persons])
        dimension_heights: list[int] = [0 for _ in range(len(dimensions))]

        for p_index, person in enumerate(persons):
            row = next((i for i, _ in enumerate(dimensions)
                       if sum(dimensions[:i+1]) > p_index), -1)
            person_position_lines = person['Positionszeilen'] if 'Positionszeilen' in person else 1
            card_height = v_card_height(person_position_lines)
            dimension_heights[row] = max(dimension_heights[row], card_height)

        for p_index, person in enumerate(persons):
            add_width = persons_add_width(person)
            row = next((i for i, _ in enumerate(dimensions)
                       if sum(dimensions[:i+1]) > p_index), -1)
            assert row >= 0
            col = p_index % dimensions[row]
            person_position_lines = person['Positionszeilen'] if 'Positionszeilen' in person else 1
            mail = person['Mail'] if 'Mail' in person and person['Mail'].strip(
            ) != '' else ''
            phone = person['Telefon'] if 'Telefon' in person and person['Telefon'].strip(
            ) != '' else ''
            address = person['Adresse'] if 'Adresse' in person and person['Adresse'].strip(
            ) != '' else ''
            card_height = v_card_height(person_position_lines)
            v_card = generate_v_card(person['Vorname'], person['Nachname'], person['Position'], person_position_lines, mail, phone, address, organization, person['Website'], person['Bild'], add_width,
                                     relative_x=vertical_padding + (max_width-v_card_width(add_width))/2 + col*(
                                         max_width+margin) + (max(dimensions)-dimensions[row])*(margin+max_width)/2,
                                     relative_y=top_padding-margin + row*margin + sum(dimension_heights[:row]) + (dimension_heights[row]-card_height)/2)
            v_cards.append(v_card)

        field_width = (2*vertical_padding-margin) + \
            max(dimensions)*(max_width+margin)
        field_height = (top_padding-margin) + \
            margin*len(dimensions) + \
            sum(dimension_heights)
        organization_field = generate_organization_field(
            organization, field_width, field_height, v_cards)
        with open('results/' + organization.replace('/', '-') + '.svg', 'w', encoding='utf-8') as file:
            file.write(pre(field_width+1, field_height+1))
            file.write(organization_field)
            file.write(post())

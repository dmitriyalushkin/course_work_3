import json


def read_data(filepath):
    '''Функция читает файл и переводит содержимое в объект Python'''
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_executed_operations(list_operations):
    '''Функция считывает список по значению EXECUTED'''
    executed_list = []
    for operation in list_operations:
        if operation.get('state') == 'EXECUTED':
            executed_list.append(operation)
    return executed_list



def get_sorted_operations(list_operations):
    '''Функция сортирует список по ключу 'date', начиная с последнего элемента'''
    operations = sorted(list_operations, key=lambda x: x['date'], reverse=True)
    return operations



def get_operation_info(operation):
    '''
    {'date': '2019-12-08T22:46:21.935582',
     'description': 'Открытие вклада',
     'id': 863064926,
     'operationAmount':
         {'amount': '41096.24',
          'currency':
              {'code': 'USD',
               'name': 'USD'}
          },
     'state': 'EXECUTED',
     'to': 'Счет 90424923579946435907'}
     '''
    line_1 = []
    date = operation['date'].split('T')[0]
    date_parts = date.split('-')
    date_reversed = reversed(date_parts)
    date_joined = ".".join(date_reversed)
    line_1.append(date_joined)
    line_1.append(operation['description'])
    line_1_str = ' '.join(line_1)

    "Visa Platinum 7000 79** **** 6361 -> Счет **9638"
    line_2 = []
    if operation.get("from"):
        if operation['from'].startswith("Счет"):
            masked_account = mask_number_account(operation['from'])
            line_2.append(masked_account)
        else:
            masked_card = mask_number_card(operation['from'])
            line_2.append(masked_card)
    else:
        line_2.append("Взнос наличными")
    line_2.append("->")
    masked_account_to = mask_number_account(operation['to'])
    line_2.append(masked_account_to)
    line_2_str = ' '.join(line_2)

    line_3_str = f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"
    return f"{line_1_str}\n" \
           f"{line_2_str}\n" \
           f"{line_3_str}\n"


def mask_number_card(card_info):
    '''Функция маскирует номер карты в формате XXXX XX** **** XXXX'''
    number_card = card_info.split(' ')
    if len(number_card) == 3:
        return f'{number_card[0]} {number_card[1]} {number_card[2][:4]} {number_card[2][4:6]}** **** {number_card[2][12:16]}'
    elif len(number_card) == 2:
        return f'{number_card[0]} {number_card[1][:4]} {number_card[1][4:6]}** **** {number_card[1][12:16]}'



def mask_number_account(account_info):
    '''Функция маскирует номер счета в формате **XXXX'''
    number_account = account_info.split(' ')
    return f'{number_account[0]} **{number_account[1][-4:]}'


if __name__ == '__main__':
    print(get_executed_operations())

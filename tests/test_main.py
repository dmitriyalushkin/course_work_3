from utils import mask_number_account, mask_number_card, get_executed_operations, get_sorted_operations, get_operation_info

def test_mask_number_account():
    assert mask_number_account("Счет 14211924144426031657") == "Счет **1657"

def test_mask_number_card():
    assert mask_number_card("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"
    assert mask_number_card("Maestro 3928549031574026") == "Maestro 3928 54** **** 4026"

def test_get_executed_operations():
    data = [
        {
            'id': 1,
            'state': 'EXECUTED'
        },
        {
            'id': 2,
            'state': 'CANCELED'
        },
        {
            'id': 3,
            'state': 'EXECUTED'
        }
    ]
    expected = [
        {
            'id': 1,
            'state': 'EXECUTED'
        },
        {
            'id': 3,
            'state': 'EXECUTED'
        }
    ]
    assert get_executed_operations(data) == expected

def test_get_sorted_operations():
    data = [
        {
            "date": "2018-01-26T15:40:13.413061"
        },
        {
            "date": "2019-01-26T15:40:13.413061"
        },
        {
            "date": "2017-01-26T15:40:13.413061"
        }
    ]
    expected = [
        {
            "date": "2019-01-26T15:40:13.413061"
        },
        {
            "date": "2018-01-26T15:40:13.413061"
        },
        {
            "date": "2017-01-26T15:40:13.413061"
        }
    ]
    assert get_sorted_operations(data) == expected

def test_get_operation_info_account_to_account():
    data = {
    "id": 649467725,
    "state": "EXECUTED",
    "date": "2018-04-14T19:35:28.978265",
    "operationAmount": {
      "amount": "96995.73",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 27248529432547658655",
    "to": "Счет 97584898735659638967"
  }
    expected = f"14.04.2018 Перевод организации\n"\
               f"Счет **8655 -> Счет **8967\n" \
               f"96995.73 руб.\n"
    assert get_operation_info(data) == expected

def test_get_operation_info_card_to_account():
    data = {
    "id": 649467725,
    "state": "EXECUTED",
    "date": "2018-04-14T19:35:28.978265",
    "operationAmount": {
      "amount": "96995.73",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa 3152479541115065",
    "to": "Счет 97584898735659638967"
  }
    expected = f"14.04.2018 Перевод организации\n"\
               f"Visa 3152 47** **** 5065 -> Счет **8967\n" \
               f"96995.73 руб.\n"
    assert get_operation_info(data) == expected



def test_get_operation_info_cash_to_account():
    data = {
    "id": 649467725,
    "state": "EXECUTED",
    "date": "2018-04-14T19:35:28.978265",
    "operationAmount": {
      "amount": "96995.73",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "to": "Счет 97584898735659638967"
  }
    expected = f"14.04.2018 Перевод организации\n"\
               f"Взнос наличными -> Счет **8967\n" \
               f"96995.73 руб.\n"
    assert get_operation_info(data) == expected
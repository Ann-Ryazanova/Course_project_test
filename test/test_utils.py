from utils import get_data, get_filtered_data, get_last_values, get_formated_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_date):
    assert len(get_filtered_data(test_date)) == 3


def test_get_last_values(test_date):
    data = get_last_values(test_date, 2)
    assert [x['date'] for x in data] == ['2018-11-29T07:18:23.941293', '2018-09-12T21:27:25.241689']


def test_get_formated_data(test_date):
    data = get_formated_data(test_date[:1])
    assert data[0] == '\n30.06.2018 Перевод организации \nСчет 7510 68** **** 6952 -> Счет **6702\n9824.07 USD'

import json
from datetime import datetime


def get_data():
    with open("operations.json", "r", encoding="utf8") as file:
        data = json.load(file)
    return data


def get_filtered_data(data):
    data_state = []
    for data in data:
        if "state" in data and data["state"] == "EXECUTED":
            if "from" in data:
                data_state.append(data)

    return data_state


def get_last_values(data_state, count_vales):
    data_last_values = sorted(data_state, key=lambda x: x['date'], reverse=True)
    return data_last_values[:count_vales]


def get_formated_data(data_last_values):
    formated_data = []
    for row in data_last_values:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")

        description = row['description']

        sender = row["from"].split()
        from_bill = sender.pop(-1)
        from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
        from_info = " ".join(sender)

        recipient = row["to"].split()
        recipient_bill = recipient.pop(-1)
        recipient_bill = f"**{recipient_bill[-4:]}"
        recipient_info = " ".join(recipient)

        amount = f"{row['operationAmount'] ['amount']} {row['operationAmount'] ['currency'] ['name']}"

        formated_data.append(f"""
{date} {description} 
{from_info} {from_bill} -> {recipient_info} {recipient_bill}
{amount}""")

    return formated_data

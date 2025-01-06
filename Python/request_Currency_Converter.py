import requests


def convert_currency(curr_type, api_k):
    try:
        base_url = f'https://v6.exchangerate-api.com/v6/{api_k}/latest/{curr_type}'
        new_request = requests.get(base_url).json()['conversion_rates']
        return new_request
    except Exception as err:
        error_message = err.args
        return error_message


api_key = '7d888357b88491bc40d23740'

currency_type = ['USD', 'CAD', 'EUR', 'JPY', 'MXN']
currency_input = input(f'Which currency, {currency_type}, you want to convert ? : ')

get_info_conv = convert_currency(currency_input, api_key)

print(get_info_conv)

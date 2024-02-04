import requests
import json
import argparse

def get_currency_data(api_key):
    url = f"http://data.fixer.io/api/latest?access_key={api_key}"
    response = requests.get(url)
    return response.json()

def main():
    parser = argparse.ArgumentParser(description='fixer.io API fetch PoC')
    parser.add_argument('-key', type=str, required=True, help='API key of fixer.io')

    args = parser.parse_args()

    currency_data = get_currency_data(args.key)
    print(json.dumps(currency_data, indent=4))

if __name__ == "__main__":
    main()

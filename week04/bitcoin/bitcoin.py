import requests
import sys
import json

def main():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        else:
            quantity = float(sys.argv[1])
            total = bit_coin(quantity)
            print(f"${total:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")


def bit_coin(quantity):

    try:
        req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        #print(req)
        price_per_unit = req['bpi']['USD']['rate_float']
        #print(price_per_unit)
        total_price = price_per_unit * quantity
        #print(total_price)
        return(total_price)

    except requests.RequestException:
        #sys.exit("Request could not be handled")
        return None


if __name__ == "__main__":
    main()

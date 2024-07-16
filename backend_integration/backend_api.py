import requests

def fetch_account_balance(user_id):
    try:
        response = requests.get(f"https://api.yourbank.com/account/{user_id}/balance")
        if response.status_code == 200:
            return response.json()['balance']
        else:
            return "Error fetching account balance."
    except requests.ConnectionError:
        return "Connection error. Please try again later."

# Example usage
if __name__ == "__main__":
    balance = fetch_account_balance("user123")
    print(balance)

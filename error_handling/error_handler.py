def handle_error(error):
    if isinstance(error, ValueError):
        return "Invalid input provided."
    elif isinstance(error, ConnectionError):
        return "There seems to be a connection issue. Please try again later."
    else:
        return "An unexpected error occurred."

# Example usage
if __name__ == "__main__":
    try:
        raise ValueError("Invalid value")
    except Exception as e:
        response = handle_error(e)
        print(response)

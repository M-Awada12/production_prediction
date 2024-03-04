import requests

def production_prediction(latitude, longitude, declination, direction, panel_power):
    try:
        response = requests.get(f"https://api.forecast.solar/estimate/{latitude}/{longitude}/{declination}/{direction}/{panel_power}")

        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"An error occurred: {e}"

api_url = "https://api.forecast.solar/estimate/70/130/45/0/60"

latitude = input("Enter latitude: ")
longitude = input("Enter longitude: ")
declination = input("Enter declination: ")
direction = input("Enter direction: ")
panel_power = input("Enter panel power: ")

print(production_prediction(latitude, longitude, declination, direction, panel_power))

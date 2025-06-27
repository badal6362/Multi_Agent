import requests

def launch_agent():
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching launch data")
        return {}

    data = response.json()
    if data:
        # Sort launches by date_utc to get the nearest launch
        data.sort(key=lambda x: x.get("date_utc", ""))
        next_launch = data[0]
        location = next_launch.get("launchpad")
        name = next_launch.get("name")
        date = next_launch.get("date_utc")
        return {"name": name, "launchpad_id": location, "date": date}
    return {}

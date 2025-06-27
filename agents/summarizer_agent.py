def summarizer_agent(launch_data, weather_data):
    if not launch_data:
        return "No launch data available."
    if weather_data:
        condition = weather_data['weather'][0]['main']
        if condition in ['Rain', 'Thunderstorm']:
            return f"Launch '{launch_data['name']}' might be delayed due to {condition}."
        else:
            return f"Launch '{launch_data['name']}' is unlikely to be delayed. Weather is {condition}."
    return "No weather data available to determine delay."
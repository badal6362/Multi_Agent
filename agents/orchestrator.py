def orchestrator(user_goal):
    from agents.planner_agent import planner_agent
    from agents.launch_agent import launch_agent
    from agents.weather_agent import weather_agent
    from agents.summarizer_agent import summarizer_agent
    

    launchpad_location_map = {
        "5e9e4502f5090995de566f86": "Cape Canaveral",
        "5e9e4501f509094ba4566f84": "Vandenberg",
        "5e9e4501f509094ba4566f85": "Lompoc"  # Add this if needed
    }

    steps = planner_agent(user_goal)
    data = {}
    summary = ""
    news = []

    for step in steps:
        if step == "launch_agent":
            data['launch'] = launch_agent()
        elif step == "weather_agent":
            if 'launch' in data:
                launchpad_id = data['launch'].get("launchpad_id")
                print("Using launchpad ID:", launchpad_id)
                city = launchpad_location_map.get(launchpad_id, "Lompoc")
                print("Fetching weather for city:", city)
                data['weather'] = weather_agent(city)
        elif step == "summarizer_agent":
            summary = summarizer_agent(data.get("launch", {}), data.get("weather", {}))
        elif step == "news_agent":
            try:
                from agents.news_agent import news_agent
                news = news_agent()
            except Exception as e:
                print("News agent error:", e)
                news = []

    # ✅ ✅ ✅ Add this return at the end:
    return {
        "launch": data.get("launch"),
        "weather": data.get("weather"),
        "summary": summary,
        "news": news
    }
if __name__ == "__main__":
    test_goal = "Give me the SpaceX launch weather update and latest news"
    result = orchestrator(test_goal)
    print(result)


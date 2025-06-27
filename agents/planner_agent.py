def planner_agent(user_goal):
    user_goal = user_goal.lower()
    steps = []
    if "spacex" in user_goal and "weather" in user_goal:
        steps += ["launch_agent", "weather_agent", "summarizer_agent"]
    if "news" in user_goal or "latest" in user_goal:
        steps.append("news_agent")
    return steps

from typing import Literal

TimeOfDay = Literal["morning", "afternoon", "evening"]

MORNING_START_HOUR = 5
AFTERNOON_START_HOUR = 12
EVENING_START_HOUR = 18


def classify_time_of_day(hour: int) -> TimeOfDay:
    """挨拶文を時間帯ごとに出し分けるため、時刻を時間帯に分類する"""
    if MORNING_START_HOUR <= hour < AFTERNOON_START_HOUR:
        return "morning"
    if AFTERNOON_START_HOUR <= hour < EVENING_START_HOUR:
        return "afternoon"
    return "evening"


def build_greeting_message(name: str, time_of_day: TimeOfDay) -> str:
    """利用者に表示する、時間帯に合った挨拶文を組み立てる"""
    match time_of_day:
        case "morning":
            return f"おはようございます、{name}さん"
        case "afternoon":
            return f"こんにちは、{name}さん"
        case "evening":
            return f"こんばんは、{name}さん"

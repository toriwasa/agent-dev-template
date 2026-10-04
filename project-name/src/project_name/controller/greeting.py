from dataclasses import dataclass

from project_name.infrastructure.clock import get_current_hour
from project_name.logic.greeting import (
    TimeOfDay,
    build_greeting_message,
    classify_time_of_day,
)


@dataclass(slots=True, frozen=True)
class GreetingRequest:
    """handler 層で検証済みの入力を、挨拶処理へ受け渡すためのデータクラス"""

    name: str


@dataclass(slots=True, frozen=True)
class GreetingResult:
    """挨拶処理の結果を handler 層へ返し、表示方法を handler 層に委ねるためのデータクラス"""

    time_of_day: TimeOfDay
    message: str


def greet_user(request: GreetingRequest) -> GreetingResult:
    """現在の時間帯に合った挨拶文を利用者向けに作成する"""
    hour = get_current_hour()
    time_of_day = classify_time_of_day(hour)
    message = build_greeting_message(request.name, time_of_day)
    return GreetingResult(time_of_day=time_of_day, message=message)

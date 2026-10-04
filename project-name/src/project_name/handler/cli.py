import argparse

from project_name.controller.greeting import GreetingRequest, greet_user


def parse_greeting_request(argv: list[str] | None = None) -> GreetingRequest:
    """コマンドライン引数を検証し、挨拶処理の入力データクラスに変換する"""
    parser = argparse.ArgumentParser(description="時間帯に合った挨拶を表示する")
    parser.add_argument("--name", required=True, help="挨拶する相手の名前")
    args = parser.parse_args(argv)
    name = str(args.name).strip()
    if not name:
        parser.error("--name に空文字は指定できません")
    return GreetingRequest(name=name)


def main() -> None:
    """CLI のエントリーポイントとして、入力の検証から挨拶の表示までを実行する"""
    request = parse_greeting_request()
    result = greet_user(request)
    print(result.message)

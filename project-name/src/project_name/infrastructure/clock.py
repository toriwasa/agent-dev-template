from datetime import datetime


def get_current_hour() -> int:
    """現在時刻の取得を logic 層から切り離し、時間帯判定を純粋関数に保つための I/O 関数"""
    return datetime.now().hour

import pytest

from project_name.logic.greeting import build_greeting_message, classify_time_of_day


@pytest.mark.small()
def test_時間帯判定_12時ちょうどから午後とみなす() -> None:
    """午後の開始時刻ちょうどが、午前ではなく午後に分類されることを検証する

    テスト観点:
        - 午前と午後の境界値
    """

    # Arrange
    # 入力値の準備
    hour = 12

    # 期待値の準備
    expected = "afternoon"

    # Act
    actual = classify_time_of_day(hour)

    # Assert
    assert actual == expected


@pytest.mark.small()
def test_挨拶文作成_時間帯に応じた挨拶に名前を添える() -> None:
    """時間帯に対応する挨拶の言葉に、相手の名前が添えられることを検証する

    テスト観点:
        - 朝の時間帯の挨拶文
    """

    # Arrange
    # 入力値の準備
    name = "山田"

    # 期待値の準備
    expected = "おはようございます、山田さん"

    # Act
    actual = build_greeting_message(name, "morning")

    # Assert
    assert actual == expected

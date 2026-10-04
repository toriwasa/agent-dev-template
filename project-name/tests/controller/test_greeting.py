import pytest

from project_name.controller.greeting import GreetingRequest, GreetingResult, greet_user


@pytest.mark.middle()
def test_挨拶_現在時刻の時間帯に合った挨拶文を返す(monkeypatch: pytest.MonkeyPatch) -> None:
    """現在時刻から判定した時間帯と、それに合った挨拶文が返されることを検証する

    テスト観点:
        - 夜の時間帯の正常系最小ケース
    """

    # Arrange
    # 入力値の準備
    # 実行時刻によって結果が変わらないよう、現在時刻の取得を固定値に差し替える
    monkeypatch.setattr("project_name.controller.greeting.get_current_hour", lambda: 20)
    request = GreetingRequest(name="山田")

    # 期待値の準備
    expected = GreetingResult(time_of_day="evening", message="こんばんは、山田さん")

    # Act
    actual = greet_user(request)

    # Assert
    assert actual == expected

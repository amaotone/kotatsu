import freezegun
import pytest
from kotatsu.cron.anniversary import create_message


@pytest.mark.parametrize(
    ("today", "expected"),
    [
        ("2000-02-01", ":tada::tada::tada:\n今日は付き合い始めて1ヶ月です！\n:tada::tada::tada:"),
        ("2001-01-01", ":tada::tada::tada:\n今日は付き合い始めて1年です！\n:tada::tada::tada:"),
        ("2001-02-01", ":tada::tada::tada:\n今日は付き合い始めて1年1ヶ月です！\n:tada::tada::tada:"),
        ("2000-01-02", ""),
        ("1999-01-01", ""),
    ],
)
def test_create_message(today, expected, mocker):
    mocker.patch("os.environ.get", side_effect=lambda _: "2000-01-01")
    with freezegun.freeze_time(today):
        actual = create_message()
        assert actual == expected

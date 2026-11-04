
from password_policy import check_password, strength, suggest_fix


def test_valid_password():
    assert check_password("Abcdef1!") == []


def test_password_length():
    assert "too short" in check_password("abc")
    assert "too long" in check_password("A" + "a" * 63 + "1!")


def test_common_password():
    assert "common" in check_password("password")


def test_missing_character_types():
    assert "no uppercase" in check_password("abcdefg1!")
    assert "no lowercase" in check_password("ABCDEFG1!")
    assert "no digit" in check_password("Abcdefgh!")
    assert "no special" in check_password("Abcdefg1")


def test_password_strength():
    assert strength("Abcdefghijk1!Z") == "strong"
    assert strength("Abcdef1!") == "good"
    assert strength("abcdefg1!") == "weak"
    assert strength("abc") == "very weak"


def test_suggest_fix():
    assert suggest_fix([]) == "none needed"
    assert suggest_fix(["too short"]) == "add more characters"
    assert suggest_fix(["common"]) == "avoid common passwords"
    assert suggest_fix(["no uppercase"]) == "add uppercase"
    assert suggest_fix(["too long"]) == "shorten it"

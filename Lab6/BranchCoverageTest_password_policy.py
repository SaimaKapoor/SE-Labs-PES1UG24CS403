
from password_policy import check_password, strength, suggest_fix


def test_all_password_character_branches():
    assert check_password("Abcdef1!") == []
    assert check_password("abcdefg1!") == ["no uppercase"]
    assert check_password("ABCDEFG1!") == ["no lowercase"]
    assert check_password("Abcdefgh!") == ["no digit"]
    assert check_password("Abcdefg1") == ["no special"]


def test_length_branches():
    assert "too short" in check_password("abc")
    assert "too long" in check_password("A" + "a" * 63 + "1!")
    assert check_password("Abcdef1!") == []


def test_common_password_branches():
    assert "common" in check_password("password")
    assert "common" not in check_password("Abcdef1!")


def test_strength_branches():
    assert strength("Abcdefghijk1!Z") == "strong"
    assert strength("Abcdef1!") == "good"
    assert strength("abcdefg1!") == "weak"
    assert strength("abc") == "very weak"


def test_suggest_fix_branches():
    assert suggest_fix([]) == "none needed"
    assert suggest_fix(["too short"]) == "add more characters"
    assert suggest_fix(["common"]) == "avoid common passwords"
    assert suggest_fix(["no uppercase"]) == "add uppercase"
    assert suggest_fix(["too long"]) == "shorten it"

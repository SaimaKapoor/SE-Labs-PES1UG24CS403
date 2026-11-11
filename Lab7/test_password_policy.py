
from hypothesis import given, strategies as st, example
from password_policy import first_character_type, split_credentials, digit_ratio


@given(st.one_of(st.text(), st.none()))
@example("")
@example(None)
def test_first_character_type_no_crash(s):
    result = first_character_type(s)

    assert result in {"empty", "digit", "letter", "symbol"}

    if not s:
        assert result == "empty"
    elif s[0].isdigit():
        assert result == "digit"
    elif s[0].isalpha():
        assert result == "letter"
    else:
        assert result == "symbol"


@given(st.one_of(st.text(), st.none()))
@example("")
@example(None)
@example("alice")
@example("alice:one:two")
def test_split_credentials_no_crash(s):
    result = split_credentials(s)

    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(x, str) for x in result)

    if s is None:
        assert result == ("", "")
    elif ":" not in s:
        assert result == (s.strip(), "")
    else:
        user, password = s.split(":", 1)
        assert result == (user.strip(), password.strip())


@given(st.one_of(st.text(), st.none()))
@example("")
@example(None)
def test_digit_ratio_no_crash(s):
    result = digit_ratio(s)

    assert isinstance(result, float)
    assert 0.0 <= result <= 1.0

    if not s:
        assert result == 0.0
    else:
        expected = sum(c.isdigit() for c in s) / len(s)
        assert result == expected

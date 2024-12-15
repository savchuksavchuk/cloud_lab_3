from app import invert_string

def test_invert_string():
    assert invert_string("hello") == "olleh"
    assert invert_string("") == ""
    assert invert_string("12345") == "54321"

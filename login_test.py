
# login_test.py
# Sample tests for AttendX login

def test_valid_login():
    username = "student01"
    password = "correct123"

    if username and password:
        print("PASS: Login fields are filled")
    else:
        print("FAIL: Login fields are empty")


def test_empty_login():
    username = ""
    password = ""

    if not username and not password:
        print("PASS: Empty login fields detected")
    else:
        print("FAIL: Empty field test failed")


if __name__ == "__main__":
    test_valid_login()
    test_empty_login()

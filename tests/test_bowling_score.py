def get_score_from_frame(frame):
    if frame == "X":
        return 10
    if frame[1] == "/":
        return 10
    first_roll = int(frame[0])
    second_roll = int(frame[1])

    return first_roll + second_roll

def test_strike_equals_10():
    assert get_score_from_frame("X") == 10


def test_frame_no_score():
    assert get_score_from_frame("00") == 0

def test_frame_with_score():
    assert get_score_from_frame("34") == 7

def test_frame_with_spare():
    assert get_score_from_frame("4/") == 10
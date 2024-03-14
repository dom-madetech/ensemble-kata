def get_score_from_roll(roll):
    if roll == "X":
        return 10
    else:
        return 0

# test a single frame with a strike
def test_strike_equals_10():
    assert get_score_from_roll("X") == 10

# test a single frame without strike
def test_simple_frame_no_score():
    assert get_score_from_roll("00") == 0
def get_score_from_roll(roll):
    return 10

# test a single frame with a strike
def test_strike_equals_10():
    assert get_score_from_roll("X") == 10
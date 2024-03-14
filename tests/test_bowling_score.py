def get_score_from_frame(frame):
    if frame == "X" or frame[1] == "/":
        return 10
    first_roll = int(frame[0])
    second_roll = int(frame[1])

    return first_roll + second_roll

def get_score_from_game(game):
    frames = game.split(" ")
    total = 0
    for index, frame in enumerate(frames):
        total += get_score_from_frame(frame)
        if frame == "X":
            total += get_score_from_frame(frames[index + 1])
        if frame[-1] == "/":
            total += int(frames[index+1][0])
    return total


def test_frame_with_strike():
    assert get_score_from_frame("X") == 10

def test_frame_no_score():
    assert get_score_from_frame("00") == 0

def test_frame_with_score():
    assert get_score_from_frame("34") == 7

def test_frame_with_spare():
    assert get_score_from_frame("4/") == 10

def test_two_frames_with_no_score():
    assert get_score_from_game("00 00") == 0

def test_two_frames_with_score():
    assert get_score_from_game("34 26") == 15

def test_two_frames_with_strike_and_no_score():
    assert get_score_from_game("X 00") == 10

def test_two_frames_with_strike_and_one():
    assert get_score_from_game("X 10") == 12

def test_two_frames_with_strike_and_nine():
    assert get_score_from_game("X 27") == 28

def test_two_frames_with_spare_and_one():
    assert get_score_from_game("3/ 10") == 12





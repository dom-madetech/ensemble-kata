class Frame: 
    def is_strike(self):
        return False
frame = Frame()





def test_frame_not_strike():
    assert frame.is_strike() == False

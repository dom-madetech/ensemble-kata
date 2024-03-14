class Frame: 
    def __init__(self, rolls):
        self.rolls = rolls

    def is_strike(self):
        return self.rolls == "X"
    
    def is_spare(self):
        return "/" in self.rolls
    

no_strike_frame = Frame("34")

strike_frame = Frame("X")

spare_frame = Frame("3/")





def test_frame_not_strike():
    assert no_strike_frame.is_strike() == False

def test_frame_is_strike():
    assert strike_frame.is_strike() == True

def test_frame_is_not_spare():
    assert no_strike_frame.is_spare() == False

def test_frame_is_spare():
    assert spare_frame.is_spare() == True

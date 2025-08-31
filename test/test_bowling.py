
from src.scoreCard import ScoreCard



def test_score_card():

    card = ScoreCard("12345678911234567891")
    assert card


def test_get_pins():

    PINS = "1235678911234567891"
    card = ScoreCard(PINS)
    assert card.getPins() == PINS


def test_normal_score():

    PINS = "12345123451234512345"       # PINS == 60
    card = ScoreCard(PINS)
    assert 60 == card.computeScore()

def test_missed_rolls():
    PINS = "9-9-9-9-9-9-9-9-9-9-"      # PINS == 90
    card = ScoreCard(PINS)
    assert 90 == card.computeScore()

def test_score_spare():                # PINS == 121
    PINS = "9-3/613/815/-/8-7/8-"
    card = ScoreCard(PINS)
    assert 121 == card.computeScore()

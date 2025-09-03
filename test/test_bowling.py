import pytest
from src.scoreCard import ScoreCard



def test_score_card():

    card = ScoreCard("12345678911234567891")
    assert card


def test_get_pins():

    PINS = "12345678911234567891"
    card = ScoreCard(PINS)
    assert card.get_pins() == PINS

@pytest.mark.normal_score
def test_normal_score():

    PINS = "12345678911234567891"       # PINS == 92
    card = ScoreCard(PINS)
    assert 92 == card.get_score()

@pytest.mark.missed_rolls
def test_missed_rolls():
    PINS = "1234-6-8911234-6-891"      # PINS == 68
    card = ScoreCard(PINS)
    assert 68 == card.get_score()

@pytest.mark.score_spare
def test_score_spare():
    PINS = "5/5/5/5/5/5/5/5/5/5/5"
    card = ScoreCard(PINS)
    assert 150 == card.get_score()


def test_symbols_to_numbers():
    PINS = "5/XX4/1/7/2-23X12"
    card = ScoreCard(PINS)
    assert "55101046197320231012" == card.symbols_to_numbers()

def test_
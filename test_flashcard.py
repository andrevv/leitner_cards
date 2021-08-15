from flashcard import Flashcard


def test_init():
    card = Flashcard(question='What is the capital of Italy?', answer='Rome')
    assert card.question == 'What is the capital of Italy?'
    assert card.answer == 'Rome'

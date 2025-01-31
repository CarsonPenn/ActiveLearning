import pytest
from unittest.mock import patch
from io import StringIO
from question_class import question
from LOTRquiz_final import main, easy, medium, hard, print_questions_and_answers

# Sample data for testing
sample_easy_questions = [
    question("Question 1: Where does Frodo live?: \n(a) Rohan\n(b) Shire\n(c) Pelinor Fields\n\n", "b"),
    question("Question 2: How many people are there in the fellowship?: \n(a) 7\n(b) 10\n(c) 9\n\n", "c"),
    # Add more sample questions if needed
]

sample_medium_questions = [
    question("Question 1: Where does Barliman Butterbur work at?\n(a) The Prancing Pony\n(b) The Green Dragon\n(c) Worm Tongue Inn\n\n", "a"),
    question("Question 2: Who is Théodred\n(a) Son of Eomer\n(b) Son of Théoden\n(c) Son of Theothor\n\n", "b"),
    # Add more sample questions if needed
]

sample_hard_questions = [
    question("Question 1: What is Aragorn's Father's name?\n(a) Arathorn II\n(b) Aragon I\n(c) Aroniel\n\n", "a"),
    question("Question 2: What is the name of the Eagle King?\n(a) Thror\n(b) Thorondor\n(c) Your mom\n\n", "b"),
    # Add more sample questions if needed
]

# Patching input() function to provide predefined inputs
def patched_input(mock, inputs):
    def inner(prompt):
        print(prompt, end="")
        return inputs.pop(0)
    mock.side_effect = inner

# Test easy() function
def test_easy():
    with patch('builtins.input') as mocked_input:
        mocked_input.side_effect = ["b"] * len(sample_easy_questions)
        output = easy(sample_easy_questions)
        assert len(output) == len(sample_easy_questions)
        assert output == [("Question 1: Where does Frodo live?: \n(a) Rohan\n(b) Shire\n(c) Pelinor Fields\n\n", "b")] * len(sample_easy_questions)

# Test medium() function
def test_medium():
    with patch('builtins.input') as mocked_input:
        mocked_input.side_effect = ["a"] * len(sample_medium_questions)
        output = medium(sample_medium_questions)
        assert len(output) == len(sample_medium_questions)
        assert output == [("Question 1: Where does Barliman Butterbur work at?\n(a) The Prancing Pony\n(b) The Green Dragon\n(c) Worm Tongue Inn\n\n", "a")] * len(sample_medium_questions)

# Test hard() function
def test_hard():
    with patch('builtins.input') as mocked_input:
        mocked_input.side_effect = ["a"] * len(sample_hard_questions)
        output = hard(sample_hard_questions)
        assert len(output) == len(sample_hard_questions)
        assert output == [("Question 1: What is Aragorn's Father's name?\n(a) Arathorn II\n(b) Aragon I\n(c) Aroniel\n\n", "a")] * len(sample_hard_questions)

# Test main() function
def test_main():
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ["e", "y", "n"]
            main()
            output = mock_stdout.getvalue()
            assert "You got" in output

# Test print_questions_and_answers() function
def test_print_questions_and_answers():
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        print_questions_and_answers([("Question 1", "Answer 1"), ("Question 2", "Answer 2")])
        output = mock_stdout.getvalue()
        assert "Question 1" in output
        assert "Answer 1" in output
        assert "Question 2" in output
        assert "Answer 2" in output

if __name__ == "__main__":
    pytest.main()

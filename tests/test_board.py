import pytest

from src.board import Board, Square

@pytest.fixture(scope='class')
def board_fixture() -> Board:
    return Board()


@pytest.mark.board
class TestBoard:


    def test_create_board(self, board_fixture):
        assert all(type(square) == Square for row in board_fixture() for square in row)

    def test_board_str(self, board_fixture):
        assert all(type(square) == str for row in board_fixture.__str__() for square in row)

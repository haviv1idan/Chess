import pytest

from src import Board, Square

@pytest.fixture(scope='class')
def board_fixture() -> Board:
    return Board()


@pytest.mark.board
class TestBoard:


    def test_create_board(self, board_fixture):
        assert all(type(square) == Square for row in board_fixture() for square in row)

    def test_board_str(self, board_fixture):
        assert all(type(square) == str for row in board_fixture.__str__() for square in row)

    def test_board_dict(self, board_fixture):
        board_hash: dict[str, Square] = board_fixture.convert_board_to_dict()
        print(board_hash)
        for row in board_fixture():
            for square in row:
                chess_col = square.column
                chess_row = str(square.row)
                assert board_hash[chess_col + chess_row] == square

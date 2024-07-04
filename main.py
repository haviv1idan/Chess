from logging_config import get_logger
from argparse import ArgumentParser, BooleanOptionalAction
from game import GameObject

logger = get_logger(__name__)


def main(debug=False, default=True):
    game = GameObject(debug_mode=debug, default_board=default)
    game.start_game()
    print(game._game, file=open('games.pgn', 'a'), end="\n\n")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--debug", help='DEBUG mode', action=BooleanOptionalAction, default=True)
    parser.add_argument("--default", help='Default board', action=BooleanOptionalAction, default=True)
    
    # for no debug mode
    # python main.py --no-debug

    args = parser.parse_args()
    debug_mode = args.debug  
    default = args.default
    print(f"{debug_mode = }")
    print(f"{default = }")
    main(debug_mode, default)

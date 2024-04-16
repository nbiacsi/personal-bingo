import random
import numpy as np
import pandas as pd


def main() -> None:
    players: list[str] = [
        "Player 1",
        "Player 2",
        "Player 3",
    ]

    for player in players:
        numbers: range = random.sample(range(1, 26), 25)
        array = np.array(numbers).reshape(5, 5)
        board = pd.DataFrame(array)
        board = board.rename(columns={0: "B", 1: "I", 2: "N", 3: "G", 4: "O"})
        board.to_csv(
            rf"folderlocation\{player}_BingoBoard.csv",
            index=False,
        )


if __name__ == "__main__":
    main()

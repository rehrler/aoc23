def load_file(filename: str) -> list:
    with open(filename, "r", encoding="utf8") as file_opened:
        lines = file_opened.readlines()
    games_loaded = []
    for line in lines:
        line = line.rstrip()
        game = line.split(": ")[0]
        sets = line.split(": ")[1].split("; ")
        new_game = Game(int(game.split(" ")[-1]))
        for game_set in sets:
            new_set = {}
            for cube in game_set.split(", "):
                new_set[cube.split(" ")[1]] = int(cube.split(" ")[0])
            new_game.add_set(game_set=new_set)
        games_loaded.append(new_game)
    return games_loaded


class Game:
    def __init__(self, game_id: int):
        self._game_id = game_id
        self.sets = []

    def add_set(self, game_set: dict):
        self.sets.append(game_set)

    def get_id(self) -> int:
        return self._game_id


def play_part1(games_part1: list) -> int:
    sum_game_ids = 0
    limits = {"red": 12, "green": 13, "blue": 14}
    for game in games_part1:
        limited_reached = False
        for games_set in game.sets:
            for limit in limits.items():
                if limit[0] in games_set:
                    if games_set[limit[0]] > limit[1]:
                        limited_reached = True
                        break
        if not limited_reached:
            sum_game_ids += game.get_id()
    return sum_game_ids


def play_part2(games_part2: list) -> int:
    sum_game_ids = 0
    keys = ["red", "green", "blue"]
    for game in games_part2:
        maxs = {"red": 0, "green": 0, "blue": 0}
        for game_set in game.sets:
            for key in keys:
                if key in game_set:
                    if game_set[key] > maxs[key]:
                        maxs[key] = game_set[key]
        sum_intr = 1
        for key in keys:
            sum_intr *= maxs[key]
        sum_game_ids += sum_intr
    return sum_game_ids


if __name__ == "__main__":
    games = load_file("../data/day02.txt")

    PART_1_RESULT = play_part1(games)

    print(f"Part 1: {PART_1_RESULT}")

    PART_2_RESULT = play_part2(games)

    print(f"Part 2: {PART_2_RESULT}")

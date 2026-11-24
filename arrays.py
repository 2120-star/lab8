import sys

DEFAULT_SCORES = [85, 92, 78, 65, 99]


def get_scores():
    # 1. Command-line arguments (used by Jenkins)
    if len(sys.argv) > 1:
        return [float(x) for x in sys.argv[1:]]

    # 2. Interactive prompt (only when run from a real terminal)
    if sys.stdin is not None and sys.stdin.isatty():
        try:
            raw = input("Enter scores separated by spaces: ").split()
            if raw:
                return [float(x) for x in raw]
        except EOFError:
            pass

    # 3. Fallback for non-interactive runs
    return DEFAULT_SCORES


def calculate_sum(scores):
    return sum(scores)


def calculate_average(scores):
    return sum(scores) / len(scores)


def find_max(scores):
    return max(scores)


def find_min(scores):
    return min(scores)


def main():
    scores = get_scores()
    print(f"Scores : {scores}")
    print(f"Sum    : {calculate_sum(scores)}")
    print(f"Average: {calculate_average(scores):.2f}")
    print(f"Maximum: {find_max(scores)}")
    print(f"Minimum: {find_min(scores)}")


if __name__ == "__main__":
    main()
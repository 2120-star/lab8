import sys

DEFAULT_SCORES = [85, 92, 78, 65, 99]


def get_scores():
    """Get scores from CLI args, an interactive prompt, or a default (for CI)."""
    if len(sys.argv) > 1:
        raw = sys.argv[1:]
    elif sys.stdin.isatty():
        raw = input("Enter scores separated by spaces: ").split()
    else:
        return DEFAULT_SCORES  # non-interactive (e.g. Jenkins)
    return [float(x) for x in raw]


def calculate_sum(scores):
    return sum(scores)


def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0


def main():
    scores = get_scores()
    if not scores:
        print("No scores provided.")
        return
    print(f"Scores : {scores}")
    print(f"Sum    : {calculate_sum(scores)}")
    print(f"Average: {calculate_average(scores):.2f}")


if __name__ == "__main__":
    main()
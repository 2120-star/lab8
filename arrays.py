
def calculate_sum_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return total, average


def calculate_max_min(scores):
    maximum = max(scores)
    minimum = min(scores)
    return maximum, minimum


def main():
    score_input = input("Enter scores separated by spaces: ")

    scores = [int(score) for score in score_input.split()]

    if len(scores) == 0:
        print("Please enter at least one score.")
        return

    total, average = calculate_sum_average(scores)
    maximum, minimum = calculate_max_min(scores)

    print("Scores:", scores)
    print("Sum of scores:", total)
    print("Average of scores:", average)
    print("Maximum score:", maximum)
    print("Minimum score:", minimum)


if __name__ == "__main__":
    main()

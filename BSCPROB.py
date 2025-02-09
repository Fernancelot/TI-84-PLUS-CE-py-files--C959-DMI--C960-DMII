# UNIT 5: Basic Probability
# Purpose:
# This program calculates basic probabilities for events in a sample space.

def probability(event_outcomes, total_outcomes):
    if total_outcomes == 0:
        return 0
    return event_outcomes / total_outcomes

def main():
    print("Basic Probability Calculator")
    try:
        event_outcomes = int(input("Enter the number of event outcomes: "))
        total_outcomes = int(input("Enter the total number of outcomes: "))
        if event_outcomes < 0 or total_outcomes <= 0:
            print("Error: Outcomes must be non-negative, and total outcomes must be positive.")
            return

        result = probability(event_outcomes, total_outcomes)
        print("Probability = " + str(result))
    except ValueError:
        print("Error: Please enter valid integers.")

main()

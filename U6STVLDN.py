# UNIT 6: State Validation
# Purpose:
# This program checks if a given string is accepted by an FSM or NFA.

def is_accepted_by_fsm(transition_table, start_state, accepting_states, input_string):
    current_state = start_state
    for char in input_string:
        if char not in transition_table[current_state]:
            return False
        current_state = transition_table[current_state][char]
    return current_state in accepting_states

def main():
    print("FSM Acceptance Check")
    print("Checks if an input string is accepted by the FSM.")

    # Example FSM with accepting states
    transition_table = {
        "A": {"0": "D", "1": "B"},
        "B": {"0": "B", "1": "C"},
        "C": {"0": "B", "1": "A"},
        "D": {"0": "C", "1": "A"}
    }
    start_state = "A"
    accepting_states = ["C"]

    input_string = input("Enter the input string (e.g., 1011): ")
    if is_accepted_by_fsm(transition_table, start_state, accepting_states, input_string):
        print("The string is accepted by the FSM.")
    else:
        print("The string is NOT accepted by the FSM.")

main()

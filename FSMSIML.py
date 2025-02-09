# UNIT 6: FSM Simulation
# Purpose:
# This program simulates a finite state machine (FSM) based on a transition table.
# It processes an input string and determines the final state.

def fsm_simulation(transition_table, start_state, input_string):
    current_state = start_state
    for char in input_string:
        if char not in transition_table[current_state]:
            print("Invalid input:", char)
            return None
        current_state = transition_table[current_state][char]
    return current_state

def main():
    print("Finite State Machine (FSM) Simulation")
    print("Simulates transitions and determines the final state.")

    # Example transition table
    transition_table = {
        "A": {"0": "D", "1": "B"},
        "B": {"0": "B", "1": "C"},
        "C": {"0": "B", "1": "A"},
        "D": {"0": "C", "1": "A"}
    }
    start_state = "A"

    input_string = input("Enter the input string (e.g., 001100): ")
    final_state = fsm_simulation(transition_table, start_state, input_string)

    if final_state:
        print("Final state:", final_state)
    else:
        print("Input string is not valid for the FSM.")

main()

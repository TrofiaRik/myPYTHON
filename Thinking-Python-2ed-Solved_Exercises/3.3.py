def right_justify(s):
    workspace_cols = 80
    calc_len = len(s)
    calc_justify_spaces = workspace_cols - calc_len
    print(" "*calc_justify_spaces+s)
right_justify("genova")

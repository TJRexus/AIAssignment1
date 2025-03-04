#Step function that takes an action in the GridWorld Environment
#Takes the action and determine if the state is allowed and then returns true or false
def step(self, action):
    # Actions: 0=up, 1=right, 2=down, 3=left
    r, c = self.state
    if action == 0:   # up
        r = max(r - 1, 0) #Need to make it -1 to ensure it doesn't go past the lower boundary
    # (Other actions omitted for brevity)
    self.state = (r, c)
    # Terminal state check
    if self.state in self.terminal:
        return self.state, 1, True
    else:
        return self.state, 0, False
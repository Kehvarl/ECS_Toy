from Components.component import Component


class AIComponent(Component):
    def __init__(self):
        self.goals = []
        self.target = None
        self.next_move = None

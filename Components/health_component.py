from Components.component import Component


class HealthComponent(Component):
    """
    Keep track of HP and alive state
    """
    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.alive = True

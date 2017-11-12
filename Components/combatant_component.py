from Components.component import Component


class CombatantComponent(Component):
    """
    Keep track of HP and alive state
    """
    def __init__(self, max_hp, defense, offense):
        """
        :param int max_hp: Max Hit Points
        :param int defense: Base Defense Power
        :param int offense: Base Attack Power
        """
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.alive = True
        self.defense = defense
        self.offense = offense

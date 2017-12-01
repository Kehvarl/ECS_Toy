from random import randint
from Systems.system import System
from Components.combatant_component import CombatantComponent


class CombatSystem(System):
    def update(self):
        entities = self.entity_manager.get_all_entities_with_component(CombatantComponent.__name__)
        for entity in entities:
            combat_component = self.entity_manager.get_component_for_entity(CombatantComponent.__name__, entity)
            if randint(1, 100) < 10:
                combat_component.current_hp -= 1

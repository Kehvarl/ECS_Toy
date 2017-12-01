from Systems.system import System
from Components.combatant_component import CombatantComponent


class HealthSystem(System):
    """
    Handle health components for all entities.
    """
    def update(self):
        entities = self.entity_manager.get_all_entities_with_component(CombatantComponent.__name__)
        for entity in entities:
            health_component = self.entity_manager.get_component_for_entity(CombatantComponent.__name__, entity)
            if not health_component.alive:
                return
            if health_component.max_hp == 0:
                return
            if health_component.current_hp <= 0:
                health_component.alive = False
                self.entity_manager.remove_entity(entity)

from random import randint
from Systems.system import System
from Components.ai_component import AIComponent


class AISystem(System):
    def update(self):
        entities = self.entity_manager.get_all_entities_with_component(AIComponent.__name__)
        for entity in entities:
            ai_component = self.entity_manager.get_component_for_entity(AIComponent.__name__, entity)
            dx = randint(-1, 1)
            dy = randint(-1, 1)
            ai_component.next_move = (dx, dy)

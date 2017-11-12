from Systems.system import System
from Components.position_component import PositionComponent
from Components.ai_component import AIComponent


class MovementSystem(System):
    def update(self):
        entities = self.entity_manager.get_all_entities_with_component(PositionComponent.__name__)
        for entity in entities:
            position_component = self.entity_manager.get_component_for_entity(PositionComponent.__name__, entity)
            ai_component = self.entity_manager.get_component_for_entity(AIComponent.__name__, entity)
            if ai_component and ai_component.next_move:
                dx, dy = ai_component.next_move
                position_component.x += dx
                position_component.y += dy

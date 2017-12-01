from Entities.entity_manager import EntityManager
from Components.combatant_component import CombatantComponent
from Components.position_component import PositionComponent
from Components.ai_component import AIComponent
from Systems.health_system import HealthSystem
from Systems.ai_system import AISystem
from Systems.movement_system import MovementSystem
from Systems.combat_system import CombatSystem

"""
ECS Toy
Author: Kehvarl

Playing around with ECS Concepts

November 2017 Implementation based on:
https://www.raywenderlich.com/24878/introduction-to-component-based-architecture-in-games
"""

if __name__ == "__main__":
    mgr = EntityManager()
    health_system = HealthSystem(mgr)
    ai = AISystem(mgr)
    movement = MovementSystem(mgr)
    combat = CombatSystem(mgr)

    player = mgr.create_entity()
    mgr.add_component_to_entity(CombatantComponent(10, 1, 1), player)
    mgr.add_component_to_entity(AIComponent(), player)
    mgr.add_component_to_entity(PositionComponent(10, 10), player)

    player_health = mgr.get_component_for_entity(CombatantComponent.__name__, player)
    player_location = mgr.get_component_for_entity(PositionComponent.__name__, player)

    while player_health.alive:
        ai.update()
        movement.update()
        combat.update()
        print("{0} ({1},{2})".format(player_health.current_hp, player_location.x, player_location.y))
        health_system.update()
    print("Player Died!")

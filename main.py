from random import randint

from Entities.entity_manager import EntityManager
from Components.combatant_component import CombatantComponent
from Systems.health_system import HealthSystem

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

    player = mgr.create_entity()
    mgr.add_component_to_entity(CombatantComponent(10, 1, 1), player)
    player_health = mgr.get_component_for_entity(CombatantComponent.__name__, player)

    while player_health.alive:
        if randint(0, 100) > 90:
            player_health.current_hp -= 1
        print(player_health.current_hp)
        health_system.update()

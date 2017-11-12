"""
ECS Toy
Author: Kehvarl

Playing around with ECS Concepts

November 2017 Implementation based on:
https://www.raywenderlich.com/24878/introduction-to-component-based-architecture-in-games
"""


class Entity:
    def __init__(self, entity_id):
        self.entity_id = entity_id


class Component:
    pass


class HealthComponent(Component):
    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.alive = True


class EntityManager:
    MAX_ENTITIES = 100

    def __init__(self):
        self.entities = []
        self.components_by_class = {}
        self.lowest_unassigned_entity_id = 0

    def generate_new_entity_id(self):
        """
        :return: Next available entity ID
        """
        if self.lowest_unassigned_entity_id < EntityManager.MAX_ENTITIES:
            self.lowest_unassigned_entity_id += 1
            return self.lowest_unassigned_entity_id
        else:
            for entity_id in range(1, EntityManager.MAX_ENTITIES):
                if self.entities[entity_id] is None:
                    return entity_id
        raise BaseException("No available Entity IDs")

    def create_entity(self):
        """
        Generate a new Entity ID and append it to the list of Entities
        :return Entity: The Entity object
        """
        entity_id = self.generate_new_entity_id()
        self.entities.append(entity_id)
        return Entity(entity_id)

    def add_component_to_entity(self, component, entity):
        """
        :param component: component to add to entity
        :param Entity entity: Entity object to add component to
        """
        components = self.components_by_class[component.__class__]
        if components is None:
            components = {}
            self.components_by_class[component.__class__] = components
        components[entity.entity_id] = component

    def get_component_for_entity(self, component, entity):
        """
        :param component:
        :param Entity entity:
        :return Component:
        """
        return self.components_by_class[component.__class__][entity.entity_id]

    def remove_entity(self, entity):
        """
        :param Entity entity:
        """
        for components in self.components_by_class:
            components[entity.entity_id] = None
        self.entities.remove(entity.entity_id)

    def get_all_entities_with_component(self, component):
        """
        :param component:
        :return list: Entity objects
        """
        components = self.components_by_class[component.__class__]
        entities = []
        if components:
            for entity_id, _ in components:
                entities.append(Entity(entity_id))
        return entities


class System:
    def __init__(self, entity_manager):
        """
        :param EntityManager entity_manager:
        """
        self.entity_manager = entity_manager

    def update(self):
        pass


class HealthSystem(System):
    def update(self):
        entities = self.entity_manager.get_all_entities_with_component(HealthComponent)
        for entity in entities:
            health_component = self.entity_manager.get_component_for_entity(HealthComponent, entity)
            if not health_component.alive:
                return
            if health_component.max_hp == 0:
                return
            if health_component.current_hp <= 0:
                health_component.alive = False
                self.entity_manager.remove_entity(entity)

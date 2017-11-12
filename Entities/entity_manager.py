from Entities.entity import Entity


class EntityManager:
    """
    Track entities and their components.
    """
    MAX_ENTITIES = 100

    def __init__(self):
        self.entities = []
        self.components_by_class = {}
        self.lowest_unassigned_entity_id = 0

    def generate_new_entity_id(self):
        """
        :return int: Next available entity ID
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
        :return Entity.Entity: The Entity object
        """
        entity_id = self.generate_new_entity_id()
        self.entities.append(entity_id)
        return Entity(entity_id)

    def add_component_to_entity(self, component, entity):
        """
        :param component: component to add to entity
        :param Entity.Entity entity: Entity object to add component to
        """
        components = self.components_by_class.get(type(component).__name__)
        if components is None:
            components = {}
            self.components_by_class[type(component).__name__] = components
        components[entity.entity_id] = component

    def get_component_for_entity(self, component_name, entity):
        """
        :param component_name:
        :param Entity.Entity entity:
        :return Component:
        """
        return self.components_by_class.get(component_name)[entity.entity_id]

    def remove_entity(self, entity):
        """
        :param Entity.Entity entity:
        """
        for components in self.components_by_class:
            self.components_by_class[components][entity.entity_id] = None
        self.entities.remove(entity.entity_id)

    def get_all_entities_with_component(self, component_name):
        """
        :param component_name:
        :return list: Entity objects
        """
        components = self.components_by_class[component_name]
        entities = []
        if components:
            for entity_id, component_type in components.items():
                entities.append(Entity(entity_id))
        return entities

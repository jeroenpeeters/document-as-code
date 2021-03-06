"""
    Iso25010CharacteristicBase - base class for ISO 25010 software quality characteristics
"""
from domain import base


class Iso25010CharacteristicBase(base.Base):
    """
    base class for ISO 25010 software quality characteristics
    """

    name = None  # name of the characteristic
    description = None  # description of the characteristic

    def __init__(self, identifier, name, description):
        """
        create an ISO 25010 base characteristic
        :param identifier: identifier for the characteristic
        :param name: name for the characteristic
        :param description: description for the characteristic
        """
        super().__init__(identifier)

        self.name = name
        self.description = description

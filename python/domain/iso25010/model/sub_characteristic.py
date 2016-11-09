'''
    Iso25010SubCharacteristic - ISO 25010 software quality sub characteristic
'''
from __future__ import absolute_import
from __future__ import print_function


from .characteristic_base import Iso25010CharacteristicBase


class Iso25010SubCharacteristic( Iso25010CharacteristicBase ):
    '''
    ISO 25010 software quality sub characteristic
    '''

    _main_characteristic = None


    def __init__( self, identifier, name, description, part_of=None ):
        '''
        Constructor
        '''
        super(Iso25010SubCharacteristic, self).__init__( identifier, name, description )

        if part_of:
            self.part_of( part_of )


    def part_of( self, main_characteristic ):
        """
        make sub characteristic part of a main characteristic
        """
        if self._main_characteristic is None:
            self._main_characteristic = main_characteristic
            main_characteristic.sub_characteristic( self )

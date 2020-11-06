class PlayerCharacter:

    # Class attributes
    LEVEL_MIN = 1
    LEVEL_MAX = 100

    def __init__(self, name, level):
        # Instance attributes
        self.name = name
        self.level = level

    # Define getter
    @property
    def level(self):
        print("Getting level...")
        return self._level

    # Define setter
    @level.setter
    def level(self, value):
        print("Setting level...")
        if value < PlayerCharacter.LEVEL_MIN:
            raise ValueError(f'Cannot set level character below {PlayerCharacter.LEVEL_MIN}')
        elif value > PlayerCharacter.LEVEL_MAX:
            raise ValueError(f'Cannot set a level above {PlayerCharacter.LEVEL_MAX}')
        else:
            self._level = value

    """
    It is also possible to define a property without the @property decoration this is done by explicitly using the 
    Property class.
    
    The property above could also be written as:
    
        def get_level(self):
            print("Getting level...")
            return self._level
        
        def set_level(self, value):
            print("Setting level...")
            if value < PlayerCharacter.LEVEL_MIN:
                raise ValueError(f'Cannot set level character below {PlayerCharacter.LEVEL_MIN}')
            elif value > PlayerCharacter.LEVEL_MAX:
                raise ValueError(f'Cannot set a level above {PlayerCharacter.LEVEL_MAX}')
            else:
                self._level = value
        
        level = property(get_level, set_level)
        
    The accessor methods can even be specified even more explicitly using the .getter(), .setter() and .deleter()
    function of the Property class.
    
    However, the decorator @property reduces overall clutter and makes the code easier to read.
    """


if __name__ == "__main__":

    # Create PlayerCharacter object
    player = PlayerCharacter(name="Conan", level=10)
    print(player.level)

    player.level = 15
    print(player.level)

    # Intentionally try to set level to invalid value
    try:
        player.level = 101
    except ValueError as e:
        print(e)

    """
    Output:
    
    Setting level...
    Getting level...
    10
    Setting level...
    Getting level...
    15
    Setting level...
    Cannot set a level above 100
    """

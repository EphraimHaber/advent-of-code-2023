from location import Location


class SchematicChar:
    _is_number: bool
    _is_dot: bool
    _is_special_symbol: bool
    _value: str
    _location: Location
    _symbol_start: Location
    _symbol_end: Location

    def __init__(self, is_number: bool, is_dot: bool, is_special_symbol: bool, value: str, location: Location,
                 symbol_start: Location, symbol_end: Location):
        self._is_number = is_number
        self._is_dot = is_dot
        self._is_special_symbol = is_special_symbol
        self._value = value
        self._location = location
        self._symbol_start = symbol_start
        self._symbol_end = symbol_end

    @property
    def is_dot(self):
        return self._is_dot

    @property
    def is_special_symbol(self):
        return self._is_special_symbol

    @property
    def location(self):
        return self._location

    @property
    def value(self):
        return self._value

    @property
    def symbol_end(self):
        return self._symbol_end

    @property
    def is_number(self):
        return self._is_number

    @property
    def symbol_start(self):
        return self._symbol_start

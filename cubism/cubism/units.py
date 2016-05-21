# units
from pint import UnitRegistry
units = UnitRegistry()

## units
DEFAULT_UNIT = "mm"

__all__ = ["unit", "inch2mm", "mm2inch"]

def unit(val, **kw):
    _unit = kw.get("unit", DEFAULT_UNIT)
    if _unit != None:
        _unit = units.parse_expression(_unit)
    if type(val) != units.Quantity:
        if type(val) in (int, float):
            assert _unit, "value %r of type '%r' requires a unit definition" % (val, type(val))
            val = val * _unit
        elif type(val) in (str, unicode):
            val = units.parse_expression(val)
        else:
            raise TypeError, "I don't know how to convert type '%s' to a unit" % str(type(val))
    assert type(val) == units.Quantity, "%r != %r" % (type(val), units.Quantity)
    if _unit:
        val = val.to(_unit)
    return val

def inch2mm(inches):
    inches = unit(inches, unit="inch")
    return inches.to(units.mm).magnitude

def mm2inch(mm):
    mm = unit(mm, unit="mm")
    return mm.to(units.inch).magnitude

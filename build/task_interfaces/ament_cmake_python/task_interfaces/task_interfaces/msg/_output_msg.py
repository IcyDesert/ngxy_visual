# generated from rosidl_generator_py/resource/_idl.py.em
# with input from task_interfaces:msg/OutputMsg.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_OutputMsg(type):
    """Metaclass of message 'OutputMsg'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('task_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'task_interfaces.msg.OutputMsg')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__output_msg
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__output_msg
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__output_msg
            cls._TYPE_SUPPORT = module.type_support_msg__msg__output_msg
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__output_msg

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class OutputMsg(metaclass=Metaclass_OutputMsg):
    """Message class 'OutputMsg'."""

    __slots__ = [
        '_x',
        '_vx',
        '_y',
        '_vy',
        '_z',
        '_vz',
        '_theta',
        '_vtheta',
        '_r_offset',
        '_z_offset',
        '_timestamp',
    ]

    _fields_and_field_types = {
        'x': 'double',
        'vx': 'double',
        'y': 'double',
        'vy': 'double',
        'z': 'double',
        'vz': 'double',
        'theta': 'double',
        'vtheta': 'double',
        'r_offset': 'double',
        'z_offset': 'double',
        'timestamp': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.x = kwargs.get('x', float())
        self.vx = kwargs.get('vx', float())
        self.y = kwargs.get('y', float())
        self.vy = kwargs.get('vy', float())
        self.z = kwargs.get('z', float())
        self.vz = kwargs.get('vz', float())
        self.theta = kwargs.get('theta', float())
        self.vtheta = kwargs.get('vtheta', float())
        self.r_offset = kwargs.get('r_offset', float())
        self.z_offset = kwargs.get('z_offset', float())
        self.timestamp = kwargs.get('timestamp', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.x != other.x:
            return False
        if self.vx != other.vx:
            return False
        if self.y != other.y:
            return False
        if self.vy != other.vy:
            return False
        if self.z != other.z:
            return False
        if self.vz != other.vz:
            return False
        if self.theta != other.theta:
            return False
        if self.vtheta != other.vtheta:
            return False
        if self.r_offset != other.r_offset:
            return False
        if self.z_offset != other.z_offset:
            return False
        if self.timestamp != other.timestamp:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def x(self):
        """Message field 'x'."""
        return self._x

    @x.setter
    def x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'x' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._x = value

    @builtins.property
    def vx(self):
        """Message field 'vx'."""
        return self._vx

    @vx.setter
    def vx(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vx' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'vx' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._vx = value

    @builtins.property
    def y(self):
        """Message field 'y'."""
        return self._y

    @y.setter
    def y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'y' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._y = value

    @builtins.property
    def vy(self):
        """Message field 'vy'."""
        return self._vy

    @vy.setter
    def vy(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vy' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'vy' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._vy = value

    @builtins.property
    def z(self):
        """Message field 'z'."""
        return self._z

    @z.setter
    def z(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'z' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'z' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._z = value

    @builtins.property
    def vz(self):
        """Message field 'vz'."""
        return self._vz

    @vz.setter
    def vz(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vz' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'vz' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._vz = value

    @builtins.property
    def theta(self):
        """Message field 'theta'."""
        return self._theta

    @theta.setter
    def theta(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'theta' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'theta' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._theta = value

    @builtins.property
    def vtheta(self):
        """Message field 'vtheta'."""
        return self._vtheta

    @vtheta.setter
    def vtheta(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vtheta' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'vtheta' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._vtheta = value

    @builtins.property
    def r_offset(self):
        """Message field 'r_offset'."""
        return self._r_offset

    @r_offset.setter
    def r_offset(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'r_offset' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'r_offset' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._r_offset = value

    @builtins.property
    def z_offset(self):
        """Message field 'z_offset'."""
        return self._z_offset

    @z_offset.setter
    def z_offset(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'z_offset' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'z_offset' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._z_offset = value

    @builtins.property
    def timestamp(self):
        """Message field 'timestamp'."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'timestamp' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'timestamp' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._timestamp = value

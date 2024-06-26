# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/simulation/simulation_obstacle.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.message import pnc_point_pb2 as common_dot_message_dot_pnc__point__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/message/simulation/simulation_obstacle.proto',
  package='citibot.common.message',
  syntax='proto2',
  serialized_pb=_b('\n3common/message/simulation/simulation_obstacle.proto\x12\x16\x63itibot.common.message\x1a\x1e\x63ommon/message/pnc_point.proto\"\xae\x07\n\x12SimulationObstacle\x12\r\n\x02id\x18\x01 \x01(\x05:\x01\x30\x12\x31\n\x06\x63\x65nter\x18\x02 \x01(\x0b\x32!.citibot.common.message.PathPoint\x12\x10\n\x05width\x18\x03 \x01(\x01:\x01\x30\x12\x11\n\x06length\x18\x04 \x01(\x01:\x01\x30\x12\x10\n\x05speed\x18\x05 \x01(\x01:\x01\x30\x12=\n\x04type\x18\x06 \x01(\x0e\x32/.citibot.common.message.SimulationObstacle.Type\x12\x44\n\x08sub_type\x18\x07 \x01(\x0e\x32\x32.citibot.common.message.SimulationObstacle.SubType\"\xeb\x01\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0fUNKNOWN_MOVABLE\x10\x01\x12\x15\n\x11UNKNOWN_UNMOVABLE\x10\x02\x12\x0e\n\nPEDESTRIAN\x10\x03\x12\x0b\n\x07\x42ICYCLE\x10\x04\x12\x0b\n\x07VEHICLE\x10\x05\x12\x12\n\x0eWARING_THROUGH\x10\x06\x12\x0c\n\x08TOLL_BAR\x10\x07\x12\x11\n\rWARING_UNSAFE\x10\x08\x12\x0c\n\x08PLATFORM\x10\t\x12\r\n\tSUSPENDED\x10\n\x12\x0b\n\x07GARBAGE\x10\x0b\x12\x14\n\x10\x43HARGING_STATION\x10\x0c\x12\x0b\n\x07\x44USTBIN\x10\r\"\xab\x03\n\x07SubType\x12\x0e\n\nST_UNKNOWN\x10\x00\x12\x16\n\x12ST_UNKNOWN_MOVABLE\x10\x01\x12\x18\n\x14ST_UNKNOWN_UNMOVABLE\x10\x02\x12\r\n\tST_PERSON\x10\x03\x12\x0c\n\x08ST_RIDER\x10\x04\x12\x0e\n\nST_CYCLIST\x10\x05\x12\x13\n\x0fST_MOTORCYCLIST\x10\x06\x12\n\n\x06ST_CAR\x10\x07\x12\n\n\x06ST_BUS\x10\x08\x12\x0c\n\x08ST_TRUCK\x10\t\x12\x0c\n\x08ST_TRAIN\x10\n\x12\x13\n\x0fST_TRAFFIC_CONE\x10\x0b\x12\x14\n\x10ST_TRAFFIC_FENCE\x10\x0c\x12\x14\n\x10ST_TRAFFIC_LIGHT\x10\r\x12\x13\n\x0fST_TRAFFIC_SIGN\x10\x0e\x12\x15\n\x11ST_MAN_HOLE_COVER\x10\x0f\x12\x0f\n\x0bST_TOLL_BAR\x10\x10\x12\x0f\n\x0bST_PLATFORM\x10\x11\x12\r\n\tST_LEAVES\x10\x12\x12\x0f\n\x0bST_CONFETTI\x10\x13\x12\x0e\n\nST_PLASTIC\x10\x14\x12\x0b\n\x07ST_CANS\x10\x15\x12\r\n\tST_STONES\x10\x16\x12\r\n\tST_BRICKS\x10\x17\"a\n\x16SimulationObstacleList\x12G\n\x13simulation_obstacle\x18\x01 \x03(\x0b\x32*.citibot.common.message.SimulationObstacle')
  ,
  dependencies=[common_dot_message_dot_pnc__point__pb2.DESCRIPTOR,])



_SIMULATIONOBSTACLE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='citibot.common.message.SimulationObstacle.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_MOVABLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_UNMOVABLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PEDESTRIAN', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BICYCLE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VEHICLE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARING_THROUGH', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOLL_BAR', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARING_UNSAFE', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUSPENDED', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GARBAGE', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARGING_STATION', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUSTBIN', index=13, number=13,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=389,
  serialized_end=624,
)
_sym_db.RegisterEnumDescriptor(_SIMULATIONOBSTACLE_TYPE)

_SIMULATIONOBSTACLE_SUBTYPE = _descriptor.EnumDescriptor(
  name='SubType',
  full_name='citibot.common.message.SimulationObstacle.SubType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ST_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_UNKNOWN_MOVABLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_UNKNOWN_UNMOVABLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_PERSON', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_RIDER', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_CYCLIST', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_MOTORCYCLIST', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_CAR', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_BUS', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_TRUCK', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_TRAIN', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_TRAFFIC_CONE', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_TRAFFIC_FENCE', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_TRAFFIC_LIGHT', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_TRAFFIC_SIGN', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_MAN_HOLE_COVER', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_TOLL_BAR', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_PLATFORM', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_LEAVES', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_CONFETTI', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_PLASTIC', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_CANS', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_STONES', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_BRICKS', index=23, number=23,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=627,
  serialized_end=1054,
)
_sym_db.RegisterEnumDescriptor(_SIMULATIONOBSTACLE_SUBTYPE)


_SIMULATIONOBSTACLE = _descriptor.Descriptor(
  name='SimulationObstacle',
  full_name='citibot.common.message.SimulationObstacle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='citibot.common.message.SimulationObstacle.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='center', full_name='citibot.common.message.SimulationObstacle.center', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='citibot.common.message.SimulationObstacle.width', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='citibot.common.message.SimulationObstacle.length', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed', full_name='citibot.common.message.SimulationObstacle.speed', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='citibot.common.message.SimulationObstacle.type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub_type', full_name='citibot.common.message.SimulationObstacle.sub_type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SIMULATIONOBSTACLE_TYPE,
    _SIMULATIONOBSTACLE_SUBTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=1054,
)


_SIMULATIONOBSTACLELIST = _descriptor.Descriptor(
  name='SimulationObstacleList',
  full_name='citibot.common.message.SimulationObstacleList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='simulation_obstacle', full_name='citibot.common.message.SimulationObstacleList.simulation_obstacle', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1056,
  serialized_end=1153,
)

_SIMULATIONOBSTACLE.fields_by_name['center'].message_type = common_dot_message_dot_pnc__point__pb2._PATHPOINT
_SIMULATIONOBSTACLE.fields_by_name['type'].enum_type = _SIMULATIONOBSTACLE_TYPE
_SIMULATIONOBSTACLE.fields_by_name['sub_type'].enum_type = _SIMULATIONOBSTACLE_SUBTYPE
_SIMULATIONOBSTACLE_TYPE.containing_type = _SIMULATIONOBSTACLE
_SIMULATIONOBSTACLE_SUBTYPE.containing_type = _SIMULATIONOBSTACLE
_SIMULATIONOBSTACLELIST.fields_by_name['simulation_obstacle'].message_type = _SIMULATIONOBSTACLE
DESCRIPTOR.message_types_by_name['SimulationObstacle'] = _SIMULATIONOBSTACLE
DESCRIPTOR.message_types_by_name['SimulationObstacleList'] = _SIMULATIONOBSTACLELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimulationObstacle = _reflection.GeneratedProtocolMessageType('SimulationObstacle', (_message.Message,), dict(
  DESCRIPTOR = _SIMULATIONOBSTACLE,
  __module__ = 'common.message.simulation.simulation_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.SimulationObstacle)
  ))
_sym_db.RegisterMessage(SimulationObstacle)

SimulationObstacleList = _reflection.GeneratedProtocolMessageType('SimulationObstacleList', (_message.Message,), dict(
  DESCRIPTOR = _SIMULATIONOBSTACLELIST,
  __module__ = 'common.message.simulation.simulation_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.SimulationObstacleList)
  ))
_sym_db.RegisterMessage(SimulationObstacleList)


# @@protoc_insertion_point(module_scope)

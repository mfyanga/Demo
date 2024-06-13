# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/scheduler/door_control.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/message/scheduler/door_control.proto',
  package='citibot.common.message',
  syntax='proto2',
  serialized_pb=_b('\n+common/message/scheduler/door_control.proto\x12\x16\x63itibot.common.message\"u\n\x0e\x44oorControlCmd\x12/\n\x07\x64oor_id\x18\x01 \x01(\x0e\x32\x1e.citibot.common.message.DoorID\x12\x32\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\".citibot.common.message.DoorAction\"L\n\x10\x44oorControlProto\x12\x38\n\x08\x64oor_cmd\x18\x01 \x01(\x0b\x32&.citibot.common.message.DoorControlCmd*L\n\x06\x44oorID\x12\x0e\n\nFRONT_DOOR\x10\x01\x12\x0f\n\x0bMIDDLE_DOOR\x10\x02\x12\r\n\tBACK_DOOR\x10\x03\x12\x12\n\x0e\x43\x41RGO_BOX_DOOR\x10\x04*+\n\nDoorAction\x12\x08\n\x04OPEN\x10\x01\x12\t\n\x05\x43LOSE\x10\x02\x12\x08\n\x04STOP\x10\x03')
)

_DOORID = _descriptor.EnumDescriptor(
  name='DoorID',
  full_name='citibot.common.message.DoorID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FRONT_DOOR', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIDDLE_DOOR', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BACK_DOOR', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARGO_BOX_DOOR', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=268,
  serialized_end=344,
)
_sym_db.RegisterEnumDescriptor(_DOORID)

DoorID = enum_type_wrapper.EnumTypeWrapper(_DOORID)
_DOORACTION = _descriptor.EnumDescriptor(
  name='DoorAction',
  full_name='citibot.common.message.DoorAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPEN', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=346,
  serialized_end=389,
)
_sym_db.RegisterEnumDescriptor(_DOORACTION)

DoorAction = enum_type_wrapper.EnumTypeWrapper(_DOORACTION)
FRONT_DOOR = 1
MIDDLE_DOOR = 2
BACK_DOOR = 3
CARGO_BOX_DOOR = 4
OPEN = 1
CLOSE = 2
STOP = 3



_DOORCONTROLCMD = _descriptor.Descriptor(
  name='DoorControlCmd',
  full_name='citibot.common.message.DoorControlCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='door_id', full_name='citibot.common.message.DoorControlCmd.door_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='citibot.common.message.DoorControlCmd.action', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  serialized_start=71,
  serialized_end=188,
)


_DOORCONTROLPROTO = _descriptor.Descriptor(
  name='DoorControlProto',
  full_name='citibot.common.message.DoorControlProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='door_cmd', full_name='citibot.common.message.DoorControlProto.door_cmd', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=190,
  serialized_end=266,
)

_DOORCONTROLCMD.fields_by_name['door_id'].enum_type = _DOORID
_DOORCONTROLCMD.fields_by_name['action'].enum_type = _DOORACTION
_DOORCONTROLPROTO.fields_by_name['door_cmd'].message_type = _DOORCONTROLCMD
DESCRIPTOR.message_types_by_name['DoorControlCmd'] = _DOORCONTROLCMD
DESCRIPTOR.message_types_by_name['DoorControlProto'] = _DOORCONTROLPROTO
DESCRIPTOR.enum_types_by_name['DoorID'] = _DOORID
DESCRIPTOR.enum_types_by_name['DoorAction'] = _DOORACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DoorControlCmd = _reflection.GeneratedProtocolMessageType('DoorControlCmd', (_message.Message,), dict(
  DESCRIPTOR = _DOORCONTROLCMD,
  __module__ = 'common.message.scheduler.door_control_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.DoorControlCmd)
  ))
_sym_db.RegisterMessage(DoorControlCmd)

DoorControlProto = _reflection.GeneratedProtocolMessageType('DoorControlProto', (_message.Message,), dict(
  DESCRIPTOR = _DOORCONTROLPROTO,
  __module__ = 'common.message.scheduler.door_control_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.DoorControlProto)
  ))
_sym_db.RegisterMessage(DoorControlProto)


# @@protoc_insertion_point(module_scope)
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message/scheduler/driving_direction.proto

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
  name='message/scheduler/driving_direction.proto',
  package='citibot.common.message',
  syntax='proto2',
  serialized_pb=_b('\n)message/scheduler/driving_direction.proto\x12\x16\x63itibot.common.message\"g\n\x15\x44rivingDirectionProto\x12N\n\x15\x64riving_direction_cmd\x18\x01 \x01(\x0e\x32/.citibot.common.message.VehicleDrivingDirection*;\n\x17VehicleDrivingDirection\x12\x0f\n\x0b\x44IRECTION_A\x10\x00\x12\x0f\n\x0b\x44IRECTION_B\x10\x01')
)

_VEHICLEDRIVINGDIRECTION = _descriptor.EnumDescriptor(
  name='VehicleDrivingDirection',
  full_name='citibot.common.message.VehicleDrivingDirection',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIRECTION_A', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIRECTION_B', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=174,
  serialized_end=233,
)
_sym_db.RegisterEnumDescriptor(_VEHICLEDRIVINGDIRECTION)

VehicleDrivingDirection = enum_type_wrapper.EnumTypeWrapper(_VEHICLEDRIVINGDIRECTION)
DIRECTION_A = 0
DIRECTION_B = 1



_DRIVINGDIRECTIONPROTO = _descriptor.Descriptor(
  name='DrivingDirectionProto',
  full_name='citibot.common.message.DrivingDirectionProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='driving_direction_cmd', full_name='citibot.common.message.DrivingDirectionProto.driving_direction_cmd', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=69,
  serialized_end=172,
)

_DRIVINGDIRECTIONPROTO.fields_by_name['driving_direction_cmd'].enum_type = _VEHICLEDRIVINGDIRECTION
DESCRIPTOR.message_types_by_name['DrivingDirectionProto'] = _DRIVINGDIRECTIONPROTO
DESCRIPTOR.enum_types_by_name['VehicleDrivingDirection'] = _VEHICLEDRIVINGDIRECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DrivingDirectionProto = _reflection.GeneratedProtocolMessageType('DrivingDirectionProto', (_message.Message,), dict(
  DESCRIPTOR = _DRIVINGDIRECTIONPROTO,
  __module__ = 'message.scheduler.driving_direction_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.DrivingDirectionProto)
  ))
_sym_db.RegisterMessage(DrivingDirectionProto)


# @@protoc_insertion_point(module_scope)

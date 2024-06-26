# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message/error_code.proto

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
  name='message/error_code.proto',
  package='citibot.common',
  syntax='proto2',
  serialized_pb=_b('\n\x18message/error_code.proto\x12\x0e\x63itibot.common\"J\n\x08StatusPb\x12\x31\n\nerror_code\x18\x01 \x01(\x0e\x32\x19.citibot.common.ErrorCode:\x02OK\x12\x0b\n\x03msg\x18\x02 \x01(\t*\xea\x07\n\tErrorCode\x12\x06\n\x02OK\x10\x00\x12\x12\n\rCONTROL_ERROR\x10\xe8\x07\x12\x17\n\x12\x43ONTROL_INIT_ERROR\x10\xe9\x07\x12\x1a\n\x15\x43ONTROL_COMPUTE_ERROR\x10\xea\x07\x12\x11\n\x0c\x43\x41NBUS_ERROR\x10\xd0\x0f\x12\x1a\n\x15\x43\x41N_CLIENT_ERROR_BASE\x10\xb4\x10\x12(\n#CAN_CLIENT_ERROR_OPEN_DEVICE_FAILED\x10\xb5\x10\x12\x1f\n\x1a\x43\x41N_CLIENT_ERROR_FRAME_NUM\x10\xb6\x10\x12!\n\x1c\x43\x41N_CLIENT_ERROR_SEND_FAILED\x10\xb7\x10\x12!\n\x1c\x43\x41N_CLIENT_ERROR_RECV_FAILED\x10\xb8\x10\x12\x17\n\x12LOCALIZATION_ERROR\x10\xb8\x17\x12\x1b\n\x16LOCALIZATION_ERROR_MSG\x10\x9c\x18\x12\x1d\n\x18LOCALIZATION_ERROR_LIDAR\x10\x80\x19\x12\x1d\n\x18LOCALIZATION_ERROR_INTEG\x10\xe4\x19\x12\x1c\n\x17LOCALIZATION_ERROR_GNSS\x10\xc8\x1a\x12\x15\n\x10PERCEPTION_ERROR\x10\xa0\x1f\x12\x18\n\x13PERCEPTION_ERROR_TF\x10\xa1\x1f\x12\x1d\n\x18PERCEPTION_ERROR_PROCESS\x10\xa2\x1f\x12\x15\n\x10PERCEPTION_FATAL\x10\xa3\x1f\x12\x1a\n\x15PERCEPTION_ERROR_NONE\x10\xa4\x1f\x12\x1d\n\x18PERCEPTION_ERROR_UNKNOWN\x10\xa5\x1f\x12\x15\n\x10PREDICTION_ERROR\x10\x88\'\x12\x13\n\x0ePLANNING_ERROR\x10\xf0.\x12\x1d\n\x18PLANNING_ERROR_NOT_READY\x10\xf1.\x12\x15\n\x10HDMAP_DATA_ERROR\x10\xd8\x36\x12\x12\n\rROUTING_ERROR\x10\xc0>\x12\x1a\n\x15ROUTING_ERROR_REQUEST\x10\xc1>\x12\x1b\n\x16ROUTING_ERROR_RESPONSE\x10\xc2>\x12\x1c\n\x17ROUTING_ERROR_NOT_READY\x10\xc3>\x12\x11\n\x0c\x45ND_OF_INPUT\x10\xa8\x46\x12\x15\n\x10HTTP_LOGIC_ERROR\x10\x90N\x12\x17\n\x12HTTP_RUNTIME_ERROR\x10\x91N\x12\x1e\n\x19NAVIGATION_ERROR_RESPONSE\x10\xfaU\x12\x17\n\x12RELATIVE_MAP_ERROR\x10\xf8U\x12\x1b\n\x16RELATIVE_MAP_NOT_READY\x10\xf9U\x12\x16\n\x11\x44RIVER_ERROR_GNSS\x10\xe0]\x12\x1a\n\x15\x44RIVER_ERROR_VELODYNE\x10\xc8\x65')
)

_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='citibot.common.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_ERROR', index=1, number=1000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_INIT_ERROR', index=2, number=1001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_COMPUTE_ERROR', index=3, number=1002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANBUS_ERROR', index=4, number=2000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAN_CLIENT_ERROR_BASE', index=5, number=2100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAN_CLIENT_ERROR_OPEN_DEVICE_FAILED', index=6, number=2101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAN_CLIENT_ERROR_FRAME_NUM', index=7, number=2102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAN_CLIENT_ERROR_SEND_FAILED', index=8, number=2103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAN_CLIENT_ERROR_RECV_FAILED', index=9, number=2104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCALIZATION_ERROR', index=10, number=3000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCALIZATION_ERROR_MSG', index=11, number=3100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCALIZATION_ERROR_LIDAR', index=12, number=3200,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCALIZATION_ERROR_INTEG', index=13, number=3300,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCALIZATION_ERROR_GNSS', index=14, number=3400,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERCEPTION_ERROR', index=15, number=4000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERCEPTION_ERROR_TF', index=16, number=4001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERCEPTION_ERROR_PROCESS', index=17, number=4002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERCEPTION_FATAL', index=18, number=4003,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERCEPTION_ERROR_NONE', index=19, number=4004,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERCEPTION_ERROR_UNKNOWN', index=20, number=4005,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREDICTION_ERROR', index=21, number=5000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLANNING_ERROR', index=22, number=6000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLANNING_ERROR_NOT_READY', index=23, number=6001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HDMAP_DATA_ERROR', index=24, number=7000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTING_ERROR', index=25, number=8000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTING_ERROR_REQUEST', index=26, number=8001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTING_ERROR_RESPONSE', index=27, number=8002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTING_ERROR_NOT_READY', index=28, number=8003,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_OF_INPUT', index=29, number=9000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTTP_LOGIC_ERROR', index=30, number=10000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTTP_RUNTIME_ERROR', index=31, number=10001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAVIGATION_ERROR_RESPONSE', index=32, number=11002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELATIVE_MAP_ERROR', index=33, number=11000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELATIVE_MAP_NOT_READY', index=34, number=11001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRIVER_ERROR_GNSS', index=35, number=12000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRIVER_ERROR_VELODYNE', index=36, number=13000,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=121,
  serialized_end=1123,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODE)

ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
OK = 0
CONTROL_ERROR = 1000
CONTROL_INIT_ERROR = 1001
CONTROL_COMPUTE_ERROR = 1002
CANBUS_ERROR = 2000
CAN_CLIENT_ERROR_BASE = 2100
CAN_CLIENT_ERROR_OPEN_DEVICE_FAILED = 2101
CAN_CLIENT_ERROR_FRAME_NUM = 2102
CAN_CLIENT_ERROR_SEND_FAILED = 2103
CAN_CLIENT_ERROR_RECV_FAILED = 2104
LOCALIZATION_ERROR = 3000
LOCALIZATION_ERROR_MSG = 3100
LOCALIZATION_ERROR_LIDAR = 3200
LOCALIZATION_ERROR_INTEG = 3300
LOCALIZATION_ERROR_GNSS = 3400
PERCEPTION_ERROR = 4000
PERCEPTION_ERROR_TF = 4001
PERCEPTION_ERROR_PROCESS = 4002
PERCEPTION_FATAL = 4003
PERCEPTION_ERROR_NONE = 4004
PERCEPTION_ERROR_UNKNOWN = 4005
PREDICTION_ERROR = 5000
PLANNING_ERROR = 6000
PLANNING_ERROR_NOT_READY = 6001
HDMAP_DATA_ERROR = 7000
ROUTING_ERROR = 8000
ROUTING_ERROR_REQUEST = 8001
ROUTING_ERROR_RESPONSE = 8002
ROUTING_ERROR_NOT_READY = 8003
END_OF_INPUT = 9000
HTTP_LOGIC_ERROR = 10000
HTTP_RUNTIME_ERROR = 10001
NAVIGATION_ERROR_RESPONSE = 11002
RELATIVE_MAP_ERROR = 11000
RELATIVE_MAP_NOT_READY = 11001
DRIVER_ERROR_GNSS = 12000
DRIVER_ERROR_VELODYNE = 13000



_STATUSPB = _descriptor.Descriptor(
  name='StatusPb',
  full_name='citibot.common.StatusPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='citibot.common.StatusPb.error_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='citibot.common.StatusPb.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=44,
  serialized_end=118,
)

_STATUSPB.fields_by_name['error_code'].enum_type = _ERRORCODE
DESCRIPTOR.message_types_by_name['StatusPb'] = _STATUSPB
DESCRIPTOR.enum_types_by_name['ErrorCode'] = _ERRORCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatusPb = _reflection.GeneratedProtocolMessageType('StatusPb', (_message.Message,), dict(
  DESCRIPTOR = _STATUSPB,
  __module__ = 'message.error_code_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.StatusPb)
  ))
_sym_db.RegisterMessage(StatusPb)


# @@protoc_insertion_point(module_scope)

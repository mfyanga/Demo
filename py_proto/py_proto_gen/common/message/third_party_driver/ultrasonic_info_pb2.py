# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/third_party_driver/ultrasonic_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.message import header_pb2 as common_dot_message_dot_header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/message/third_party_driver/ultrasonic_info.proto',
  package='citibot.common.message',
  syntax='proto2',
  serialized_pb=_b('\n7common/message/third_party_driver/ultrasonic_info.proto\x12\x16\x63itibot.common.message\x1a\x1b\x63ommon/message/header.proto\"T\n\x0eUltrasonicInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08\x64istance\x18\x02 \x01(\x02\x12\x11\n\trange_max\x18\x03 \x01(\x02\x12\x11\n\trange_min\x18\x04 \x01(\x02\"\x81\x01\n\rUltrasonicMsg\x12.\n\x06header\x18\x01 \x01(\x0b\x32\x1e.citibot.common.message.Header\x12@\n\x10ultrasonic_infos\x18\x02 \x03(\x0b\x32&.citibot.common.message.UltrasonicInfo')
  ,
  dependencies=[common_dot_message_dot_header__pb2.DESCRIPTOR,])




_ULTRASONICINFO = _descriptor.Descriptor(
  name='UltrasonicInfo',
  full_name='citibot.common.message.UltrasonicInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='citibot.common.message.UltrasonicInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance', full_name='citibot.common.message.UltrasonicInfo.distance', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range_max', full_name='citibot.common.message.UltrasonicInfo.range_max', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range_min', full_name='citibot.common.message.UltrasonicInfo.range_min', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=112,
  serialized_end=196,
)


_ULTRASONICMSG = _descriptor.Descriptor(
  name='UltrasonicMsg',
  full_name='citibot.common.message.UltrasonicMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='citibot.common.message.UltrasonicMsg.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ultrasonic_infos', full_name='citibot.common.message.UltrasonicMsg.ultrasonic_infos', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=199,
  serialized_end=328,
)

_ULTRASONICMSG.fields_by_name['header'].message_type = common_dot_message_dot_header__pb2._HEADER
_ULTRASONICMSG.fields_by_name['ultrasonic_infos'].message_type = _ULTRASONICINFO
DESCRIPTOR.message_types_by_name['UltrasonicInfo'] = _ULTRASONICINFO
DESCRIPTOR.message_types_by_name['UltrasonicMsg'] = _ULTRASONICMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UltrasonicInfo = _reflection.GeneratedProtocolMessageType('UltrasonicInfo', (_message.Message,), dict(
  DESCRIPTOR = _ULTRASONICINFO,
  __module__ = 'common.message.third_party_driver.ultrasonic_info_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.UltrasonicInfo)
  ))
_sym_db.RegisterMessage(UltrasonicInfo)

UltrasonicMsg = _reflection.GeneratedProtocolMessageType('UltrasonicMsg', (_message.Message,), dict(
  DESCRIPTOR = _ULTRASONICMSG,
  __module__ = 'common.message.third_party_driver.ultrasonic_info_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.UltrasonicMsg)
  ))
_sym_db.RegisterMessage(UltrasonicMsg)


# @@protoc_insertion_point(module_scope)

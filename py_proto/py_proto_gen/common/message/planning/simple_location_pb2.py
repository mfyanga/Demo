# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/planning/simple_location.proto

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
  name='common/message/planning/simple_location.proto',
  package='citibot.common.message',
  syntax='proto2',
  serialized_pb=_b('\n-common/message/planning/simple_location.proto\x12\x16\x63itibot.common.message\x1a\x1b\x63ommon/message/header.proto\"\x95\x01\n\x0eSimpleLocation\x12.\n\x06header\x18\x01 \x01(\x0b\x32\x1e.citibot.common.message.Header\x12\x0c\n\x01x\x18\x02 \x01(\x01:\x01\x30\x12\x0c\n\x01y\x18\x03 \x01(\x01:\x01\x30\x12\x0c\n\x01z\x18\x04 \x01(\x01:\x01\x30\x12\x10\n\x05theta\x18\x05 \x01(\x01:\x01\x30\x12\x17\n\x08is_valid\x18\x06 \x01(\x08:\x05\x66\x61lse')
  ,
  dependencies=[common_dot_message_dot_header__pb2.DESCRIPTOR,])




_SIMPLELOCATION = _descriptor.Descriptor(
  name='SimpleLocation',
  full_name='citibot.common.message.SimpleLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='citibot.common.message.SimpleLocation.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='citibot.common.message.SimpleLocation.x', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='citibot.common.message.SimpleLocation.y', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='citibot.common.message.SimpleLocation.z', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='theta', full_name='citibot.common.message.SimpleLocation.theta', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_valid', full_name='citibot.common.message.SimpleLocation.is_valid', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=103,
  serialized_end=252,
)

_SIMPLELOCATION.fields_by_name['header'].message_type = common_dot_message_dot_header__pb2._HEADER
DESCRIPTOR.message_types_by_name['SimpleLocation'] = _SIMPLELOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleLocation = _reflection.GeneratedProtocolMessageType('SimpleLocation', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLELOCATION,
  __module__ = 'common.message.planning.simple_location_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.SimpleLocation)
  ))
_sym_db.RegisterMessage(SimpleLocation)


# @@protoc_insertion_point(module_scope)

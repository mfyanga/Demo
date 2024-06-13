# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message/header.proto

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
  name='message/header.proto',
  package='citibot.common.message',
  syntax='proto2',
  serialized_pb=_b('\n\x14message/header.proto\x12\x16\x63itibot.common.message\"\xd7\x01\n\x06Header\x12\x14\n\ttimestamp\x18\x01 \x01(\x04:\x01\x30\x12\x1d\n\x12measured_timestamp\x18\x02 \x01(\x04:\x01\x30\x12\x17\n\x0csequence_num\x18\x03 \x01(\x04:\x01\x30\x12\x46\n\nmsg_status\x18\x04 \x01(\x0e\x32!.citibot.common.message.MsgStatus:\x0fMSG_STATUS_INIT\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x11\n\x06source\x18\x07 \x01(\r:\x01\x30*f\n\tMsgStatus\x12\x13\n\x0fMSG_STATUS_INIT\x10\x00\x12\x14\n\x10MSG_STATUS_SLEEP\x10\x01\x12\x15\n\x11MSG_STATUS_NORMAL\x10\x02\x12\x17\n\x13MSG_STATUS_ABNORMAL\x10\x03')
)

_MSGSTATUS = _descriptor.EnumDescriptor(
  name='MsgStatus',
  full_name='citibot.common.message.MsgStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MSG_STATUS_INIT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSG_STATUS_SLEEP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSG_STATUS_NORMAL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSG_STATUS_ABNORMAL', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=266,
  serialized_end=368,
)
_sym_db.RegisterEnumDescriptor(_MSGSTATUS)

MsgStatus = enum_type_wrapper.EnumTypeWrapper(_MSGSTATUS)
MSG_STATUS_INIT = 0
MSG_STATUS_SLEEP = 1
MSG_STATUS_NORMAL = 2
MSG_STATUS_ABNORMAL = 3



_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='citibot.common.message.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='citibot.common.message.Header.timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='measured_timestamp', full_name='citibot.common.message.Header.measured_timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequence_num', full_name='citibot.common.message.Header.sequence_num', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_status', full_name='citibot.common.message.Header.msg_status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='citibot.common.message.Header.version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='citibot.common.message.Header.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='citibot.common.message.Header.source', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=49,
  serialized_end=264,
)

_HEADER.fields_by_name['msg_status'].enum_type = _MSGSTATUS
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.enum_types_by_name['MsgStatus'] = _MSGSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'message.header_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.Header)
  ))
_sym_db.RegisterMessage(Header)


# @@protoc_insertion_point(module_scope)

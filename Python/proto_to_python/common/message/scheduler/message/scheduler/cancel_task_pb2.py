# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message/scheduler/cancel_task.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message/scheduler/cancel_task.proto',
  package='citibot.common.message',
  syntax='proto2',
  serialized_pb=_b('\n#message/scheduler/cancel_task.proto\x12\x16\x63itibot.common.message\".\n\x0f\x43\x61ncelTaskProto\x12\r\n\x05token\x18\x01 \x01(\x04\x12\x0c\n\x04type\x18\x02 \x01(\r')
)




_CANCELTASKPROTO = _descriptor.Descriptor(
  name='CancelTaskProto',
  full_name='citibot.common.message.CancelTaskProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='citibot.common.message.CancelTaskProto.token', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='citibot.common.message.CancelTaskProto.type', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=63,
  serialized_end=109,
)

DESCRIPTOR.message_types_by_name['CancelTaskProto'] = _CANCELTASKPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CancelTaskProto = _reflection.GeneratedProtocolMessageType('CancelTaskProto', (_message.Message,), dict(
  DESCRIPTOR = _CANCELTASKPROTO,
  __module__ = 'message.scheduler.cancel_task_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.CancelTaskProto)
  ))
_sym_db.RegisterMessage(CancelTaskProto)


# @@protoc_insertion_point(module_scope)
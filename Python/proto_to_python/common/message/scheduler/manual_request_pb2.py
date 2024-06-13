# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/scheduler/manual_request.proto

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
  name='common/message/scheduler/manual_request.proto',
  package='citibot.common.message',
  syntax='proto2',
  serialized_pb=_b('\n-common/message/scheduler/manual_request.proto\x12\x16\x63itibot.common.message\"\xc0\x01\n\x12ManualRequestProto\x12J\n\x04type\x18\x01 \x01(\x0e\x32<.citibot.common.message.ManualRequestProto.ManualRequestType\"^\n\x11ManualRequestType\x12\x0f\n\x0b\x43HANGE_LEFT\x10\x00\x12\x10\n\x0c\x43HANGE_RIGHT\x10\x01\x12\x11\n\rPULLOVER_STOP\x10\x02\x12\t\n\x05START\x10\x03\x12\x08\n\x04STOP\x10\x04')
)



_MANUALREQUESTPROTO_MANUALREQUESTTYPE = _descriptor.EnumDescriptor(
  name='ManualRequestType',
  full_name='citibot.common.message.ManualRequestProto.ManualRequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHANGE_LEFT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANGE_RIGHT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PULLOVER_STOP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=172,
  serialized_end=266,
)
_sym_db.RegisterEnumDescriptor(_MANUALREQUESTPROTO_MANUALREQUESTTYPE)


_MANUALREQUESTPROTO = _descriptor.Descriptor(
  name='ManualRequestProto',
  full_name='citibot.common.message.ManualRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='citibot.common.message.ManualRequestProto.type', index=0,
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
    _MANUALREQUESTPROTO_MANUALREQUESTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=266,
)

_MANUALREQUESTPROTO.fields_by_name['type'].enum_type = _MANUALREQUESTPROTO_MANUALREQUESTTYPE
_MANUALREQUESTPROTO_MANUALREQUESTTYPE.containing_type = _MANUALREQUESTPROTO
DESCRIPTOR.message_types_by_name['ManualRequestProto'] = _MANUALREQUESTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ManualRequestProto = _reflection.GeneratedProtocolMessageType('ManualRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _MANUALREQUESTPROTO,
  __module__ = 'common.message.scheduler.manual_request_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.ManualRequestProto)
  ))
_sym_db.RegisterMessage(ManualRequestProto)


# @@protoc_insertion_point(module_scope)
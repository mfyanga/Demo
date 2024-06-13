# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message/scheduler/scheduler_decision.proto

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
  name='message/scheduler/scheduler_decision.proto',
  package='citibot.common.message',
  syntax='proto2',
  serialized_pb=_b('\n*message/scheduler/scheduler_decision.proto\x12\x16\x63itibot.common.message\"\xd0\x01\n\x16SchedulerDecisionProto\x12R\n\x04type\x18\x01 \x01(\x0e\x32\x44.citibot.common.message.SchedulerDecisionProto.SchedulerDecisionType\"b\n\x15SchedulerDecisionType\x12\x0f\n\x0b\x43HANGE_LEFT\x10\x00\x12\x10\n\x0c\x43HANGE_RIGHT\x10\x01\x12\x11\n\rPULLOVER_STOP\x10\x02\x12\t\n\x05START\x10\x03\x12\x08\n\x04STOP\x10\x04')
)



_SCHEDULERDECISIONPROTO_SCHEDULERDECISIONTYPE = _descriptor.EnumDescriptor(
  name='SchedulerDecisionType',
  full_name='citibot.common.message.SchedulerDecisionProto.SchedulerDecisionType',
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
  serialized_start=181,
  serialized_end=279,
)
_sym_db.RegisterEnumDescriptor(_SCHEDULERDECISIONPROTO_SCHEDULERDECISIONTYPE)


_SCHEDULERDECISIONPROTO = _descriptor.Descriptor(
  name='SchedulerDecisionProto',
  full_name='citibot.common.message.SchedulerDecisionProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='citibot.common.message.SchedulerDecisionProto.type', index=0,
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
    _SCHEDULERDECISIONPROTO_SCHEDULERDECISIONTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=279,
)

_SCHEDULERDECISIONPROTO.fields_by_name['type'].enum_type = _SCHEDULERDECISIONPROTO_SCHEDULERDECISIONTYPE
_SCHEDULERDECISIONPROTO_SCHEDULERDECISIONTYPE.containing_type = _SCHEDULERDECISIONPROTO
DESCRIPTOR.message_types_by_name['SchedulerDecisionProto'] = _SCHEDULERDECISIONPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SchedulerDecisionProto = _reflection.GeneratedProtocolMessageType('SchedulerDecisionProto', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULERDECISIONPROTO,
  __module__ = 'message.scheduler.scheduler_decision_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.SchedulerDecisionProto)
  ))
_sym_db.RegisterMessage(SchedulerDecisionProto)


# @@protoc_insertion_point(module_scope)
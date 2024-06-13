# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/scheduler/scheduler_signal.proto

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
  name='common/message/scheduler/scheduler_signal.proto',
  package='citibot.common.message',
  syntax='proto2',
  serialized_pb=_b('\n/common/message/scheduler/scheduler_signal.proto\x12\x16\x63itibot.common.message\"\xeb\x01\n\x0cTrafficLight\x12\x39\n\x05\x63olor\x18\x01 \x01(\x0e\x32*.citibot.common.message.TrafficLight.Color\x12\n\n\x02id\x18\x02 \x01(\t\x12\x15\n\nconfidence\x18\x03 \x01(\x01:\x01\x31\x12\x15\n\rtracking_time\x18\x04 \x01(\x01\x12\r\n\x05\x62link\x18\x05 \x01(\x08\x12\x16\n\x0eremaining_time\x18\x06 \x01(\x01\"?\n\x05\x43olor\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03RED\x10\x01\x12\n\n\x06YELLOW\x10\x02\x12\t\n\x05GREEN\x10\x03\x12\t\n\x05\x42LACK\x10\x04\"S\n\x14SchedulerSignalProto\x12;\n\rtraffic_light\x18\x01 \x01(\x0b\x32$.citibot.common.message.TrafficLight')
)



_TRAFFICLIGHT_COLOR = _descriptor.EnumDescriptor(
  name='Color',
  full_name='citibot.common.message.TrafficLight.Color',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YELLOW', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREEN', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLACK', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=248,
  serialized_end=311,
)
_sym_db.RegisterEnumDescriptor(_TRAFFICLIGHT_COLOR)


_TRAFFICLIGHT = _descriptor.Descriptor(
  name='TrafficLight',
  full_name='citibot.common.message.TrafficLight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='color', full_name='citibot.common.message.TrafficLight.color', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='citibot.common.message.TrafficLight.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='citibot.common.message.TrafficLight.confidence', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tracking_time', full_name='citibot.common.message.TrafficLight.tracking_time', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blink', full_name='citibot.common.message.TrafficLight.blink', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remaining_time', full_name='citibot.common.message.TrafficLight.remaining_time', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRAFFICLIGHT_COLOR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=311,
)


_SCHEDULERSIGNALPROTO = _descriptor.Descriptor(
  name='SchedulerSignalProto',
  full_name='citibot.common.message.SchedulerSignalProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='traffic_light', full_name='citibot.common.message.SchedulerSignalProto.traffic_light', index=0,
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
  serialized_start=313,
  serialized_end=396,
)

_TRAFFICLIGHT.fields_by_name['color'].enum_type = _TRAFFICLIGHT_COLOR
_TRAFFICLIGHT_COLOR.containing_type = _TRAFFICLIGHT
_SCHEDULERSIGNALPROTO.fields_by_name['traffic_light'].message_type = _TRAFFICLIGHT
DESCRIPTOR.message_types_by_name['TrafficLight'] = _TRAFFICLIGHT
DESCRIPTOR.message_types_by_name['SchedulerSignalProto'] = _SCHEDULERSIGNALPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrafficLight = _reflection.GeneratedProtocolMessageType('TrafficLight', (_message.Message,), dict(
  DESCRIPTOR = _TRAFFICLIGHT,
  __module__ = 'common.message.scheduler.scheduler_signal_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.TrafficLight)
  ))
_sym_db.RegisterMessage(TrafficLight)

SchedulerSignalProto = _reflection.GeneratedProtocolMessageType('SchedulerSignalProto', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULERSIGNALPROTO,
  __module__ = 'common.message.scheduler.scheduler_signal_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.SchedulerSignalProto)
  ))
_sym_db.RegisterMessage(SchedulerSignalProto)


# @@protoc_insertion_point(module_scope)

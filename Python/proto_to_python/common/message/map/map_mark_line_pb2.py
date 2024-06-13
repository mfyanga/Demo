# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/map/map_mark_line.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.message import geometry_pb2 as common_dot_message_dot_geometry__pb2
from common.message.map import map_id_pb2 as common_dot_message_dot_map_dot_map__id__pb2
from common.message.map import map_geometry_pb2 as common_dot_message_dot_map_dot_map__geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/message/map/map_mark_line.proto',
  package='citibot.common.hdmap',
  syntax='proto2',
  serialized_pb=_b('\n&common/message/map/map_mark_line.proto\x12\x14\x63itibot.common.hdmap\x1a\x1d\x63ommon/message/geometry.proto\x1a\x1f\x63ommon/message/map/map_id.proto\x1a%common/message/map/map_geometry.proto\"\xa3\x02\n\x08MarkLine\x12$\n\x02id\x18\x01 \x01(\x0b\x32\x18.citibot.common.hdmap.Id\x12,\n\noverlap_id\x18\x02 \x03(\x0b\x32\x18.citibot.common.hdmap.Id\x12)\n\x04line\x18\x03 \x03(\x0b\x32\x1b.citibot.common.hdmap.Curve\x12\x31\n\x04type\x18\x04 \x01(\x0e\x32#.citibot.common.hdmap.MarkLine.Type\x12*\n\x04size\x18\x05 \x01(\x0b\x32\x1c.citibot.common.message.Size\"9\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07\x42\x41RRIER\x10\x01\x12\n\n\x06GANTRY\x10\x02\x12\x0b\n\x07QUEUING\x10\x03')
  ,
  dependencies=[common_dot_message_dot_geometry__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__id__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__geometry__pb2.DESCRIPTOR,])



_MARKLINE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='citibot.common.hdmap.MarkLine.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BARRIER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GANTRY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEUING', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=402,
  serialized_end=459,
)
_sym_db.RegisterEnumDescriptor(_MARKLINE_TYPE)


_MARKLINE = _descriptor.Descriptor(
  name='MarkLine',
  full_name='citibot.common.hdmap.MarkLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='citibot.common.hdmap.MarkLine.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='overlap_id', full_name='citibot.common.hdmap.MarkLine.overlap_id', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line', full_name='citibot.common.hdmap.MarkLine.line', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='citibot.common.hdmap.MarkLine.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='citibot.common.hdmap.MarkLine.size', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MARKLINE_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=459,
)

_MARKLINE.fields_by_name['id'].message_type = common_dot_message_dot_map_dot_map__id__pb2._ID
_MARKLINE.fields_by_name['overlap_id'].message_type = common_dot_message_dot_map_dot_map__id__pb2._ID
_MARKLINE.fields_by_name['line'].message_type = common_dot_message_dot_map_dot_map__geometry__pb2._CURVE
_MARKLINE.fields_by_name['type'].enum_type = _MARKLINE_TYPE
_MARKLINE.fields_by_name['size'].message_type = common_dot_message_dot_geometry__pb2._SIZE
_MARKLINE_TYPE.containing_type = _MARKLINE
DESCRIPTOR.message_types_by_name['MarkLine'] = _MARKLINE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MarkLine = _reflection.GeneratedProtocolMessageType('MarkLine', (_message.Message,), dict(
  DESCRIPTOR = _MARKLINE,
  __module__ = 'common.message.map.map_mark_line_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.hdmap.MarkLine)
  ))
_sym_db.RegisterMessage(MarkLine)


# @@protoc_insertion_point(module_scope)
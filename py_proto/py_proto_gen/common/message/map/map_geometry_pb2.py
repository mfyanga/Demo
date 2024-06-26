# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/map/map_geometry.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/message/map/map_geometry.proto',
  package='citibot.common.hdmap',
  syntax='proto2',
  serialized_pb=_b('\n%common/message/map/map_geometry.proto\x12\x14\x63itibot.common.hdmap\x1a\x1d\x63ommon/message/geometry.proto\":\n\x07Polygon\x12/\n\x05point\x18\x01 \x03(\x0b\x32 .citibot.common.message.PointENU\">\n\x0bLineSegment\x12/\n\x05point\x18\x01 \x03(\x0b\x32 .citibot.common.message.PointENU\"\x89\x02\n\x0c\x43urveSegment\x12\x39\n\x0cline_segment\x18\x01 \x01(\x0b\x32!.citibot.common.hdmap.LineSegmentH\x00\x12\t\n\x01s\x18\x06 \x01(\x01\x12\x38\n\x0estart_position\x18\x07 \x01(\x0b\x32 .citibot.common.message.PointENU\x12\x0f\n\x07heading\x18\x08 \x01(\x01\x12\x0e\n\x06length\x18\t \x01(\x01\x12\n\n\x02\x63\x30\x18\x14 \x01(\x01\x12\n\n\x02\x63\x31\x18\x15 \x01(\x01\x12\n\n\x02\x63\x32\x18\x16 \x01(\x01\x12\n\n\x02\x63\x33\x18\x17 \x01(\x01\x12\r\n\x05start\x18\x18 \x01(\x01\x12\x0b\n\x03\x65nd\x18\x19 \x01(\x01\x42\x0c\n\ncurve_type\"<\n\x05\x43urve\x12\x33\n\x07segment\x18\x01 \x03(\x0b\x32\".citibot.common.hdmap.CurveSegment')
  ,
  dependencies=[common_dot_message_dot_geometry__pb2.DESCRIPTOR,])




_POLYGON = _descriptor.Descriptor(
  name='Polygon',
  full_name='citibot.common.hdmap.Polygon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='citibot.common.hdmap.Polygon.point', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=94,
  serialized_end=152,
)


_LINESEGMENT = _descriptor.Descriptor(
  name='LineSegment',
  full_name='citibot.common.hdmap.LineSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='citibot.common.hdmap.LineSegment.point', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=154,
  serialized_end=216,
)


_CURVESEGMENT = _descriptor.Descriptor(
  name='CurveSegment',
  full_name='citibot.common.hdmap.CurveSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='line_segment', full_name='citibot.common.hdmap.CurveSegment.line_segment', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='s', full_name='citibot.common.hdmap.CurveSegment.s', index=1,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_position', full_name='citibot.common.hdmap.CurveSegment.start_position', index=2,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heading', full_name='citibot.common.hdmap.CurveSegment.heading', index=3,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='citibot.common.hdmap.CurveSegment.length', index=4,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c0', full_name='citibot.common.hdmap.CurveSegment.c0', index=5,
      number=20, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c1', full_name='citibot.common.hdmap.CurveSegment.c1', index=6,
      number=21, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c2', full_name='citibot.common.hdmap.CurveSegment.c2', index=7,
      number=22, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c3', full_name='citibot.common.hdmap.CurveSegment.c3', index=8,
      number=23, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='citibot.common.hdmap.CurveSegment.start', index=9,
      number=24, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='citibot.common.hdmap.CurveSegment.end', index=10,
      number=25, type=1, cpp_type=5, label=1,
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
    _descriptor.OneofDescriptor(
      name='curve_type', full_name='citibot.common.hdmap.CurveSegment.curve_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=219,
  serialized_end=484,
)


_CURVE = _descriptor.Descriptor(
  name='Curve',
  full_name='citibot.common.hdmap.Curve',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='segment', full_name='citibot.common.hdmap.Curve.segment', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=486,
  serialized_end=546,
)

_POLYGON.fields_by_name['point'].message_type = common_dot_message_dot_geometry__pb2._POINTENU
_LINESEGMENT.fields_by_name['point'].message_type = common_dot_message_dot_geometry__pb2._POINTENU
_CURVESEGMENT.fields_by_name['line_segment'].message_type = _LINESEGMENT
_CURVESEGMENT.fields_by_name['start_position'].message_type = common_dot_message_dot_geometry__pb2._POINTENU
_CURVESEGMENT.oneofs_by_name['curve_type'].fields.append(
  _CURVESEGMENT.fields_by_name['line_segment'])
_CURVESEGMENT.fields_by_name['line_segment'].containing_oneof = _CURVESEGMENT.oneofs_by_name['curve_type']
_CURVE.fields_by_name['segment'].message_type = _CURVESEGMENT
DESCRIPTOR.message_types_by_name['Polygon'] = _POLYGON
DESCRIPTOR.message_types_by_name['LineSegment'] = _LINESEGMENT
DESCRIPTOR.message_types_by_name['CurveSegment'] = _CURVESEGMENT
DESCRIPTOR.message_types_by_name['Curve'] = _CURVE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Polygon = _reflection.GeneratedProtocolMessageType('Polygon', (_message.Message,), dict(
  DESCRIPTOR = _POLYGON,
  __module__ = 'common.message.map.map_geometry_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.hdmap.Polygon)
  ))
_sym_db.RegisterMessage(Polygon)

LineSegment = _reflection.GeneratedProtocolMessageType('LineSegment', (_message.Message,), dict(
  DESCRIPTOR = _LINESEGMENT,
  __module__ = 'common.message.map.map_geometry_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.hdmap.LineSegment)
  ))
_sym_db.RegisterMessage(LineSegment)

CurveSegment = _reflection.GeneratedProtocolMessageType('CurveSegment', (_message.Message,), dict(
  DESCRIPTOR = _CURVESEGMENT,
  __module__ = 'common.message.map.map_geometry_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.hdmap.CurveSegment)
  ))
_sym_db.RegisterMessage(CurveSegment)

Curve = _reflection.GeneratedProtocolMessageType('Curve', (_message.Message,), dict(
  DESCRIPTOR = _CURVE,
  __module__ = 'common.message.map.map_geometry_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.hdmap.Curve)
  ))
_sym_db.RegisterMessage(Curve)


# @@protoc_insertion_point(module_scope)

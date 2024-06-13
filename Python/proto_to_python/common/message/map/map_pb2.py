# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/map/map.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.message.map import map_clear_area_pb2 as common_dot_message_dot_map_dot_map__clear__area__pb2
from common.message.map import map_crosswalk_pb2 as common_dot_message_dot_map_dot_map__crosswalk__pb2
from common.message.map import map_junction_pb2 as common_dot_message_dot_map_dot_map__junction__pb2
from common.message.map import map_lane_pb2 as common_dot_message_dot_map_dot_map__lane__pb2
from common.message.map import map_overlap_pb2 as common_dot_message_dot_map_dot_map__overlap__pb2
from common.message.map import map_signal_pb2 as common_dot_message_dot_map_dot_map__signal__pb2
from common.message.map import map_speed_bump_pb2 as common_dot_message_dot_map_dot_map__speed__bump__pb2
from common.message.map import map_stop_sign_pb2 as common_dot_message_dot_map_dot_map__stop__sign__pb2
from common.message.map import map_yield_sign_pb2 as common_dot_message_dot_map_dot_map__yield__sign__pb2
from common.message.map import map_road_pb2 as common_dot_message_dot_map_dot_map__road__pb2
from common.message.map import map_parking_space_pb2 as common_dot_message_dot_map_dot_map__parking__space__pb2
from common.message.map import map_pnc_junction_pb2 as common_dot_message_dot_map_dot_map__pnc__junction__pb2
from common.message.map import map_mark_point_pb2 as common_dot_message_dot_map_dot_map__mark__point__pb2
from common.message.map import map_remark_pb2 as common_dot_message_dot_map_dot_map__remark__pb2
from common.message.map import map_mark_polygon_pb2 as common_dot_message_dot_map_dot_map__mark__polygon__pb2
from common.message.map import map_mark_line_pb2 as common_dot_message_dot_map_dot_map__mark__line__pb2
from common.message.map import map_station_pb2 as common_dot_message_dot_map_dot_map__station__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/message/map/map.proto',
  package='citibot.common.hdmap',
  syntax='proto2',
  serialized_pb=_b('\n\x1c\x63ommon/message/map/map.proto\x12\x14\x63itibot.common.hdmap\x1a\'common/message/map/map_clear_area.proto\x1a&common/message/map/map_crosswalk.proto\x1a%common/message/map/map_junction.proto\x1a!common/message/map/map_lane.proto\x1a$common/message/map/map_overlap.proto\x1a#common/message/map/map_signal.proto\x1a\'common/message/map/map_speed_bump.proto\x1a&common/message/map/map_stop_sign.proto\x1a\'common/message/map/map_yield_sign.proto\x1a!common/message/map/map_road.proto\x1a*common/message/map/map_parking_space.proto\x1a)common/message/map/map_pnc_junction.proto\x1a\'common/message/map/map_mark_point.proto\x1a#common/message/map/map_remark.proto\x1a)common/message/map/map_mark_polygon.proto\x1a&common/message/map/map_mark_line.proto\x1a$common/message/map/map_station.proto\"\x1a\n\nProjection\x12\x0c\n\x04proj\x18\x01 \x01(\t\"6\n\x06Offset\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\x0b\n\x03hdg\x18\x04 \x01(\x01\"\xaf\x02\n\x06Header\x12\x0f\n\x07version\x18\x01 \x01(\x0c\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\x0c\x12\x34\n\nprojection\x18\x03 \x01(\x0b\x32 .citibot.common.hdmap.Projection\x12\x10\n\x08\x64istrict\x18\x04 \x01(\x0c\x12\x12\n\ngeneration\x18\x05 \x01(\x0c\x12\x11\n\trev_major\x18\x06 \x01(\x0c\x12\x11\n\trev_minor\x18\x07 \x01(\x0c\x12\x0c\n\x04left\x18\x08 \x01(\x01\x12\x0b\n\x03top\x18\t \x01(\x01\x12\r\n\x05right\x18\n \x01(\x01\x12\x0e\n\x06\x62ottom\x18\x0b \x01(\x01\x12\x0e\n\x06vendor\x18\x0c \x01(\x0c\x12,\n\x06offset\x18\x15 \x01(\x0b\x32\x1c.citibot.common.hdmap.Offset\x12\x0c\n\x04name\x18\x16 \x01(\x0c\"\x8b\x07\n\x03Map\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.citibot.common.hdmap.Header\x12\x32\n\tcrosswalk\x18\x02 \x03(\x0b\x32\x1f.citibot.common.hdmap.Crosswalk\x12\x30\n\x08junction\x18\x03 \x03(\x0b\x32\x1e.citibot.common.hdmap.Junction\x12(\n\x04lane\x18\x04 \x03(\x0b\x32\x1a.citibot.common.hdmap.Lane\x12\x31\n\tstop_sign\x18\x05 \x03(\x0b\x32\x1e.citibot.common.hdmap.StopSign\x12,\n\x06signal\x18\x06 \x03(\x0b\x32\x1c.citibot.common.hdmap.Signal\x12.\n\x05yield\x18\x07 \x03(\x0b\x32\x1f.citibot.common.hdmap.YieldSign\x12.\n\x07overlap\x18\x08 \x03(\x0b\x32\x1d.citibot.common.hdmap.Overlap\x12\x33\n\nclear_area\x18\t \x03(\x0b\x32\x1f.citibot.common.hdmap.ClearArea\x12\x33\n\nspeed_bump\x18\n \x03(\x0b\x32\x1f.citibot.common.hdmap.SpeedBump\x12(\n\x04road\x18\x0b \x03(\x0b\x32\x1a.citibot.common.hdmap.Road\x12\x39\n\rparking_space\x18\x0c \x03(\x0b\x32\".citibot.common.hdmap.ParkingSpace\x12\x37\n\x0cpnc_junction\x18\r \x03(\x0b\x32!.citibot.common.hdmap.PNCJunction\x12\x33\n\nmark_point\x18\x15 \x03(\x0b\x32\x1f.citibot.common.hdmap.MarkPoint\x12,\n\x06remark\x18\x16 \x03(\x0b\x32\x1c.citibot.common.hdmap.Remark\x12\x37\n\x0cmark_polygon\x18\x17 \x03(\x0b\x32!.citibot.common.hdmap.MarkPolygon\x12\x31\n\tmark_line\x18\x18 \x03(\x0b\x32\x1e.citibot.common.hdmap.MarkLine\x12.\n\x07station\x18\x19 \x03(\x0b\x32\x1d.citibot.common.hdmap.Station')
  ,
  dependencies=[common_dot_message_dot_map_dot_map__clear__area__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__crosswalk__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__junction__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__lane__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__overlap__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__signal__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__speed__bump__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__stop__sign__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__yield__sign__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__road__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__parking__space__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__pnc__junction__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__mark__point__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__remark__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__mark__polygon__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__mark__line__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__station__pb2.DESCRIPTOR,])




_PROJECTION = _descriptor.Descriptor(
  name='Projection',
  full_name='citibot.common.hdmap.Projection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proj', full_name='citibot.common.hdmap.Projection.proj', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=727,
  serialized_end=753,
)


_OFFSET = _descriptor.Descriptor(
  name='Offset',
  full_name='citibot.common.hdmap.Offset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='citibot.common.hdmap.Offset.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='citibot.common.hdmap.Offset.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='citibot.common.hdmap.Offset.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hdg', full_name='citibot.common.hdmap.Offset.hdg', index=3,
      number=4, type=1, cpp_type=5, label=1,
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
  serialized_start=755,
  serialized_end=809,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='citibot.common.hdmap.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='citibot.common.hdmap.Header.version', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date', full_name='citibot.common.hdmap.Header.date', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='projection', full_name='citibot.common.hdmap.Header.projection', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='district', full_name='citibot.common.hdmap.Header.district', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='generation', full_name='citibot.common.hdmap.Header.generation', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rev_major', full_name='citibot.common.hdmap.Header.rev_major', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rev_minor', full_name='citibot.common.hdmap.Header.rev_minor', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='left', full_name='citibot.common.hdmap.Header.left', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='top', full_name='citibot.common.hdmap.Header.top', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right', full_name='citibot.common.hdmap.Header.right', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bottom', full_name='citibot.common.hdmap.Header.bottom', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vendor', full_name='citibot.common.hdmap.Header.vendor', index=11,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='citibot.common.hdmap.Header.offset', index=12,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='citibot.common.hdmap.Header.name', index=13,
      number=22, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=812,
  serialized_end=1115,
)


_MAP = _descriptor.Descriptor(
  name='Map',
  full_name='citibot.common.hdmap.Map',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='citibot.common.hdmap.Map.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crosswalk', full_name='citibot.common.hdmap.Map.crosswalk', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='junction', full_name='citibot.common.hdmap.Map.junction', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lane', full_name='citibot.common.hdmap.Map.lane', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop_sign', full_name='citibot.common.hdmap.Map.stop_sign', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signal', full_name='citibot.common.hdmap.Map.signal', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='yield', full_name='citibot.common.hdmap.Map.yield', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='overlap', full_name='citibot.common.hdmap.Map.overlap', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clear_area', full_name='citibot.common.hdmap.Map.clear_area', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed_bump', full_name='citibot.common.hdmap.Map.speed_bump', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='road', full_name='citibot.common.hdmap.Map.road', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parking_space', full_name='citibot.common.hdmap.Map.parking_space', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pnc_junction', full_name='citibot.common.hdmap.Map.pnc_junction', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mark_point', full_name='citibot.common.hdmap.Map.mark_point', index=13,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remark', full_name='citibot.common.hdmap.Map.remark', index=14,
      number=22, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mark_polygon', full_name='citibot.common.hdmap.Map.mark_polygon', index=15,
      number=23, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mark_line', full_name='citibot.common.hdmap.Map.mark_line', index=16,
      number=24, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='station', full_name='citibot.common.hdmap.Map.station', index=17,
      number=25, type=11, cpp_type=10, label=3,
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
  serialized_start=1118,
  serialized_end=2025,
)

_HEADER.fields_by_name['projection'].message_type = _PROJECTION
_HEADER.fields_by_name['offset'].message_type = _OFFSET
_MAP.fields_by_name['header'].message_type = _HEADER
_MAP.fields_by_name['crosswalk'].message_type = common_dot_message_dot_map_dot_map__crosswalk__pb2._CROSSWALK
_MAP.fields_by_name['junction'].message_type = common_dot_message_dot_map_dot_map__junction__pb2._JUNCTION
_MAP.fields_by_name['lane'].message_type = common_dot_message_dot_map_dot_map__lane__pb2._LANE
_MAP.fields_by_name['stop_sign'].message_type = common_dot_message_dot_map_dot_map__stop__sign__pb2._STOPSIGN
_MAP.fields_by_name['signal'].message_type = common_dot_message_dot_map_dot_map__signal__pb2._SIGNAL
_MAP.fields_by_name['yield'].message_type = common_dot_message_dot_map_dot_map__yield__sign__pb2._YIELDSIGN
_MAP.fields_by_name['overlap'].message_type = common_dot_message_dot_map_dot_map__overlap__pb2._OVERLAP
_MAP.fields_by_name['clear_area'].message_type = common_dot_message_dot_map_dot_map__clear__area__pb2._CLEARAREA
_MAP.fields_by_name['speed_bump'].message_type = common_dot_message_dot_map_dot_map__speed__bump__pb2._SPEEDBUMP
_MAP.fields_by_name['road'].message_type = common_dot_message_dot_map_dot_map__road__pb2._ROAD
_MAP.fields_by_name['parking_space'].message_type = common_dot_message_dot_map_dot_map__parking__space__pb2._PARKINGSPACE
_MAP.fields_by_name['pnc_junction'].message_type = common_dot_message_dot_map_dot_map__pnc__junction__pb2._PNCJUNCTION
_MAP.fields_by_name['mark_point'].message_type = common_dot_message_dot_map_dot_map__mark__point__pb2._MARKPOINT
_MAP.fields_by_name['remark'].message_type = common_dot_message_dot_map_dot_map__remark__pb2._REMARK
_MAP.fields_by_name['mark_polygon'].message_type = common_dot_message_dot_map_dot_map__mark__polygon__pb2._MARKPOLYGON
_MAP.fields_by_name['mark_line'].message_type = common_dot_message_dot_map_dot_map__mark__line__pb2._MARKLINE
_MAP.fields_by_name['station'].message_type = common_dot_message_dot_map_dot_map__station__pb2._STATION
DESCRIPTOR.message_types_by_name['Projection'] = _PROJECTION
DESCRIPTOR.message_types_by_name['Offset'] = _OFFSET
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Map'] = _MAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Projection = _reflection.GeneratedProtocolMessageType('Projection', (_message.Message,), dict(
  DESCRIPTOR = _PROJECTION,
  __module__ = 'common.message.map.map_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.hdmap.Projection)
  ))
_sym_db.RegisterMessage(Projection)

Offset = _reflection.GeneratedProtocolMessageType('Offset', (_message.Message,), dict(
  DESCRIPTOR = _OFFSET,
  __module__ = 'common.message.map.map_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.hdmap.Offset)
  ))
_sym_db.RegisterMessage(Offset)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'common.message.map.map_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.hdmap.Header)
  ))
_sym_db.RegisterMessage(Header)

Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), dict(
  DESCRIPTOR = _MAP,
  __module__ = 'common.message.map.map_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.hdmap.Map)
  ))
_sym_db.RegisterMessage(Map)


# @@protoc_insertion_point(module_scope)

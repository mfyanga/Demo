# !/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"

PY_OUT_PATH=${DIR}/py_proto_gen
mkdir -p ${PY_OUT_PATH}

function build_pb2() {
    proto_files=$(find ${DIR} -name *.proto)
    for proto_file in ${proto_files}; do
	echo "dir = ${DIR}"
	echo "out_path = ${PY_OUT_PATH}"
	echo "proto_file = ${proto_file}"
        protoc -I=${DIR} --python_out=${PY_OUT_PATH} ${proto_file}
    done
    echo "Generating all proto file"
}

function creat_folder_init(){
    folder=$1
    touch ${folder}/__init__.py
    for ele in $(ls ${folder}); do
        cur_file=${folder}/${ele}
        if [ -d ${cur_file} ]; then
            touch ${folder}/${ele}/__init__.py
        fi
    done
}

build_pb2
#touch ${PY_OUT_PATH}/common/__init__.py
#creat_folder_init ${PY_OUT_PATH}/common/message

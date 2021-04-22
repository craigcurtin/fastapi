#!/usr/bin/env bash

function exit_test {
    "$@"
    local STATUS=$?
    if (( STATUS != 0 )); then
        echo "error with $1" >&2
    fi
    return ${STATUS}
}

clear ;

DOCKER_IMAGE="fastAPI"
read -n1 -s -r -p $'Press space to continue...\n' key

docker build -t ${DOCKER_IMAGE} .
#exit_test $?

read -n1 -s -r -p $'Press space to continue...\n' key
docker run -t ${DOCKER_IMAGE}
#exit_test $?


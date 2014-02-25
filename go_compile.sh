#!/bin/bash

set -e

cd `dirname $0`
export GOPATH=`pwd`

echo "Installing packages..."

go get -u -v labix.org/v2/mgo
go get -u -v labix.org/v2/mgo/bson

echo "Done"
echo "Compiling..."

go build golang_mongo.go

echo "Done"

cd $OLDPWD


PROTOC = protoc
CXX = g++
CXXFLAGS = -std=c++14 -O3 -fno-exceptions

INCLUDE = -I$(CURDIR)/build

all: build/nemesis_pb2.py build/nemesis.pb.o build/nemesis.pb.h

build/nemesis.pb.o: prepare build/nemesis.pb.cc build/nemesis.pb.h
	$(CXX) $(CXXFLAGS) $(INCLUDE) -c -o $(CURDIR)/build/nemesis.pb.o $(CURDIR)/build/nemesis.pb.cc

build/nemesis_pb2.py: prepare nemesis.proto
	$(PROTOC) nemesis.proto --python_out=$(CURDIR)/build/

build/nemesis.pb.cc: prepare nemesis.proto
	$(PROTOC) nemesis.proto --cpp_out=$(CURDIR)/build/

build/nemesis.pb.h: prepare nemesis.proto
	$(PROTOC) nemesis.proto --cpp_out=$(CURDIR)/build/

prepare:
	@mkdir -p build

distclean:
	@rm -rf build

.PHONY: all prepare distclean

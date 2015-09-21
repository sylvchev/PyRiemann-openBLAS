#!/bin/bash

cd SourceCode
make -B
cd ..

cd Benchmark
make -B
cd ..
#!/bin/bash

echo "generating..."

rm midiml.dot
rm midiml.dot.png

textx generate midiml.tx --target dot
dot -Tpng -O midiml.dot
#!/bin/bash

echo "generating..."

rm program.dot
rm program.dot.png

textx generate program.midiml --grammar midiml.tx --target dot
dot -Tpng -O program.dot
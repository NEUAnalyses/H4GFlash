#!/bin/bash

for i in {0..800};
do
echo $i
  python ../TreeSkimmerPy/H4GTreeSkimmer.py -i /eos/user/t/twamorka/2016_Data/output_DoubleEG_sethzenz-ReMiniAOD-03Feb2017-2_5_4-2_5_1-v0-Run2016H-03Feb2017_ver3-v1-6641814fa0affc4e30f35b89f3ef055c_USER_${i}.root  -o /eos/user/t/twamorka/SkimmedTrees_2016/DataH2_${i}.root
done

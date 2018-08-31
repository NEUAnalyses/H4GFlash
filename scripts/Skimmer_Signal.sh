#!/bin/bash

for i in 0p1 1 5 10 15 20 25 30 35 40 45 50 55 60;
do
	echo $i
       python ../TreeSkimmerPy/H4GTreeSkimmer.py -i /eos/user/t/twamorka/2016_Signal/signal_m_${i}.root  -o /eos/cms/store/user/twamorka/FlatTrees_2016/Signal/signal_m_${i}.root
done

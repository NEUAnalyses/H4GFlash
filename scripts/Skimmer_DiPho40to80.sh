for i in {0..800};
do
echo $i
  python ../TreeSkimmerPy/H4GTreeSkimmer.py -i /eos/user/t/twamorka/2016_Background/output_DiPhotonJetsBox_M40_80-Sherpa_${i}.root  -o /eos/user/t/twamorka/SkimmedTrees_2016/DiPho40to80_${i}.root
done

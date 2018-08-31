for i in {0..800};
do
echo $i
  python ../TreeSkimmerPy/H4GTreeSkimmer.py -i /eos/user/t/twamorka/2016_Background/output_DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa_${i}.root  -o /eos/user/t/twamorka/SkimmedTrees_2016/DiPho80toInf_${i}.root
done

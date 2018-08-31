for i in {0..800};
do
echo $i
  python H4GTreeSkimmer.py -i /eos/user/t/twamorka/2016_Background/output_GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8_${i}.root  -o /eos/user/t/twamorka/SkimmedTrees_2016/GJets20to40_${i}.root
done

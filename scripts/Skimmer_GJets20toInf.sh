for i in {0..800};
do
echo $i
  python ../TreeSkimmerPy/H4GTreeSkimmer.py -i /eos/user/t/twamorka/2016_Background/output_GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8_${i}.root  -o /eos/user/t/twamorka/SkimmedTrees_2016/GJets20toInf_${i}.root
done

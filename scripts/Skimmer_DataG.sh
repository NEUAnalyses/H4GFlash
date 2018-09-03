for i in {0..800};
do
echo $i
  python ../TreeSkimmerPy/H4GTreeSkimmer.py -i /eos/user/t/twamorka/2016_Data/output_DoubleEG_sethzenz-ReMiniAOD-03Feb2017-2_5_4-2_5_1-v0-Run2016G-03Feb2017-v1-b445e20eddb612afa0076163dede615e_USER_${i}.root  -o /eos/user/t/twamorka/SkimmedTrees_2016/DataG_${i}.root
done

for i in {0..800};
do
echo $i

  python ../TreeSkimmerPy/H4GTreeSkimmer.py -i /eos/user/t/twamorka/2016_Data/output_DoubleEG_sethzenz-ReMiniAOD-03Feb2017-2_5_5-2_5_5-v0-Run2016B-03Feb2017_ver2-v2-a56cd34be537fa6f2c9a0e455e52bfcd_USER_${i}.root  -o /eos/user/t/twamorka/SkimmedTrees_2016/DataB2_${i}.root
done

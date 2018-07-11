#!/bin/bash

#for i in 0	1	2	3	4	5	6	7	8	9  10	11	12	13	14	15	16	17	18	19 20	21	22	23	24	25	26	27	28	29 30	31	32	33	34	35	36	37	38	39 40	41	42	43	44	45	46	47	48	49 50;
#for i in {0..1000}

#for i in 100 101 102 103 105 106 107 108 109 111 112 113 114 115 116 117 124 126 127 129 130 132 133 135 136 141 149 14 150 151 152 153 158 15 161 162 163 166 167 16 174 175 177 179 17 180 181 183 184 185 186 187 18 190 196 197 198 199 19 31 37 38 39 3 40 41 42 43 49 50 51 52 53 54 55 58 59 5 61 62 64 65 66 67 70 71 72 73 74 76 80 81 82 83 84 85 86 87 8 91 92 93 94 95 96 98 99;
#for i in B_1 B_2 C_1 C_2 E F H_2;
#for i in output_GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8_*
#for i in DiPhoJets40to80 DiPhoJets80toInf GJets20to40 GJets20toInf GJets40toInf QCD30t040 QCD30toInf QCD40toInf
#for i in 0 1 2 3 4 5
#for i in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17;
#for i in 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449 450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 ;
for i in 0p1 1 5 10 15 20 25 30 35 40 45 50 55 60;
#for i in {0..348};
#for i in 177 178 179 180 181;
do
	echo $i
#python H4GTreeSkimmer.py -i /eos/user/t/twamorka/Apr3_2018_pt0/output_QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8_${i}.root -o /eos/user/t/twamorka/SkimTrees/QCD40toInf_${i}.root
    python H4GTreeSkimmer.py -i /eos/user/t/twamorka/Signal_ntuples_Jul3/signal_${i}.root  -o FlatTrees_Signal/signal_m_${i}.root
#python H4GTreeSkimmer.py -i /eos/user/t/twamorka/Apr3_2018_pt0/${i}.root  -o Apr7_Background/Background_${i}.root -p 4 -f 2
done

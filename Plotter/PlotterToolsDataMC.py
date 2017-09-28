
## trigger scale factors --where are you??

from ROOT import *

## Cuts to selection
Cuts = 'tp_mass > 100 && tp_mass < 180 && dp1_mass/tp_mass < 0.55 && dp2_mass/tp_mass < 0.50'
genCut = 'genTotalWeight'
BlindCut = 'genTotalWeight && !(tp_mass >115 && tp_mass <135)'
Blind = '!(tp_mass >115 && tp_mass <135)'


## location of plots 
outputLoc = '/afs/cern.ch/user/t/twamorka/www/H4G/MC_Sep26/'


## Get pretty colors

cNiceBlue = TColor.GetColor('#51A7F9')
cNiceBlueDark = TColor.GetColor('#2175E0')
cNiceGreen = TColor.GetColor('#6FBF41')
#cNiceGreen2 = TColor.GetColor(NiceGreen2)
cNiceGreenDark = TColor.GetColor('#008040')
cNiceYellow = TColor.GetColor('#FBE12A')
#cNiceYellow2 = TColor.GetColor(NiceYellow2)
cNiceOrange = TColor.GetColor('#F0951A')
cNiceRed = TColor.GetColor('#FA4912')
cNicePurple = TColor.GetColor('#885BB2')
cNicePaleYellow = TColor.GetColor('#FFFF66')
cNiceMidnight = TColor.GetColor('#000080')
cNiceTangerine = TColor.GetColor('#FF8000')



nbins = 35


##Variables to be plotted
#[ name of tree branch, name of pdf file, name of variable, number of bins, min bin, max bin]
Vars = []
Vars.append([ 'p1_pt', 'p1_pt', ';E_{T}(#gamma-1) [GeV];Normalized Yields', nbins, 25, 125,'p_{T}(#gamma-1)[GeV]'])
Vars.append([ 'p2_pt', 'p2_pt', ';E_{T}(#gamma-2) [GeV];Normalized Yields', nbins, 10, 110,'p_{T}(#gamma-2)[GeV]'])
Vars.append([ 'p3_pt', 'p3_pt', ';E_{T}(#gamma-3) [GeV];Normalized Yields', nbins, 10, 110,'p_{T}(#gamma-3)[GeV]'])
Vars.append([ 'p4_pt', 'p4_pt', ';E_{T}(#gamma-4) [GeV];Normalized Yields', nbins, 10, 45,'p_{T}(#gamma-4)[GeV]'])
Vars.append([ 'p1_eta', 'p1_eta', ';#eta(#gamma-1);Normalized Yields', nbins, -3, 3,'#eta(#gamma-1)'])
Vars.append([ 'p2_eta', 'p2_eta', ';#eta(#gamma-2);Normalized Yields', nbins, -3, 3,'#eta(#gamma-2)'])
Vars.append([ 'p3_eta', 'p3_eta', ';#eta(#gamma-3);Normalized Yields', nbins, -3, 3,'#eta(#gamma-3)'])
Vars.append([ 'p4_eta', 'p4_eta', ';#eta(#gamma-4);Normalized Yields', nbins, -3, 3,'#eta(#gamma-4)'])
Vars.append([ 'tp_mass', 'tp_mass', ';M(#gamma#gamma#gamma#gamma) [GeV];Normalized Yields', nbins, 100, 180,'M(#gamma#gamma#gamma#gamma) [GeV]'])
Vars.append([ 'dp1_mass', 'dp1_mass', ';M(#gamma#gamma-1) [GeV];Normalized Yields', nbins, 0, 120,'M(#gamma#gamma-1) [GeV]'])
Vars.append([ 'dp1_mass/tp_mass', 'dp1_mass_over_tp_mass', ';M(#gamma#gamma-1)/M(#gamma#gamma#gamma#gamma);Normalized Yields', nbins, 0, 1.0,'M(#gamma#gamma-1)/M(#gamma#gamma#gamma#gamma)'])
Vars.append([ 'dp2_mass', 'dp2_mass', ';M(#gamma#gamma-2) [GeV];Normalized Yields', nbins, 0, 120,'M(#gamma#gamma-2) [GeV]'])
Vars.append([ 'dp2_mass/tp_mass', 'dp2_mass_over_tp_mass', ';M(#gamma#gamma-2)/M(#gamma#gamma#gamma#gamma);Normalized Yields', nbins, 0, 1.0,'M(#gamma#gamma-2)/M(#gamma#gamma#gamma#gamma)'])
Vars.append([ 'p1_mva','p1_mva','MVA (#gamma-1); Normalized Yields',nbins,-1.5,1.5,'MVA (#gamma-1)'])
Vars.append([ 'p2_mva','p2_mva','MVA (#gamma-2); Normalized Yields',nbins,-1.5,1.5,'MVA (#gamma-2)'])
Vars.append([ 'p3_mva','p3_mva','MVA (#gamma-3); Normalized Yields',nbins,-1.5,1.5,'MVA (#gamma-3)'])
Vars.append([ 'p4_mva','p4_mva','MVA (#gamma-4); Normalized Yields',nbins,-1.5,1.5,'MVA (#gamma-4)'])
Vars.append([ '(dp1_mass - dp2_mass)/tp_mass','|U|',';|U| ; Normalized Yields',nbins,0,1,'|U|'])

MC = []

## MC is scaled as : Lumi*Xsection*1000/weights
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/DiphoJets80_Inf_gen.root','#gamma#gammaJets80toInf',cNiceBlue,cNiceBlue,36*84.4*1000/27363279.712975])       
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/DiphoJets40_80_gen.root','#gamma#gammaJets40to80',cNiceBlue,cNiceBlue,36*303.2*1000/3601376.531525])
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/GJets20_40_gen.root','#gammaJet20to40',cNiceBlueDark,cNiceBlueDark,36*220*1000/24989649])
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/GJets20_Inf_gen.root','#gammaJet20toInf',cNiceBlueDark,cNiceBlueDark,36*3216*1000/37274572])
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/GJets40_Inf_gen.root','#gammaJet40toInf',cNiceBlueDark,cNiceBlueDark,36*850.8*1000/72299185]) 
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/QCD30_40_gen.root','QCD30to40',cNicePaleYellow,cNicePaleYellow,36*22110*1000/18009320.786133])
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/QCD40_Inf_gen.root','QCD40toInf',cNicePaleYellow,cNicePaleYellow,36*113400*1000/20632076])
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/QCD30_Inf_gen.root','QCD30toInf',cNicePaleYellow,cNicePaleYellow,36*260500*1000/37562075])


## Data is always correct!

Data = []
Data.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/data.root','Data',1,0,1])

## signal is scaled as : Lumi*Xsection*1000*10(for magnification)/weights

Signal = []
Signal.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/sig60_skim.root','Sig60GeV',4,36*0.001*1000*10/198014])

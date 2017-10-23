
## trigger scale factors --where are you??

from ROOT import *

## Cuts to selection
Cuts = 'tp_mass > 100 && tp_mass < 180 && dp1_mass/tp_mass < 0.55 && dp2_mass/tp_mass < 0.50'
genCut = 'genTotalWeight'
BlindCut = '!(tp_mass >115 && tp_mass <135)'
Blind = '!(tp_mass >115 && tp_mass <135) && genTotalWeight'


## location of plots 
outputLoc = '/afs/cern.ch/user/t/twamorka/www/H4G/Oct18/'


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
cNicePaleYellow = TColor.GetColor('#FFFF66')
cNiceMidnight = TColor.GetColor('#000080')
cNiceTangerine = TColor.GetColor('#FF8000')



nbins = 35


##Variables to be plotted
#[ name of tree branch, name of pdf file, name of variable, number of bins, min bin, max bin]
Vars = []
#Vars.append([ 'p1_pt', 'p1_pt', ';E_{T}(#gamma-1) [GeV];Normalized Yields', nbins, 25, 125,'p_{T}(#gamma-1)[GeV]'])
#Vars.append([ 'p2_pt', 'p2_pt', ';E_{T}(#gamma-2) [GeV];Normalized Yields', nbins, 10, 110,'p_{T}(#gamma-2)[GeV]'])
#Vars.append([ 'p3_pt', 'p3_pt', ';E_{T}(#gamma-3) [GeV];Normalized Yields', nbins, 10, 110,'p_{T}(#gamma-3)[GeV]'])
#Vars.append([ 'p4_pt', 'p4_pt', ';E_{T}(#gamma-4) [GeV];Normalized Yields', nbins, 10, 45,'p_{T}(#gamma-4)[GeV]'])
#Vars.append([ 'p1_eta', 'p1_eta', ';#eta(#gamma-1);Normalized Yields', nbins, -3, 3,'#eta(#gamma-1)'])
#Vars.append([ 'p2_eta', 'p2_eta', ';#eta(#gamma-2);Normalized Yields', nbins, -3, 3,'#eta(#gamma-2)'])
#Vars.append([ 'p3_eta', 'p3_eta', ';#eta(#gamma-3);Normalized Yields', nbins, -3, 3,'#eta(#gamma-3)'])
#Vars.append([ 'p4_eta', 'p4_eta', ';#eta(#gamma-4);Normalized Yields', nbins, -3, 3,'#eta(#gamma-4)'])
Vars.append([ 'tp_mass', 'tp_mass', ';M(#gamma#gamma#gamma#gamma) [GeV];Normalized Yields', nbins, 100, 180,'M(#gamma#gamma#gamma#gamma) [GeV]'])
#Vars.append([ 'dp1_mass', 'dp1_mass', ';M(#gamma#gamma-1) [GeV];Normalized Yields', nbins, 0, 120,'M(#gamma#gamma-1) [GeV]'])
#Vars.append([ 'dp1_mass/tp_mass', 'dp1_mass_over_tp_mass', ';M(#gamma#gamma-1)/M(#gamma#gamma#gamma#gamma);Normalized Yields', nbins, 0, 1.0,'M(#gamma#gamma-1)/M(#gamma#gamma#gamma#gamma)'])
#Vars.append([ 'dp2_mass', 'dp2_mass', ';M(#gamma#gamma-2) [GeV];Normalized Yields', nbins, 0, 120,'M(#gamma#gamma-2) [GeV]'])
#Vars.append([ 'dp2_mass/tp_mass', 'dp2_mass_over_tp_mass', ';M(#gamma#gamma-2)/M(#gamma#gamma#gamma#gamma);Normalized Yields', nbins, 0, 1.0,'M(#gamma#gamma-2)/M(#gamma#gamma#gamma#gamma)'])
#Vars.append([ 'p1_mva','p1_mva','MVA (#gamma-1); Normalized Yields',nbins,-1.5,1.5,'MVA (#gamma-1)'])
#Vars.append([ 'p2_mva','p2_mva','MVA (#gamma-2); Normalized Yields',nbins,-1.5,1.5,'MVA (#gamma-2)'])
#Vars.append([ 'p3_mva','p3_mva','MVA (#gamma-3); Normalized Yields',nbins,-1.5,1.5,'MVA (#gamma-3)'])
#Vars.append([ 'p4_mva','p4_mva','MVA (#gamma-4); Normalized Yields',nbins,-1.5,1.5,'MVA (#gamma-4)'])
#Vars.append([ '(dp1_mass - dp2_mass)/tp_mass','|U|',';|U| ; Normalized Yields',nbins,0,1,'|U|'])

MC = []

## MC is scaled as : Lumi*Xsection*1000/weights
## Signal region
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/DiphoJets80_Inf_gen.root','#gamma#gammaJets',cNiceBlue,cNiceBlue,0.111,1])       
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/DiphoJets40_80_gen.root','#gamma#gammaJets',cNiceBlue,cNiceBlue,3.030,1])
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/GJets20_40_gen.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,0.316,1])
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/GJets20_Inf_gen.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,3.106,1])
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/GJets40_Inf_gen.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,0.423,1]) 
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/QCD30_40_gen.root','QCD',cNiceGreenDark,cNiceGreenDark,0.56*44.197,1])
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/QCD40_Inf_gen.root','QCD',cNiceGreenDark,cNiceGreenDark,0.56*197.866,1])
MC.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/QCD30_Inf_gen.root','QCD',cNiceGreenDark,cNiceGreenDark,0.56*249.667,1])
## Control Region
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/DiphoJets80_Inf_gen.root','#gamma#gammaJets',cNiceBlue,cNiceBlue,0.111,1])  
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/DiphoJets40_80_gen.root','#gamma#gammaJets',cNiceBlue,cNiceBlue,3.030,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/GJets20_40_gen.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,0.316,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/GJets20_Inf_gen.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,3.106,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/GJets40_Inf_gen.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,0.423,1]) 
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/QCD30_40_gen.root','QCD',cNiceGreenDark,cNiceGreenDark,0.2*44.197,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/QCD40_Inf_gen.root','QCD',cNiceGreenDark,cNiceGreenDark,0.2*197.866,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/QCD30_Inf_gen.root','QCD',cNiceGreenDark,cNiceGreenDark,0.2*249.667,1])
## 3 photons

#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/DiphoJets80_Inf.root','#gamma#gammaJets',cNiceBlue,cNiceBlue,0.111,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/DiphoJets40_80.root','#gamma#gammaJets',cNiceBlue,cNiceBlue,3.030,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/GJets20_40.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,0.316,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/GJets20_Inf.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,3.106,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/GJets40_Inf.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,0.423,1]) 
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/QCD30_40.root','QCD',cNiceGreenDark,cNiceGreenDark,0.56*44.197,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/QCD40_Inf.root','QCD',cNiceGreenDark,cNiceGreenDark,0.56*197.866,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/QCD30_Inf.root','QCD',cNiceGreenDark,cNiceGreenDark,0.56*249.667,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/Oct17_Skim3/DiphoJets80_Inf.root','#gamma#gammaJets',cNiceBlue,cNiceBlue,0.111,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/Oct17_Skim3/DiphoJets40_80.root','#gamma#gammaJets',cNiceBlue,cNiceBlue,3.030,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/Oct17_Skim3/GJets20_40.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,0.316,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/Oct17_Skim3/GJets20_Inf.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,3.106,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/Oct17_Skim3/GJets40_Inf.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,0.423,1]) 
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/Oct17_Skim3/QCD30_40.root','QCD',cNiceGreenDark,cNiceGreenDark,0.48*44.197,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/Oct17_Skim3/QCD40_Inf.root','QCD',cNiceGreenDark,cNiceGreenDark,0.48*197.866,1])
#MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/Oct17_Skim3/QCD30_Inf.root','QCD',cNiceGreenDark,cNiceGreenDark,0.48*249.667,1])


## Data is always correct!

Data = []
Data.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/data.root','Data',1,0,1])  ##signal region
#Data.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/data_skim.root','Data',1,0,1]) ## control region
#Data.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/data.root','Data',1,0,1]) ## 3 photons
#Data.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/Oct17_Skim3/data.root','Data',1,0,1])

## signal is scaled as : Lumi*Xsection*1000*10(for magnification)/weights

Signal1 = []
Signal1.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/sig60_skim.root','Sig60GeV',4,36*0.001*1000*10/198014]) ##signal region
#Signal1.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/sig60_skim.root','Sig60GeV',4,36*0.001*1000*10/198014]) ## control region
#Signal1.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/sig60_skim.root','Sig60GeV',4,36*0.001*1000*10000/198014]) ## 3 photon signal region
#Signal1.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/Oct17_Skim3/Sig20.root','Sig20GeV',4,36*0.001*1000*2500/200000])

Signal2 = []
Signal2.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/sig45_skim.root','Sig45GeV',2,36*0.001*1000*10/198033]) ##signal region
#Signal2.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/sig45_skim.root','Sig45GeV',2,36*0.001*1000*10/198033]) ## control region
#Signal2.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/sig45_skim.root','Sig45GeV',2,36*0.001*1000*10000/198033]) ## 3 photon signal region
#Signal2.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/Oct17_Skim2/Sig15.root','Sig15GeV',2,36*0.001*1000*2500/200000])
Signal3 = []
Signal3.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/sig25_skim.root','Sig25GeV',3,36*0.001*1000*10/200000]) ##signal region
#Signal3.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/sig25_skim.root','Sig25GeV',3,36*0.001*1000*10/200000]) ## control region
#Signal3.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/sig25_skim.root','Sig25GeV',3,36*0.001*1000*10000/200000])  ## 3 photoni signal region
#Signal3.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/Oct17_Skim3/Sig10.root','Sig10GeV',3,36*0.001*1000*2500/195505])
Signal4 = []
Signal4.append(['/eos/cms/store/user/twamorka/4gamma/skimtrees/sig10_skim.root','Sig10GeV',6,36*0.001*1000*10/195505]) ##signal region
#Signal4.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/sig10_skim.root','Sig10GeV',6,36*0.001*1000*10/195505]) ## control region
#Signal4.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/sig10_skim.root','Sig10GeV',6,36*0.001*1000*10000/195505])  ## 3 photon signal region
#Signal4.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/Oct17_Skim3/Sig5.root','Sig5GeV',6,36*0.001*1000*2500/200000])

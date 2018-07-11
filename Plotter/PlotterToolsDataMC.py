
## trigger scale factors --where are you??

from ROOT import *

## Cuts to selection
#Cuts = 'tp_mass > 100 && tp_mass < 180 && dp1_mass/tp_mass < 0.55 && dp2_mass/tp_mass < 0.50'

Cuts = 'abs(v_pho_eta[0])>1.4442'
genCutSig = 'abs(p1_eta) > 1.479 && abs(p2_eta) > 1.479 && abs(p3_eta) > 1.479 && abs(p4_eta) > 1.479 && genTotalWeight && p1_genmatch==1 && p2_genmatch==1 && p3_genmatch==1 && p4_genmatch==1 && tp_mass > 100 && tp_mass < 180 && dp1_mass/tp_mass < 0.55 && dp2_mass/tp_mass < 0.50'
#genCutSig = 'genTotalWeight && p1_genmatch==1 && p2_genmatch==1 && p3_genmatch==1 && tp_mass > 100 && tp_mass < 180'
genCutBack = 'genTotalWeight && tp_mass > 100 && tp_mass < 180'
BlindCut = '!( tp_mass > 115 && tp_mass <135) && tp_mass > 100 && tp_mass < 180 && dp1_mass/tp_mass < 0.55 && dp2_mass/tp_mass < 0.50'
BlindSig = '!(tp_mass >115 && tp_mass <135) && genTotalWeight && p1_genmatch==1 && p2_genmatch==1 && p3_genmatch==1 && p4_genmatch==1 && tp_mass > 100 && tp_mass < 180 && dp1_mass/tp_mass < 0.55 && dp2_mass/tp_mass < 0.50'
BlindBack = 'abs(p1_eta) > 1.479 && abs(p2_eta) > 1.479 && abs(p3_eta) > 1.479 && abs(p4_eta) > 1.479 && genTotalWeight && tp_mass > 100 && tp_mass < 180 && dp1_mass/tp_mass < 0.55 && dp2_mass/tp_mass < 0.50'
Cut_resolved = 'v_genmatch_pt<0'
Cut_fat = 'v_genmatch_pt>0'
Cut = 'abs(p1_eta) > 1.479 && abs(p2_eta) > 1.479 && abs(p3_eta) > 1.479 && abs(p4_eta) > 1.479'
## location of plots 
outputLoc = '/afs/cern.ch/user/t/twamorka/www/Higgsto4Gamma/RecoLevel/Signal_Background_4Gamma/'


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



nbins = 55


##Variables to be plotted
#[ name of tree branch, name of pdf file, name of variable, number of bins, min bin, max bin]
Vars = []
#Vars.append([ 'p1_pt', 'p1_pt', 'P_{T}(#gamma_{1}) [GeV]', nbins, 25, 110])
#Vars.append([ 'p2_pt', 'p2_pt', 'P_{T}(#gamma_{2}) [GeV]', nbins, 10, 110])
#Vars.append([ 'p3_pt', 'p3_pt', 'P_{T}(#gamma_{3}) [GeV]', nbins, 0, 110])
#Vars.append([ 'p4_pt', 'p4_pt', 'P_{T}(#gamma_{4}) [GeV]', nbins, 0, 110])
#Vars.append([ 'p1_eta', 'p1_eta', '#eta(#gamma_{1})', nbins, -3.0, 3.0])
#Vars.append([ 'p2_eta', 'p2_eta', '#eta(#gamma_{2})', nbins, -3.0, 3.0])
#Vars.append([ 'p3_eta', 'p3_eta', '#eta(#gamma_{3})', nbins, -3.0, 3.0])
#Vars.append([ 'p4_eta', 'p4_eta', '#eta(#gamma_{4})', nbins, -3.0, 3.0])
#Vars.append([ 'p1_phi', 'p1_phi', '#phi(#gamma_{1})', nbins, -3.5, 3.5])
#Vars.append([ 'p2_phi', 'p2_phi', '#phi(#gamma_{2})', nbins, -3.5, 3.5])
#Vars.append([ 'p3_phi', 'p3_phi', '#phi(#gamma_{3})', nbins -3.5, 3.5])
#Vars.append([ 'p4_phi', 'p4_phi', '#phi(#gamma_{4})', nbins -3.5, 3.5])
#Vars.append([ 'p1_M', 'p1_M', ';M(#gamma_{1});Normalized Yields'nbins 0, 10])
#Vars.append([ 'p2_M', 'p2_M', ';M(#gamma_{2});Normalized Yields'nbins 0, 10])
#Vars.append([ 'p3_M', 'p3_M', ';M(#gamma_{3});Normalized Yields'nbins 0, 10])
#Vars.append([ 'p4_M', 'p4_M', ';M(#gamma_{4});Normalized Yields'nbins 0, 10])
#Vars.append([ 'p1_mva', 'p1_mva', 'MVA(#gamma_{1})',nbins, -1.5, 1.5])
#Vars.append([ 'p2_mva', 'p2_mva', 'MVA(#gamma_{2})',nbins, -1.5, 1.5])
#Vars.append([ 'p3_mva', 'p3_mva', 'MVA(#gamma_{3})',nbins, -1.5, 1.5])
#Vars.append([ 'p4_mva', 'p4_mva', 'MVA(#gamma_{4})',nbins, -1.5, 1.5])
#Vars.append([ 'p1_r9', 'p1_r9', 'R9(#gamma_{1})',nbins, 0, 1.2])
#Vars.append([ 'p2_r9', 'p2_r9', 'R9(#gamma_{2})',nbins, 0, 1.2])
#Vars.append([ 'p3_r9', 'p3_r9', 'R9(#gamma_{3})',nbins, 0, 1.2])
#Vars.append([ 'p4_r9', 'p4_r9', 'R9(#gamma_{4})',nbins, 0, 1.2])
#Vars.append([ 'p1_full5x5_r9', 'p1_full5x5_r9', 'Full 5X5 R9(#gamma_{1})',nbins, 0, 1.2])
#Vars.append([ 'p2_full5x5_r9', 'p2_full5x5_r9', 'Full 5X5 R9(#gamma_{2})',nbins, 0, 1.2])
#Vars.append([ 'p3_full5x5_r9', 'p3_full5x5_r9', 'Full 5X5 R9(#gamma_{3})',nbins, 0, 1.2])
#Vars.append([ 'p4_full5x5_r9', 'p4_full5x5_r9', 'Full 5X5 R9(#gamma_{4})',nbins, 0, 1.2])
#Vars.append([ 'p1_full5x5_sigmaIetaIeta', 'p1_full5x5_sigmaIetaIeta_EE', 'Full 5X5 #sigma_{i#etai#eta}(#gamma_{1})',nbins, 0.01, 0.035])
#Vars.append([ 'p2_full5x5_sigmaIetaIeta', 'p2_full5x5_sigmaIetaIeta_EE', 'Full 5X5 #sigma_{i#etai#eta}(#gamma_{2})',nbins, 0.01, 0.035])
#Vars.append([ 'p3_full5x5_sigmaIetaIeta', 'p3_full5x5_sigmaIetaIeta_EE', 'Full 5X5 #sigma_{i#etai#eta}(#gamma_{3})',nbins, 0.01, 0.035])
#Vars.append([ 'p4_full5x5_sigmaIetaIeta', 'p4_full5x5_sigmaIetaIeta_EE', 'Full 5X5 #sigma_{i#etai#eta}(#gamma_{4})',nbins, 0.01, 0.035])
#Vars.append([ 'p1_full5x5_sigmaEtaEta', 'p1_full5x5_sigmaEtaEta_EE', 'Full 5X5 #sigma_{#eta#eta}(#gamma_{1})',nbins, 0.01, 0.035])
#Vars.append([ 'p2_full5x5_sigmaEtaEta', 'p2_full5x5_sigmaEtaEta_EE', 'Full 5X5 #sigma_{#eta#eta}(#gamma_{2})',nbins, 0.01, 0.035])
#Vars.append([ 'p3_full5x5_sigmaEtaEta', 'p3_full5x5_sigmaEtaEta_EE', 'Full 5X5 #sigma_{#eta#eta}(#gamma_{3})',nbins, 0.01, 0.035])
#Vars.append([ 'p4_full5x5_sigmaEtaEta', 'p4_full5x5_sigmaEtaEta_EE', 'Full 5X5 #sigma_{#eta#eta}(#gamma_{4})',nbins, 0.01, 0.035])
#Vars.append([ 'p1_sigmaEtaEta', 'p1_sigmaEtaEta_EE', '#sigma_{#eta#eta}(#gamma_{1})',nbins, 0.01, 0.035])
#Vars.append([ 'p2_sigmaEtaEta', 'p2_sigmaEtaEta_EE', '#sigma_{#eta#eta}(#gamma_{2})',nbins, 0.01, 0.035])
#Vars.append([ 'p3_sigmaEtaEta', 'p3_sigmaEtaEta_EE', '#sigma_{#eta#eta}(#gamma_{3})',nbins, 0.01, 0.035])
#Vars.append([ 'p4_sigmaEtaEta', 'p4_sigmaEtaEta_EE', '#sigma_{#eta#eta}(#gamma_{4})',nbins, 0.01, 0.035])
#Vars.append(['p1_hadronicOverEm','p1_hadronicOverEm','HadronicOverEm(#gamma_{1})',nbins,0,0.08])
#Vars.append(['p2_hadronicOverEm','p2_hadronicOverEm','HadronicOverEm(#gamma_{2})',nbins,0,0.08])
#Vars.append(['p3_hadronicOverEm','p3_hadronicOverEm','HadronicOverEm(#gamma_{3})',nbins,0,0.08])
#Vars.append(['p4_hadronicOverEm','p4_hadronicOverEm','HadronicOverEm(#gamma_{4})',nbins,0,0.08])
Vars.append([ 'p_mindr','p_mindr','min #Delta R',nbins,0,4])
Vars.append([ 'p_maxdr','p_maxdr','max #Delta R',nbins,0,4])
Vars.append([ 'p_maxmass','p_maxmass','max DiPhoton Mass',nbins,40,120])
Vars.append([ 'dp1_dr', 'dp1_dr', '#Delta R DiPhoton_{1}',nbins, 0, 4])
Vars.append([ 'dp2_dr', 'dp2_dr', '#Delta R DiPhoton_{2}',nbins, 0, 4])
Vars.append([ 'dp1_mass', 'dp1_mass', 'M(#gamma#gamma_{1}) [GeV]',nbins, 0, 120])
Vars.append([ 'dp2_mass', 'dp2_mass', 'M(#gamma#gamma_{2}) [GeV]',nbins, 0, 120])
Vars.append([ 'dp1_pt', 'dp1_pt', 'P_{T}(#gamma#gamma_{1}) [GeV]',nbins, 0, 120])
Vars.append([ 'dp2_pt', 'dp2_pt', 'P_{T}(#gamma#gamma_{2}) [GeV]',nbins, 0, 120])
Vars.append([ 'dp1_eta', 'dp1_eta', '#eta(#gamma#gamma_{1})',nbins, -3.5, 3.5])
Vars.append([ 'dp2_eta', 'dp2_eta', '#eta(#gamma#gamma_{2})',nbins, -3.5, 3.5])
Vars.append([ 'dp1_phi', 'dp1_phi', '#phi(#gamma#gamma_{1})',nbins, -3.5, 3.5])
Vars.append([ 'dp2_phi', 'dp2_phi', '#phi(#gamma#gamma_{2})',nbins, -3.5, 3.5])
Vars.append(['tp_mass','tp_mass','M(#gamma#gamma#gamma#gamma) [GeV]',nbins,60,180])
Vars.append([ 'tp_eta', 'tp_eta', '#eta(#gamma#gamma#gamma#gamma)',nbins, -3.5, 3.5])
Vars.append([ 'tp_phi', 'tp_phi', '#phi(#gamma#gamma#gamma#gamma)',nbins, -3.5, 3.5])
Vars.append([ 'tp_pt', 'tp_pt', 'P_{T}(#gamma#gamma#gamma#gamma) [GeV]',nbins, 0, 200])



#Vars.append([ 'v_pho_hadronicOverEm[0]', 'v_pho_hadronicOverEm[0]', ';HoE;Normalized Yields', nbins, 0, 1,'HoE'])
#Vars.append(['v_pho_r9[0]','v_pho_r9[0]','; R9 ; Normalized Yields',nbins,0,1.2,' R9'])
#Vars.append(['v_pho_ecalPFClusterIso[0]','v_pho_ecalPFClusterIso[0]',';PF Photon Isolation ; Normalized Yields',nbins,0,20, 'PF Photon Isolation'])
#Vars.append(['v_pho_mva[0]','v_pho_mva[0]',';Photon ID MVA ; Normalized Yields',nbins,-1.2,1.2, 'Photon ID MVA'])
#Vars.append([ 'v_pho_sigmaIetaIeta[0]', 'v_pho_sigmaIetaIeta[0]', ';#sigma_{#eta#eta}(#gamma);Normalized Yields', nbins, 0.01, 0.034,'Sigma Eta Eta'])
#Vars.append([ 'p1_pt', 'p1_pt', ';P_{T}(#gamma_{1}) [GeV];Normalized Yields'nbins 0, 110])
#Vars.append(['dp1_dr','dp1_dr',';DiPhoton #Delta R ;Normalized Yields',100,0,3.5])





#Vars.append([ 'v_pho_pt[0]', 'v_pho_pt[0]', ';P_{T}(#gamma) [GeV];Normalized Yields', nbins, 0, 125,'P_{T}(#gamma)[GeV]'])
#Vars.append([ 'v_pho_eta[0]', 'v_pho_eta[0]', ';#eta(#gamma);Normalized Yields', nbins, -4, 4,'#eta(#gamma)'])
#Vars.append([ 'v_pho_phi[0]', 'v_pho_phi[0]', ';#phi(#gamma);Normalized Yields', nbins, -4, 4,'#phi(#gamma)'])
#Vars.append([ 'v_pho_mva[0]', 'v_pho_mva[0]', ';MVA(#gamma);Normalized Yields', nbins, -1.5, 1.5,'MVA(#gamma)'])
#Vars.append([ 'v_pho_hadronicOverEm[0]', 'v_pho_hadronicOverEm[0]', ';HoE(#gamma);Normalized Yields', nbins, 0, 1,'HoE(#gamma)'])
#Vars.append([ 'v_pho_r9[0]', 'v_pho_r9[0]', ';R9(#gamma);Normalized Yields', nbins, 0, 1.5,'R9(#gamma)'])
#Vars.append([ 'v_pho_full5x5_r9[0]', 'v_pho_full5x5_r9[0]', ';Full 5x5 R9(#gamma);Normalized Yields', nbins, 0, 1.5,'Full5x5 R9(#gamma)'])
#Vars.append([ 'v_pho_r9[0]', 'v_pho_r9[0]', ';R9(#gamma);Normalized Yields', nbins, 0, 1.5,'R9(#gamma)'])
#Vars.append([ 'v_pho_sigmaEtaEta [0]', 'v_pho_sigmaEtaEta [0]', ';#sigma_{#eta#eta}(#gamma);Normalized Yields', nbins, 0, ,'R9(#gamma)'])

#Vars.append([ 'p1_pt', 'p1_pt', ';E_{T}(#gamma_{1}) [GeV];Normalized Yields', nbins, 25, 125,'p_{T}(#gamma_{1})[GeV]'])
#Vars.append([ 'p2_pt', 'p2_pt', ';E_{T}(#gamma_{2}) [GeV];Normalized Yields', nbins, 10, 110,'p_{T}(#gamma_{2})[GeV]'])
#Vars.append([ 'p3_pt', 'p3_pt', ';E_{T}(#gamma_{3}) [GeV];Normalized Yields', nbins, 0, 110,'p_{T}(#gamma_{3})[GeV]'])
#Vars.append([ 'p4_pt', 'p4_pt', ';E_{T}(#gamma_{4}) [GeV];Normalized Yields', nbins, 0, 45,'p_{T}(#gamma_{4})[GeV]'])
#Vars.append([ 'p1_eta', 'p1_eta', ';#eta(#gamma_{1});Normalized Yields', nbins, -3, 3,'#eta(#gamma_{1})'])
#Vars.append([ 'p2_eta', 'p2_eta', ';#eta(#gamma_{2});Normalized Yields', nbins, -3, 3,'#eta(#gamma_{2})'])
#Vars.append([ 'p3_eta', 'p3_eta', ';#eta(#gamma_{3});Normalized Yields', nbins, -3, 3,'#eta(#gamma_{3})'])
#Vars.append([ 'p4_eta', 'p4_eta', ';#eta(#gamma_{4});Normalized Yields', nbins, -3, 3,'#eta(#gamma_{4})'])
#Vars.append([ 'tp_mass', 'tp_mass', ';M(#gamma#gamma#gamma#gamma) [GeV];Normalized Yields', nbins, 60, 180,'M(#gamma#gamma#gamma#gamma) [GeV]'])
#Vars.append([ 'dp1_mass', 'dp1_mass', ';M(#gamma#gamma_{1}) [GeV];Normalized Yields', nbins, 0, 120,'M(#gamma#gamma_{1}) [GeV]'])
#Vars.append([ 'dp1_mass/tp_mass', 'dp1_mass_over_tp_mass', ';M(#gamma#gamma_{1})/M(#gamma#gamma#gamma#gamma);Normalized Yields', nbins, 0, 1.0,'M(#gamma#gamma_{1})/M(#gamma#gamma#gamma#gamma)'])
#Vars.append([ 'dp2_mass', 'dp2_mass', ';M(#gamma#gamma_{2}) [GeV];Normalized Yields', nbins, 0, 120,'M(#gamma#gamma_{2}) [GeV]'])
#Vars.append([ 'dp2_mass/tp_mass', 'dp2_mass_over_tp_mass', ';M(#gamma#gamma_{2})/M(#gamma#gamma#gamma#gamma);Normalized Yields', nbins, 0, 1.0,'M(#gamma#gamma_{2})/M(#gamma#gamma#gamma#gamma)'])
#Vars.append([ 'p1_mva','p1_mva','MVA (#gamma_{1}); Normalized Yields',nbins,-1.5,1.5,'MVA (#gamma_{1})'])
#Vars.append([ 'p2_mva','p2_mva','MVA (#gamma_{2}); Normalized Yields',nbins,-1.5,1.5,'MVA (#gamma_{2})'])
#Vars.append([ 'p3_mva','p3_mva','MVA (#gamma_{3}); Normalized Yields',nbins,-1.5,1.5,'MVA (#gamma_{3})'])
#Vars.append([ 'p4_mva','p4_mva','MVA (#gamma_{4}); Normalized Yields',nbins,-1.5,1.5,'MVA (#gamma_{4})'])
#Vars.append([ 'max(p1_mva,p2_mva,p3_mva,p4_mva)','maximumMVA','Max MVA ; Normalized Yields',nbins,-1.5,1.5,'Max MVA'])
#Vars.append([ '(dp1_mass - dp2_mass)/tp_mass','massHandle',';|U| ; Normalized Yields',nbins,0,1,'|U|'])
#Vars.append(['tp_pt / tp_mass','tp_ptovertp_mass',';tp_pt/tp_mass; Normalized Yields',nbins,0,4,'tp_pt/tp_mass'])
#Vars.append(['p1_full5x5_r9','p1_full5x5_r9',';Full 5x5 R9 (#gamma-1)]);Normalized Yields',nbins,0,1.2,'Full 5x5 R9 (#gamma-1)'])
#Vars.append(['p2_full5x5_r9','p2_full5x5_r9',';Full 5x5 R9 (#gamma-2)]);Normalized Yields',nbins,0,1.2,'Full 5x5 R9 (#gamma-2)'])
#Vars.append(['p3_full5x5_r9','p3_full5x5_r9',';Full 5x5 R9 (#gamma-3)]);Normalized Yields',nbins,0,1.2,'Full 5x5 R9 (#gamma-3)'])
#Vars.append(['p4_full5x5_r9','p4_full5x5_r9',';Full 5x5 R9 (#gamma-4)]);Normalized Yields',nbins,0,1.2,'Full 5x5 R9 (#gamma-4)'])
MC = []

## MC is scaled as : Lumi*Xsection*1000/weights
## Signal region#

#MC.append(['/eos/cms/store/user/torimoto/physics/4gamma/Background/DiPhoJets80toInf.root','#gamma#gammaJets',cNiceBlue,cNiceBlue,0.111,1])
#MC.append(['/eos/cms/store/user/torimoto/physics/4gamma/Background/DiPhoJets40to80.root','#gamma#gammaJets',cNiceBlue,cNiceBlue,3.030,1])
#MC.append(['/eos/cms/store/user/torimoto/physics/4gamma/Background/GJets20to40.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,0.316,1])
#MC.append(['/eos/cms/store/user/torimoto/physics/4gamma/Background/GJets20toInf.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,3.106,1])
#MC.append(['/eos/cms/store/user/torimoto/physics/4gamma/Background/GJets40toInf.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,0.423,1])
#MC.append(['/eos/cms/store/user/torimoto/physics/4gamma/Background/QCD30to40.root','QCD',cNiceGreenDark,cNiceGreenDark,44.197,1])
#MC.append(['/eos/cms/store/user/torimoto/physics/4gamma/Background/QCD40toInf.root','QCD',cNiceGreenDark,cNiceGreenDark,197.866,1])
#MC.append(['/eos/cms/store/user/torimoto/physics/4gamma/Background/QCD30toInf.root','QCD',cNiceGreenDark,cNiceGreenDark,249.667,1])

MC.append(['/eos/cms/store/user/twamorka/FlatTrees/DiPho80toInf.root','#gamma#gammaJets',cNiceBlue,cNiceBlue,0.111,1])
MC.append(['/eos/cms/store/user/twamorka/FlatTrees/DiPho40to80.root','#gamma#gammaJets',cNiceBlue,cNiceBlue,3.030,1])
MC.append(['/eos/cms/store/user/twamorka/FlatTrees/GJets20to40.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,0.316,1])
MC.append(['/eos/cms/store/user/twamorka/FlatTrees/GJets20toInf.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,3.106,1])
MC.append(['/eos/cms/store/user/twamorka/FlatTrees/GJets40toInf.root','#gammaJet',cNiceBlueDark,cNiceBlueDark,0.423,1])
MC.append(['/eos/cms/store/user/twamorka/FlatTrees/QCD30to40.root','QCD',cNiceGreenDark,cNiceGreenDark,44.197,1])
MC.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/FlatTrees/QCD40toInf.root','QCD',cNiceGreenDark,cNiceGreenDark,197.866,1])
MC.append(['/eos/cms/store/user/twamorka/FlatTrees/QCD30toInf.root','QCD',cNiceGreenDark,cNiceGreenDark,249.667,1])



## Data is always correct!

Data = []
#Data.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Mar3_2018/data.root','Data',1,0,1])  ##signal region
#Data.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/data_skim.root','Data',1,0,1]) ## control region
#Data.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/data.root','Data',1,0,1]) ## 3 photons
#Data.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/Oct17_Skim3/data.root','Data',1,0,1])

## signal is scaled as : Lumi*Xsection*1000*10(for magnification)/weights

Signal1 = []

#Signal1.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/FlatTrees/FatPho0p1_Match0p15/signal_m_10.root','m(a) = 10 GeV ',kViolet-5, 0, 1])
#Signal1.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/FlatTrees/FatPho0p1_Match0p15/signal_m_25.root','m(a) = 25 GeV ',kOrange+10, 0, 1])
#Signal1.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/FlatTrees/FatPho0p1_Match0p15/signal_m_40.root','m(a) = 40 GeV ',kGreen-6, 0, 1])
#Signal1.append(['/eos/user/t/twamorka/FatPho0p1_Match0p15/sig60.root','m(a) = 60 GeV ',kPink-5, 0, 1])

Signal1.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/FlatTrees/FatPho0p1_Match0p15/signal_m_30and18_60.root','Signal m(a)=60GeV',4,36*0.001*1000*1000/198014])

#Signal1.append(['/eos/user/t/twamorka/Apr3_2018_pt0/sig60.root','Sig60GeV',4,36*0.001*1000*10/198014])

#Signal1.append(['../TreeSkimmerPy/Mar3_2018/sig60.root','Sig60GeV',4,36*0.001*1000*10/198014]) ##signal region
#Signal1.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/sig60_skim.root','Sig60GeV',4,36*0.001*1000*10/198014]) ## control region
#Signal1.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/sig60_skim.root','Sig60GeV',4,36*0.001*1000*10000/198014]) ## 3 photon signal region
#Signal1.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Cat_4Gamma/sig20.root','Sig20GeV',4,36*0.001*1000*10/200000])
#Signal1.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Oct25_skimtrees/sig60.root','Sig60GeV',4,36*0.001*1000*10/195505])
#Signal2 = []
#Signal2.append(['../TreeSkimmerPy/Mar3_2018/sig35.root','Sig35GeV',2,36*0.001*1000*10/200000]) ##signal region
#Signal2.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/sig45_skim.root','Sig45GeV',2,36*0.001*1000*10/198033]) ## control region
#Signal2.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/sig45_skim.root','Sig45GeV',2,36*0.001*1000*10000/198033]) ## 3 photon signal region
#Signal2.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Cat_4Gamma/sig15.root','Sig15GeV',2,36*0.001*1000*10/200000])
#Signal2.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Oct25_skimtrees2/sig5.root','Sig5GeV',2,36*0.001*1000*10/200000])
#Signal3 = []
#Signal3.append(['../TreeSkimmerPy/Mar3_2018/sig20.root','Sig20GeV',3,36*0.001*1000*10/200000]) ##signal region
#Signal3.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/sig25_skim.root','Sig25GeV',3,36*0.001*1000*10/200000]) ## control region
#Signal3.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/sig25_skim.root','Sig25GeV',3,36*0.001*1000*10000/200000])  ## 3 photoni signal region
#Signal3.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Cat_4Gamma/sig10.root','Sig10GeV',3,36*0.001*1000*10/195505])
#Signal3.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Oct25_skimtrees2/sig1.root','Sig1GeV',3,36*0.001*1000*10/200000])
#Signal4 = []
#Signal4.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Oct25_skimtrees/sig10.root','Sig10GeV',6,36*0.001*1000*10/195505]) ##signal region
#Signal4.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/control_fake1/sig10_skim.root','Sig10GeV',6,36*0.001*1000*10/195505]) ## control region
#Signal4.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_3/sig10_skim.root','Sig10GeV',6,36*0.001*1000*10000/195505])  ## 3 photon signal region
#Signal4.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Cat_4Gamma/sig5.root','Sig5GeV',6,36*0.001*1000*10/200000])
#Signal4.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Oct25_skimtrees2/sig0p1.root','Sig0p1GeV',6,36*0.001*1000*10/200000])

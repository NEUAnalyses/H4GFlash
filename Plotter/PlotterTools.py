from ROOT import *

## Cuts to selection
Cuts = 'tp_mass > 100 && tp_mass < 180 && dp1_mass/tp_mass < 0.55 && dp2_mass/tp_mass < 0.50'
#Cuts = 'tp_mass > 100 && tp_mass < 180'# && dp1_mass/tp_mass < 0.6 && dp2_mass/tp_mass < 0.6'
#Cuts = 'tp_mass > 100 && tp_mass < 180 && dp1_mass < 65 && dp2_mass < 65'# && dp1_mass/tp_mass < 0.6 && dp2_mass/tp_mass < 0.6'
#Cuts = ''
## Plots output location
outputLoc = '/afs/cern.ch/user/t/twamorka/www/H4G/HighMass/'

##Variables to be plotted
#[ name of tree branch, name of pdf file, name of variable, number of bins, min bin, max bin]
Vars = []
Vars.append([ 'p1_pt', 'p1_pt', ';E_{T}(#gamma-1) [GeV];Normalized Yields', 100, 25, 125])
Vars.append([ 'p2_pt', 'p2_pt', ';E_{T}(#gamma-2) [GeV];Normalized Yields', 100, 10, 110])
Vars.append([ 'p3_pt', 'p3_pt', ';E_{T}(#gamma-3) [GeV];Normalized Yields', 100, 10, 110])
Vars.append([ 'p4_pt', 'p4_pt', ';E_{T}(#gamma-4) [GeV];Normalized Yields', 100, 10, 45])
Vars.append([ 'p1_eta', 'p1_eta', ';#eta(#gamma-1);Normalized Yields', 100, -3, 3])
Vars.append([ 'p2_eta', 'p2_eta', ';#eta(#gamma-2);Normalized Yields', 100, -3, 3])
Vars.append([ 'p3_eta', 'p3_eta', ';#eta(#gamma-3);Normalized Yields', 100, -3, 3])
Vars.append([ 'p4_eta', 'p4_eta', ';#eta(#gamma-4);Normalized Yields', 100, -3, 3])
Vars.append([ 'tp_mass', 'tp_mass', ';M(#gamma#gamma#gamma#gamma) [GeV];Normalized Yields', 100, 100, 180])
Vars.append([ 'dp1_mass', 'dp1_mass', ';M(#gamma#gamma-1) [GeV];Normalized Yields', 100, 0, 120])
Vars.append([ 'dp1_mass/tp_mass', 'dp1_mass_over_tp_mass', ';M(#gamma#gamma-1)/M(#gamma#gamma#gamma#gamma);Normalized Yields', 100, 0, 1.0])
Vars.append([ 'dp2_mass', 'dp2_mass', ';M(#gamma#gamma-2) [GeV];Normalized Yields', 100, 0, 120])
Vars.append([ 'dp2_mass/tp_mass', 'dp2_mass_over_tp_mass', ';M(#gamma#gamma-2)/M(#gamma#gamma#gamma#gamma);Normalized Yields', 100, 0, 1.0])
Vars.append([ '(fabs(dp1_mass-dp2_mass)/(dp1_mass + dp2_mass))', 'dp_massdiff', ';|U_{M}|;Normalized Yields', 100, 0, 1])
Vars.append([ 'p1_mva', 'p1_mva', ';MVA score (#gamma-1); Normalized Yields',100,-3,3])
Vars.append([ 'p2_mva', 'p2_mva', ';MVA score (#gamma-2); Normalized Yields',100,-3,3])
Vars.append([ 'p3_mva', 'p3_mva', ';MVA score (#gamma-3); Normalized Yields',100,-3,3])
Vars.append([ 'p4_mva', 'p4_mva', ';MVA score (#gamma-4); Normalized Yields',100,-3,3])
Vars.append([ 'p_mindr','p_mindr',';minDR; Normalized Yields',100,0,4])
Vars.append([ '(dp1_mass - dp2_mass)/tp_mass','|U|',';|U|; Normalized Yields',100,0,1])



#Vars = []
#Vars.append([ 'v_pho_pt', 'v_pho_pt', ';E_{T}(#gamma) [GeV];Normalized Yields', 50, 0, 150])
#Vars.append([ 'v_pho_eta', 'v_pho_eta', ';Eta}(#gamma) [GeV];Normalized Yields', 50, -3, 3])
#Vars.append([ 'v_pho_mva', 'v_pho_mva', ' ; #gamma MVA score ; Normalized Yields', 50,-1.5,1.5])
#Vars.append([ 'v_pho_r9', 'v_pho_r9', '; R9 ; Normalized Yields', 50,0,1.5])
#Vars.append([ 'v_pho_full5x5_r9', 'v_pho_full5x5_r9', '; Full 5X5 R9 ; Normalized Yields', 50,0,2])
#Vars.append([ 'v_pho_chargedHadronIso','v_pho_chargedHadronIso', ';ChargedHadronIso ; Normalized Yields', 50,0,20])
#Vars.append([ 'v_pho_hadronicOverEm','v_pho_hadronicOverEm', '; HadronicoverEm ; Normalized Yields', 50,0,0.6])
#Vars.append([ 'v_pho_hasPixelSeed', 'v_pho_hasPixelSeed', ';PixelSeed ; Normalized Yields', 50,0,1.5])
#Vars.append([ '((v_pho_chargedHadronIso)/(v_pho_pt))','ChargedHadronIsooverPt',';ChargedHadronIsooverPt ;Normalized Yields', 50,0,5])
#Vars.append([ 'v_pho_phi', 'v_pho_phi', ';Phi(#gamma) [GeV];Normalized Yields', 100, -4, 4])
#Vars.append([ 'n_pho','n_pho',';Number of #gamma ; Normalized Yields',100,0,9])
#Vars.append([ 'v_pho_sigmaEtaEta','v_pho_sigmaEtaEta',';{Sigma}(#eta#eta);Normalized Yields',100,0,0.04])
#Vars.append([ 'v_pho_full5x5_sigmaEtaEta','v_pho_full5x5_sigmaEtaEta',';Sigma(#eta#eta);Normalized Yields',100,0,0.04])
#Vars.append([ 'v_pho_full5x5_sigmaIetaIeta','v_pho_full5x5_sigmaIetaIeta',';SigmaI(#eta#eta);Normalized Yields',100,0.005,0.01])
#Vars.append([ 'v_pho_mindr','v_pho_mindr',';minDR;Normalized Yields',100,0,3])

Gen=[]

Gen.append([ 'v_gen_mindr','v_gen_mindr',';gen_mindr;Normalized Yields',100,0,2])

H4GFiles = []

H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig0p1.root','m(A) = 0.1GeV',1,0,1])
H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig1.root','m(A) = 1 GeV', kRed, 0, 1])
#H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig5.root','m(A) = 5 GeV', kBlue, 0, 1])
H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig10.root','m(A) = 10 GeV', kGreen+3, 0, 1])
H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig15.root','m(A)  = 15 GeV',kBlue+1,0,1])
H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig20.root','m(A)  = 20 GeV',kViolet-5,0,1])
#H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig25.root','m(A)  = 25 GeV',kRed-6,0,1])
H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig30.root','m(A)  = 30 GeV',kBlue-9,0,1])
H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig35.root','m(A)  = 35 GeV',kGreen-6,0,1])
#H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig40.root','m(A)  = 40 GeV',kGreen-2,0,1])
H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig45.root','m(A)  = 45 GeV',kOrange+10,0,1])
#H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig50.root','m(A)  = 50 GeV',kOrange+3,0,1])
H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig55.root','m(A) = 55 GeV', kOrange, 0, 1])
H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig60.root','m(A)  = 60 GeV',kPink-5,0,1])

Genfiles = []

#Genfiles.append(['/afs/cern.ch/user/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/AnalyzerPy/gen_sig0p1.root','m(A) = 0.1GeV',1,0,1])
Genfiles.append(['/afs/cern.ch/user/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/AnalyzerPy/gen_sig1.root','m(A) = 1 GeV', kRed, 0, 1])
Genfiles.append(['/afs/cern.ch/user/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/AnalyzerPy/gen_sig5.root','m(A) = 5 GeV', kBlue, 0, 1])
Genfiles.append(['/afs/cern.ch/user/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/AnalyzerPy/gen_sig10.root','m(A) = 10 GeV', kGreen+3, 0, 1])
Genfiles.append(['/afs/cern.ch/user/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/AnalyzerPy/gen_sig15.root','m(A)  = 15 GeV',kBlue+1,0,1])
Genfiles.append(['/afs/cern.ch/user/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/AnalyzerPy/gen_sig20.root','m(A)  = 20 GeV',kViolet-5,0,1])
Genfiles.append(['/afs/cern.ch/user/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/AnalyzerPy/gen_sig25.root','m(A)  = 25 GeV',kRed-6,0,1])
Genfiles.append(['/afs/cern.ch/user/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/AnalyzerPy/gen_sig30.root','m(A)  = 30 GeV',kBlue-9,0,1])
Genfiles.append(['/afs/cern.ch/user/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/AnalyzerPy/gen_sig35.root','m(A)  = 35 GeV',kGreen-6,0,1])
Genfiles.append(['/afs/cern.ch/user/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/AnalyzerPy/gen_sig40.root','m(A)  = 40 GeV',kGreen-2,0,1])
Genfiles.append(['/afs/cern.ch/user/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/AnalyzerPy/gen_sig45.root','m(A)  = 45 GeV',kOrange+10,0,1])
Genfiles.append(['/afs/cern.ch/user/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/AnalyzerPy/gen_sig50.root','m(A)  = 50 GeV',kOrange+3,0,1])
Genfiles.append(['/afs/cern.ch/user/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/AnalyzerPy/gen_sig55.root','m(A) = 55 GeV', kOrange, 0, 1])
Genfiles.append(['/afs/cern.ch/user/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/AnalyzerPy/gen_sig60.root','m(A)  = 60 GeV',kPink-5,0,1])


##Files to be plotted
#[ file name, legend, line color, fill color, normalization]
Files = []

#Files.append(['/afs/cern.ch/work/t/torimoto/public/forTanvi/skimmedtrees/E.root','Data',33,33,1])
#Files.append(['/afs/cern.ch/work/t/torimoto/public/forTanvi/skimmedtrees/D.root','Data',33,33,1])
#Files.append(['/afs/cern.ch/work/t/torimoto/public/forTanvi/skimmedtrees/C_2.root','Data',33,33,1])
#Files.append(['/afs/cern.ch/work/t/torimoto/public/forTanvi/skimmedtrees/C_1.root','Data',33,33,1])
#Files.append(['/afs/cern.ch/work/t/torimoto/public/forTanvi/skimmedtrees/B_2.root','Data',33,33,1])
#Files.append(['/afs/cern.ch/work/t/torimoto/public/forTanvi/skimmedtrees/B_1.root','Data',33,33,1])
#Files.append(['/afs/cern.ch/work/t/torimoto/public/forTanvi/skimmedtrees/F.root','Data',33,33,1])
#Files.append(['/afs/cern.ch/work/t/torimoto/public/forTanvi/skimmedtrees/G.root','Data',33,33,1])
#Files.append(['/afs/cern.ch/work/t/torimoto/public/forTanvi/skimmedtrees/H_1.root','Data',33,33,1])
#Files.append(['/afs/cern.ch/work/t/torimoto/public/forTanvi/skimmedtrees/H_2.root','Data',33,33,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_2/sig0p1_skim.root','m(A) = 0.1GeV',1,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_2/sig1_skim.root', 'm(A) = 1 GeV', kRed, 0, 1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_2/sig5_skim.root', 'm(A) = 5 GeV', kBlue, 0, 1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/skim_2/sig10_skim.root', 'm(A) = 10 GeV', kGreen+3, 0, 1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/sep14_skim/sig15_skim.root','m(A)  = 15 GeV',kBlue+1,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/sep14_skim/sig20_skim.root','m(A)  = 20 GeV',kViolet-5,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/sep14_skim/sig25_skim.root','m(A)  = 25 GeV',kRed-6,0,1])
Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/sep14_skim/sig30_skim.root','m(A)  = 30 GeV',kBlue-9,0,1])
Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/sep14_skim/sig35_skim.root','m(A)  = 35 GeV',kGreen-6,0,1])
Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/sep14_skim/sig40_skim.root','m(A)  = 40 GeV',kGreen-2,0,1])
Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/sep14_skim/sig45_skim.root','m(A)  = 45 GeV',kOrange+10,0,1])
Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/sep14_skim/sig50_skim.root','m(A)  = 50 GeV',kOrange+3,0,1])
Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/sep14_skim/sig55_skim.root', 'm(A) = 55 GeV', kOrange, 0, 1])
Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/sep14_skim/sig60_skim.root','m(A)  = 60 GeV',kPink-5,0,1])


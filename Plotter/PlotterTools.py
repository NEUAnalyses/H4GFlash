from ROOT import *

## Cuts to selection
#Cuts = 'tp_mass > 100 && tp_mass < 180 && dp1_mass/tp_mass < 0.55 && dp2_mass/tp_mass < 0.50'
#Cuts = 'tp_mass > 100 && tp_mass < 180'# && dp1_mass/tp_mass < 0.6 && dp2_mass/tp_mass < 0.6'
#Cuts = 'tp_mass > 100 && tp_mass < 180 && dp1_mass < 65 && dp2_mass < 65'# && dp1_mass/tp_mass < 0.6 && dp2_mass/tp_mass < 0.6'
#Cuts = 'abs(gen1_eta)<2.5 && abs(gen2_eta)<2.5 && abs(gen3_eta)<2.5 && abs(gen4_eta)<2.5'
#Cuts = 'abs(isopho1_eta_case2)<2.5 && abs(isopho2_eta_case2)<2.5 && abs(isopho3_eta_case2)<2.5 && abs(misspho_eta_case2)<2.5'
#Cuts = 'abs(p1_eta_case1)<2.5 && abs(p2_eta_case1)<2.5 && abs(p3_eta_case1)<2.5 && abs(p4_eta_case1)<2.5 && p1_pt_case1 > 15 && p2_pt_case1 > 15 && p3_pt_case1 > 10 && p4_pt_case1 > 10'
#Cuts = 'abs(p1_eta_case1)<2.5 && abs(p2_eta_case1)<2.5 && abs(p3_eta_case1)<2.5 && abs(p4_eta_case1)<2.5 && p1_pt_case1 > 15 && p2_pt_case1 > 15 && p3_pt_case1 > 10 && p4_pt_case1 < 10'
#Cuts = 'abs(isopho1_eta_case2)<2.5 && abs(isopho2_eta_case2)<2.5 && abs(fatpho_eta_case2)<2.5 && fatpho_pt_case2 > 15 && isopho1_pt_case2 > 10 && isopho2_pt_case2 >10'
#Cuts = 'abs(isopho1_eta_case2)<2.5 && abs(isopho2_eta_case2)<2.5 && abs(fatpho_eta_case2)<2.5 && fatpho_pt_case2 > 15 && isopho1_pt_case2 > 10 && isopho2_pt_case2 <10'
#Cuts = 'abs(fatpho1_eta_case3)<2.5 && abs(fatpho2_eta_case3)<2.5 && fatpho1_pt_case3 >15 && fatpho2_pt_case3 > 15 '
#Cut_resolved = 'v_genmatch_pt[0]<0'
#Cut_fat = 'v_genmatch_pt[0]>0'
#Cut = 'abs(p1_eta) < 1.479 && abs(p2_eta) < 1.479 && abs(p3_eta) < 1.479 && abs(p4_eta) < 1.479'
Cut_fat = 'v_fatpho1_pt < 0 && v_fatpho_pt > 0 && v_fatpho_pt > 60 && abs(v_pho_eta) < 1.479 '
Cut_resolved = 'v_genmatch_pt<0'
## Plots output location
#outputLoc = '/afs/cern.ch/user/t/twamorka/www/H4G_plots/H4GTreeLevel/'
#outputLoc = '/afs/cern.ch/user/t/twamorka/www/H4G_forPrelim/'
#outputLoc = '/afs/cern.ch/user/t/twamorka/www/H4G_forPrelim/SignalOnly/4Gamma/'
outputLoc = '/afs/cern.ch/user/t/twamorka/www/2018_HGGGG/old/'


nbins = 70
##Variables to be plotted
#[ name of tree branch, name of pdf file, name of variable, number of bins, min bin, max bin]
Vars = []

#Vars.append(['v_pho_hadronicOverEm[0]','v_pho_hadronicOverEm[0]',';HoE ; Normalized Yields',100,0,1])
#Vars.append(['v_pho_e3x3[0]','v_pho_e3x3[0]',';Energy 3x3(#gamma_{1}) ; Normalized Yields',100,0,1400])
#Vars.append(['v_pho_r9[0]','v_pho_r9[0]',';R9 ; Normalized Yields',100,0,1.2])
#Vars.append(['v_pho_r9[0]','v_pho_r9[0]',';R9(#gamma_{1}) ; Normalized Yields',100,0,1.5])
#Vars.append(['v_pho_pt[0]','v_pho_pt[0]',';P_{T}(#gamma_{1}) ; Normalized Yields',100,0,400])
#Vars.append(['v_pho_eta[0]','v_pho_eta[0]',';#eta(#gamma_{1}) ; Normalized Yields',100,-3.5,3.5])
#Vars.append(['v_pho_phi[0]','v_pho_phi[0]',';#phi(#gamma_{1}) ; Normalized Yields',100,-4.0,4.0])
#Vars.append(['v_pho_mva[0]','v_pho_mva[0]',';MVA(#gamma_{1}) ; Normalized Yields',100,-1.5,1.5])
#Vars.append(['v_pho_ecalIso[0]','v_pho_ecalIso[0]',';ECAL Iso(#gamma_{1}) ; Normalized Yields',100,0,200.0])
#Vars.append(['v_pho_e[0]','v_pho_e[0]',';Energy(#gamma_{1}) ; Normalized Yields',100,0,900])
#Vars.append(['v_pho_e5x5[0]','v_pho_e5x5[0]',';Energy 5x5(#gamma_{1}) ; Normalized Yields',100,0,900])
#Vars.append(['v_pho_full5x5_e5x5[0]','v_pho_full5x5_e5x5[0]',';Energy Full 5x5(#gamma_{1}) ; Normalized Yields',100,0,900])
#Vars.append(['v_pho_sigmaEtaEta[0]','v_pho_sigmaEtaEta[0]',';Sigma #eta#eta(#gamma_{1}) ; Normalized Yields',100,0,0.09])
#Vars.append(['v_pho_full5x5_sigmaEtaEta[0]','v_pho_full5x5_sigmaEtaEta[0]',';Full 5x5 Sigma #eta#eta(#gamma_{1}) ; Normalized Yields',100,0,0.09])
#Vars.append(['v_pho_ecalPFClusterIso[0]','v_pho_ecalPFClusterIso[0]',';ECAL PF Cluster Isolation(#gamma_{1}) ; Normalized Yields',100,0,200])
#Vars.append(['v_pho_trackIso[0]','v_pho_trackIso[0]',';Track Isolation ; Normalized Yields',100,0,20])
#Vars.append(['v_pho_chargedHadronIso[0]','v_pho_chargedHadronIso',';Charged Hadron Isolation(#gamma_{1}) ; Normalized Yields',100,0,10])
Vars.append(['v_fatpho_pt / v_pho_pt','Ratio Variable_check_new',';Energy Ratio ; Normalized Yields',100,0,2])







# Vars.append(['gen1_pt', 'gen1_pt', ';P_{T}(#gamma_{1}) [GeV];Normalized Yields', 100, 0, 110])
# Vars.append(['gen2_pt', 'gen2_pt', ';P_{T}(#gamma_{2}) [GeV];Normalized Yields', 100, 0, 110])
# Vars.append(['gen3_pt', 'gen3_pt', ';P_{T}(#gamma_{3}) [GeV];Normalized Yields', 100, 0, 110])
# Vars.append(['gen4_pt', 'gen4_pt', ';P_{T}(#gamma_{4}) [GeV];Normalized Yields', 100, 0, 110])
# Vars.append(['gen1_eta', 'gen1_eta', ';#eta(#gamma_{1});Normalized Yields', 100, -3.0, 3.0])
# Vars.append(['gen2_eta', 'gen2_eta', ';#eta(#gamma_{2});Normalized Yields', 100, -3.0, 3.0])
# Vars.append(['gen3_eta', 'gen3_eta', ';#eta(#gamma_{3});Normalized Yields', 100, -3.0, 3.0])
# Vars.append(['gen4_eta', 'gen4_eta', ';#eta(#gamma_{4});Normalized Yields', 100, -3.0, 3.0])
# Vars.append(['gen12_mass', 'gen12_mass', ';M(#gamma_{12});Normalized Yields', 100, 0, 100])
# Vars.append(['gen13_mass', 'gen13_mass', ';M(#gamma_{13});Normalized Yields', 100, 0, 100])
# Vars.append(['gen14_mass', 'gen14_mass', ';M(#gamma_{14});Normalized Yields', 100, 0, 100])
# Vars.append(['gen23_mass', 'gen23_mass', ';M(#gamma_{23});Normalized Yields', 100, 0, 100])
# Vars.append(['gen24_mass', 'gen24_mass', ';M(#gamma_{24});Normalized Yields', 100, 0, 100])
# Vars.append(['gen34_mass', 'gen34_mass', ';M(#gamma_{34});Normalized Yields', 100, 0, 100])
# Vars.append(['gen12dr','gen12dr',';#Delta R(#gamma_{12});Normalized Yields',100,0,0.5])
# Vars.append(['gen13dr','gen13dr',';#Delta R(#gamma_{13});Normalized Yields',100,0,0.5])
# Vars.append(['gen14dr','gen14dr',';#Delta R(#gamma_{14});Normalized Yields',100,0,0.5])
# Vars.append(['gen23dr','gen23dr',';#Delta R(#gamma_{23});Normalized Yields',100,0,0.5])
# Vars.append(['gen24dr','gen24dr',';#Delta R(#gamma_{24});Normalized Yields',100,0,0.5])
# Vars.append(['gen34dr','gen34dr',';#Delta R(#gamma_{34});Normalized Yields',100,0,0.5])
# Vars.append(['gen_mindr','gen_mindr',';Minimum #Delta R;Normalized Yields',100,0,0.5])
# Vars.append(['gen_maxdr','gen_maxdr',';Maximum #Delta R;Normalized Yields',100,0,0.5])
# Vars.append(['tp_mass', 'tp_mass', ';M(#gamma#gamma#gamma#gamma) [GeV];Normalized Yields', 100, 110, 140])


#Vars.append([ 'p1_pt', 'p1_pt', ';P_{T}(#gamma_{1}) [GeV];Normalized Yields', 100, 0, 110])
#Vars.append([ 'p2_pt', 'p2_pt', ';P_{T}(#gamma_{2}) [GeV];Normalized Yields', 100, 0, 110])
#Vars.append([ 'p3_pt', 'p3_pt', ';P_{T}(#gamma_{3}) [GeV];Normalized Yields', 100, 0, 110])
#Vars.append([ 'p4_pt', 'p4_pt', ';P_{T}(#gamma_{4}) [GeV];Normalized Yields', 100, 0, 110])
#Vars.append([ 'p1_eta', 'p1_eta', ';#eta(#gamma_{1});Normalized Yields', 100, -3.0, 3.0])
#Vars.append([ 'p2_eta', 'p2_eta', ';#eta(#gamma_{2});Normalized Yields', 100, -3.0, 3.0])
#Vars.append([ 'p3_eta', 'p3_eta', ';#eta(#gamma_{3});Normalized Yields', 100, -3.0, 3.0])
#Vars.append([ 'p4_eta', 'p4_eta', ';#eta(#gamma_{4});Normalized Yields', 100, -3.0, 3.0])
#Vars.append([ 'p1_phi', 'p1_phi', ';#phi(#gamma_{1});Normalized Yields', 100, -3.5, 3.5])
#Vars.append([ 'p2_phi', 'p2_phi', ';#phi(#gamma_{2});Normalized Yields', 100, -3.5, 3.5])
#Vars.append([ 'p3_phi', 'p3_phi', ';#phi(#gamma_{3});Normalized Yields', 100, -3.5, 3.5])
#Vars.append([ 'p4_phi', 'p4_phi', ';#phi(#gamma_{4});Normalized Yields', 100, -3.5, 3.5])
#Vars.append([ 'p1_M', 'p1_M', ';M(#gamma_{1});Normalized Yields', 100, 0, 10])
#Vars.append([ 'p2_M', 'p2_M', ';M(#gamma_{2});Normalized Yields', 100, 0, 10])
#Vars.append([ 'p3_M', 'p3_M', ';M(#gamma_{3});Normalized Yields', 100, 0, 10])
#Vars.append([ 'p4_M', 'p4_M', ';M(#gamma_{4});Normalized Yields', 100, 0, 10])
#Vars.append([ 'p1_mva', 'p1_mva', ';MVA(#gamma_{1});Normalized Yields', 100, -1.5, 1.5])
#Vars.append([ 'p2_mva', 'p2_mva', ';MVA(#gamma_{2});Normalized Yields', 100, -1.5, 1.5])
#Vars.append([ 'p3_mva', 'p3_mva', ';MVA(#gamma_{3});Normalized Yields', 100, -1.5, 1.5])
#Vars.append([ 'p4_mva', 'p4_mva', ';MVA(#gamma_{4});Normalized Yields', 100, -1.5, 1.5])
#Vars.append([ 'p1_r9', 'p1_r9', ';R9(#gamma_{1});Normalized Yields', 100, 0, 1.2])
#Vars.append([ 'p2_r9', 'p2_r9', ';R9(#gamma_{2});Normalized Yields', 100, 0, 1.2])
#Vars.append([ 'p3_r9', 'p3_r9', ';R9(#gamma_{3});Normalized Yields', 100, 0, 1.2])
#Vars.append([ 'p4_r9', 'p4_r9', ';R9(#gamma_{4});Normalized Yields', 100, 0, 1.2])
#Vars.append([ 'p1_full5x5_r9', 'p1_full5x5_r9', ';Full 5X5 R9(#gamma_{1});Normalized Yields', 100, 0, 2])
#Vars.append([ 'p2_full5x5_r9', 'p2_full5x5_r9', ';Full 5X5 R9(#gamma_{2});Normalized Yields', 100, 0, 2])
#Vars.append([ 'p3_full5x5_r9', 'p3_full5x5_r9', ';Full 5X5 R9(#gamma_{3});Normalized Yields', 100, 0, 2])
#Vars.append([ 'p4_full5x5_r9', 'p4_full5x5_r9', ';Full 5X5 R9(#gamma_{4});Normalized Yields', 100, 0, 2])
#Vars.append([ 'p1_full5x5_sigmaIetaIeta', 'p1_full5x5_sigmaIetaIeta_EB', ';Full 5X5 #sigma_{i#etai#eta}(#gamma_{1});Normalized Yields', 100, 0, 0.012])
#Vars.append([ 'p2_full5x5_sigmaIetaIeta', 'p2_full5x5_sigmaIetaIeta_EB', ';Full 5X5 #sigma_{i#etai#eta}(#gamma_{2});Normalized Yields', 100, 0, 0.012])
#Vars.append([ 'p3_full5x5_sigmaIetaIeta', 'p3_full5x5_sigmaIetaIeta_EB', ';Full 5X5 #sigma_{i#etai#eta}(#gamma_{3});Normalized Yields', 100, 0, 0.012])
#Vars.append([ 'p4_full5x5_sigmaIetaIeta', 'p4_full5x5_sigmaIetaIeta_EB', ';Full 5X5 #sigma_{i#etai#eta}(#gamma_{4});Normalized Yields', 100, 0, 0.012])
#Vars.append([ 'p1_full5x5_sigmaEtaEta', 'p1_full5x5_sigmaEtaEta_EB', ';Full 5X5 #sigma_{#eta#eta}(#gamma_{1});Normalized Yields', 100, 0, 0.012])
#Vars.append([ 'p2_full5x5_sigmaEtaEta', 'p2_full5x5_sigmaEtaEta_EB', ';Full 5X5 #sigma_{#eta#eta}(#gamma_{2});Normalized Yields', 100, 0, 0.012])
#Vars.append([ 'p3_full5x5_sigmaEtaEta', 'p3_full5x5_sigmaEtaEta_EB', ';Full 5X5 #sigma_{#eta#eta}(#gamma_{3});Normalized Yields', 100, 0, 0.012])
#Vars.append([ 'p4_full5x5_sigmaEtaEta', 'p4_full5x5_sigmaEtaEta_EB', ';Full 5X5 #sigma_{#eta#eta}(#gamma_{4});Normalized Yields', 100, 0, 0.012])
#Vars.append([ 'p1_sigmaEtaEta', 'p1_sigmaEtaEta_EB', ';#sigma_{#eta#eta}(#gamma_{1});Normalized Yields', 100, 0, 0.012])
#Vars.append([ 'p2_sigmaEtaEta', 'p2_sigmaEtaEta_EB', ';#sigma_{#eta#eta}(#gamma_{2});Normalized Yields', 100, 0, 0.012])
#Vars.append([ 'p3_sigmaEtaEta', 'p3_sigmaEtaEta_EB', ';#sigma_{#eta#eta}(#gamma_{3});Normalized Yields', 100, 0, 0.012])
#Vars.append([ 'p4_sigmaEtaEta', 'p4_sigmaEtaEta_EB', ';#sigma_{#eta#eta}(#gamma_{4});Normalized Yields', 100, 0, 0.012])
#Vars.append(['p1_hadronicOverEm','p1_hadronicOverEm',';HadronicOverEm(#gamma_{1});Normalized Yields',100,0,0.08])
#Vars.append(['p2_hadronicOverEm','p2_hadronicOverEm',';HadronicOverEm(#gamma_{2});Normalized Yields',100,0,0.08])
#Vars.append(['p3_hadronicOverEm','p3_hadronicOverEm',';HadronicOverEm(#gamma_{3});Normalized Yields',100,0,0.08])
#Vars.append(['p4_hadronicOverEm','p4_hadronicOverEm',';HadronicOverEm(#gamma_{4});Normalized Yields',100,0,0.08])
#Vars.append([ 'p_mindr','p_mindr',';min #Delta R; Normalized Yields',100,0,4])
#Vars.append([ 'p_maxdr','p_maxdr',';max #Delta R; Normalized Yields',100,0,4])
#Vars.append([ 'p_maxmass','p_maxmass',';max DiPhoton M; Normalized Yields',100,0,120])
#Vars.append([ 'dp1_dr', 'dp1_dr', ';#Delta R DiPhoton_{1};Normalized Yields', 100, 0, 4])
#Vars.append([ 'dp2_dr', 'dp2_dr', ';#Delta R DiPhoton_{2};Normalized Yields', 100, 0, 4])
#Vars.append([ 'dp1_mass', 'dp1_mass', ';M(#gamma#gamma_{1}) [GeV];Normalized Yields', 100, 0, 120])
#Vars.append([ 'dp2_mass', 'dp2_mass', ';M(#gamma#gamma_{2}) [GeV];Normalized Yields', 100, 0, 120])
#Vars.append([ 'dp1_pt', 'dp1_pt', ';P_{T}(#gamma#gamma_{1}) [GeV];Normalized Yields', 100, 0, 120])
#Vars.append([ 'dp2_pt', 'dp2_pt', ';P_{T}(#gamma#gamma_{2}) [GeV];Normalized Yields', 100, 0, 120])
#Vars.append([ 'dp1_eta', 'dp1_eta', ';#eta(#gamma#gamma_{1});Normalized Yields', 100, -3.5, 3.5])
#Vars.append([ 'dp2_eta', 'dp2_eta', ';#eta(#gamma#gamma_{2});Normalized Yields', 100, -3.5, 3.5])
#Vars.append([ 'dp1_phi', 'dp1_phi', ';#phi(#gamma#gamma_{1});Normalized Yields', 100, -3.5, 3.5])
#Vars.append([ 'dp2_phi', 'dp2_phi', ';#phi(#gamma#gamma_{2});Normalized Yields', 100, -3.5, 3.5])
#Vars.append(['tp_mass','tp_mass',';M(#gamma#gamma#gamma#gamma) [GeV]; Normalized Yields',100,60,180])
# Vars.append([ 'tp_eta', 'tp_eta', ';#eta(#gamma#gamma#gamma#gamma);Normalized Yields', 100, -3.5, 3.5])
# Vars.append([ 'tp_phi', 'tp_phi', ';#phi(#gamma#gamma#gamma#gamma);Normalized Yields', 100, -3.5, 3.5])
# Vars.append([ 'tp_pt', 'tp_pt', ';P_{T}(#gamma#gamma#gamma#gamma);Normalized Yields', 100, 0, 200])

#Vars.append([ 'p1_pt_case1', 'p1_pt_case1', ';P_{T}(#gamma_{1}) [GeV];Normalized Yields', 100, 0, 110])
#Vars.append([ 'p2_pt_case1', 'p2_pt_case1', ';P_{T}(#gamma_{2}) [GeV];Normalized Yields', 100, 0, 110])
#Vars.append([ 'p3_pt_case1', 'p3_pt_case1', ';P_{T}(#gamma_{3}) [GeV];Normalized Yields', 100, 0, 110])
#Vars.append([ 'p4_pt_case1', 'p4_pt_case1', ';P_{T}(#gamma_{4}) [GeV];Normalized Yields', 100, 0, 110])
#Vars.append([ 'p1_eta_case1', 'p1_eta_case1', ';#eta(#gamma_{1}) [GeV];Normalized Yields', 100, -6, 6])
#Vars.append([ 'p2_eta_case1', 'p2_eta_case1', ';#eta(#gamma_{2}) [GeV];Normalized Yields', 100, -6, 6])
#Vars.append([ 'p3_eta_case1', 'p3_eta_case1', ';#eta(#gamma_{3}) [GeV];Normalized Yields', 100, -6, 6])
#Vars.append([ 'p4_eta_case1', 'p4_eta_case1', ';#eta(#gamma_{4}) [GeV];Normalized Yields', 100, -6, 6])
#Vars.append([ 'p12_dr_case1', 'p12_dr_case1', ';#Delta R(#gamma_{12});Normalized Yields', 100, 0, 4])
#Vars.append([ 'p13_dr_case1', 'p13_dr_case1', ';#Delta R(#gamma_{13});Normalized Yields', 100, 0, 4])
#Vars.append([ 'p14_dr_case1', 'p14_dr_case1', ';#Delta R(#gamma_{14});Normalized Yields', 100, 0, 4])
#Vars.append([ 'p23_dr_case1', 'p23_dr_case1', ';#Delta R(#gamma_{23});Normalized Yields', 100, 0, 4])
#Vars.append([ 'p24_dr_case1', 'p24_dr_case1', ';#Delta R(#gamma_{24});Normalized Yields', 100, 0, 4])
#Vars.append([ 'p34_dr_case1', 'p34_dr_case1', ';#Delta R(#gamma_{34});Normalized Yields', 100, 0, 4])
#Vars.append(['p12_mass_case1', 'p12_mass_case1', ';M(#gamma_{12});Normalized Yields', 100, 0, 100])
#Vars.append(['p13_mass_case1', 'p13_mass_case1', ';M(#gamma_{13});Normalized Yields', 100, 0, 100])
#Vars.append(['p14_mass_case1', 'p14_mass_case1', ';M(#gamma_{14});Normalized Yields', 100, 0, 100])
#Vars.append(['p23_mass_case1', 'p23_mass_case1', ';M(#gamma_{23});Normalized Yields', 100, 0, 100])
#Vars.append(['p24_mass_case1', 'p24_mass_case1', ';M(#gamma_{24});Normalized Yields', 100, 0, 100])
#Vars.append(['p34_mass_case1', 'p34_mass_case1', ';M(#gamma_{34});Normalized Yields', 100, 0, 100])
#Vars.append(['tp_mass_case1','tp_mass_case1',';M(#gamma#gamma#gamma#gamma) [GeV]; Normalized Yields',100,120,130])

#Vars.append([ 'fatpho_pt_case2', 'fatpho_pt_case2', ';P_{T}(#gamma_{Merged}) [GeV];Normalized Yields', 100, 100, 400])
#Vars.append([ 'isopho1_pt_case2', 'isopho1_pt_case2', ';P_{T}(#gamma_{Resolved 1}) [GeV];Normalized Yields', 100, 0, 200])
#Vars.append([ 'isopho2_pt_case2', 'isopho2_pt_case2', ';P_{T}(#gamma_{Resolved 2}) [GeV];Normalized Yields', 100, 0, 200])
#Vars.append([ 'fatpho_eta_case2', 'fatpho_eta_case2', ';#eta(#gamma_{Merged}) [GeV];Normalized Yields', 100, -6, 6])
#Vars.append([ 'isopho1_eta_case2', 'isopho1_eta_case2', ';#eta(#gamma_{Resolved 1}) [GeV];Normalized Yields', 100, -6, 6])
#Vars.append([ 'isopho2_eta_case2', 'isopho2_eta_case2', ';#eta(#gamma_{Resolved 2}) [GeV];Normalized Yields', 100, -6, 6])
#Vars.append([ 'fatpho_isopho1_dr_case2', 'fatpho_isopho1_dr_case2', ';#Delta R(#gamma_{Merged-Resolved 1}) ;Normalized Yields', 100, 0, 4])
#Vars.append([ 'fatpho_isopho2_dr_case2', 'fatpho_isopho2_dr_case2', ';#Delta R(#gamma_{Merged-Resolved 2});Normalized Yields', 100, 0, 4])
#Vars.append([ 'isopho1_isopho2_dr_case2', 'isopho1_isopho2_dr_case2', ';#Delta R(#gamma_{Resolved 1 - Resolved 2});Normalized Yields', 100, 0, 4])
#Vars.append(['fatpho_mass_case2', 'fatpho_mass_case2', ';M(#gamma_{Merged});Normalized Yields', 100, 0, 100])
#Vars.append(['isopho12_mass_case2', 'isopho12_mass_case2', ';M(#gamma_{Resolved 1 - Resolved 2});Normalized Yields', 100, 0, 100])
#Vars.append(['tp_mass_case2','tp_mass_case2',';M(#gamma#gamma#gamma)[GeV]; Normalized Yields',100,120,130])

#Vars.append([ 'fatpho1_pt_case3', 'fatpho1_pt_case3', ';P_{T}(#gamma_{Merged 1}) [GeV];Normalized Yields', 100, 0, 250])
#Vars.append([ 'fatpho2_pt_case3', 'fatpho2_pt_case3', ';P_{T}(#gamma_{Merged 2}) [GeV];Normalized Yields', 100, 0, 250])
#Vars.append([ 'fatpho1_eta_case3', 'fatpho1_eta_case3', ';#eta(#gamma_{Merged 1}) [GeV];Normalized Yields', 100, -6, 6])
#Vars.append([ 'fatpho2_eta_case3', 'fatpho2_eta_case3', ';#eta(#gamma_{Merged 2}) [GeV];Normalized Yields', 100, -6, 6])
#Vars.append([ 'fatpho1_fatpho2_dr_case3', 'fatpho1_fatpho2_dr_case3', ';#Delta R(#gamma_{Merged 1 - Merged 2}) [GeV];Normalized Yields', 100, 0, 4])
#Vars.append(['fatpho1_mass_case3', 'fatpho1_mass_case3', ';M(#gamma_{Merged1});Normalized Yields', 100, 0, 100])
#Vars.append(['fatpho2_mass_case3', 'fatpho2_mass_case3', ';M(#gamma_{Merged2});Normalized Yields', 100, 0, 100])
#Vars.append(['tp_mass_case3','tp_mass_case3',';M(#gamma#gamma)[GeV]; Normalized Yields',100,120,130])









#Vars.append([ 'v_pho_pt[0]', 'v_pho_pt[0]', ';P_{T}(#gamma) [GeV];Normalized Yields', nbins, 0, 125,'P_{T}(#gamma)[GeV]'])
#Vars.append([ 'v_pho_eta', 'v_pho_eta[0]', ';#eta(#gamma);Normalized Yields', nbins, -4, 4,'#eta(#gamma)'])
#Vars.append([ 'v_pho_phi[0]', 'v_pho_phi[0]', ';#phi(#gamma);Normalized Yields', nbins, -4, 4,'#phi(#gamma)'])
#Vars.append([ 'v_pho_mva[0]', 'v_pho_mva[0]', ';MVA(#gamma);Normalized Yields', nbins, -1.5, 1.5,'MVA(#gamma)'])
#Vars.append([ 'v_pho_hadronicOverEm[0]', 'v_pho_hadronicOverEm[0]', ';HoE(#gamma);Normalized Yields', nbins, 0, 1,'HoE(#gamma)'])
#Vars.append([ 'v_pho_r9[0]', 'v_pho_r9[0]', ';R9(#gamma);Normalized Yields', nbins, 0, 1.5,'R9(#gamma)'])
#Vars.append([ 'v_pho_full5x5_r9[0]', 'v_pho_full5x5_r9[0]', ';Full 5x5 R9(#gamma);Normalized Yields', nbins, 0, 1.5,'Full5x5 R9(#gamma)'])
#Vars.append(['p0_sigmaetaeta','p0_sigmaetaeta','; Sigma Eta Eta ; Normalized Yields',100,0,3])





#Vars.append(['misspho_isopho1_dr_case2','misspho_isopho1_dr_case2',';#gamma_{Missing} #gamma_{1} #Delta R; Normalized Yields',100,0,4])
#Vars.append(['misspho_isopho2_dr_case2','misspho_isopho2_dr_case2',';#gamma_{Missing} #gamma_{2} #Delta R; Normalized Yields',100,0,4])
#Vars.append(['misspho_isopho3_dr_case2','misspho_isopho3_dr_case2',';#gamma_{Missing} #gamma_{3} #Delta R; Normalized Yields',100,0,4])
#Vars.append(['min(misspho_isopho1_dr_case2,misspho_isopho2_dr_case2,misspho_isopho3_dr_case2)','mindr_miss_iso',';Min #gamma_{Missing} #gamma_{Resolved} #Delta R;Normalized Yields',100,0,4])

#Vars.append([ 'tp_mass', 'tp_mass', ';M(#gamma#gamma#gamma#gamma) [GeV];Normalized Yields', 100, 100, 180])
#Vars.append([ 'dp1_mass', 'dp1_mass_sigonly', ';M(#gamma#gamma_{1}) [GeV];Normalized Yields', 100, 0, 120])
#Vars.append([ 'dp1_mass/tp_mass', 'dp1_mass_over_tp_mass', ';M(#gamma#gamma-1)/M(#gamma#gamma#gamma#gamma);Normalized Yields', 100, 0, 1.0])
#Vars.append([ 'dp2_mass', 'dp2_mass', ';M(#gamma#gamma-2) [GeV];Normalized Yields', 100, 0, 120])
#Vars.append([ 'dp2_mass/tp_mass', 'dp2_mass_over_tp_mass', ';M(#gamma#gamma-2)/M(#gamma#gamma#gamma#gamma);Normalized Yields', 100, 0, 1.0])
#Vars.append([ '(fabs(dp1_mass-dp2_mass)/(dp1_mass + dp2_mass))', 'dp_massdiff', ';|U_{M}|;Normalized Yields', 100, 0, 1])
#Vars.append([ 'p1_mva', 'p1_mva', ';MVA score (#gamma-1); Normalized Yields',100,-3,3])
#Vars.append([ 'p2_mva', 'p2_mva', ';MVA score (#gamma-2); Normalized Yields',100,-3,3])
#Vars.append([ 'p3_mva', 'p3_mva', ';MVA score (#gamma-3); Normalized Yields',100,-3,3])
#Vars.append([ 'p4_mva', 'p4_mva', ';MVA score (#gamma-4); Normalized Yields',100,-3,3])
#Vars.append([ 'mva_max1','mva_max1',';Max MVA; Normalized Yields',100,-3,3])
#Vars.append([ 'mva_max2','mva_max2',';2nd Max MVA; Normalized Yields',100,-3,3])
#Vars.append([ 'mva_max3','mva_max3',';3rd Max MVA; Normalized Yields',100,-3,3])
#Vars.append([ 'mva_max4','mva_max4',';4th Max MVA; Normalized Yields',100,-3,3])
#Vars.append([ 'dphigh_mass','dphigh_mass',';M(#gamma_{1})+M(#gamma_{2}); Normalized Yields',100,0,120])
#Vars.append([ 'p_mindr','p_mindr',';minDR; Normalized Yields',100,0,6])
#Vars.append([ '(dp1_mass - dp2_mass)/tp_mass','|U|',';|U|; Normalized Yields',100,0,1])
#Vars.append([ 'p1_conversion','p1_conversion',';(#gamma-1);Normalized Yields',100,0,1.5])
#Vars.append([ 'p2_conversion','p2_conversion',';(#gamma-2);Normalized Yields',100,0,1.5])
#Vars.append([ 'p1_r9_2', 'p1_r9_2', ';R9 (#gamma-1); Normalized Yields', 100, 0.65,1.5])
#Vars.append([ 'p2_r9_2', 'p2_r9_2', ';R9 (#gamma-2); Normalized Yields', 100, 0.65,1.5])
#Vars.append([ 'p1_full5x5_r9_2', 'p1_full5x5_r9_2', ';full 5x5 R9 (#gamma-1); Normalized Yields', 100, 0.65,1.5])
#Vars.append([ 'p2_full5x5_r9_2', 'p2_full5x5_r9_2', ';full 5x5 R9 (#gamma-2); Normalized Yields', 100, 0.65,1.5])
#Vars.append([ 'p1_full5x5_sigmaIetaIeta_2','p1_full5x5_sigmaIetaIeta_2',';full5x5_sigmaIetaIeta(#gamma-1);Normalized Yields',100,0,0.05])
#Vars.append([ 'p2_full5x5_sigmaIetaIeta_2','p2_full5x5_sigmaIetaIeta_2',';full5x5_sigmaIetaIeta(#gamma-2);Normalized Yields',100,0,0.05])
#Vars.append([ 'p1_sigmaIphiIphi_2','p1_sigmaIphiIphi_2',';sigmaIphiIphi(#gamma-1);Normalized Yields',100,0,0.08])
#Vars.append([ 'p2_sigmaIphiIphi_2','p2_sigmaIphiIphi_2',';sigmaIphiIphi(#gamma-2);Normalized Yields',100,0,0.06])
#Vars.append(['p1_sigmaEtaEta','p1_sigmaEtaEta',';sigmaEtaEta(#gamma-1);Normalized Yields',100,0,0.04])
#Vars.append(['p2_sigmaEtaEta','p2_sigmaEtaEta',';sigmaEtaEta(#gamma-2);Normalized Yields',100,0,0.04])
#Vars.append(['p1_full5x5_sigmaEtaEta','p1_full5x5_sigmaEtaEta',';full5x5 sigmaEtaEta(#gamma-1);Normalized Yields',100,0,0.04])
#Vars.append(['p1_full5x5_sigmaEtaEta','p1_full5x5_sigmaEtaEta',';full5x5 sigmaEtaEta(#gamma-2);Normalized Yields',100,0,0.04])
#Vars.append(['p1_hadronicOverEm','p1_hadronicOverEm',';HadronicOverEm(#gamma-1);Normalized Yields',100,0,0.08])
#Vars.append(['p2_hadronicOverEm','p2_hadronicOverEm',';HadronicOverEm(#gamma-2;Normalized Yields',100,0,0.08])


#Vars.append(['dp2_dr','dp2_dr',';dp2_dr ;Normalized Yields',100,0,2])
#Vars.append(['tp_mass_2','tp_mass_2',';Max M(#gamma#gamma)[GeV];Normalized Yields',100,0,200])




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

Genfiles.append(['../AnalyzerPy/Mar26_2018/gen1.root','m(a) = 1 GeV', kGreen-2, 0, 1])
Genfiles.append(['../AnalyzerPy/Mar26_2018/gen0p1.root','m(a) = 0.1 GeV', kBlue-9, 0, 1])
#Genfiles.append(['../AnalyzerPy/Mar26_2018/gen30.root','m(a)  = 30 GeV',kBlue-9,0,1])
#Genfiles.append(['../AnalyzerPy/Mar26_2018/gen60.root','m(a)  = 60 GeV',kPink-5,0,1])
#Genfiles.append(['../AnalyzerPy/Mar26_2018/gen40.root','m(a)  = 40 GeV',kRed,0,1])
#Genfiles.append(['../AnalyzerPy/Mar26_2018/gen10.root','m(a)  = 10 GeV',kBlue,0,1])

##Files to be plotted
#[ file name, legend, line color, fill color, normalization]
Files = []
Files.append(['/eos/user/t/twamorka/addall.root','',kRed,kBlack, 0, 1])
#Files.append(['/eos/user/t/twamorka/FatPho0p1_Match0p15/sig60.root','m(a) = 60 GeV ',kViolet-5, 0, 1])
#Files.append(['/eos/user/t/twamorka/FatPho0p1_Match0p15/sig40.root','m(a) = 40 GeV ',kOrange+10, 0, 1])
#Files.append(['/eos/user/t/twamorka/FatPho0p1_Match0p15/sig25.root','m(a) = 25 GeV ',kGreen-6, 0, 1])
#Files.append(['/eos/user/t/twamorka/FatPho0p1_Match0p15/sig15.root','m(a) = 15 GeV ',kPink-5, 0, 1])


#Files.append(['/eos/user/t/twamorka/FatPho0p1_Match0p15/sig60.root','m(a) = 60 GeV','Merged Photon', kViolet-5,0,1])
#Files.append(['/eos/cms/store/user/twamorka/FlatTrees/sig60.root','m(a) = 60 GeV','Merged Photon', kViolet-5,0,1])


#Files.append(['/eos/user/t/twamorka/FatPho0p1_Match0p3/sig30.root','Resolved Photon','Merged Photon', kViolet-5,0,1])

# Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/AnalyzerPy/Genlevel_wcorrection/gen_signal_60.root','m(a) = 60 GeV ',kViolet-5, 0, 1,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/AnalyzerPy/Genlevel_wcorrection/gen_signal_55.root','m(a) = 55 GeV ',kGreen-6, 0, 1])
# Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/AnalyzerPy/Genlevel_wcorrection/gen_signal_50.root','m(a) = 50 GeV ',kOrange+10, 0, 1,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/AnalyzerPy/Genlevel_wcorrection/gen_signal_45.root','m(a) = 45 GeV ',kAzure+2, 0, 1])
# Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/AnalyzerPy/Genlevel_wcorrection/gen_signal_40.root','m(a) = 40 GeV ',kPink+7, 0, 1,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/AnalyzerPy/Genlevel_wcorrection/gen_signal_35.root','m(a) = 35 GeV ',kViolet-5, 0, 1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/AnalyzerPy/Genlevel_wcorrection/gen_signal_30.root','m(a) = 30 GeV ',kGreen+4, 0, 1])
# Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/AnalyzerPy/Genlevel_wcorrection/gen_signal_25.root','m(a) = 25 GeV ',kGreen-7, 0, 1,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/AnalyzerPy/Genlevel_wcorrection/gen_signal_20.root','m(a) = 20 GeV ',kSpring-8, 0, 1])
# Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/AnalyzerPy/Genlevel_wcorrection/gen_signal_15.root','m(a) = 15 GeV ',kYellow+2, 0, 1,1])
# Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/AnalyzerPy/Genlevel_wcorrection/gen_signal_10.root','m(a) = 10 GeV ',kOrange+1, 0, 1,1])
# Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/AnalyzerPy/Genlevel_wcorrection/gen_signal_5.root','m(a) = 5 GeV ',kAzure+10, 0, 1,1])
# Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/AnalyzerPy/Genlevel_wcorrection/gen_signal_1.root','m(a) = 1 GeV ',kAzure-9, 0, 1,7])
# Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/AnalyzerPy/Genlevel_wcorrection/gen_signal_0p1.root','m(a) = 0.1 GeV ',kMagenta, 0, 1,7])
#Files.append(['/eos/user/t/twamorka/Apr3_2018_pt0/sig60.root','m(a) = 60 GeV ',kPink-5, kViolet-5, 0, 1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Mar3_2018/sig0p1.root','m(a)=0.1 GeV',kPink-5,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Mar3_2018/sig1.root','m(a)=1 GeV',kOrange+10,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Mar3_2018/sig10.root','m(a)=10 GeV',kViolet-5,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Mar3_2018/sig20.root','m(a)=20 GeV',kGreen-6,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Mar3_2018/sig35.root','m(a)=35 GeV',kOrange+10,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Mar3_2018/sig60.root','m(a)=60 GeV',kPink-5,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Feb_18/hgg.root','hgg',kGreen-6,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/signal/sig0p1.root','m(a)=0p1GeV',kPink-5,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/signal/sig1.root','m(a)=1GeV',kGreen-6,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/signal/sig5.root','m(a)=5GeV',kOrange+10,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/signal/sig15.root','m(a)=15GeV',kViolet-5,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/signal/sig25.root','m(a)=25GeV',kAzure+2,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/signal/sig35.root','m(a)=35GeV',kYellow-6,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/signal/sig45.root','m(a)=45GeV',kRed,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/signal/sig60.root','m(a)=60GeV',kOrange+3,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/signal/sig0p1.root','m(a)=0p1GeV',kPink-5,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/signal/sig0p1.root','m(a)=0p1GeV',kPink-5,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/signal/sig0p1.root','m(a)=0p1GeV',kPink-5,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/signal/sig0p1.root','m(a)=0p1GeV',kPink-5,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/signal/sig0p1.root','m(a)=0p1GeV',kPink-5,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/signal/sig0p1.root','m(a)=0p1GeV',kPink-5,0,1])


#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/miniaodsim/sig1.root','m(a)=1GeV',kPink-5,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/miniaodsim/sig10.root','m(a)=10GeV',kGreen-6,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/miniaodsim/sig30.root','m(a)=30GeV',kOrange+10,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/miniaodsim/sig45.root','m(a)=45GeV',kViolet-5,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/miniaodsim/sig60.root','m(a)=60GeV',kAzure+2,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/miniaodsim_v2/miniaodsim_20.root','m(a)=20GeV',kViolet+4,0,1])
#Files.append(['/eos/cms/store/user/twamorka/minoaodsim_v2/SUSYGluGluToHToAA_AToGG_M-20_TuneCUETP8M1_13TeV_pythia8/crab_miniaodsim_gen20/171121_125950/0000/miniaodsim_20.root','m(a)=20GeV',kViolet+4,0,1])

#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/miniaodsim/miniaodsim_25.root','m(a)=25GeV',kYellow-6,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/miniaodsim/miniaodsim_30.root','m(a)=30GeV',kGreen+3,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/miniaodsim/miniaodsim_35.root','m(a)=35GeV',kRed,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/miniaodsim/miniaodsim_40.root','m(a)=40GeV',kOrange+3,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/miniaodsim_v2/miniaodsim_45.root','m(a)=45GeV',kPink-9,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/miniaodsim/miniaodsim_50.root','m(a)=50GeV',kBlue+4,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/miniaodsim_v2/miniaodsim_55.root','m(a)=55GeV',kAzure-5,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/miniaodsim_v2/miniaodsim_20.root','m(a)=20GeV',kBlack,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/miniaodsim_v2/miniaodsim_5.root','m(a)=5GeV',kGreen+3.0,1])

#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/gen0p1_aodsim.root','m(a)=0p1 GeV',kPink-5,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/aodsim_0p1.root','m(a)=0p1 GeV',kGreen-6,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/aodsim_1.root','m(a)=1 GeV',kPink,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/aodsim_5.root','m(a)=5 GeV',kOrange+10,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/aodsim_25.root','m(a)=25 GeV',kViolet-5,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/aodsim_45.root','m(a)=45 GeV',kAzure+2,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/LatinoTreesGEN/GenDumper/test/gen60_2.root','m(a)=60 GeV',kViolet+4,0,1])
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
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Skim_2018/sig0p1.root','m(A) = 0.1GeV',1,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Skim_2018_v2/sig10.root', 'm(A) = 10 GeV', kPink-5, 0, 1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Skim_2018_v2/sig25.root', 'm(A) = 25 GeV', kOrange+3, 0, 1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Skim_2018_v2/sig45.root', 'm(A) = 45 GeV', kBlue+1, 0, 1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Skim_2018_v2/sig60.root','m(A)  = 60 GeV',kViolet-5,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/SKim_2018/sig10.root','m(A)  = 10 GeV',kGreen-6,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/SKim_2018/sig5.root','m(A)  = 5 GeV',kOrange+3,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Oct25_skimtrees2/sig0p1.root','m(a)  = 0p1 GeV',kGreen-6,0,1,0])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Oct25_skimtrees/sig1.root','m(a)  = 1 GeV',kGreen-6,0,1,0])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Oct25_skimtrees/sig5.root','m(a)  = 5 GeV',kGreen-2,0,1,0])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Oct25_skimtrees/sig10.root','m(a)  = 10 GeV',kOrange+10,0,1,0])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Oct25_skimtrees2/sig15.root','m(A)  = 15 GeV',kOrange+3,0,1])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/Oct25_skimtrees2/hgg125.root', 'SM H->#gamma#gamma', kOrange+3, kOrange+3, 1,3002])
#Files.append(['/afs/cern.ch/work/t/twamorka/CMSSW_8_0_28/src/flashgg/H4GFlash/TreeSkimmerPy/sep14_skim/sig60_skim.root','m(A)  = 60 GeV',kPink-5,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/sig0p1.root','m(a)=0p1GeV',kPink-5,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/sig1.root','m(a)=1GeV',kGreen-2,0,1])
#Files.append(['/eos/cms/store/user/torimoto/physics/4gamma/Oct25/sig5.root','m(a)=5GeV',kViolet-5,0,1])
#iles.append(['/eos/cms/store/user/twamorka/4gamma/Oct25/hgg125.root','Hgg signal',kPink-10,kPink-10,1])

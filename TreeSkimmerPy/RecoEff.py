from ROOT import *
from array import array
import numpy as np



files = [
         
         "FlatTrees/FatPho0p1_Match0p3/signal_m_0p1.root",
         "FlatTrees/FatPho0p1_Match0p3/signal_m_1.root",
         "FlatTrees/FatPho0p1_Match0p3/signal_m_5.root",
         "FlatTrees/FatPho0p1_Match0p3/signal_m_10.root",
         "FlatTrees/FatPho0p1_Match0p3/signal_m_15.root",
         "FlatTrees/FatPho0p1_Match0p3/signal_m_20.root",
         "FlatTrees/FatPho0p1_Match0p3/signal_m_25.root",
         "FlatTrees/FatPho0p1_Match0p3/signal_m_30.root",
         "FlatTrees/FatPho0p1_Match0p3/signal_m_35.root",
         "FlatTrees/FatPho0p1_Match0p3/signal_m_40.root",
         "FlatTrees/FatPho0p1_Match0p3/signal_m_45.root",
         "FlatTrees/FatPho0p1_Match0p3/signal_m_50.root",
         "FlatTrees/FatPho0p1_Match0p3/signal_m_55.root",
         "FlatTrees/FatPho0p1_Match0p3/signal_m_60.root"
         ]

# for reco-level w/ preselection efficiency
files2 = [
         
         "Apr6_2018_skim/signal_m_Eff_0p1.root",
         "Apr6_2018_skim/signal_m_Eff_1.root",
         "Apr6_2018_skim/signal_m_Eff_5.root",
         "Apr6_2018_skim/signal_m_Eff_10.root",
         "Apr6_2018_skim/signal_m_Eff_15.root",
         "Apr6_2018_skim/signal_m_Eff_20.root",
         "Apr6_2018_skim/signal_m_Eff_25.root",
         "Apr6_2018_skim/signal_m_Eff_30.root",
         "Apr6_2018_skim/signal_m_Eff_35.root",
         "Apr6_2018_skim/signal_m_Eff_40.root",
         "Apr6_2018_skim/signal_m_Eff_45.root",
         "Apr6_2018_skim/signal_m_Eff_50.root",
         "Apr6_2018_skim/signal_m_Eff_55.root",
         "Apr6_2018_skim/signal_m_Eff_60.root"
         ]

masses = [0.1, 1, 5 , 10, 15, 20, 25, 30 ,35, 40, 45, 50, 55, 60]
#masses = [0.1,1,10,25,40,60]

c_2pho = []
c_3pho = []
c_4pho = []
c_otherpho = []

c_2pho_passtrigger = []
c_3pho_passtrigger = []
c_4pho_passtrigger = []
c_2pho_failtrigger = []
c_3pho_failtrigger = []
c_4pho_failtrigger = []

c_4pho_passtrigger_allresolved_inacceptance = []
c_4pho_passtrigger_allresolved_outacceptance = []
c_4pho_other = []

c_3pho_passtrigger_fatpho_inacceptance = []
c_3pho_passtrigger_allresolved_outacceptance = []
c_3pho_other = []

c_2pho_passtrigger_allresolved_outacceptance = []
c_2pho_passtrigger_2fat_inacceptance = []
c_2pho_other = []

pho = []

c_v2_2 = []
c_v2_3 = []
c_v2_4 = []
c_v2_2_sel = []
c_v2_3_sel = []
c_v2_4_sel = []
c_v2_2_presel = []
c_v2_3_presel = []
c_v2_4_presel = []

c_v2_phosel = []
c_v2_presel = []
c_v2_presel_2 = []
c_v2_presel_3 = []
c_v2_presel_4 = []

bins = []
c1 = []
c1_4A = []
c1_3A = []
c1_other = []

c2 = []
c2_4A = []
c2_3A = []
c2_other = []

c3 = []
c3_4A = []
c3_other = []
c4 = []
c4_1 = []
c4_2 = []
c4_other = []
c3_1 = []
c3_2 = []
c3_other = []
c2_1 = []
c2_2 = []
c2_other = []
c4_resolved_passtrigger0 = []
c4_resolved_passtrigger1 = []
c3_resolved = []
c3_fat = []
c4_fat = []

c_Fourpho = []
c_Threepho = []
c_Twopho = []

c_4_case1 = []
c_4_case2 = []
c_4_caseother = []

for i, m in enumerate(masses):
       tch_v2 = TChain("H4GEff")
       tch_v2.AddFile(files2[i])
       totevs_v2=tch_v2.Draw("totevs","1>0")
       
       totevs_v2_phosel=tch_v2.Draw("totevs","cut1==1")
       totevs_v2_presel=tch_v2.Draw("totevs","cut2==1")
       totevs_v2_presel_2=tch_v2.Draw("totevs","cut3==1")
       totevs_v2_presel_3=tch_v2.Draw("totevs","cut4==1")
       totevs_v2_presel_4=tch_v2.Draw("totevs","cut5==1")
       
       totevs_v2_2=tch_v2.Draw("totevs","cut4==1")
       totevs_v2_3=tch_v2.Draw("totevs","cut5==1")
       totevs_v2_4=tch_v2.Draw("totevs","cut3==1")

       totevs_v2_2_sel=tch_v2.Draw("totevs","cut10==1")
       totevs_v2_3_sel=tch_v2.Draw("totevs","cut11==1")
       totevs_v2_4_sel=tch_v2.Draw("totevs","cut9==1")

       totevs_v2_2_presel=tch_v2.Draw("totevs","cut13==1")
       totevs_v2_3_presel=tch_v2.Draw("totevs","cut14==1")
       totevs_v2_4_presel=tch_v2.Draw("totevs","cut20==1")
       
       eff_v2_phosel = float(totevs_v2_phosel)/float(totevs_v2)
       eff_v2_presel = float(totevs_v2_presel)/float(totevs_v2)
       eff_v2_presel_2 = float(totevs_v2_presel_2)/float(totevs_v2)
       eff_v2_presel_3 = float(totevs_v2_presel_3)/float(totevs_v2)
       eff_v2_presel_4 = float(totevs_v2_presel_4)/float(totevs_v2)

       eff_v2_2 = float(totevs_v2_2)/float(totevs_v2)
       eff_v2_3 = float(totevs_v2_3)/float(totevs_v2)
       eff_v2_4 = float(totevs_v2_4)/float(totevs_v2)
       eff_v2_2_sel = float(totevs_v2_2_sel)/float(totevs_v2)
       eff_v2_3_sel = float(totevs_v2_3_sel)/float(totevs_v2)
       eff_v2_4_sel = float(totevs_v2_4_sel)/float(totevs_v2)
       eff_v2_2_presel = float(totevs_v2_2_presel)/float(totevs_v2)
       eff_v2_3_presel = float(totevs_v2_3_presel)/float(totevs_v2)
       eff_v2_4_presel = float(totevs_v2_4_presel)/float(totevs_v2)


       c_v2_phosel.append(eff_v2_phosel)
       c_v2_presel.append(eff_v2_presel)
       c_v2_presel_2.append(eff_v2_presel_2)
       c_v2_presel_3.append(eff_v2_presel_3)
       c_v2_presel_4.append(eff_v2_presel_4)

       c_v2_2.append(eff_v2_2)
       c_v2_3.append(eff_v2_3)
       c_v2_4.append(eff_v2_4)
       c_v2_2_sel.append(eff_v2_2_sel)
       c_v2_3_sel.append(eff_v2_3_sel)
       c_v2_4_sel.append(eff_v2_4_sel)
       c_v2_2_presel.append(eff_v2_2_presel)
       c_v2_3_presel.append(eff_v2_3_presel)
       c_v2_4_presel.append(eff_v2_4_presel)


for i, m in enumerate(masses):
       tch = TChain("H4GSel_0")
       tch.AddFile(files[i])
       totevs = tch.Draw("p0_pt","p0_npho>0")
       
       tch0 = TChain("H4GSel_all")
       tch0.AddFile(files[i])
       totevs0 = tch0.Draw("p_pt","1>0")
       
       tch4 = TChain("H4GSel")
       tch4.AddFile(files[i])
       totevs4 = tch4.Draw("p1_pt","1>0")
       
       tch3 = TChain("H4GSel_3")
       tch3.AddFile(files[i])
       totevs3 = tch3.Draw("p1_pt_3","1>0")
 
       tch2 = TChain("H4GSel_2")
       tch2.AddFile(files[i])
       totevs2 = tch2.Draw("p1_pt_2","1>0")
       
       
       
       Fourpho = TCut('p_npho>3')
       Threepho = TCut('p_npho==3')
       Twopho = TCut('p_npho==2')
       
       
       
       evs_2pho = tch.Draw("p0_pt",TCut('p0_npho==2'))
       evs_3pho = tch.Draw("p0_pt",TCut('p0_npho==3'))
       evs_4pho = tch.Draw("p0_pt",TCut('p0_npho>3'))
       
       evs_2pho_passtrigger = tch.Draw("p0_pt",TCut('p0_npho==2 && p0_passTrigger==1'))
       evs_3pho_passtrigger = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_passTrigger==1'))
       evs_4pho_passtrigger = tch.Draw("p0_pt",TCut('p0_npho>3 && p0_passTrigger==1'))
       
       evs_2pho_failtrigger = tch.Draw("p0_pt",TCut('p0_npho==2 && p0_passTrigger==0'))
       evs_3pho_failtrigger = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_passTrigger==0'))
       evs_4pho_failtrigger = tch.Draw("p0_pt",TCut('p0_npho>3 && p0_passTrigger==0'))
       
       evs_4pho_passtrigger_allresolved_inacceptance = tch.Draw("p0_pt",TCut('p0_npho>3 && p0_passTrigger==1 && p0_resolvedcount==4 && p0_outofptcount==0 && p0_outofetacount==0'))
       evs_4pho_passtrigger_allresolved_outacceptance = tch.Draw("p0_pt",TCut('p0_npho>3 && p0_passTrigger==1 && p0_resolvedcount==4 && ((p0_outofptcount==1 && p0_outofetacount==0) ||(p0_outofptcount==0 && p0_outofetacount==1)||(p0_outofptcount==1 && p0_outofetacount==1))'))
       
       evs_3pho_passtrigger_allresolved_outacceptance = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_passTrigger==1 && p0_resolvedcount==3 '))
       evs_3pho_passtrigger_fatpho_inacceptance = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_passTrigger==1 && p0_resolvedcount==2 && p0_outofptcount == 0 && p0_outofetacount==0 '))
       
       evs_2pho_passtrigger_allresolved_outacceptance = tch.Draw("p0_pt",TCut('p0_npho==2 && p0_passTrigger==1 && p0_resolvedcount==2 '))
       evs_2pho_passtrigger_2fat_inacceptance = tch.Draw("p0_pt",TCut('p0_npho==2 && p0_passTrigger==1 && p0_resolvedcount==0 && p0_outofptcount==0 && p0_outofetacount==0'))
       
       Case1_4 = TCut('p0_npho>3') # events with more than 3 photons
       Case1_3 = TCut('p0_npho==3') # events with exactly 3 photons
       Case1_2 = TCut('p0_npho==2') # events with exactly 2 photons
       
       #Case1_4_case1 = TCut('p1_matchpho_pt <0 && p2_matchpho_pt<0 && p3_matchpho_pt < 0 && p4_matchpho_pt < 0 && passTrigger==1 && p1_pt > 15 && p2_pt > 15 &&p3_pt >10 && p4_pt>10 && abs(p1_eta) < 2.5 && abs(p2_eta)<2.5 && abs(p3_eta) < 2.5 &7 abs(p4_eta)<2.5 ')
       #Case1_4_case2 = TCut('p1_matchpho_pt > 0 && p2_matchpho_pt>0 && p3_matchpho_pt > 0 && p4_matchpho_pt > 0 && passTrigger==1 &&( (p1_pt > 15 && p2_pt > 15 &&p3_pt >10 && p4_pt<10) || (  abs(p1_eta) < 2.5 && abs(p2_eta)<2.5 && abs(p3_eta) < 2.5 && abs(p4_eta)>2.5 ) ) || (p1_pt > 15 && p2_pt > 15 &&p3_pt >10 && p4_pt<10) && (  abs(p1_eta) < 2.5 && abs(p2_eta)<2.5 && abs(p3_eta) < 2.5 &7 abs(p4_eta)>2.5 ) ) ')
       
       passtrigger_1 = TCut('p0_passTrigger==1') # pass trigger
       passTrigger_0 = TCut('p0_passTrigger==0') # fail trigger

       resolved_4 = TCut('p0_resolvedcount==4')
       resolved_3 = TCut('p0_resolvedcount==3')
       resolved_2 = TCut('p0_resolvedcount==2')


       ptcut = TCut('p0_pt>10')
       etacut = TCut('abs(p0_eta)<2.5')
       acceptance = TCut('p0_pt>10 && abs(p0_eta)<2.5')
       conversion = TCut('p0_conversion')

       Case1_4_allresolved_passtrigger1_inacceptance = TCut('p0_npho>3 && p0_resolvedcount==4 && p0_passTrigger==1 && p0_outofptcount==0 && p0_outofetacount ==0')
       Case1_4_allresolved_passtrigger1_outacceptance = TCut('p0_npho>3 && p0_resolvedcount==4 && p0_passTrigger==1 && (p0_outofptcount==1 || p0_outofetacount ==1)')
       
       Case1_3_allresolved_passtrigger1_outacceptance = TCut('p0_npho==3 && p0_resolvedcount ==3 && p0_passTrigger==1 && (p0_outofptcount==1 || p0_outofetacount ==1)')
       Case1_3_fat_passtrigger1_inacceptance = TCut('p0_npho==3 && p0_resolvedcount == 2 && p0_passTrigger==1 && p0_outofptcount==0 && p0_outofetacount ==0')
       
       Case1_2_2fat_passtrigger1_inacceptance = TCut('p0_npho==2 && p0_resolvedcount==0 && p0_passTrigger==1 && p0_outofptcount==0 && p0_outofetacount ==0 ')
       Case1_2_2resolved_passtrigger1_outacceptance = TCut('p0_npho==2 && p0_resolvedcount==2 && p0_passTrigger==1 && p0_outofptcount==2 && p0_outofetacount ==2 ')

       
       #Case1_4_allresolved_passtrigger0 = TCut('p0_npho>3 && p0_genmatchpt<0 && p0_passTrigger==0')
       #Case1_3_allresolved = TCut('p0_npho==3 && p0_genmatchpt<0')
       #Case1_3_fat = TCut('p0_npho==3 && p0_genmatchpt>0 &&p0_passTrigger==1')
       #Case1_4_fat = TCut('p0_npho>3 && p0_genmatchpt>0')

       evs_4 = tch.Draw("p0_pt",TCut(Case1_4))
       evs_3 = tch.Draw("p0_pt",TCut(Case1_3))
       evs_2 = tch.Draw("p0_pt",TCut(Case1_2))
       
       
       #evs_4_case1 = tch4.Draw("p1_pt",TCut(Case1_4_case1))
       #evs_4_case2 = tch4.Draw("p1_pt",TCut(Case1_4_case2))

       evs_4_allresolved_passtrigger1_inacceptance = tch.Draw("p0_pt",TCut(Case1_4_allresolved_passtrigger1_inacceptance))
       evs_4_allresolved_passtrigger1_outacceptance = tch.Draw("p0_pt",TCut(Case1_4_allresolved_passtrigger1_outacceptance))
       evs_3_allresolved_passtrigger1_outacceptance = tch.Draw("p0_pt",TCut(Case1_3_allresolved_passtrigger1_outacceptance))
       evs_3_fat_passtrigger1_inacceptance = tch.Draw("p0_pt", TCut(Case1_3_fat_passtrigger1_inacceptance))
       evs_2_2fat_passtrigger1_inacceptance = tch.Draw("p0_pt",TCut(Case1_2_2fat_passtrigger1_inacceptance))
       evs_2_2resolved_passtrigger1_outacceptance = tch.Draw("p0_pt",TCut(Case1_2_2resolved_passtrigger1_outacceptance))
       
       
       evs_Fourpho = tch0.Draw("p_pt",TCut(Fourpho))
       evs_Threepho = tch0.Draw("p_pt",TCut(Threepho))
       evs_Twopho = tch0.Draw("p_pt",TCut(Twopho))

                        
#evs_3_allresolved = tch.Draw("p0_pt",TCut(Case1_3_allresolved))
#evs_3_fat = tch.Draw("p0_pt",TCut(Case1_3_fat))
#evs_4_fat = tch.Draw("p0_pt",TCut(Case1_4_fat))

       eff_evs_2pho = float(evs_2pho)/float(totevs)
       eff_evs_3pho = float(evs_3pho)/float(totevs)
       eff_evs_4pho = float(evs_4pho)/float(totevs)
       eff_evs_otherpho = 1- (eff_evs_2pho + eff_evs_3pho + eff_evs_4pho)
       
       eff_evs_2pho_passtrigger = float(evs_2pho_passtrigger)/float(totevs)
       eff_evs_3pho_passtrigger = float(evs_3pho_passtrigger)/float(totevs)
       eff_evs_4pho_passtrigger = float(evs_4pho_passtrigger)/float(totevs)
       
       eff_evs_2pho_failtrigger = float(evs_2pho_failtrigger)/float(totevs)
       eff_evs_3pho_failtrigger = float(evs_3pho_failtrigger)/float(totevs)
       eff_evs_4pho_failtrigger = float(evs_4pho_failtrigger)/float(totevs)
       
       eff_evs_4pho_allresolved_passtrigger_inacceptance = float(evs_4pho_passtrigger_allresolved_inacceptance)/float(totevs)
       eff_evs_4pho_allresolved_passtrigger_outacceptance = float(evs_4pho_passtrigger_allresolved_outacceptance)/float(totevs)
       eff_evs_4pho_other = eff_evs_4pho - (eff_evs_4pho_allresolved_passtrigger_inacceptance+eff_evs_4pho_allresolved_passtrigger_outacceptance)
       
       eff_evs_3pho_passtrigger_allresolved_outacceptance = float(evs_3pho_passtrigger_allresolved_outacceptance)/float(totevs)
       eff_evs_3pho_passtrigger_fatpho_inacceptance = float(evs_3pho_passtrigger_fatpho_inacceptance)/float(totevs)
       eff_evs_3pho_other = eff_evs_3pho - (eff_evs_3pho_passtrigger_allresolved_outacceptance + eff_evs_3pho_passtrigger_fatpho_inacceptance)
    
       eff_evs_2pho_passtrigger_allresolved_outacceptance = float(evs_2pho_passtrigger_allresolved_outacceptance)/float(totevs)
       eff_evs_2pho_passtrigger_fatpho_inacceptance = float(evs_2pho_passtrigger_2fat_inacceptance)/float(totevs)
       eff_evs_2pho_other = eff_evs_2pho - (eff_evs_2pho_passtrigger_allresolved_outacceptance + eff_evs_2pho_passtrigger_fatpho_inacceptance )
       
       eff_evs_4 = float(evs_4)/float(totevs)
       eff_evs_3 = float(evs_3)/float(totevs)
       eff_evs_2 = float(evs_2)/float(totevs)

       eff_evs_4_allresolved_passtrigger1_inacceptance = float(evs_4_allresolved_passtrigger1_inacceptance)/float(totevs)
       eff_evs_4_allresolved_passtrigger1_outacceptance = float(evs_4_allresolved_passtrigger1_outacceptance)/float(totevs)
       eff_evs_4_other = eff_evs_4 - (eff_evs_4_allresolved_passtrigger1_inacceptance+eff_evs_4_allresolved_passtrigger1_outacceptance)
       
       eff_evs_3_allresolved_passtrigger1_outacceptance = float(evs_3_allresolved_passtrigger1_outacceptance)/float(totevs)
       eff_evs_3_fat_passtrigger1_inacceptance = float(evs_3_fat_passtrigger1_inacceptance)/float(totevs)
       eff_evs_3_other = eff_evs_3 - (eff_evs_3_fat_passtrigger1_inacceptance + eff_evs_3_allresolved_passtrigger1_outacceptance)
       
       #eff_evs_2_passtrigger_allresolved_outacceptance = float(evs_2pho_passtrigger_allresolved_outacceptance)/float(totevs)
       #eff_evs_2_passtrigger_2fat_inacceptance = float(evs_2pho_passtrigger_2fat_inacceptance)/float(totevs)
       #eff_evs_2_other = eff_evs_2 - (eff_evs_2_passtrigger_allresolved_outacceptance + eff_evs_2pho_passtrigger_2fat_inacceptance)

                              
       eff_evs_Fourpho = float(evs_Fourpho)/float(totevs0)
       eff_evs_Threepho = float(evs_Threepho)/float(totevs0)
       eff_evs_Twopho = float(evs_Twopho)/float(totevs0)
       
       #eff_evs_4_case1 = float(evs_4_case1)/float(totevs0)
       #eff_evs_4_case2 = float(evs_4_case2)/float(totevs0)
       #eff_evs_4_caseother = eff_evs_Fourpho - (eff_evs_4_case1 + eff_evs_4_case2)
#eff_evs_3_resolved = float(evs_3_allresolved)/float(totevs)

#eff_evs_3_fat = float(evs_3_fat)/float(totevs)
#eff_evs_4_fat = float(evs_4_fat)/float(totevs)
       #Cut_case1_4A = TCut(EtaCut_case1)
       #Cut_case1_4A =TCut(PtCut_case1_4A)
       #Cut_case1_3A = TCut(EtaCut_case1)
       #Cut_case1_3A =TCut(PtCut_case1_3A)

#Cut_case2_4A = TCut(EtaCut_case2)
#Cut_case2_4A =TCut(PtCut_case2_4A)
       #Cut_case2_3A = TCut(EtaCut_case2)
       #Cut_case2_3A =TCut(PtCut_case2_3A)
       
       #Cut_case3_4A = TCut(EtaCut_case3)
       #Cut_case3_4A =TCut(PtCut_case3_4A)
       
       #tch1 = TChain("H4GGen_case1")
       #tch1.AddFile(files[i])
       #evs_case1 = tch1.Draw("tp_mass_case1","1>0")
       #evs_case1_4A = tch1.Draw("tp_mass_case1",TCut(Cut_case1_4A))
       #evs_case1_3A = tch1.Draw("tp_mass_case1",TCut(Cut_case1_3A))

       
       #tch2 = TChain("H4GGen_case2")
       #tch2.AddFile(files[i])
       #evs_case2 = tch2.Draw("tp_mass_case2","1>0")
       #evs_case2_4A = tch2.Draw("tp_mass_case2",TCut(Cut_case2_4A))
       #evs_case2_3A = tch2.Draw("tp_mass_case2",TCut(Cut_case2_3A))
       
                                      
       
       #tch3 = TChain("H4GGen_case3")
       #tch3.AddFile(files[i])
       #evs_case3 = tch3.Draw("tp_mass_case3","1>0")
       #evs_case3_4A = tch3.Draw("tp_mass_case3",TCut(Cut_case3_4A))
       

#eff_case1 = float(evs_case1)/float(totevs)
#eff_case1_4A = float(evs_case1_4A)/float(totevs)
#eff_case1_3A = float(evs_case1_3A)/float(totevs)
#eff_case1_other = eff_case1 - (eff_case1_4A+eff_case1_3A)
       
       #eff_case2 = float(evs_case2)/float(totevs)
       #eff_case2_4A = float(evs_case2_4A)/float(totevs)
       #eff_case2_3A = float(evs_case2_3A)/float(totevs)
       #eff_case2_other = eff_case2 - (eff_case2_4A+eff_case2_3A)
       
       #eff_case3 = float(evs_case3)/float(totevs)
       #eff_case3_4A = float(evs_case3_4A)/float(totevs)
       #eff_case3_other = eff_case3 - eff_case3_4A
       
       
       #eff_other = 1.0 - (eff_case1+eff_case2+eff_case3)
       
       c_2pho.append(eff_evs_2pho)
       c_3pho.append(eff_evs_3pho)
       c_4pho.append(eff_evs_4pho)
       c_otherpho.append(eff_evs_otherpho)
       
       c_2pho_passtrigger.append(eff_evs_2pho_passtrigger)
       c_3pho_passtrigger.append(eff_evs_3pho_passtrigger)
       c_4pho_passtrigger.append(eff_evs_4pho_passtrigger)
       
       c_2pho_failtrigger.append(eff_evs_2pho_failtrigger)
       c_3pho_failtrigger.append(eff_evs_3pho_failtrigger)
       c_4pho_failtrigger.append(eff_evs_4pho_failtrigger)
       
       c_4pho_passtrigger_allresolved_inacceptance.append(eff_evs_4pho_allresolved_passtrigger_inacceptance)
       c_4pho_passtrigger_allresolved_outacceptance.append(eff_evs_4pho_allresolved_passtrigger_outacceptance)
       c_4pho_other.append(eff_evs_4pho_other)
       
       c_3pho_passtrigger_allresolved_outacceptance.append(eff_evs_3pho_passtrigger_allresolved_outacceptance)
       c_3pho_passtrigger_fatpho_inacceptance.append(eff_evs_3pho_passtrigger_fatpho_inacceptance)
       c_3pho_other.append(eff_evs_3pho_other)
       
       c_2pho_passtrigger_2fat_inacceptance.append(eff_evs_2pho_passtrigger_fatpho_inacceptance)
       c_2pho_passtrigger_allresolved_outacceptance.append(eff_evs_2pho_passtrigger_allresolved_outacceptance)
       c_2pho_other.append(eff_evs_2pho_other)
       
    
       c4.append(eff_evs_4) # efficiency for case1
       c4_1.append(eff_evs_4_allresolved_passtrigger1_inacceptance)
       c4_2.append(eff_evs_4_allresolved_passtrigger1_outacceptance)
       c4_other.append(eff_evs_4_other)
       #c1_3A.append(eff_case1_3A)
       #c1_other.append(eff_case1_other)
       
       c3.append(eff_evs_3) # efficiency for case2
       c3_1.append(eff_evs_3_fat_passtrigger1_inacceptance)
       c3_2.append(eff_evs_3_allresolved_passtrigger1_outacceptance)
       c3_other.append(eff_evs_3_other)
       #c2_4A.append(eff_case2_4A)
       #c2_3A.append(eff_case2_3A)
       #c2_other.append(eff_case2_other)
       
       c2.append(eff_evs_2) # efficiency for case3
       #c2_1.append(eff_evs_2_2fat_passtrigger1_inacceptance)
       #c2_2.append(eff_evs_2_2resolved_passtrigger1_outaccetpance)
       #c2_other.append(eff_evs_2_other)
       
       c_Fourpho.append(eff_evs_Fourpho)
       c_Threepho.append(eff_evs_Threepho)
       c_Twopho.append(eff_evs_Twopho)

#c_4_case1.append(eff_evs_4_case1)
#c_4_case2.append(eff_evs_4_case2)
#c_4_caseother.append(eff_evs_4_caseother)

canvas = TCanvas( 'canvas', 'reco efficiency', 200, 10, 1000, 600 )

bin_edges = np.array([0.1,1, 5 , 10, 15, 20, 25,30 ,35, 40, 45, 50, 55, 60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80], dtype='float64')

h1_2pho = TH1F('h1_2pho','2 Photons',len(bin_edges)-1, bin_edges )
h1_3pho = TH1F('h1_3pho','3 Photons',len(bin_edges)-1, bin_edges )
h1_4pho = TH1F('h1_4pho','4 Photons',len(bin_edges)-1, bin_edges )
h1_otherpho = TH1F('h1_otherpho','Other Photons',len(bin_edges)-1, bin_edges )

h1_2pho_passtrigger = TH1F('h1_2pho_passtrigger','2 Photons + pass Trigger',len(bin_edges)-1, bin_edges )
h1_3pho_passtrigger = TH1F('h1_3pho_passtrigger','3 Photons + pass Trigger',len(bin_edges)-1, bin_edges )
h1_4pho_passtrigger = TH1F('h1_4pho_passtrigger','4 Photons + pass Trigger',len(bin_edges)-1, bin_edges )


h1_2pho_failtrigger = TH1F('h1_2pho_failtrigger','2 Photons + fail Trigger',len(bin_edges)-1, bin_edges )
h1_3pho_failtrigger = TH1F('h1_3pho_failtrigger','3 Photons + fail Trigger',len(bin_edges)-1, bin_edges )
h1_4pho_failtrigger = TH1F('h1_4pho_failtrigger','4 Photons + fail Trigger',len(bin_edges)-1, bin_edges )

h1_4pho_allresolved_passtrigger_inaccpetance = TH1F('h1_4pho_allresolved_passtrigger_inacceptance','4 Photons + passtrigger+ all resolved + all in acceptance',len(bin_edges)-1, bin_edges )
h1_4pho_allresolved_passtrigger_outaccpetance = TH1F('h1_4pho_allresolved_passtrigger_outacceptance','4 Photons + passtrigger+ all resolved + 1 missing',len(bin_edges)-1, bin_edges )
h1_4pho_other = TH1F('h1_4pho_other','4 Photons : Other',len(bin_edges)-1, bin_edges)

h1_3pho_passtrigger_allresolved_outacceptance = TH1F('h1_3pho_3pho_passtrigger_allresolved_outacceptance','3 Photons + passtrigger+ 1 Missng',len(bin_edges)-1, bin_edges )
h1_3pho_passtrigger_fatpho_inacceptance = TH1F('h1_3pho_passtrigger_fatpho_inacceptance','2 resolved + 1 fat + pass trigger + inacceptance',len(bin_edges)-1, bin_edges)
h1_3pho_other = TH1F('h1_3pho_other','3 Photons : Other',len(bin_edges)-1, bin_edges)

h1_2pho_passtrigger_2fat_inacceptance = TH1F('h1_2pho_passtrigger_2fat_inacceptance','2 Fat Photons + passtrigger + inacceptance',len(bin_edges)-1, bin_edges)
h1_2pho_passtrigger_allresolved_outacceptance = TH1F('h1_2pho_passtrigger_allresolved_outacceptance','2 resolved photons + pass trigger + out of acceptance',len(bin_edges)-1, bin_edges)
h1_2pho_other = TH1F('h1_2pho_other','2 Photons: Other ',len(bin_edges)-1, bin_edges)

h1f_v2_2 = TH1F('h1f_v2_2','2 Photons',len(bin_edges)-1, bin_edges )
h1f_v2_3 = TH1F('h1f_v2_3','3 Photons',len(bin_edges)-1, bin_edges )
h1f_v2_4 = TH1F('h1f_v2_4','4 Photons',len(bin_edges)-1, bin_edges )
h1f_v2_2_sel = TH1F('h1f_v2_2_sel','2 Photons+pass selections',len(bin_edges)-1, bin_edges )
h1f_v2_3_sel = TH1F('h1f_v2_3_sel','3 Photons+pass selections',len(bin_edges)-1, bin_edges )
h1f_v2_4_sel = TH1F('h1f_v2_4_sel','4 Photons+pass selections',len(bin_edges)-1, bin_edges )
h1f_v2_2_presel = TH1F('h1f_v2_2_presel','2 Photons+pass selections + preselections',len(bin_edges)-1, bin_edges )
h1f_v2_3_presel = TH1F('h1f_v2_3_presel','3 Photons+pass selections + preselections',len(bin_edges)-1, bin_edges )
h1f_v2_4_presel = TH1F('h1f_v2_4_presel','4 Photons+pass selections + preselections',len(bin_edges)-1, bin_edges )




h1f_4 = TH1F( 'h1f', '4 Photons', len(bin_edges)-1, bin_edges )
h1f_3 = TH1F( 'h1f', '3 Photons', len(bin_edges)-1, bin_edges )
h1f_2 = TH1F( 'h1f', '2 Photons', len(bin_edges)-1, bin_edges )
h1f_4_1 = TH1F( 'h1f_4_1','4 Photons : all resolved + passtrigger +in acceptnace ', len(bin_edges)-1, bin_edges)
h1f_4_2 = TH1F( 'h1f_4_2','4 Photons : all resolved + passtrigger + 1 out of acceptance ', len(bin_edges)-1, bin_edges)
h1f_4_other = TH1F('h1f_4_other','4 Photons : other',len(bin_edges)-1, bin_edges)
h1f_3_1 = TH1F('h1f_3_1','3 Photons : 2 resolved+1Fat +pass Trigger + in acceptance',len(bin_edges)-1, bin_edges)
h1f_3_2 = TH1F('h1f_3_2','3 Photons : 3 resolved+1 Missing +pass Trigger',len(bin_edges)-1, bin_edges)
h1f_3_other = TH1F('h1f_3_other','3 Photons : Other',len(bin_edges)-1, bin_edges)
h1f_2_1 = TH1F('h1F_2_1','2 Photons : 2 fat + passtrigger + in acceptance',len(bin_edges)-1, bin_edges)
h1f_2_2 = TH1F('h1f_2_2','2 Photons : 2 resolved + passtrigger + out of acceptance',len(bin_edges)-1, bin_edges)
h1f_2_other = TH1F('h1f_2_other','2 Photons : other',len(bin_edges)-1, bin_edges)

h1f_Fourpho = TH1F ('h1f_Fourpho','4 Photons',len(bin_edges)-1, bin_edges )
h1f_Threepho = TH1F ('h1f_Threepho','3 Photons',len(bin_edges)-1, bin_edges )
h1f_Twopho = TH1F ('h1f_Twopho','2 Photons',len(bin_edges)-1, bin_edges )
#h1f_4_case1 = TH1F ('h1f_4_case1','4 Photons:case1',len(bin_edges)-1, bin_edges )
#h1f_4_case2 = TH1F ('h1f_4_case2','4 Photons:case1',len(bin_edges)-1, bin_edges )
#h1f_4_caseother = TH1F ('h1f_4_caseother','4 Photons:case other',len(bin_edges)-1, bin_edges )
for i in range(0,14):
    #print c5
    h1_2pho.Fill(masses[i],c_2pho[i])
    h1_3pho.Fill(masses[i],c_3pho[i])
    h1_4pho.Fill(masses[i],c_4pho[i])
    h1_otherpho.Fill(masses[i],c_otherpho[i])
    
    h1_2pho_passtrigger.Fill(masses[i],c_2pho_passtrigger[i])
    h1_3pho_passtrigger.Fill(masses[i],c_3pho_passtrigger[i])
    h1_4pho_passtrigger.Fill(masses[i],c_4pho_passtrigger[i])
    
    h1_2pho_failtrigger.Fill(masses[i],c_2pho_failtrigger[i])
    h1_3pho_failtrigger.Fill(masses[i],c_3pho_failtrigger[i])
    h1_4pho_failtrigger.Fill(masses[i],c_4pho_failtrigger[i])
    
    h1_4pho_allresolved_passtrigger_inacceptance.Fill(masses[i],c_4pho_passtrigger_allresolved_inacceptance[i])
    h1_4pho_allresolved_passtrigger_outacceptance.Fill(masses[i],c_4pho_passtrigger_allresolved_outacceptance[i])
    h1_4pho_other.Fill(masses[i],c_4pho_other[i])
    
    h1_3pho_passtrigger_allresolved_outacceptance.Fill(masses[i],c_3pho_passtrigger_allresolved_outacceptance[i])
    h1_3pho_passtrigger_fatpho_inacceptance.Fill(masses[i],c_3pho_passtrigger_fatpho_inacceptance[i])
    h1_3pho_other.Fill(masses[i],c_3pho_other[i])
    
    h1_2pho_passtrigger_2fat_inacceptance.Fill(masses[i],c_2pho_passtrigger_2fat_inacceptance[i])
    h1_2pho_passtrigger_allresolved_outacceptance.Fill(masses[i],c_2pho_passtrigger_allresolved_outacceptance[i])
    h1_2pho_other.Fill(masses[i],c_2pho_other[i])
    
    
    h1f_v2_2.Fill(masses[i],c_v2_2[i])
    h1f_v2_3.Fill(masses[i],c_v2_3[i])
    h1f_v2_4.Fill(masses[i],c_v2_4[i])
    h1f_v2_2_sel.Fill(masses[i],c_v2_2_sel[i])
    h1f_v2_3_sel.Fill(masses[i],c_v2_3_sel[i])
    h1f_v2_4_sel.Fill(masses[i],c_v2_4_sel[i])
    h1f_v2_2_presel.Fill(masses[i],c_v2_2_presel[i])
    h1f_v2_3_presel.Fill(masses[i],c_v2_3_presel[i])
    h1f_v2_4_presel.Fill(masses[i],c_v2_4_presel[i])
    
    
    h1f_4.Fill(masses[i],c4[i])
    h1f_3.Fill(masses[i],c3[i])
    h1f_2.Fill(masses[i],c2[i])
    h1f_4_1.Fill(masses[i],c4_1[i])
    h1f_4_2.Fill(masses[i],c4_2[i])
    h1f_4_other.Fill(masses[i],c4_other[i])
    h1f_3_1.Fill(masses[i],c3_1[i])
    h1f_3_2.Fill(masses[i],c3_2[i])
    h1f_3_other.Fill(masses[i],c3_other[i])
    #h1f_2_1.Fill(masses[i],c2_1[i])
    #h1f_2_2.Fill(masses[i],c2_2[i])
    #h1f_2_other.Fill(masses[i],c2_other[i])
                              
    h1f_Fourpho.Fill(masses[i],c_Fourpho[i])
    h1f_Threepho.Fill(masses[i],c_Threepho[i])
    h1f_Twopho.Fill(masses[i],c_Twopho[i])

#h1f_4_case1.Fill(masses[i],c_4_case1[i])
#h1f_4_case2.Fill(masses[i],c_4_case2[i])
#h1f_4_caseother.Fill(masses[i],c_4_caseother[i])

#h6f.Fill(masses[i],c6[i])
#Get pretty colors
cNiceBlue = TColor.GetColor('#51A7F9')
cNiceBlueDark = TColor.GetColor('#2175E0')
cNiceGreen = TColor.GetColor('#6FBF41')
cNiceGreenDark = TColor.GetColor('#008040')

h1_2pho.SetFillColor(kAzure+3)
h1_2pho.SetLineColor(kAzure+3)
h1_2pho_passtrigger.SetFillColor(kAzure+3)
h1_2pho_passtrigger.SetLineColor(kAzure+3)
#h1_2pho_passtrigger.SetFillStyle(3001)
h1_2pho_failtrigger.SetFillColor(kAzure+3)
h1_2pho_failtrigger.SetLineColor(kAzure+3)
h1_2pho_failtrigger.SetFillStyle(3001)
h1_2pho_passtrigger_2fat_inacceptance.SetFillColor(kAzure+3)
h1_2pho_passtrigger_2fat_inacceptance.SetLineColor(kAzure+3)
h1_2pho_passtrigger_allresolved_outacceptance.SetFillColor(kAzure+3)
h1_2pho_passtrigger_allresolved_outacceptance.SetLineColor(kAzure+3)
h1_2pho_passtrigger_allresolved_outacceptance.SetFillStyle(3006)
h1_2pho_other.SetFillColor(kAzure+3)
h1_2pho_other.SetLineColor(kAzure+3)
h1_2pho_other.SetFillStyle(3015)



h1_3pho.SetFillColor(kAzure+4)
h1_3pho.SetLineColor(kAzure+4)
h1_3pho_passtrigger.SetFillColor(kAzure+4)
h1_3pho_passtrigger.SetLineColor(kAzure+4)
#h1_3pho_passtrigger.SetFillStyle(3001)
h1_3pho_failtrigger.SetFillColor(kAzure+4)
h1_3pho_failtrigger.SetLineColor(kAzure+4)
h1_3pho_failtrigger.SetFillStyle(3001)
h1_3pho_passtrigger_allresolved_outacceptance.SetFillColor(kAzure+4)
h1_3pho_passtrigger_allresolved_outacceptance.SetLineColor(kAzure+4)
h1_3pho_passtrigger_allresolved_outacceptance.SetFillStyle(3006)
h1_3pho_passtrigger_fatpho_inacceptance.SetFillColor(kAzure+4)
h1_3pho_passtrigger_fatpho_inacceptance.SetLineColor(kAzure+4)
h1_3pho_other.SetFillColor(kAzure+4)
h1_3pho_other.SetLineColor(kAzure+4)
h1_3pho_other.SetFillStyle(3015)


h1_4pho.SetFillColor(cNiceBlue)
h1_4pho.SetLineColor(cNiceBlue)
h1_4pho_passtrigger.SetFillColor(cNiceBlue)
h1_4pho_passtrigger.SetLineColor(cNiceBlue)
#h1_4pho_passtrigger.SetFillStyle(3001)
h1_4pho_failtrigger.SetFillColor(cNiceBlue)
h1_4pho_failtrigger.SetLineColor(cNiceBlue)
h1_4pho_failtrigger.SetFillStyle(3001)
h1_4pho_allresolved_passtrigger_inacceptance.SetFillColor(cNiceBlue)
h1_4pho_allresolved_passtrigger_inacceptance.SetLineColor(cNiceBlue)
h1_4pho_allresolved_passtrigger_outacceptance.SetFillColor(cNiceBlue)
h1_4pho_allresolved_passtrigger_outacceptance.SetLineColor(cNiceBlue)
h1_4pho_allresolved_passtrigger_outacceptance.SetFillStyle(3006)
h1_4pho_other.SetFillColor(cNiceBlue)
h1_4pho_other.SetLineColor(cNiceBlue)
h1_4pho_other.SetFillStyle(3015)



h1_otherpho.SetFillColor(cNiceGreen)
h1_otherpho.SetLineColor(cNiceGreen)



h1f_v2_2.SetFillColor(kAzure+3)
h1f_v2_2.SetLineColor(kAzure+3)
h1f_v2_2.SetFillStyle(3006)
h1f_v2_2_sel.SetFillColor(kAzure+3)
h1f_v2_2_sel.SetLineColor(kAzure+3)
h1f_v2_2_sel.SetFillStyle(3001)
h1f_v2_2_presel.SetFillColor(kAzure+3)
h1f_v2_2_presel.SetLineColor(kAzure+3)


h1f_v2_3.SetFillColor(cNiceGreenDark)
h1f_v2_3.SetLineColor(cNiceGreenDark)
h1f_v2_3.SetFillStyle(3006)
h1f_v2_3_sel.SetFillColor(cNiceGreenDark)
h1f_v2_3_sel.SetLineColor(cNiceGreenDark)
h1f_v2_3_sel.SetFillStyle(3001)
h1f_v2_3_presel.SetFillColor(cNiceGreenDark)
h1f_v2_3_presel.SetLineColor(cNiceGreenDark)


h1f_v2_4.SetFillColor(cNiceBlue)
h1f_v2_4.SetLineColor(cNiceBlue)
h1f_v2_4.SetFillStyle(3006)
h1f_v2_4_sel.SetFillColor(cNiceBlue)
h1f_v2_4_sel.SetLineColor(cNiceBlue)
h1f_v2_4_sel.SetFillStyle(3001)
h1f_v2_4_presel.SetFillColor(cNiceBlue)
h1f_v2_4_presel.SetLineColor(cNiceBlue)


#h1f.SetFillColor(kPink-9)
h1f_4.SetFillColor(cNiceBlue)
h1f_4.SetLineColor(cNiceBlue)
h1f_4_1.SetFillColor(cNiceBlue)
h1f_4_1.SetLineColor(cNiceBlue)
#h1f_4_resolved_passtrigger1.SetFillStyle(3023)
h1f_4_2.SetFillColor(cNiceBlue)
h1f_4_2.SetLineColor(cNiceBlue)
h1f_4_2.SetFillStyle(3001)

h1f_4_other.SetFillColor(cNiceBlue)
h1f_4_other.SetLineColor(cNiceBlue)
h1f_4_other.SetFillStyle(3015)

#h1f_3A.SetFillColor(cNiceBlue)
#h1f_3A.SetFillStyle(3001)
#h1f_3A.SetLineColor(cNiceBlue)
#h1f_other.SetFillColor(cNiceBlue)
#h1f_other.SetFillStyle(3006)
#h1f_other.SetLineColor(cNiceBlue)

#h2f.SetFillColor(39)
#h2f.SetFillStyle(3144)
h1f_3.SetFillColor(cNiceGreenDark)
h1f_3.SetLineColor(cNiceGreenDark)
h1f_3_1.SetFillColor(cNiceGreenDark)
h1f_3_1.SetLineColor(cNiceGreenDark)
h1f_3_2.SetFillColor(cNiceGreenDark)
h1f_3_2.SetLineColor(cNiceGreenDark)
h1f_3_2.SetFillStyle(3001)
h1f_3_other.SetFillColor(cNiceGreenDark)
h1f_3_other.SetLineColor(cNiceGreenDark)
h1f_3_other.SetFillStyle(3015)
#h1f_3A.SetFillColor(cNiceGreenDark)
#h2f_3A.SetFillStyle(3001)
#h2f_3A.SetLineColor(cNiceGreenDark)
#h2f_other.SetFillColor(cNiceGreenDark)
#h2f_other.SetFillStyle(3006)
#h2f_other.SetLineColor(cNiceGreenDark)

#h3f.SetFillColor(kOrange+10)
#h3f.SetFillStyle(3088)
h1f_2.SetFillColor(kAzure+3)
h1f_2.SetLineColor(kAzure+3)
h1f_2_1.SetFillColor(kAzure+3)
h1f_2_1.SetLineColor(kAzure+3)
h1f_2_2.SetFillColor(kAzure+3)
h1f_2_2.SetLineColor(kAzure+3)
h1f_2_2.SetFillStyle(3001)
h1f_2_other.SetFillColor(kAzure+3)
h1f_2_other.SetLineColor(kAzure+3)
h1f_2_other.SetFillStyle(3015)

h1f_Fourpho.SetLineColor(cNiceBlue)
h1f_Fourpho.SetFillColor(cNiceBlue)
h1f_Threepho.SetLineColor(cNiceGreenDark)
h1f_Threepho.SetFillColor(cNiceGreenDark)
h1f_Twopho.SetLineColor(kAzure+3)
h1f_Twopho.SetFillColor(kAzure+3)

#h1f_4_case1.SetLineColor(cNiceBlue)
#h1f_4_case1.SetFillColor(cNiceBlue)

#h1f_4_case2.SetLineColor(cNiceBlue)
#h1f_4_case2.SetFillColor(cNiceBlue)
#h1f_4_case2.SetFillStyle(3001)
#h1f_4_caseother.SetLineColor(cNiceBlue)
#h1f_4_caseother.SetFillColor(cNiceBlue)
#h1f_4_caseother.SetFillStyle(3006)


#h1f_v2_4.Draw()
#h1f_v2_4_sel.Draw("same")
#h1f_v2_4_presel.Draw("same")

s = THStack("s","Reco level categorization ")

#s.Add(h1_4pho)
#s.Add(h1_3pho)
#s.Add(h1_2pho)
#s.Add(h1_otherpho)
#s.Add(h1_4pho_passtrigger)
s.Add(h1_4pho_allresolved_passtrigger_inacceptance)
s.Add(h1_3pho_passtrigger_fatpho_inacceptance)
s.Add(h1_2pho_passtrigger_2fat_inacceptance)
s.Add(h1_4pho_allresolved_passtrigger_outacceptance)
s.Add(h1_3pho_passtrigger_allresolved_outacceptance)
s.Add(h1_2pho_passtrigger_allresolved_outacceptance)
s.Add(h1_4pho_other)
s.Add(h1_3pho_other)
s.Add(h1_2pho_other)
#s.Add(h1_3pho_passtrigger)
#s.Add(h1_2pho_passtrigger)
#s.Add(h1_4pho_failtrigger)
#s.Add(h1_3pho_failtrigger)
#s.Add(h1_2pho_failtrigger)




#s.Add(h1f_v2_4_presel)
#s.Add(h1f_v2_3_presel)
#s.Add(h1f_v2_2_presel)
#s.Add(h1f_v2_4_sel)
#s.Add(h1f_v2_3_sel)
#s.Add(h1f_v2_2_sel)
#s.Add(h1f_v2_4)
#s.Add(h1f_v2_4_sel)
#s.Add(h1f_v2_4_presel)
#s.Add(h1f_v2_3)
#s.Add(h1f_v2_2)


#s.Add(h1f)
#s.Add(h1_test)
#s.Add(h1f_4)
#s.Add(h1f_4_1)
#s.Add(h1f_3_1)
#s.Add(h1f_2_1)

#s.Add(h1f_4_2)
#s.Add(h1f_3_2)
#s.Add(h1f_2_2)

#s.Add(h1f_4_other)
#s.Add(h1f_4_resolved_passtrigger1)
#s.Add(h1f_4_resolved_passtrigger0)
                            
                            #s.Add(h1f_4_fat)
#s.Add(h1f_3)
#s.Add(h1f_3_other)
#s.Add(h1f_3_fat)
#s.Add(h1f_3_resolved)
#s.Add(h1f_2)
#s.Add(h1f_2_other)

#s.Add(h1f_4A_14)
#s.Add(h1f_4A_13)
#s.Add(h1f_4A_12)
#s.Add(h1f_4A_11)
#s.Add(h1f_4A_10)
#s.Add(h2f_4A)
#s.Add(h3f_4A)
#s.Add(h1f_other)
#s.Add(h2f)
#s.Add(h2f_4A)
#s.Add(h1f_3A)
#s.Add(h2f_3A)
#s.Add(h1f_other)
#s.Add(h2f_other)
#s.Add(h3f)
#s.Add(h3f_4A)

#s.Add(h3f_other)
#s.Add(h6f)
#s.Add(h1f_Fourpho)
#s.Add(h1f_4_case1)
#s.Add(h1f_4_case2)
#s.Add(h1f_4_caseother)
#s.Add(h1f_Threepho)
#s.Add(h1f_Twopho)



s.Draw("hist")
s.SetMaximum(1.0)
s.GetXaxis().SetTitle('m(a) GeV')
s.GetYaxis().SetTitle('Reco level efficiency')
s.GetYaxis().SetTitleOffset(1)

gr_v2_phosel = TGraph(len(masses),array('d',masses),array('d',c_v2_phosel))
gr_v2_presel = TGraph(len(masses),array('d',masses),array('d',c_v2_presel))
gr_v2_presel_2 = TGraph(len(masses),array('d',masses),array('d',c_v2_presel_2))
gr_v2_presel_3 = TGraph(len(masses),array('d',masses),array('d',c_v2_presel_3))
gr_v2_presel_4 = TGraph(len(masses),array('d',masses),array('d',c_v2_presel_4))

gr_v2_3 = TGraph(len(masses),array('d',masses),array('d',c_v2_3))
gr_v2_3_sel = TGraph(len(masses),array('d',masses),array('d',c_v2_3_sel))
gr_v2_3_presel = TGraph(len(masses),array('d',masses),array('d',c_v2_3_presel))


gr_v2_phosel.SetMarkerColor(cNiceBlue)
gr_v2_phosel.SetLineColor(cNiceBlue)
gr_v2_phosel.SetLineWidth(2)
gr_v2_phosel.SetMarkerStyle(20)

gr_v2_presel.SetMarkerColor(kRed)
gr_v2_presel.SetLineColor(kRed)
gr_v2_presel.SetLineWidth(2)
gr_v2_presel.SetMarkerStyle(21)

gr_v2_presel_2.SetMarkerColor(cNiceGreenDark)
gr_v2_presel_2.SetLineColor(cNiceGreenDark)
gr_v2_presel_2.SetLineWidth(2)
gr_v2_presel_2.SetMarkerStyle(22)

gr_v2_presel_3.SetMarkerColor(kMagenta+3)
gr_v2_presel_3.SetLineColor(kMagenta+3)
gr_v2_presel_3.SetLineWidth(2)
gr_v2_presel_3.SetMarkerStyle(23)

gr_v2_presel_4.SetMarkerColor(kViolet-4)
gr_v2_presel_4.SetLineColor(kViolet-4)
gr_v2_presel_4.SetLineWidth(2)
gr_v2_presel_4.SetMarkerStyle(24)

gr_v2_3.SetMarkerColor(cNiceBlue)
gr_v2_3.SetLineColor(cNiceBlue)
gr_v2_3.SetLineWidth(2)
gr_v2_3.SetMarkerStyle(20)


gr_v2_3_sel.SetMarkerColor(kRed)
gr_v2_3_sel.SetLineColor(kRed)
gr_v2_3_sel.SetLineWidth(2)
gr_v2_3_sel.SetMarkerStyle(21)

gr_v2_3_presel.SetMarkerColor(kMagenta+3)
gr_v2_3_presel.SetLineColor(kMagenta+3)
gr_v2_3_presel.SetLineWidth(2)
gr_v2_3_presel.SetMarkerStyle(22)
#gr_15 = TGraph(len(masses),array('d',masses),array('d',c1_3A_15))
#gr_15.SetLineColor(kBlue+1)
#gr_15.SetLineWidth(2)
#gr_15.SetMarkerStyle(24)
               
#gr_14 = TGraph(len(masses),array('d',masses),array('d',c1_3A_14))
#gr_14.SetLineColor(kAzure+10)
#gr_14.SetLineWidth(2)
#gr_14.SetMarkerStyle(25)
               
#gr_13 = TGraph(len(masses),array('d',masses),array('d',c1_3A_13))
#gr_13.SetLineColor(kViolet-4)
#gr_13.SetLineWidth(2)
#gr_13.SetMarkerStyle(26)
               
#gr_12 = TGraph(len(masses),array('d',masses),array('d',c1_3A_12))
#gr_12.SetLineColor(kMagenta+3)
#gr_12.SetLineWidth(2)
#gr_12.SetMarkerStyle(27)
               
#gr_11 = TGraph(len(masses),array('d',masses),array('d',c1_3A_11))
#gr_11.SetLineColor(kRed)
#gr_11.SetLineWidth(2)
#gr_11.SetMarkerStyle(28)
               
#gr_10 = TGraph(len(masses),array('d',masses),array('d',c1_3A_10))
#gr_10.SetLineColor(kBlack)
#gr_10.SetLineWidth(2)
#gr_10.SetMarkerStyle(29)

mg = TMultiGraph()
#mg.SetTitle(" 4 resolved photons -- 3 in acceptance ; m(a) GeV; ");
mg.SetMaximum(1.5)
mg.SetMinimum(0)
mg.Add(gr_v2_phosel)
mg.Add(gr_v2_presel)
mg.Add(gr_v2_presel_2)
mg.Add(gr_v2_presel_3)
mg.Add(gr_v2_presel_4)
#mg.Add(gr_v2_phosel)
#mg.Add(gr_v2_presel)
#mg.Add(gr_v2_presel_2)
#mg.Add(gr_v2_presel_3)
#mg.Add(gr_v2_presel_4)

#mg.Add(gr_15)
#mg.Add(gr_14)
#mg.Add(gr_13)
#mg.Add(gr_12)
#mg.Add(gr_11)
#mg.Add(gr_10)
#mg.Draw("APL")
#mg.GetXaxis().SetTitle("m(a) GeV")
#mg.GetYaxis().SetTitle("Efficiency")


               
               
#leg = TLegend(0.1,0.7,0.48,0.9)
leg = TLegend(0.71245,0.664247,0.89479,0.872958)
#leg = TLegend(0.6, 0.7, 0.89, 0.89)
#leg = TLegend(0.13,0.65,0.87, 0.89)
leg.SetBorderSize(0)
leg.SetHeader("Reco level categories")
#leg.AddEntry(h1_4pho,">3 Photons",'f')
#leg.AddEntry(h1_3pho,"=3 Photons",'f')
#leg.AddEntry(h1_2pho,"=2 Photons",'f')
#leg.AddEntry(h1_4pho_passtrigger,">3 Photons + passTrigger",'f')
#leg.AddEntry(h1_4pho_allresolved_passtrigger_inacceptance,">3 Photons + passTrigger + all resolved + in acceptance",'f')
leg.AddEntry(h1_4pho_allresolved_passtrigger_inacceptance,"4 resolved: passTrigger+All in acceptance",'f')
leg.AddEntry(h1_3pho_passtrigger_fatpho_inacceptance,"2 resolved + 1 Fat: passTrigger+All in acceptance",'f')
leg.AddEntry(h1_2pho_passtrigger_2fat_inacceptance,"2 Fat: passTrigger+All in acceptance",'f')
leg.AddEntry(h1_4pho_allresolved_passtrigger_outacceptance,"4 resolved: passTrigger+1 Missing ",'f')
leg.AddEntry(h1_3pho_passtrigger_allresolved_outacceptance,"2 resolved + 1 Fat: passTrigger+1 Missing",'f')
leg.AddEntry(h1_2pho_passtrigger_allresolved_outacceptance,"2 Fat: passTrigger+1 Missing",'f')
#leg.AddEntry(h1_3pho_passtrigger_fatpho_inacceptance,"=3 Photons + passTrigger + 1 Fat Photon + in acceptance",'f')
#leg.AddEntry(h1_3pho_passtrigger,"=3 Photons + passTrigger",'f')
#leg.AddEntry(h1_2pho_passtrigger_2fat_inacceptance,"=2 Fat Photons + passTrigger + in acceptance ",'f')
#leg.AddEntry(h1_2pho_passtrigger,"=2 Photons + passTrigger",'f')
#leg.AddEntry(h1_4pho_allresolved_passtrigger_outacceptance,">3 Photons + passTrigger + all resolved + 1 Missing",'f')
#leg.AddEntry(h1_3pho_passtrigger_allresolved_outacceptance,"=3 Photons + passTrigger + all resolved + 1 Missing",'f')
#leg.AddEntry(h1_2pho_passtrigger_allresolved_outacceptance,"=2 Photons + passTrigger + Missing case ",'f')
#leg.AddEntry(h1_4pho_failtrigger,">3 Photons + failTrigger",'f')
#leg.AddEntry(h1_3pho_failtrigger,"=3 Photons + failTrigger",'f')
#leg.AddEntry(h1_2pho_failtrigger,"=2 Photons + failTrigger",'f')
leg.AddEntry(h1_4pho_other,"4 resolved: Other",'f')
leg.AddEntry(h1_3pho_other,"2 resolved + 1 Fat: Other",'f')
leg.AddEntry(h1_2pho_other,"2 Fat: Other",'f')



#leg.AddEntry(h1_otherpho,"<2 Photons",'f')

#leg.AddEntry(gr_v2_phosel,"Events w/ good photons",'p')
#leg.AddEntry(gr_v2_presel,"Events w/ good photons + pass preselections",'p')
#leg.AddEntry(gr_v2_presel_2,"Events w/ good photons + pass preselections + exactly 2 photons",'p')
#leg.AddEntry(gr_v2_presel_3,"Events w/ good photons + pass preselections + exactly 3 photons",'p')
#leg.AddEntry(gr_v2_presel_4,"Events w/ good photons + pass preselections + more than 3 photons",'p')
#leg.AddEntry(gr_v2_3_presel,"3 Good Photons + preselections",'p')
#leg.AddEntry(h1f_v2_3_presel,"3 Good Photons + preselections",'f')
#leg.AddEntry(h1f_v2_2_presel,"2 Good Photons + preselections",'f')
#leg.AddEntry(gr_v2_3_sel,"3 Good Photons",'p')
#leg.AddEntry(h1f_v2_3_sel,"3 Good Photons",'f')
#leg.AddEntry(h1f_v2_2_sel,"2 Good Photons",'f')
#leg.AddEntry(gr_v2_3,"3 Photons",'p')
#leg.AddEntry(h1f_v2_3,"3 Photons",'f')
#leg.AddEntry(h1f_v2_2,"2 Photons",'f')
#leg.SetHeader("Pt threshold on 3rd and 4th photon")
#leg.AddEntry(gr_15,"Pt>15","lp")
#leg.AddEntry(gr_14,"Pt>14","lp")
#leg.AddEntry(gr_13,"Pt>13","lp")
#leg.AddEntry(gr_12,"Pt>12","lp")
#leg.AddEntry(gr_11,"Pt>11","lp")
#leg.AddEntry(gr_10,"Pt>10","lp")

#leg.AddEntry(h6f,"Others",'f')
#leg.AddEntry(h1f,"4 resolved ",'f')
#leg.AddEntry(h1f_4,"=>4 Photons",'f')
#leg.AddEntry(h1f_3,"3 Photons",'f')
#leg.AddEntry(h1f_4_1,"4 Photons: all resolved+pass trigger+acceptance",'f')
#leg.AddEntry(h1f_3_1,"3 Photons: 1Fat+2resolved + passTrigger +acceptance",'f')
#leg.AddEntry(h1f_2_1,"2 Photons: 2 Fat+passtrigger+acceptance",'f')
#leg.AddEntry(h1f_4_2,"4 Photons: all resolved+pass trigger+1 missing",'f')
#leg.AddEntry(h1f_3_2,"3 Photons: all resolved+pass trigger+1 missing",'f')
#leg.AddEntry(h1f_2_2,"2 Photons: 2 resolved + passtrigger+out of acceptance")
#leg.AddEntry(h1f_4_other,"4 Photons : others",'f')
#leg.AddEntry(h1f_3_other,"3 Photons : others",'f')
#leg.AddEntry(h1f_2_other, "2 Photons : others", 'f')

#leg.AddEntry(h1f_Fourpho, "4 Photons", 'f')
#leg.AddEntry(h1f_Threepho, "3 Photons", 'f')
#leg.AddEntry(h1f_Twopho, "2 Photons", 'f')
                              
leg.SetTextSize(0.02)
leg.SetFillStyle(0)
leg.Draw("same")

#canvas.BuildLegend()
canvas.Update()
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/H4G_forPrelim/RecoCatEff_today_new.png")
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/H4G_forPrelim/RecoCatEff_today_new.pdf")
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/H4G_forPrelim/RecoCatEff_today_new.root")


       
       

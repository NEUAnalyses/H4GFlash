from ROOT import *
from array import array
import numpy as np
from prettytable import PrettyTable



text_file = open("testing.txt","w")

files = [

         "FlatTrees_Signal/signal_m_0p1.root",
         "FlatTrees_Signal/signal_m_1.root",
         "FlatTrees_Signal/signal_m_5.root",
         "FlatTrees_Signal/signal_m_10.root",
         "FlatTrees_Signal/signal_m_15.root",
         "FlatTrees_Signal/signal_m_20.root",
         "FlatTrees_Signal/signal_m_25.root",
         "FlatTrees_Signal/signal_m_30.root",
         "FlatTrees_Signal/signal_m_35.root",
         "FlatTrees_Signal/signal_m_40.root",
         "FlatTrees_Signal/signal_m_45.root",
         "FlatTrees_Signal/signal_m_50.root",
         "FlatTrees_Signal/signal_m_55.root",
         "FlatTrees_Signal/signal_m_60.root"
         ]



masses = [0.1,1,5,10,15,20,25,30,35,40,45,50,55,60]


c_2pho = []
c_3pho = []
c_4pho = []
c_2pho_not = []
c_3pho_not = []
c_4pho_not = []

c_otherpho = []

c_2pho_passtrigger = []
c_3pho_passtrigger = []
c_4pho_passtrigger = []
c_2pho_failtrigger = []
c_3pho_failtrigger = []
c_4pho_failtrigger = []


c_4pho_allresolved_allinacceptance = []
c_4pho_allresolved_1missing = []
c_4pho_other = []



c_3pho_fatpho_allinacceptance = []
c_3pho_fatpho_1missing = []
c_3pho_other = []
c_3pho_1missing = []
c_3pho_2missing = []
c_3pho_3missing = []
c_3pho_4missing = []
c_3pho_3pho_1res_2fat = []
c_3pho_3fat = []
c_3pho_3resolved_3inacceptance = []
c_3pho_3resolved_2inacceptance = []
c_3pho_3resolved_1inacceptance = []
c_3pho_3resolved_0inacceptance = []

#c_2pho_passtrigger_2fat_outacceptance = []
#c_2pho_passtrigger_2fat_inacceptance = []
#c_2pho_other = []

c_2pho_2fat_1missing = []
c_2pho_2fat_allinacceptance = []
c_2pho_other = []
c_2pho_2missing = []
c_2pho_3missing = []
c_2pho_4missing = []
c_2pho_1res_1fat = []
c_2pho_2res = []
c_2pho_2resolved_2inacceptance = []
c_2pho_2resolved_1inacceptance = []
c_2pho_2resolved_0inacceptance = []


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

c_2 = []
c2_4A = []
c2_3A = []
c2_other = []

c_3 = []
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

c_4 = []

c_Fourpho = []
c_Threepho = []
c_Twopho = []

c_4_case1 = []
c_4_case2 = []
c_4_caseother = []



for i, m in enumerate(masses):
       print m
       tch = TChain("H4GSel_0")
       tch.AddFile(files[i])
       allevs = tch.Draw("p0_pt","1>0")
       totevs = tch.Draw("p0_pt","p0_npho>0")




       evs_4 = tch.Draw("p0_pt",TCut('p0_npho>3'))  # events with at least 4 photons
       evs_4pho = tch.Draw("p0_pt",TCut('p0_npho>3 && p0_resolvedcount>3 '))
       evs_4pho_allresolved_allinacceptance = tch.Draw("p0_pt",TCut('p0_npho>3  && p0_resolvedcount>3 && p0_Pho1out==0 && p0_Pho2out==0 && p0_Pho3out==0 && p0_Pho4out ==0'))
       evs_4pho_allresolved_1missing = tch.Draw("p0_pt",TCut('p0_npho>3  && p0_resolvedcount>3 && ( (p0_Pho1out==1 && p0_Pho2out==0 && p0_Pho3out==0 && p0_Pho4out==0) || (p0_Pho1out==0 && p0_Pho2out==1 && p0_Pho3out==0 && p0_Pho4out==0) || (p0_Pho1out==0 && p0_Pho2out==0 && p0_Pho3out==1 && p0_Pho4out==0) || (p0_Pho1out==0 && p0_Pho2out==0 && p0_Pho3out==0 && p0_Pho4out==1))'))
       evs_4pho_other  = evs_4pho - (evs_4pho_allresolved_allinacceptance + evs_4pho_allresolved_1missing)
       evs_4pho_not = evs_4 - evs_4pho

    #    print float(evs_4pho+evs_4pho_not)/float(totevs)
       evs_3 = tch.Draw("p0_pt",TCut('p0_npho==3'))
       evs_3pho = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_resolvedcount_revised == 2'))
       evs_3pho_fatpho_allinacceptance = tch.Draw("p0_pt",TCut('p0_npho==3  && p0_resolvedcount==2 && p0_Pho1out==0 && p0_Pho2out==0 && p0_Pho3out==0 '))
       evs_3pho_fatpho_1missing = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_resolvedcount==2 && ((p0_Pho1out==1 && p0_Pho2out==0 && p0_Pho3out==0) || (p0_Pho1out==0 && p0_Pho2out==1 && p0_Pho3out==0) || (p0_Pho1out==0 && p0_Pho2out==0 && p0_Pho3out==1) )'))
       evs_3pho_other = evs_3pho - (evs_3pho_fatpho_allinacceptance + evs_3pho_fatpho_1missing)
       #evs_3pho_not = evs_3 - evs_3pho

       evs_3pho_3resolved_3inacceptance = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_resolvedcount == 3 && p0_Pho1out==0 && p0_Pho2out==0 && p0_Pho3out==0'))
       evs_3pho_3resolved_2inacceptance = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_resolvedcount == 3 && ((p0_Pho1out==1 && p0_Pho2out==0 && p0_Pho3out==0) || (p0_Pho1out==0 && p0_Pho2out==1 && p0_Pho3out==0) || (p0_Pho1out==0 && p0_Pho2out==0 && p0_Pho3out==1))'))
       evs_3pho_3resolved_1inacceptance = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_resolvedcount == 3 && ((p0_Pho1out==1 && p0_Pho2out==1 && p0_Pho3out==0) || (p0_Pho1out==1 && p0_Pho2out==0 && p0_Pho3out==1) || (p0_Pho1out==0 && p0_Pho2out==1 && p0_Pho3out==1))'))
       evs_3pho_3resolved_0inacceptance = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_resolvedcount == 3 && p0_Pho1out==1 && p0_Pho2out==1 && p0_Pho3out==1'))

    #    evs_3pho_1resolved_2fat = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_resolvedcount == 1'))
    #    evs_3pho_3fat = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_resolvedcount == 0'))
    #    evs_3pho_1missing = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_resolvedcount == 3 && p0_Pho1out==0 && p0_Pho2out==0 && p0_Pho3out==0'))
    #    evs_3pho_2missing = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_resolvedcount == 3 && ((p0_Pho1out==1 && p0_Pho2out==0 && p0_Pho3out==0) || (p0_Pho1out==0 && p0_Pho2out==1 && p0_Pho3out==0) || (p0_Pho1out==0 && p0_Pho2out==0 && p0_Pho3out==1) )'))
    #    evs_3pho_3missing = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_resolvedcount == 3 && ((p0_Pho1out==1 && p0_Pho2out==1 && p0_Pho3out==0) || (p0_Pho1out==0 && p0_Pho2out==1 && p0_Pho3out==1) || (p0_Pho1out==1 && p0_Pho2out==0 && p0_Pho3out==1) )'))
    #    evs_3pho_4missing = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_resolvedcount == 3 && p0_Pho1out==1 && p0_Pho2out==1 && p0_Pho3out==1'))
    #    evs_3pho_1res_2fat = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_resolvedcount == 1'))
    #    evs_3pho_3fat = tch.Draw("p0_pt",TCut('p0_npho==3 && p0_resolvedcount == 0'))
       evs_3pho_not = evs_3 - (evs_3pho+evs_3pho_3resolved_3inacceptance+evs_3pho_3resolved_2inacceptance+evs_3pho_3resolved_1inacceptance+evs_3pho_3resolved_0inacceptance)
    #    print float(evs_3pho+evs_3pho_3resolved+evs_3pho_1resolved_2fat+evs_3pho_3fat+evs_3pho_not)/float(totevs)
       evs_2 = tch.Draw("p0_pt",TCut('p0_npho==2'))
       evs_2pho = tch.Draw("p0_pt",TCut('p0_npho==2 && p0_resolvedcount == 0 '))
       evs_2pho_2fat_allinacceptance = tch.Draw("p0_pt",TCut('p0_npho==2  && p0_resolvedcount == 0 && p0_Pho1out==0 && p0_Pho2out==0 '))
       evs_2pho_2fat_1missing = tch.Draw("p0_pt",TCut('p0_npho==2  && p0_resolvedcount == 0 && ( (p0_Pho1out==1 && p0_Pho2out==0) || (p0_Pho1out==0 && p0_Pho2out==1) ) '))
       evs_2pho_other = evs_2pho - (evs_2pho_2fat_allinacceptance + evs_2pho_2fat_1missing)
    #    evs_2pho_not = evs_2 - evs_2pho

       evs_2pho_2resolved_2inacceptance = tch.Draw("p0_pt",TCut('p0_npho==2 && p0_resolvedcount == 2 && p0_Pho1out==0 && p0_Pho2out==0'))
       evs_2pho_2resolved_1inacceptance = tch.Draw("p0_pt",TCut('p0_npho==2 && p0_resolvedcount == 2 && ( (p0_Pho1out==1 && p0_Pho2out==0) || (p0_Pho1out==0 && p0_Pho2out==1) )'))
       evs_2pho_2resolved_0inacceptance = tch.Draw("p0_pt",TCut('p0_npho==2 && p0_resolvedcount == 2 && p0_Pho1out==1 && p0_Pho2out==1'))

    #    evs_2pho_1resolved_1fat = tch.Draw("p0_pt",TCut('p0_npho==2 && p0_resolvedcount == 1 '))

    #    evs_2pho_2missing = tch.Draw("p0_pt",TCut('p0_npho==2 && p0_resolvedcount == 2 && p0_Pho1out==0 && p0_Pho2out==0  '))
    #    evs_2pho_3missing = tch.Draw("p0_pt",TCut('p0_npho==2 && p0_resolvedcount == 2 && ( (p0_Pho1out==1 && p0_Pho2out==0) || (p0_Pho1out==0 && p0_Pho2out==1) )  '))
    #    evs_2pho_4missing = tch.Draw("p0_pt",TCut('p0_npho==2 && p0_resolvedcount == 2 && p0_Pho1out==1 && p0_Pho2out==1  '))
    #    evs_2pho_1res_1fat = tch.Draw("p0_pt",TCut('p0_npho==2 && p0_resolvedcount == 1 '))
    #    evs_2pho_2res = tch.Draw("p0_pt",TCut('p0_npho==2 && p0_resolvedcount == 2 '))
       evs_2pho_not = evs_2 - (evs_2pho+evs_2pho_2resolved_2inacceptance+evs_2pho_2resolved_1inacceptance+evs_2pho_2resolved_0inacceptance)
    #    print (evs_4pho+evs_4pho_not+evs_3pho+evs_3pho_3resolved+evs_3pho_1resolved_2fat+evs_3pho_3fat+evs_3pho_not+evs_2pho+evs_2pho_2resolved+evs_2pho_1resolved_1fat+evs_2pho_not)/(evs_2+evs_3+evs_4)
    #    print float(evs_2pho+evs_2pho_2resolved+evs_2pho_1resolved_1fat+evs_2pho_not)/float(totevs)
#print " 2 pho ", evs_2, " under category ", evs_2pho, "not ", evs_2pho_not, " all in acceptance ", evs_2pho_2fat_inacceptance, " 1 missing ", evs_2pho_2fat_outacceptance, " others ", evs_2pho_other
#print " 3 pho ", evs_3," under category ", evs_3pho, "not ", evs_3 - evs_3pho
#       print " all resolved ", evs_3pho_1missing + evs_3pho_2missing + evs_3pho_3missing + evs_3pho_4missing
#       print " 1 resolved + 2 merged ", evs_3pho_1res_2fat
#       print " 3 merged ", evs_3pho_3fat

    #    print (evs_4pho_allresolved_inacceptance+evs_4pho_allresolved_outacceptance+evs_4pho_other+evs_4pho_not+evs_3pho_fatpho_inacceptance+evs_3pho_fatpho_outacceptance+evs_3pho_other+evs_3pho_1missing+evs_3pho_2missing+evs_3pho_3missing+evs_3pho_4missing+evs_3pho_1res_2fat+evs_3pho_3fat+evs_3pho_not+evs_2pho_2fat_inacceptance+evs_2pho_2fat_outacceptance+evs_2pho_other+evs_2pho_2missing+evs_2pho_3missing+evs_2pho_4missing+evs_2pho_1res_1fat+evs_2pho_2res+evs_2pho_not)/totevs

    #    text_file.write(" mass : %s all events : %s More than 0 photons : %s \n " % (m,allevs,totevs))

       ## calculate efficiencies now
       eff_evs_4pho_allresolved_allinacceptance = float(evs_4pho_allresolved_allinacceptance)/float(totevs)
       eff_evs_4pho_allresolved_1missing = float(evs_4pho_allresolved_1missing)/float(totevs)
       eff_evs_4pho_other = float(evs_4pho_other)/float(totevs)
       eff_evs_4pho_not = float(evs_4pho_not)/float(totevs)

    #    eff_evs_4pho = float(evs_4pho)/float(totevs)
    #    print    eff_evs_4pho_allresolved_allinacceptance+eff_evs_4pho_allresolved_1missing+eff_evs_4pho_other+eff_evs_4pho_not
    #    print eff_evs_4pho+eff_evs_4pho_not
       eff_evs_3pho_fatpho_allinacceptance = float(evs_3pho_fatpho_allinacceptance)/float(totevs)
       eff_evs_3pho_fatpho_1missing = float(evs_3pho_fatpho_1missing)/float(totevs)
       eff_evs_3pho_other = float(evs_3pho_other)/float(totevs)
       #eff_evs_3pho_not = float(evs_3pho_not)/float(totevs)

       eff_evs_3pho_3resolved_3inacceptance = float(evs_3pho_3resolved_3inacceptance)/float(totevs)
       eff_evs_3pho_3resolved_2inacceptance = float(evs_3pho_3resolved_2inacceptance)/float(totevs)
       eff_evs_3pho_3resolved_1inacceptance = float(evs_3pho_3resolved_1inacceptance)/float(totevs)
       eff_evs_3pho_3resolved_0inacceptance = float(evs_3pho_3resolved_0inacceptance)/float(totevs)
    #    eff_evs_3pho_1resolved_2fat = float(evs_3pho_1resolved_2fat)/float(totevs)
    #    eff_evs_3pho_3fat = float(evs_3pho_3fat)/float(totevs)

       eff_evs_3pho_not = float(evs_3pho_not)/float(totevs)
    #    eff_evs_3pho = float(evs_3pho)/float(totevs)
    #    print eff_evs_3pho+eff_evs_3pho_not+eff_evs_3pho_3resolved+eff_evs_3pho_1resolved_2fat+eff_evs_3pho_3fat
    #    eff_evs_3pho_1missing = float(evs_3pho_1missing)/float(totevs)
    #    eff_evs_3pho_2missing = float(evs_3pho_2missing)/float(totevs)
    #    eff_evs_3pho_3missing = float(evs_3pho_3missing)/float(totevs)
    #    eff_evs_3pho_4missing = float(evs_3pho_4missing)/float(totevs)
    #    eff_evs_3pho_1res_2fat = float(evs_3pho_1res_2fat)/float(totevs)
    #    eff_evs_3pho_3fat = float(evs_3pho_3fat)/float(totevs)



       if float(evs_2pho_2fat_allinacceptance) > 0:
          eff_evs_2pho_2fat_allinacceptance = float(evs_2pho_2fat_allinacceptance)/float(totevs)
       else: eff_evs_2pho_2fat_allinacceptance = 0
       if float(evs_2pho_2fat_1missing) > 0:
          eff_evs_2pho_2fat_1missing = float(evs_2pho_2fat_1missing)/float(totevs)
       else: eff_evs_2pho_2fat_1missing = 0
       if float(evs_2pho_other) > 0:
          eff_evs_2pho_other =float(evs_2pho_other)/float(totevs)
       else: eff_evs_2pho_other =0
       if float(evs_2pho_2resolved_2inacceptance) > 0:
           eff_evs_2pho_2resolved_2inacceptance = float(evs_2pho_2resolved_2inacceptance)/float(totevs)
       else: eff_evs_2pho_2resolved_2inacceptance = 0
       if float(evs_2pho_2resolved_1inacceptance) > 0:
           eff_evs_2pho_2resolved_1inacceptance = float(evs_2pho_2resolved_1inacceptance)/float(totevs)
       else: eff_evs_2pho_2resolved_1inacceptance = 0
       if float(evs_2pho_2resolved_0inacceptance) > 0:
           eff_evs_2pho_2resolved_0inacceptance = float(evs_2pho_2resolved_0inacceptance)/float(totevs)
       else: eff_evs_2pho_2resolved_0inacceptance = 0
    #    if float(evs_2pho_1resolved_1fat) > 0:
    #       eff_evs_2pho_1resolved_1fat = float(evs_2pho_1resolved_1fat)/float(totevs)
    #    else: eff_evs_2pho_1resolved_1fat = 0
       if float(evs_2pho_not) > 0:
         eff_evs_2pho_not = float(evs_2pho_not)/float(totevs)
       else: eff_evs_2pho_not = 0
       print eff_evs_2pho_not+eff_evs_2pho_2resolved_2inacceptance+eff_evs_2pho_2resolved_1inacceptance+eff_evs_2pho_2resolved_0inacceptance+eff_evs_2pho_other+eff_evs_2pho_2fat_1missing+eff_evs_2pho_2fat_allinacceptance+eff_evs_3pho_not+eff_evs_3pho_3resolved_3inacceptance+eff_evs_3pho_3resolved_2inacceptance+eff_evs_3pho_3resolved_1inacceptance+eff_evs_3pho_3resolved_0inacceptance+eff_evs_3pho_fatpho_allinacceptance+eff_evs_3pho_fatpho_1missing+eff_evs_3pho_other+eff_evs_4pho_allresolved_allinacceptance+eff_evs_4pho_allresolved_1missing+eff_evs_4pho_other+eff_evs_4pho_not
    #    if float(evs_2pho) > 0:
    #      eff_evs_2pho = float(evs_2pho)/float(totevs)
    #    else: eff_evs_2pho = 0
    #    print eff_evs_2pho+eff_evs_2pho_2resolved+eff_evs_2pho_1resolved_1fat+eff_evs_2pho_not+eff_evs_3pho+eff_evs_3pho_not+eff_evs_3pho_3resolved+eff_evs_3pho_1resolved_2fat+eff_evs_3pho_3fat+eff_evs_4pho_allresolved_allinacceptance+eff_evs_4pho_allresolved_1missing+eff_evs_4pho_other+eff_evs_4pho_not

    #    if float(evs_2pho_2missing) > 0:
    #       eff_evs_2pho_2missing = float(evs_2pho_2missing)/float(totevs)
    #    else: eff_evs_2pho_2missing = 0
    #    if float(evs_2pho_3missing) > 0:
    #       eff_evs_2pho_3missing = float(evs_2pho_3missing)/float(totevs)
    #    else: eff_evs_2pho_3missing = 0
    #    if float(evs_2pho_4missing) > 0:
    #       eff_evs_2pho_4missing = float(evs_2pho_4missing)/float(totevs)
    #    else: eff_evs_2pho_4missing = 0
    #    if float(evs_2pho_1res_1fat) > 0:
    #       eff_evs_2pho_1res_1fat = float(evs_2pho_1res_1fat)/float(totevs)
    #    else: eff_evs_2pho_1res_1fat = 0
    #    if float(evs_2pho_2res) > 0:
    #       eff_evs_2pho_2res = float(evs_2pho_2res)/float(totevs)
    #    else: eff_evs_2pho_2res = 0


#        eff_2 = float(evs_2)/float(totevs)
#        eff_3 = float(evs_3)/float(totevs)
#        eff_4 = float(evs_4)/float(totevs)
#
#        eff_2pho = float(evs_2pho)/float(totevs)
#        eff_3pho = float(evs_3pho)/float(totevs)
#        eff_4pho = float(evs_4pho)/float(totevs)
#
# #       print "eff_4pho ", eff_4pho
#
#        eff_2pho_not = float(evs_2pho_not)/float(totevs)
#        eff_3pho_not = float(evs_3pho_not)/float(totevs)
#        eff_4pho_not = float(evs_4pho_not)/float(totevs)


       c_4pho_allresolved_allinacceptance.append(eff_evs_4pho_allresolved_allinacceptance)
       c_4pho_allresolved_1missing.append(eff_evs_4pho_allresolved_1missing)
       c_4pho_other.append(eff_evs_4pho_other)
       c_4pho_not.append(eff_evs_4pho_not)

       c_3pho_fatpho_allinacceptance.append(eff_evs_3pho_fatpho_allinacceptance)
       c_3pho_fatpho_1missing.append(eff_evs_3pho_fatpho_1missing)
       c_3pho_other.append(eff_evs_3pho_other)
       c_3pho_3resolved_3inacceptance.append(eff_evs_3pho_3resolved_3inacceptance)
       c_3pho_3resolved_2inacceptance.append(eff_evs_3pho_3resolved_2inacceptance)
       c_3pho_3resolved_1inacceptance.append(eff_evs_3pho_3resolved_1inacceptance)
       c_3pho_3resolved_0inacceptance.append(eff_evs_3pho_3resolved_0inacceptance)
       c_3pho_not.append(eff_evs_3pho_not)

    #    c_3pho_1missing.append(eff_evs_3pho_1missing)
    #    c_3pho_2missing.append(eff_evs_3pho_2missing)
    #    c_3pho_3missing.append(eff_evs_3pho_3missing)
    #    c_3pho_4missing.append(eff_evs_3pho_4missing)
    #    c_3pho_3pho_1res_2fat.append(eff_evs_3pho_1res_2fat)
    #    c_3pho_3fat.append(eff_evs_3pho_3fat)

       c_2pho_2fat_allinacceptance.append(eff_evs_2pho_2fat_allinacceptance)
       c_2pho_2fat_1missing.append(eff_evs_2pho_2fat_1missing)
       c_2pho_other.append(eff_evs_2pho_other)
       c_2pho_2resolved_2inacceptance.append(eff_evs_2pho_2resolved_2inacceptance)
       c_2pho_2resolved_1inacceptance.append(eff_evs_2pho_2resolved_1inacceptance)
       c_2pho_2resolved_0inacceptance.append(eff_evs_2pho_2resolved_0inacceptance)
       c_2pho_not.append(eff_evs_2pho_not)

    #    c_2pho_2missing.append(eff_evs_2pho_2missing)
    #    c_2pho_3missing.append(eff_evs_2pho_3missing)
    #    c_2pho_4missing.append(eff_evs_2pho_4missing)
    #    c_2pho_other.append(eff_evs_2pho_other)
    #    c_2pho_1res_1fat.append(eff_evs_2pho_1res_1fat)
    #    c_2pho_2res.append(eff_evs_2pho_2res)

    #    c_2.append(eff_2)
    #    c_3.append(eff_3)
    #    c_4.append(eff_4)
       #
    #    c_2pho.append(eff_2pho)
    #    c_3pho.append(eff_3pho)
    #    c_4pho.append(eff_4pho)

#       print "c_4pho  ", c_4pho





       #print eff_evs_4pho_allresolved_inacceptance+eff_evs_4pho_allresolved_outacceptance+eff_evs_4pho_other+eff_4pho_not+eff_evs_3pho_fatpho_inacceptance+eff_evs_3pho_fatpho_outacceptance+eff_evs_3pho_other+eff_evs_3pho_1res_2fat+eff_evs_3pho_3fat+eff_evs_2pho_2fat_inacceptance+eff_evs_2pho_2fat_outacceptance+eff_evs_2pho_other+eff_evs_2pho_2res+eff_3pho_not+eff_2pho_not

    #    t = PrettyTable(['m(a)','#evs_4pho_allresolved_inacceptance','#evs_4pho_allresolved_outacceptance','#evs_4pho_other','#evs_4pho_not','#evs_3pho_fatpho_inacceptance','#evs_3pho_fatpho_outacceptance','#evs_3pho_other','#evs_3pho_1missing','#evs_3pho_2missing','#evs_3pho_3missing','#evs_3pho_4missing','#evs_3pho_1res_2fat','#evs_3pho_3fat','#evs_3pho_3not','#evs_2pho_2fat_inacceptance','#evs_2pho_2fat_outacceptance','#evs_2pho_other','#evs_2pho_2missing','#evs_2pho_3missing','#evs_2pho_4missing','#evs_2pho_1res_1fat','#evs_2pho_2res','#evs_2pho_not' ])
    #    t.add_row([m, evs_4pho_allresolved_inacceptance,evs_4pho_allresolved_outacceptance,evs_4pho_other,evs_4pho_not,evs_3pho_fatpho_inacceptance,evs_3pho_fatpho_outacceptance,evs_3pho_other,evs_3pho_1missing,evs_3pho_2missing,evs_3pho_3missing,evs_3pho_3missing,evs_3pho_4missing,evs_3pho_1res_2fat,evs_3pho_3fat,evs_3pho_3not,evs_2pho_2fat_inacceptance,evs_2pho_2fat_outacceptance,evs_2pho_other,evs_2pho_2missing,evs_2pho_3missing,evs_2pho_4missing,evs_2pho_1res_1fat,evs_2pho_2res,evs_2pho_not])
    #    print t
#print " checking the sum", eff_evs_4pho_allresolved_inacceptance + eff_evs_4pho_allresolved_outacceptance + eff_evs_4pho_other + eff_4pho_not + eff_evs_3pho_fatpho_inacceptance + eff_evs_3pho_fatpho_outacceptance + eff_evs_3pho_other + eff_3pho_not + eff_evs_2pho_2fat_inacceptance + eff_evs_2pho_2fat_outacceptance + eff_evs_2pho_other + eff_2pho_not
       print "Pseudoscalar mass  ",m , "GeV"
       print " 4 resolved photons (all in acceptance)  ", eff_evs_4pho_allresolved_allinacceptance
       print " 4 resolved photons (1 missing)  ", eff_evs_4pho_allresolved_1missing
       print " 4 resolved photons (>1 missing)  ", eff_evs_4pho_other
       print " 2 resolved + 1 merged photons (all in acceptance)  ", eff_evs_3pho_fatpho_allinacceptance
       print " 2 resolved + 1 merged photons (1 missing)  ", eff_evs_3pho_fatpho_1missing
       print " 2 resolved + 1 merged photons (>1 missing)  ", eff_evs_3pho_other
       print " 2 pairs of merged photons (all in acceptance)  ", eff_evs_2pho_2fat_allinacceptance
       print " 2 pairs of merged photons (1 missing)  ", eff_evs_2pho_2fat_1missing
       print " 2 pairs of merged photons (>1 missing)  ", eff_evs_2pho_other
       print " 3 resolved photons (all in acceptance)" , eff_evs_3pho_3resolved_3inacceptance
       print " 3 resolved photons (2 in acceptance)" , eff_evs_3pho_3resolved_2inacceptance
       print " 3 resolved photons (1 in acceptance)" , eff_evs_3pho_3resolved_1inacceptance
       print " 3 resolved photons (0 in acceptance)" , eff_evs_3pho_3resolved_0inacceptance
       print " 2 resolved photons (2 in acceptance)", eff_evs_2pho_2resolved_2inacceptance
       print " 2 resolved photons (1 in acceptance)", eff_evs_2pho_2resolved_1inacceptance
       print " 2 resolved photons (0 in acceptance)", eff_evs_2pho_2resolved_0inacceptance
       print " 4 photons (not gen matched)", eff_evs_4pho_not
       print " 3 photons (not gen matched)", eff_evs_3pho_not
       print " 2 photons (not gen matched)", eff_evs_2pho_not
    #    print         eff_evs_4pho_allresolved_allinacceptance+eff_evs_4pho_allresolved_1missing+eff_evs_4pho_other+eff_evs_3pho_fatpho_allinacceptance+eff_evs_3pho_fatpho_1missing+eff_evs_3pho_other+eff_evs_2pho_2fat_allinacceptance+eff_evs_2pho_2fat_1missing+eff_evs_2pho_other+eff_evs_3pho_3resolved+eff_evs_3pho_1resolved_2fat+eff_evs_3pho_3fat+eff_evs_3pho_not+eff_evs_2pho_2resolved+eff_evs_2pho_1resolved_1fat+eff_evs_2pho_not+eff_evs_4pho_not

canvas = TCanvas( 'canvas', 'Reco efficiency', 200, 10, 1000, 600 )

bin_edges = np.array([0.1,1, 5 , 10, 15, 20, 25,30 ,35, 40, 45, 50, 55, 60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80], dtype='float64')

#h1_2pho = TH1F('h1_2pho','2 Photons',len(bin_edges)-1, bin_edges )
#h1_3pho = TH1F('h1_3pho','3 Photons',len(bin_edges)-1, bin_edges )
#h1_4pho = TH1F('h1_4pho','4 Photons',len(bin_edges)-1, bin_edges )
#h1_otherpho = TH1F('h1_otherpho','Other Photons',len(bin_edges)-1, bin_edges )


h1_4pho_allresolved_allinacceptance = TH1F('h1_4pho_allresolved_allinacceptance','4 resolved  + in acceptance',len(bin_edges)-1, bin_edges )
h1_4pho_allresolved_1missing = TH1F('h1_4pho_allresolved_1missing','4 resolved + 1 missing',len(bin_edges)-1, bin_edges )
h1_4pho_other = TH1F('h1_4pho_other','4 Photons : Other',len(bin_edges)-1, bin_edges)
h1_4pho_not = TH1F( 'h1_4pho_not', '4 Photons', len(bin_edges)-1, bin_edges )

h1_3pho_fatpho_allinacceptance = TH1F('h1_3pho_fatpho_allinacceptance','2 resolved+1 merged +   in acceptance',len(bin_edges)-1, bin_edges )
h1_3pho_fatpho_1missing = TH1F('h1_3pho_fatpho_1missing','2 resolved+1 merged +  1 missing',len(bin_edges)-1, bin_edges)
h1_3pho_other = TH1F('h1_3pho_other','3 Photons : Other',len(bin_edges)-1, bin_edges)
h1_3pho_not = TH1F( 'h1_3pho_not', '3 Photons', len(bin_edges)-1, bin_edges )
h1_3pho_3resolved_3inacceptance = TH1F( 'h1_3pho_3resolved_3inacceptance', '3 Photons: resolved +3 in acceptance', len(bin_edges)-1, bin_edges )
h1_3pho_3resolved_2inacceptance = TH1F( 'h1_3pho_3resolved_2inacceptance', '3 Photons: resolved +2 in acceptance', len(bin_edges)-1, bin_edges )
h1_3pho_3resolved_1inacceptance = TH1F( 'h1_3pho_3resolved_1inacceptance', '3 Photons: resolved +1 in acceptance', len(bin_edges)-1, bin_edges )
h1_3pho_3resolved_0inacceptance = TH1F( 'h1_3pho_3resolved_0inacceptance', '3 Photons: resolved +0 in acceptance', len(bin_edges)-1, bin_edges )

# h1_3pho_1missing = TH1F('h1_3pho_1missing','3 Photons : 3 resolved + 1 missing',len(bin_edges)-1, bin_edges)
# h1_3pho_2missing = TH1F('h1_3pho_2missing','3 Photons : 3 resolved + 2 missing',len(bin_edges)-1, bin_edges)
# h1_3pho_3missing = TH1F('h1_3pho_3missing','3 Photons : 3 resolved + 3 missing',len(bin_edges)-1, bin_edges)
# h1_3pho_4missing = TH1F('h1_3pho_4missing','3 Photons : 3 resolved + 4 missing',len(bin_edges)-1, bin_edges)
# h1_3pho_1res_2fat = TH1F('h1_3pho_1res_2fat','3 Photons : 1 resolved + 2 merged',len(bin_edges)-1, bin_edges)
# h1_3pho_3fat = TH1F('h1_3pho_3fat','3 Photons : 3 merged',len(bin_edges)-1, bin_edges)

h1_2pho_2fat_allinacceptance = TH1F('h1_2pho_2fat_allinacceptance','2 merged +  in acceptance',len(bin_edges)-1, bin_edges)
h1_2pho_2fat_1missing = TH1F('h1_2pho_2fat_1missing','2 merged +  1 missing',len(bin_edges)-1, bin_edges)
h1_2pho_other = TH1F('h1_2pho_other','2 Photons: Other ',len(bin_edges)-1, bin_edges)
h1_2pho_not = TH1F( 'h1_2pho_not', '2 Photons', len(bin_edges)-1, bin_edges )
h1_2pho_2resolved_2inacceptance = TH1F( 'h1_2pho_2resolved_2inacceptance', '2 Photons: resolved +2 in acceptance', len(bin_edges)-1, bin_edges )
h1_2pho_2resolved_1inacceptance = TH1F( 'h1_2pho_2resolved_1inacceptance', '2 Photons: resolved +1 in acceptance', len(bin_edges)-1, bin_edges )
h1_2pho_2resolved_0inacceptance = TH1F( 'h1_2pho_2resolved_0inacceptance', '2 Photons: resolved +0 in acceptance', len(bin_edges)-1, bin_edges )

# h1_2pho_2missing = TH1F('h1_2pho_2missing','2 Photons: 2 missing ',len(bin_edges)-1, bin_edges)
# h1_2pho_3missing = TH1F('h1_2pho_3missing','2 Photons: 3 missing ',len(bin_edges)-1, bin_edges)
# h1_2pho_4missing = TH1F('h1_2pho_4missing','2 Photons: 4 missing ',len(bin_edges)-1, bin_edges)
# h1_2pho_1res_1fat = TH1F('h1_2pho_1res_1fat','2 Photons: 1 resolved + 1 merged ',len(bin_edges)-1, bin_edges)
# h1_2pho_2res = TH1F('h1_2pho_2res','2 Photons: 2 resolved ',len(bin_edges)-1, bin_edges)

#h1f_v2_2 = TH1F('h1f_v2_2','2 Photons',len(bin_edges)-1, bin_edges )
#h1f_v2_3 = TH1F('h1f_v2_3','3 Photons',len(bin_edges)-1, bin_edges )
#h1f_v2_4 = TH1F('h1f_v2_4','4 Photons',len(bin_edges)-1, bin_edges )
#h1f_v2_2_sel = TH1F('h1f_v2_2_sel','2 Photons+pass selections',len(bin_edges)-1, bin_edges )
#h1f_v2_3_sel = TH1F('h1f_v2_3_sel','3 Photons+pass selections',len(bin_edges)-1, bin_edges )
#h1f_v2_4_sel = TH1F('h1f_v2_4_sel','4 Photons+pass selections',len(bin_edges)-1, bin_edges )
#h1f_v2_2_presel = TH1F('h1f_v2_2_presel','2 Photons+pass selections + preselections',len(bin_edges)-1, bin_edges )
#h1f_v2_3_presel = TH1F('h1f_v2_3_presel','3 Photons+pass selections + preselections',len(bin_edges)-1, bin_edges )
#h1f_v2_4_presel = TH1F('h1f_v2_4_presel','4 Photons+pass selections + preselections',len(bin_edges)-1, bin_edges )




# h1f_4 = TH1F( 'h1f_4', '4 Photons', len(bin_edges)-1, bin_edges )
# h1f_3 = TH1F( 'h1f_3', '3 Photons', len(bin_edges)-1, bin_edges )
# h1f_2 = TH1F( 'h1f_2', '2 Photons', len(bin_edges)-1, bin_edges )
# h1f_4pho = TH1F( 'h1f_4pho', '4 Photons', len(bin_edges)-1, bin_edges )
# h1f_3pho = TH1F( 'h1f_3pho', '3 Photons', len(bin_edges)-1, bin_edges )
# h1f_2pho = TH1F( 'h1f_2pho', '2 Photons', len(bin_edges)-1, bin_edges )

#h1f_4_1 = TH1F( 'h1f_4_1','4 Photons : all resolved + passtrigger +in acceptnace ', len(bin_edges)-1, bin_edges)
#h1f_4_2 = TH1F( 'h1f_4_2','4 Photons : all resolved + passtrigger + 1 out of acceptance ', len(bin_edges)-1, bin_edges)
#h1f_4_other = TH1F('h1f_4_other','4 Photons : other',len(bin_edges)-1, bin_edges)
#h1f_3_1 = TH1F('h1f_3_1','3 Photons : 2 resolved+1Fat +pass Trigger + in acceptance',len(bin_edges)-1, bin_edges)
#h1f_3_2 = TH1F('h1f_3_2','3 Photons : 3 resolved+1 Missing +pass Trigger',len(bin_edges)-1, bin_edges)
#h1f_3_other = TH1F('h1f_3_other','3 Photons : Other',len(bin_edges)-1, bin_edges)
#h1f_2_1 = TH1F('h1F_2_1','2 Photons : 2 fat + passtrigger + in acceptance',len(bin_edges)-1, bin_edges)
#h1f_2_2 = TH1F('h1f_2_2','2 Photons : 2 resolved + passtrigger + out of acceptance',len(bin_edges)-1, bin_edges)
#h1f_2_other = TH1F('h1f_2_other','2 Photons : other',len(bin_edges)-1, bin_edges)

#h1f_Fourpho = TH1F ('h1f_Fourpho','4 Photons',len(bin_edges)-1, bin_edges )
#h1f_Threepho = TH1F ('h1f_Threepho','3 Photons',len(bin_edges)-1, bin_edges )
#h1f_Twopho = TH1F ('h1f_Twopho','2 Photons',len(bin_edges)-1, bin_edges )
#h1f_4_case1 = TH1F ('h1f_4_case1','4 Photons:case1',len(bin_edges)-1, bin_edges )
#h1f_4_case2 = TH1F ('h1f_4_case2','4 Photons:case1',len(bin_edges)-1, bin_edges )
#h1f_4_caseother = TH1F ('h1f_4_caseother','4 Photons:case other',len(bin_edges)-1, bin_edges )
for i in range(0,14):


    #h1f_4.Fill(masses[i],c_4[i])
    #h1f_3.Fill(masses[i],c_3[i])
    #h1f_2.Fill(masses[i],c_2[i])
    # h1f_4pho.Fill(masses[i],c_4pho[i])
    # h1f_4pho_not.Fill(masses[i],c_4pho_not[i])
    # h1f_3pho.Fill(masses[i],c_3pho[i])
    # h1f_3pho_not.Fill(masses[i],c_3pho_not[i])
    # h1f_2pho.Fill(masses[i],c_2pho[i])
    # h1f_2pho_not.Fill(masses[i],c_2pho_not[i])

    h1_4pho_allresolved_allinacceptance.Fill(masses[i],c_4pho_allresolved_allinacceptance[i])
    h1_4pho_allresolved_1missing.Fill(masses[i],c_4pho_allresolved_1missing[i])
    h1_4pho_other.Fill(masses[i],c_4pho_other[i])
    h1_4pho_not.Fill(masses[i],c_4pho_not[i])

    h1_3pho_fatpho_allinacceptance.Fill(masses[i],c_3pho_fatpho_allinacceptance[i])
    h1_3pho_fatpho_1missing.Fill(masses[i],c_3pho_fatpho_1missing[i])
    h1_3pho_other.Fill(masses[i],c_3pho_other[i])
    h1_3pho_not.Fill(masses[i],c_3pho_not[i])
    h1_3pho_3resolved_3inacceptance.Fill(masses[i],c_3pho_3resolved_3inacceptance[i])
    h1_3pho_3resolved_2inacceptance.Fill(masses[i],c_3pho_3resolved_2inacceptance[i])
    h1_3pho_3resolved_1inacceptance.Fill(masses[i],c_3pho_3resolved_1inacceptance[i])
    h1_3pho_3resolved_0inacceptance.Fill(masses[i],c_3pho_3resolved_0inacceptance[i])

    # h1_3pho_1missing.Fill(masses[i],c_3pho_1missing[i])
    # h1_3pho_2missing.Fill(masses[i],c_3pho_2missing[i])
    # h1_3pho_3missing.Fill(masses[i],c_3pho_3missing[i])
    # h1_3pho_4missing.Fill(masses[i],c_3pho_4missing[i])
    # h1_3pho_1res_2fat.Fill(masses[i],c_3pho_3pho_1res_2fat[i])
    # h1_3pho_3fat.Fill(masses[i],c_3pho_3fat[i])

    h1_2pho_2fat_allinacceptance.Fill(masses[i],c_2pho_2fat_allinacceptance[i])
    h1_2pho_2fat_1missing.Fill(masses[i],c_2pho_2fat_1missing[i])
    h1_2pho_other.Fill(masses[i],c_2pho_other[i])
    h1_2pho_not.Fill(masses[i],c_2pho_not[i])
    h1_2pho_2resolved_2inacceptance.Fill(masses[i],c_2pho_2resolved_2inacceptance[i])
    h1_2pho_2resolved_1inacceptance.Fill(masses[i],c_2pho_2resolved_1inacceptance[i])
    h1_2pho_2resolved_0inacceptance.Fill(masses[i],c_2pho_2resolved_0inacceptance[i])



    # h1_2pho_2missing.Fill(masses[i],c_2pho_2missing[i])
    # h1_2pho_3missing.Fill(masses[i],c_2pho_3missing[i])
    # h1_2pho_4missing.Fill(masses[i],c_2pho_4missing[i])
    # h1_2pho_1res_1fat.Fill(masses[i],c_2pho_1res_1fat[i])
    # h1_2pho_2res.Fill(masses[i],c_2pho_2res[i])

h1_4pho_allresolved_1missing.Add(h1_3pho_3resolved_3inacceptance)
h1_4pho_other.Add(h1_3pho_3resolved_2inacceptance)
h1_4pho_other.Add(h1_3pho_3resolved_1inacceptance)
h1_4pho_other.Add(h1_3pho_3resolved_0inacceptance)
h1_4pho_other.Add(h1_2pho_2resolved_2inacceptance)
h1_4pho_other.Add(h1_2pho_2resolved_1inacceptance)
h1_4pho_other.Add(h1_2pho_2resolved_0inacceptance)


#Get pretty colors
cNiceBlue = TColor.GetColor('#51A7F9')
cNiceBlueDark = TColor.GetColor('#2175E0')
cNiceGreen = TColor.GetColor('#6FBF41')
cNiceGreenDark = TColor.GetColor('#008040')
cNiceRed = TColor.GetColor('#FA4912')



h1_4pho_allresolved_allinacceptance.SetFillColor(cNiceRed)
h1_4pho_allresolved_allinacceptance.SetLineColor(cNiceRed)
h1_4pho_allresolved_1missing.SetFillColor(cNiceRed)
h1_4pho_allresolved_1missing.SetLineColor(cNiceRed)
h1_4pho_allresolved_1missing.SetFillStyle(3004)
h1_4pho_other.SetFillColor(cNiceRed)
h1_4pho_other.SetLineColor(cNiceRed)
h1_4pho_other.SetFillStyle(3244)
h1_4pho_not.SetLineColor(cNiceRed)
h1_4pho_not.SetFillColor(cNiceRed)
h1_4pho_not.SetFillStyle(3021)

h1_3pho_fatpho_allinacceptance.SetFillColor(cNiceGreenDark)
h1_3pho_fatpho_allinacceptance.SetLineColor(cNiceGreenDark)
h1_3pho_fatpho_1missing.SetFillColor(cNiceGreenDark)
h1_3pho_fatpho_1missing.SetLineColor(cNiceGreenDark)
h1_3pho_fatpho_1missing.SetFillStyle(3004)
h1_3pho_other.SetFillColor(cNiceGreenDark)
h1_3pho_other.SetLineColor(cNiceGreenDark)
h1_3pho_other.SetFillStyle(3244)
h1_3pho_not.SetLineColor(cNiceGreenDark)
h1_3pho_not.SetFillColor(cNiceGreenDark)
h1_3pho_not.SetFillStyle(3021)
# h1_3pho_1missing.SetFillColor(cNiceRed)
# h1_3pho_1missing.SetLineColor(cNiceRed)
# h1_3pho_1missing.SetFillStyle(3004)
# h1_3pho_2missing.SetFillColor(cNiceRed)
# h1_3pho_2missing.SetLineColor(cNiceRed)
# h1_3pho_2missing.SetFillStyle(3224)
# h1_3pho_3missing.SetFillColor(cNiceRed)
# h1_3pho_3missing.SetLineColor(cNiceRed)
# h1_3pho_3missing.SetFillStyle(3224)
# h1_3pho_4missing.SetFillColor(cNiceRed)
# h1_3pho_4missing.SetLineColor(cNiceRed)
# h1_3pho_4missing.SetFillStyle(3224)
# h1_3pho_1res_2fat.SetFillColor(cNiceGreenDark)
# h1_3pho_1res_2fat.SetLineColor(cNiceGreenDark)
# h1_3pho_1res_2fat.SetFillStyle(3021)
# h1_3pho_3fat.SetFillColor(cNiceGreenDark)
# h1_3pho_3fat.SetLineColor(cNiceGreenDark)
# h1_3pho_3fat.SetFillStyle(3007)



h1_2pho_2fat_allinacceptance.SetFillColor(cNiceBlueDark)
h1_2pho_2fat_allinacceptance.SetLineColor(cNiceBlueDark)
h1_2pho_2fat_1missing.SetFillColor(cNiceBlueDark)
h1_2pho_2fat_1missing.SetLineColor(cNiceBlueDark)
h1_2pho_2fat_1missing.SetFillStyle(3004)
h1_2pho_other.SetFillColor(cNiceBlueDark)
h1_2pho_other.SetLineColor(cNiceBlueDark)
h1_2pho_other.SetFillStyle(3244)
h1_2pho_not.SetLineColor(cNiceBlueDark)
h1_2pho_not.SetFillColor(cNiceBlueDark)
h1_2pho_not.SetFillStyle(3021)
# h1_2pho_2missing.SetFillColor(cNiceRed)
# h1_2pho_2missing.SetLineColor(cNiceRed)
# h1_2pho_2missing.SetFillStyle(3244)
# h1_2pho_3missing.SetFillColor(cNiceRed)
# h1_2pho_3missing.SetLineColor(cNiceRed)
# h1_2pho_3missing.SetFillStyle(3244)
# h1_2pho_4missing.SetFillColor(cNiceRed)
# h1_2pho_4missing.SetLineColor(cNiceRed)
# h1_2pho_4missing.SetFillStyle(3244)
# h1_2pho_1res_1fat.SetFillColor(cNiceBlueDark)
# h1_2pho_1res_1fat.SetLineColor(cNiceBlueDark)
# h1_2pho_1res_1fat.SetFillStyle(3021)
# h1_2pho_2res.SetFillColor(cNiceBlueDark)
# h1_2pho_2res.SetLineColor(cNiceBlueDark)
# h1_2pho_2res.SetFillStyle(3007)

# h1f_4.SetFillColor(cNiceRed)
# h1f_4pho.SetLineColor(cNiceRed)
# h1f_4pho.SetFillColor(cNiceRed)
# #h1f_4pho.SetFillStyle(3004)
#
#
# h1f_3.SetFillColor(cNiceGreenDark)
# h1f_3pho.SetLineColor(cNiceGreenDark)
# h1f_3pho.SetFillColor(cNiceGreenDark)
# #h1f_3pho.SetFillStyle(3004)
#
#
# h1f_2.SetFillColor(cNiceBlueDark)
# h1f_2pho.SetLineColor(cNiceBlueDark)
# h1f_2pho.SetFillColor(cNiceBlueDark)
# #h1f_2pho.SetFillStyle(3004)



# h1_4pho_allresolved_outacceptance.Add(h1_3pho_1missing)
# h1_4pho_other.Add(h1_2pho_2missing)
# h1_4pho_other.Add(h1_2pho_3missing)
# h1_4pho_other.Add(h1_2pho_4missing)
# h1_4pho_other.Add(h1_3pho_2missing)
# h1_4pho_other.Add(h1_3pho_3missing)
# h1_4pho_other.Add(h1_3pho_4missing)



s = THStack("s","Reco level categorization")


s.Add(h1_4pho_allresolved_allinacceptance)
s.Add(h1_3pho_fatpho_allinacceptance)
s.Add(h1_2pho_2fat_allinacceptance)
s.Add(h1_4pho_allresolved_1missing)
s.Add(h1_3pho_fatpho_1missing)
s.Add(h1_2pho_2fat_1missing)
s.Add(h1_4pho_other)
s.Add(h1_3pho_other)
s.Add(h1_2pho_other)
s.Add(h1_4pho_not)
s.Add(h1_3pho_not)
s.Add(h1_2pho_not)

# s.Add(h1_3pho_1res_2fat)
# s.Add(h1_3pho_3fat)
# s.Add(h1_2pho_1res_1fat)
# s.Add(h1_2pho_2res)

s.Draw("hist")
s.SetMaximum(1.0)
s.GetXaxis().SetTitle('m(a) GeV')
s.GetYaxis().SetTitle('Reco level efficiency')
s.GetYaxis().SetTitleOffset(1)


#leg = TLegend(0.1,0.7,0.48,0.9)
leg = TLegend(0.71245,0.664247,0.89479,0.872958)
#leg = TLegend(0.6, 0.7, 0.89, 0.89)
#leg = TLegend(0.13,0.65,0.87, 0.89)
leg.SetBorderSize(0)
leg.SetHeader("Reco level categories")
leg.AddEntry(h1_4pho_allresolved_allinacceptance,"4 resolved: all in acceptance.",'f')
leg.AddEntry(h1_3pho_fatpho_allinacceptance,"2 resolved+1merged: all in acceptance",'f')
leg.AddEntry(h1_2pho_2fat_allinacceptance,"2 merged: all in acceptance",'f')
leg.AddEntry(h1_4pho_allresolved_1missing,"4 resolved: 1 missing ",'f')
leg.AddEntry(h1_3pho_fatpho_1missing,"2 resolved+1merged: 1 missing",'f')
leg.AddEntry(h1_2pho_2fat_1missing,"2 merged: 1 missing",'f')
leg.AddEntry(h1_4pho_other,"4 resolved: #geq 1 missing",'f')
leg.AddEntry(h1_3pho_other,"2 resolved+1merged: #geq 1 missing",'f')
leg.AddEntry(h1_2pho_other,"2 merged: #geq 1 missing",'f')
leg.AddEntry(h1_4pho_not, "#geq 4 Photons: Not gen matched", 'f')
leg.AddEntry(h1_3pho_not, "= 3 Photons: Not gen matched", 'f')
leg.AddEntry(h1_2pho_not, "= 2 Photons: Not gen matched", 'f')


#leg.AddEntry(h1_4pho,">3 Photons",'f')
#leg.AddEntry(h1_3pho,"=3 Photons",'f')
#leg.AddEntry(h1_2pho,"=2 Photons",'f')
#leg.AddEntry(h1_4pho_passtrigger,">3 Photons + passTrigger",'f')
#leg.AddEntry(h1_4pho_allresolved_passtrigger_inacceptance,">3 Photons + passTrigger + all resolved + in acceptance",'f')
#leg.AddEntry(h1_4pho_passtrigger_allresolved_inacceptance,"4 resolved:passTrigger + All in acceptance",'f')

#leg.AddEntry(h1_3pho_passtrigger_fatpho_inacceptance,"2 resolved + 1 Fat:passTrigger +  All in acceptance",'f')
#leg.AddEntry(h1_2pho_passtrigger_2fat_inacceptance,"2 Fat: passTrigger + All in acceptance",'f')
#leg.AddEntry(h1_4pho_passtrigger_allresolved_outacceptance,"4 resolved:passTrigger + 1 Missing ",'f')

#leg.AddEntry(h1_3pho_passtrigger_fatpho_outacceptance,"2 resolved + 1 Fat:passTrigger + 1 Missing",'f')
#leg.AddEntry(h1_2pho_passtrigger_2fat_outacceptance,"2 Fat: passTrigger + 1 Missing",'f')
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







#leg.AddEntry(h1f_4, ">3 Photons", 'f')
#leg.AddEntry(h1f_3, "=3 Photons", 'f')
#leg.AddEntry(h1f_2, "=2 Photons", 'f')

#leg.AddEntry(h1f_4pho, ">3 Photons: All resolved", 'f')
#leg.AddEntry(h1f_3pho, "=3 Photons: 2 resolved + 1 merged", 'f')
#leg.AddEntry(h1f_2pho, "=2 Photons: 2 merged + 2 merged", 'f')

#leg.AddEntry(h1_3pho_1missing, "=3 Photons: 1 missing", 'f')
# leg.AddEntry(h1_3pho_1res_2fat, "=3 Photons: 1 resolved + 2 merged ", 'f')
# leg.AddEntry(h1_3pho_3fat, "=3 Photons: 3 merged ", 'f')
#
# leg.AddEntry(h1_2pho_1res_1fat, "=2 Photons: 1 resolved + 1 merged", 'f')
# leg.AddEntry(h1_2pho_2res, "=2 Photons: 2 resolved", 'f')


leg.SetTextSize(0.02)
leg.SetFillStyle(0)
leg.Draw("same")

#canvas.BuildLegend()
canvas.Update()
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/2018_HGGGG/RecoCategorization_4Jul.png")
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/2018_HGGGG/RecoCategorization_4Jul.pdf")
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/2018_HGGGG/RecoCategorization_4Jul.root")

canvas.SetLogy()
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/2018_HGGGG/RecoCategorization_log_4Jul.png")
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/2018_HGGGG/RecoCategorization_log_4Jul.pdf")
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/2018_HGGGG/RecoCategorization_log_4Jul.root")

text_file.close()

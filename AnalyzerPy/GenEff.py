from ROOT import *
from array import array
import numpy as np
from prettytable import PrettyTable
from tabulate import tabulate



files = [
         "Genlevel_15151515/gen_signal_0p1.root",
         "Genlevel_15151515/gen_signal_1.root",
         "Genlevel_15151515/gen_signal_5.root",
         "Genlevel_15151515/gen_signal_10.root",
         "Genlevel_15151515/gen_signal_15.root",
         "Genlevel_15151515/gen_signal_20.root",
         "Genlevel_15151515/gen_signal_25.root",
         "Genlevel_15151515/gen_signal_30.root",
         "Genlevel_15151515/gen_signal_35.root",
         "Genlevel_15151515/gen_signal_40.root",
         "Genlevel_15151515/gen_signal_45.root",
         "Genlevel_15151515/gen_signal_50.root",
         "Genlevel_15151515/gen_signal_55.root",
         "Genlevel_15151515/gen_signal_60.root"
         ]

masses = [0.1, 1, 5 , 10, 15, 20, 25, 30 ,35, 40, 45, 50, 55, 60]
bins = []
c1 = []
c1_4A = []
c1_3A = []
c1_2A = []
c1_1A = []
c1_0A = []
c1_other = []

c2 = []
c2_4A = []
c2_3A = []
c2_2A = []
c2_1A = []
c2_other = []

c3 = []
c3_4A = []
c3_3A = []
c3_2A = []
c3_other = []

for i, m in enumerate(masses):

       tch = TChain("geninfo")
       tch.AddFile(files[i])
       totevs = tch.Draw("totevs","1>0")

       tch1 = TChain("H4GGen_4resolved")
       tch1.AddFile(files[i])
       evs_case1 = tch1.Draw("tp_mass_case1","1>0")
       evs_case1_4A = tch1.Draw("tp_mass_case1",TCut('Pho1out==0 && Pho2out==0 && Pho3out==0 && Pho4out==0'))
       evs_case1_3A = tch1.Draw("tp_mass_case1",TCut('(Pho1out==1 && Pho2out==0 && Pho3out==0 && Pho4out==0) || (Pho1out==0 && Pho2out==1 && Pho3out==0 && Pho4out==0) || (Pho1out==0 && Pho2out==0 && Pho3out==1 && Pho4out==0) || (Pho1out==0 && Pho2out==0 && Pho3out==0 && Pho4out==1)'))
       evs_case1_2A = tch1.Draw("tp_mass_case1",TCut('(Pho1out==1 && Pho2out==1 && Pho3out==0 && Pho4out==0) || (Pho1out==1 && Pho2out==0 && Pho3out==1 && Pho4out==0) || (Pho1out==1 && Pho2out==0 && Pho3out==0 && Pho4out==1) || (Pho1out==0 && Pho2out==1 && Pho3out==1 && Pho4out==0) || (Pho1out==0 && Pho2out==1 && Pho3out==0 && Pho4out==1) || (Pho1out==0 && Pho2out==0 && Pho3out==1 && Pho4out==1)'))
       evs_case1_1A = tch1.Draw("tp_mass_case1",TCut('(Pho1out==1 && Pho2out==1 && Pho3out==1 && Pho4out==0) || (Pho1out==1 && Pho2out==1 && Pho3out==0 && Pho4out==1) || (Pho1out==1 && Pho2out==0 && Pho3out==1 && Pho4out==1) || (Pho1out==0 && Pho2out==1 && Pho3out==1 && Pho4out==1)'))
       evs_case1_0A = tch1.Draw("tp_mass_case1",TCut('Pho1out==1 && Pho2out==1 && Pho3out==1 && Pho4out==1'))
       evs_case1_other = evs_case1 - (evs_case1_4A + evs_case1_3A)


       tch2 = TChain("H4GGen_2res1fat")
       tch2.AddFile(files[i])
       evs_case2 = tch2.Draw("tp_mass_case2","1>0")
       evs_case2_4A = tch2.Draw("tp_mass_case2",TCut('Fatphoout==0 && Isopho1out==0 && Isopho2out==0'))
       evs_case2_3A = tch2.Draw("tp_mass_case2",TCut('(Fatphoout==1 && Isopho1out==0 && Isopho2out==0) || (Fatphoout==0 && Isopho1out==1 && Isopho2out==0) || (Fatphoout==0 && Isopho1out==0 && Isopho2out==1)'))
       evs_case2_2A = tch2.Draw("tp_mass_case2",TCut('(Fatphoout==1 && Isopho1out==1 && Isopho2out==0) || (Fatphoout==1 && Isopho1out==0 && Isopho2out==1) || (Fatphoout==0 && Isopho1out==1 && Isopho2out==1)'))
       evs_case2_1A = tch2.Draw("tp_mass_case2",TCut('Fatphoout==1 && Isopho1out==1 && Isopho2out==1'))
       evs_case2_other = evs_case2 - (evs_case2_4A + evs_case2_3A)


       tch3 = TChain("H4GGen_2fat")
       tch3.AddFile(files[i])
       evs_case3 = tch3.Draw("tp_mass_case3","1>0")
       evs_case3_4A = tch3.Draw("tp_mass_case3",TCut('Fatpho1out==0 && Fatpho2out==0'))
       evs_case3_3A = tch3.Draw("tp_mass_case3",TCut('(Fatpho1out==1 && Fatpho2out==0) || (Fatpho1out==0 && Fatpho2out==1)'))
       evs_case3_2A = tch3.Draw("tp_mass_case3",TCut('Fatpho1out==1 && Fatpho2out==1'))
       evs_case3_other = evs_case3 - (evs_case3_4A + evs_case3_3A)

      ## Calculate efficiencies now

       eff_case1_4A = float(evs_case1_4A)/float(totevs)
       eff_case1_3A = float(evs_case1_3A)/float(totevs)
       eff_case1_2A = float(evs_case1_2A)/float(totevs)
       eff_case1_1A = float(evs_case1_1A)/float(totevs)
       eff_case1_0A = float(evs_case1_0A)/float(totevs)
       eff_case1_other = float(evs_case1_other)/float(totevs)

       if float(evs_case2_4A) > 0:
          eff_case2_4A = float(evs_case2_4A)/float(totevs)
       else: eff_case2_4A = 0
       if float(evs_case2_3A) > 0:
          eff_case2_3A = float(evs_case2_3A)/float(totevs)
       else: eff_case2_3A = 0
       if float(evs_case2_2A) > 0:
          eff_case2_2A = float(evs_case2_2A)/float(totevs)
       else: eff_case2_2A = 0
       if float(evs_case2_1A) > 0:
          eff_case2_1A = float(evs_case2_1A)/float(totevs)
       else: eff_case2_1A = 0
       eff_case2_other = float(evs_case2_other)/float(totevs)

       if float(evs_case3_4A) > 0:
           eff_case3_4A = float(evs_case3_4A)/float(totevs)
       else: eff_case3_4A = 0
       if float(evs_case3_3A) > 0:
           eff_case3_3A = float(evs_case3_3A)/float(totevs)
       else: eff_case3_3A = 0
       if float(evs_case3_2A) > 0:
           eff_case3_2A = float(evs_case3_2A)/float(totevs)
       else: eff_case3_2A =0
       eff_case3_other = float(evs_case3_other)/float(totevs)


       c1_4A.append(eff_case1_4A)
       c1_3A.append(eff_case1_3A)
       c1_2A.append(eff_case1_2A)
       c1_1A.append(eff_case1_1A)
       c1_0A.append(eff_case1_0A)
       c1_other.append(eff_case1_other)

       c2_4A.append(eff_case2_4A)
       c2_3A.append(eff_case2_3A)
       c2_2A.append(eff_case2_2A)
       c2_1A.append(eff_case2_1A)
       c2_other.append(eff_case2_other)

       c3_4A.append(eff_case3_4A)
       c3_3A.append(eff_case3_3A)
       c3_2A.append(eff_case3_2A)
       c3_other.append(eff_case3_other)


    #    t = PrettyTable(["m(a)","4 resolved (all in acceptance)","4 resolved (1 missing)","4 resolved (>1 missing)","2 resolved+1merged (all in acceptance)","2 resolved+1merged (1 missing)","2 resolved+1merged (>1 missing)","2 pairs of merged (all in acceptance)","2 pairs of merged (1 missing)","2 pairs of merged (> 1 missing)"])
    #    t.add_row([m, eff_case1_4A, eff_case1_3A, eff_case1_other, eff_case2_4A, eff_case2_3A, eff_case2_other, eff_case3_4A, eff_case3_3A, eff_case3_other])
    #    print (t)

       print "Pseudoscalar mass  ",m , "GeV"
       print " 4 resolved photons (all in acceptance)  ", eff_case1_4A
       print " 4 resolved photons (1 missing)  ", eff_case1_3A
       print " 4 resolved photons (>1 missing)  ", eff_case1_other
       print " 2 resolved + 1 merged photons (all in acceptance)  ", eff_case2_4A
       print " 2 resolved + 1 merged photons (1 missing)  ", eff_case2_3A
       print " 2 resolved + 1 merged photons (>1 missing)  ", eff_case2_other
       print " 2 pairs of merged photons (all in acceptance)  ", eff_case3_4A
       print " 2 pairs of merged photons (1 missing)  ", eff_case3_3A
       print " 2 pairs of merged photons (>1 missing)  ", eff_case3_other


canvas = TCanvas( 'canvas', 'gen cat efficiency', 200, 10, 1000, 600 )

bin_edges = np.array([0.1,1, 5 , 10, 15, 20, 25,30 ,35, 40, 45, 50, 55, 60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80], dtype='float64')

h1f_4A_4 = TH1F( 'h1f_4A_4', '4resolved:All in acceptance', len(bin_edges)-1, bin_edges )
h1f_4A_3 = TH1F( 'h1f_4A_3', '4resolved:1 Missing', len(bin_edges)-1, bin_edges )
h1f_4A_2 = TH1F( 'h1f_4A_2', '4resolved:2 in acceptance', len(bin_edges)-1, bin_edges )
h1f_4A_1 = TH1F( 'h1f_4A_1', '4resolved:1 in acceptance', len(bin_edges)-1, bin_edges )
h1f_4A_0 = TH1F( 'h1f_4A_0', '4resolved:0 in acceptance', len(bin_edges)-1, bin_edges )
h1f_4A_other = TH1F( 'h1f_4A_other', '4resolved:Other', len(bin_edges)-1, bin_edges )

h1f_3A_4 = TH1F( 'h1f_3A_4', '2resolved+1Merged:All in acceptance', len(bin_edges)-1, bin_edges )
h1f_3A_3 = TH1F( 'h1f_3A_3', '2resolved+1Merged:1 Missing', len(bin_edges)-1, bin_edges )
h1f_3A_2 = TH1F( 'h1f_3A_2', '2resolved+1Merged:1 in acceptance', len(bin_edges)-1, bin_edges )
h1f_3A_1 = TH1F( 'h1f_3A_1', '2resolved+1Merged:0 in acceptance', len(bin_edges)-1, bin_edges )
h1f_3A_other = TH1F( 'h1f_3A_other', '2resolved+1Merged:Other', len(bin_edges)-1, bin_edges )

h1f_2A_4 = TH1F( 'h1f_2A_4', '2Merged:All in acceptance', len(bin_edges)-1, bin_edges )
h1f_2A_3 = TH1F( 'h1f_2A_3', '2Merged:1 Missing', len(bin_edges)-1, bin_edges )
h1f_2A_2 = TH1F( 'h1f_2A_2', '2Merged:0 in acceptance', len(bin_edges)-1, bin_edges )
h1f_2A_other = TH1F( 'h1f_2A_other', '2Merged:other', len(bin_edges)-1, bin_edges )




for i in range(0,14):
    #h1f.Fill(masses[i],c1[i])
    h1f_4A_4.Fill(masses[i],c1_4A[i])
    h1f_4A_3.Fill(masses[i],c1_3A[i])
    h1f_4A_2.Fill(masses[i],c1_2A[i])
    h1f_4A_1.Fill(masses[i],c1_1A[i])
    h1f_4A_0.Fill(masses[i],c1_0A[i])
    h1f_4A_other.Fill(masses[i],c1_other[i])

    h1f_3A_4.Fill(masses[i],c2_4A[i])
    h1f_3A_3.Fill(masses[i],c2_3A[i])
    h1f_3A_2.Fill(masses[i],c2_2A[i])
    h1f_3A_1.Fill(masses[i],c2_1A[i])
    h1f_3A_other.Fill(masses[i],c2_other[i])

    h1f_2A_4.Fill(masses[i],c3_4A[i])
    h1f_2A_3.Fill(masses[i],c3_3A[i])
    h1f_2A_2.Fill(masses[i],c3_2A[i])
    h1f_2A_other.Fill(masses[i],c3_other[i])

#Get pretty colors
cNiceBlue = TColor.GetColor('#51A7F9')
cNiceBlueDark = TColor.GetColor('#2175E0')
cNiceGreen = TColor.GetColor('#6FBF41')
cNiceGreenDark = TColor.GetColor('#008040')
cNiceRed = TColor.GetColor('#FA4912')

h1f_4A_4.SetFillColor(cNiceRed)
h1f_4A_4.SetLineColor(cNiceRed)
h1f_4A_3.SetFillColor(cNiceRed)
h1f_4A_3.SetLineColor(cNiceRed)
h1f_4A_3.SetFillStyle(3004)
h1f_4A_2.SetFillColor(cNiceRed)
h1f_4A_2.SetLineColor(cNiceRed)
h1f_4A_2.SetFillStyle(3015)
h1f_4A_1.SetFillColor(cNiceRed)
h1f_4A_1.SetLineColor(cNiceRed)
h1f_4A_1.SetFillStyle(3019)
h1f_4A_0.SetFillColor(cNiceRed)
h1f_4A_0.SetLineColor(cNiceRed)
h1f_4A_0.SetFillStyle(3014)
h1f_4A_other.SetFillColor(cNiceRed)
h1f_4A_other.SetLineColor(cNiceRed)
h1f_4A_other.SetFillStyle(3244)

h1f_3A_4.SetFillColor(cNiceGreenDark)
h1f_3A_4.SetLineColor(cNiceGreenDark)
h1f_3A_3.SetFillColor(cNiceGreenDark)
h1f_3A_3.SetLineColor(cNiceGreenDark)
h1f_3A_3.SetFillStyle(3004)
h1f_3A_2.SetFillColor(cNiceGreenDark)
h1f_3A_2.SetLineColor(cNiceGreenDark)
h1f_3A_2.SetFillStyle(3015)
h1f_3A_1.SetFillColor(cNiceGreenDark)
h1f_3A_1.SetLineColor(cNiceGreenDark)
h1f_3A_1.SetFillStyle(3019)
h1f_3A_other.SetFillColor(cNiceGreenDark)
h1f_3A_other.SetLineColor(cNiceGreenDark)
h1f_3A_other.SetFillStyle(3244)

h1f_2A_4.SetFillColor(cNiceBlueDark)
h1f_2A_4.SetLineColor(cNiceBlueDark)
h1f_2A_3.SetFillColor(cNiceBlueDark)
h1f_2A_3.SetLineColor(cNiceBlueDark)
h1f_2A_3.SetFillStyle(3004)
h1f_2A_2.SetFillColor(cNiceBlueDark)
h1f_2A_2.SetLineColor(cNiceBlueDark)
h1f_2A_2.SetFillStyle(3015)
h1f_2A_other.SetFillColor(cNiceBlueDark)
h1f_2A_other.SetLineColor(cNiceBlueDark)
h1f_2A_other.SetFillStyle(3244)





s = THStack("s","Gen level categorization ")

s.Add(h1f_4A_4)
s.Add(h1f_3A_4)
s.Add(h1f_2A_4)

s.Add(h1f_4A_3)
s.Add(h1f_3A_3)
s.Add(h1f_2A_3)

s.Add(h1f_4A_other)
s.Add(h1f_3A_other)
s.Add(h1f_2A_other)


s.Draw("hist")
s.SetMaximum(1)
s.GetXaxis().SetTitle('m(a) GeV')
s.GetYaxis().SetTitle('Gen level cat. efficiency')
s.GetYaxis().SetTitleOffset(1)





leg = TLegend(0.71245,0.664247,0.89479,0.872958)
#leg = TLegend(0.6, 0.7, 0.89, 0.89)
leg.SetBorderSize(0)
leg.SetHeader("Gen level categories")

leg.AddEntry(h1f_4A_4,"4 resolved: all in acceptance",'f')
leg.AddEntry(h1f_3A_4,"2 resolved+1 merged: all in acceptance",'f')
leg.AddEntry(h1f_2A_4,"2 merged: all in acceptance",'f')
leg.AddEntry(h1f_4A_3,"4 resolved: 1 missing",'f')
leg.AddEntry(h1f_3A_3,"2 resolved+1 merged: 1 missing",'f')
leg.AddEntry(h1f_2A_3,"2 merged: 1 missing",'f')
leg.AddEntry(h1f_4A_other,"4 resolved: #geq 1 missing",'f')
leg.AddEntry(h1f_3A_other,"2 resolved+1 merged: #geq 1 missing",'f')
leg.AddEntry(h1f_2A_other,"2 Merged: #geq 1 missing",'f')

leg.SetTextSize(0.02)
leg.SetFillStyle(0)
leg.Draw("same")


#canvas.BuildLegend()
canvas.Update()
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/2018_HGGGG/GenLevelCat_15151515.png")
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/2018_HGGGG/GenLevelCat_15151515.pdf")
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/2018_HGGGG/GenLevelCat_15151515.root")

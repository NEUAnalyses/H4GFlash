from ROOT import *
from array import array
import numpy as np



files = [
         "TreesforGenlevelEff/gen_pt30and18_Match0p15_0p1.root",
         "TreesforGenlevelEff/gen_pt30and18_Match0p15_1.root",
         "TreesforGenlevelEff/gen_pt30and18_Match0p15_5.root",
         "TreesforGenlevelEff/gen_pt30and18_Match0p15_10.root",
         "TreesforGenlevelEff/gen_pt30and18_Match0p15_15.root",
         "TreesforGenlevelEff/gen_pt30and18_Match0p150_20.root",
         "TreesforGenlevelEff/gen_pt30and18_Match0p15_25.root",
         "TreesforGenlevelEff/gen_pt30and18_Match0p15_30.root",
         "TreesforGenlevelEff/gen_pt30and18_Match0p15_35.root",
         "TreesforGenlevelEff/gen_pt30and18_Match0p15_40.root",
         "TreesforGenlevelEff/gen_pt30and18_Match0p15_45.root",
         "TreesforGenlevelEff/gen_pt30and18_Match0p15_50.root",
         "TreesforGenlevelEff/gen_pt30and18_Match0p15_55.root",
         "TreesforGenlevelEff/gen_pt30and18_Match0p15_60.root"
         ]

masses = [0.1, 1, 5 , 10, 15, 20, 25, 30 ,35, 40, 45, 50, 55, 60]
#masses = [0.1,1,10,25,40,60]
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
       
       tch1 = TChain("H4GGen_case1")
       tch1.AddFile(files[i])
       evs_case1 = tch1.Draw("tp_mass_case1","1>0")
       evs_case1_4A = tch1.Draw("tp_mass_case1",TCut('Pho1out==0 && Pho2out==0 && Pho3out==0 && Pho4out==0'))
       evs_case1_3A = tch1.Draw("tp_mass_case1",TCut('(Pho1out==1 && Pho2out==0 && Pho3out==0 && Pho4out==0) || (Pho1out==0 && Pho2out==1 && Pho3out==0 && Pho4out==0) || (Pho1out==0 && Pho2out==0 && Pho3out==1 && Pho4out==0) || (Pho1out==0 && Pho2out==0 && Pho3out==0 && Pho4out==1)'))
       evs_case1_2A = tch1.Draw("tp_mass_case1",TCut('(Pho1out==1 && Pho2out==1 && Pho3out==0 && Pho4out==0) || (Pho1out==1 && Pho2out==0 && Pho3out==1 && Pho4out==0) || (Pho1out==1 && Pho2out==0 && Pho3out==0 && Pho4out==1) || (Pho1out==0 && Pho2out==1 && Pho3out==1 && Pho4out==0) || (Pho1out==0 && Pho2out==1 && Pho3out==0 && Pho4out==1) || (Pho1out==0 && Pho2out==0 && Pho3out==1 && Pho4out==1)'))
       evs_case1_1A = tch1.Draw("tp_mass_case1",TCut('(Pho1out==1 && Pho2out==1 && Pho3out==1 && Pho4out==0) || (Pho1out==1 && Pho2out==1 && Pho3out==0 && Pho4out==1) || (Pho1out==1 && Pho2out==0 && Pho3out==1 && Pho4out==1) || (Pho1out==0 && Pho2out==1 && Pho3out==1 && Pho4out==1)'))
       evs_case1_0A = tch1.Draw("tp_mass_case1",TCut('Pho1out==1 && Pho2out==1 && Pho3out==1 && Pho4out==1'))
       

       
       tch2 = TChain("H4GGen_case2")
       tch2.AddFile(files[i])
       evs_case2 = tch2.Draw("tp_mass_case2","1>0")
       evs_case2_4A = tch2.Draw("tp_mass_case2",TCut('Fatphoout==0 && Isopho1out==0 && Isopho2out==0'))
       evs_case2_3A = tch2.Draw("tp_mass_case2",TCut('(Fatphoout==1 && Isopho1out==0 && Isopho2out==0) || (Fatphoout==0 && Isopho1out==1 && Isopho2out==0) || (Fatphoout==0 && Isopho1out==0 && Isopho2out==1)'))
       evs_case2_2A = tch2.Draw("tp_mass_case2",TCut('(Fatphoout==1 && Isopho1out==1 && Isopho2out==0) || (Fatphoout==1 && Isopho1out==0 && Isopho2out==1) || (Fatphoout==0 && Isopho1out==1 && Isopho2out==1)'))
       evs_case2_1A = tch2.Draw("tp_mass_case2",TCut('Fatphoout==1 && Isopho1out==1 && Isopho2out==1'))
       
                                      
       
       tch3 = TChain("H4GGen_case3")
       tch3.AddFile(files[i])
       evs_case3 = tch3.Draw("tp_mass_case3","1>0")
       evs_case3_4A = tch3.Draw("tp_mass_case3",TCut('Fatpho1out==0 && Fatpho2out==0'))
       evs_case3_3A = tch3.Draw("tp_mass_case3",TCut('(Fatpho1out==1 && Fatpho2out==0) || (Fatpho1out==0 && Fatpho2out==1)'))
       evs_case3_2A = tch3.Draw("tp_mass_case3",TCut('Fatpho1out==1 && Fatpho2out==1'))
       
       

       eff_case1 = float(evs_case1)/float(totevs)
       eff_case1_4A = float(evs_case1_4A)/float(totevs)
       eff_case1_3A = float(evs_case1_3A)/float(totevs)
       #eff_case1_2A = float(evs_case1_2A)/float(totevs)
       #eff_case1_1A = float(evs_case1_1A)/float(totevs)
       #eff_case1_0A = float(evs_case1_0A)/float(totevs)
       eff_case1_other = eff_case1 - (eff_case1_4A+eff_case1_3A)#+eff_case1_2A+eff_case1_1A+eff_case1_0A)
       
       eff_case2 = float(evs_case2)/float(totevs)
       eff_case2_4A = float(evs_case2_4A)/float(totevs)
       eff_case2_3A = float(evs_case2_3A)/float(totevs)
       #eff_case2_2A = float(evs_case2_2A)/float(totevs)
       #eff_case2_1A = float(evs_case2_1A)/float(totevs)
       eff_case2_other = eff_case2 - (eff_case2_4A+eff_case2_3A)#+eff_case2_2A+eff_case2_1A)
       
       eff_case3 = float(evs_case3)/float(totevs)
       eff_case3_4A = float(evs_case3_4A)/float(totevs)
       eff_case3_3A = float(evs_case3_3A)/float(totevs)
       #eff_case3_2A = float(evs_case3_2A)/float(totevs)
       eff_case3_other = eff_case3 - (eff_case3_4A+eff_case3_3A)#+eff_case3_2A)
       
       
       eff_other = 1.0 - (eff_case1+eff_case2+eff_case3)
       
       c1.append(eff_case1) # efficiency for case1
       c1_4A.append(eff_case1_4A)
       c1_3A.append(eff_case1_3A)
       #c1_2A.append(eff_case1_2A)
       #c1_1A.append(eff_case1_1A)
       #c1_0A.append(eff_case1_0A)
       c1_other.append(eff_case1_other)
       
       c2.append(eff_case2) # efficiency for case2
       c2_4A.append(eff_case2_4A)
       c2_3A.append(eff_case2_3A)
       #c2_2A.append(eff_case2_2A)
       #c2_1A.append(eff_case2_1A)
       c2_other.append(eff_case2_other)
       
       c3.append(eff_case3) # efficiency for case3
       c3_4A.append(eff_case3_4A)
       c3_3A.append(eff_case3_3A)
       #c3_2A.append(eff_case3_2A)
       c3_other.append(eff_case3_other)





canvas = TCanvas( 'canvas', 'gen cat efficiency', 200, 10, 1000, 600 )

bin_edges = np.array([0.1,1, 5 , 10, 15, 20, 25,30 ,35, 40, 45, 50, 55, 60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80], dtype='float64')

h1f_4A_4 = TH1F( 'h1f_4A_4', '4resolved:All in acceptance', len(bin_edges)-1, bin_edges )
h1f_4A_3 = TH1F( 'h1f_4A_3', '4resolved:1 Missing', len(bin_edges)-1, bin_edges )
#h1f_4A_2 = TH1F( 'h1f_4A_2', '4resolved:2 in acceptance', len(bin_edges)-1, bin_edges )
#h1f_4A_1 = TH1F( 'h1f_4A_1', '4resolved:1 in acceptance', len(bin_edges)-1, bin_edges )
#h1f_4A_0 = TH1F( 'h1f_4A_0', '4resolved:0 in acceptance', len(bin_edges)-1, bin_edges )
h1f_4A_other = TH1F( 'h1f_4A_other', '4resolved:Other', len(bin_edges)-1, bin_edges )

h1f_3A_4 = TH1F( 'h1f_3A_4', '2resolved+1Merged:All in acceptance', len(bin_edges)-1, bin_edges )
h1f_3A_3 = TH1F( 'h1f_3A_3', '2resolved+1Merged:1 Missing', len(bin_edges)-1, bin_edges )
#h1f_3A_2 = TH1F( 'h1f_3A_2', '2resolved+1Fat:1 in acceptance', len(bin_edges)-1, bin_edges )
#h1f_3A_1 = TH1F( 'h1f_3A_1', '2resolved+1Fat:0 in acceptance', len(bin_edges)-1, bin_edges )
h1f_3A_other = TH1F( 'h1f_3A_other', '2resolved+1Merged:Other', len(bin_edges)-1, bin_edges )

h1f_2A_4 = TH1F( 'h1f_2A_4', '2Merged:All in acceptance', len(bin_edges)-1, bin_edges )
h1f_2A_3 = TH1F( 'h1f_2A_3', '2Merged:1 Missing', len(bin_edges)-1, bin_edges )
#h1f_2A_2 = TH1F( 'h1f_2A_2', '2Fat:0 in acceptance', len(bin_edges)-1, bin_edges )
h1f_2A_other = TH1F( 'h1f_2A_other', '2Merged:other', len(bin_edges)-1, bin_edges )




for i in range(0,14):
    #h1f.Fill(masses[i],c1[i])
    h1f_4A_4.Fill(masses[i],c1_4A[i])
    h1f_4A_3.Fill(masses[i],c1_3A[i])
    #h1f_4A_2.Fill(masses[i],c1_2A[i])
    #h1f_4A_1.Fill(masses[i],c1_1A[i])
    #h1f_4A_0.Fill(masses[i],c1_0A[i])
    h1f_4A_other.Fill(masses[i],c1_other[i])
    
    h1f_3A_4.Fill(masses[i],c2_4A[i])
    h1f_3A_3.Fill(masses[i],c2_3A[i])
    #h1f_3A_2.Fill(masses[i],c2_2A[i])
    #h1f_3A_1.Fill(masses[i],c2_1A[i])
    h1f_3A_other.Fill(masses[i],c2_other[i])

    h1f_2A_4.Fill(masses[i],c3_4A[i])
    h1f_2A_3.Fill(masses[i],c3_3A[i])
    #h1f_2A_2.Fill(masses[i],c3_2A[i])
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
#h1f_4A_2.SetFillColor(cNiceBlue)
#h1f_4A_2.SetLineColor(cNiceBlue)
#h1f_4A_2.SetFillStyle(3015)
#h1f_4A_1.SetFillColor(cNiceBlue)
#h1f_4A_1.SetLineColor(cNiceBlue)
#h1f_4A_1.SetFillStyle(3015)
#h1f_4A_0.SetFillColor(cNiceBlue)
#h1f_4A_0.SetLineColor(cNiceBlue)
#h1f_4A_0.SetFillStyle(3015)
h1f_4A_other.SetFillColor(cNiceRed)
h1f_4A_other.SetLineColor(cNiceRed)
h1f_4A_other.SetFillStyle(3244)

h1f_3A_4.SetFillColor(cNiceGreenDark)
h1f_3A_4.SetLineColor(cNiceGreenDark)
h1f_3A_3.SetFillColor(cNiceGreenDark)
h1f_3A_3.SetLineColor(cNiceGreenDark)
h1f_3A_3.SetFillStyle(3004)
#h1f_3A_2.SetFillColor(kAzure+4)
#h1f_3A_2.SetLineColor(kAzure+4)
#h1f_3A_2.SetFillStyle(3015)
#h1f_3A_1.SetFillColor(kAzure+4)
#h1f_3A_1.SetLineColor(kAzure+4)
#h1f_3A_1.SetFillStyle(3015)
h1f_3A_other.SetFillColor(cNiceGreenDark)
h1f_3A_other.SetLineColor(cNiceGreenDark)
h1f_3A_other.SetFillStyle(3244)

h1f_2A_4.SetFillColor(cNiceBlueDark)
h1f_2A_4.SetLineColor(cNiceBlueDark)
h1f_2A_3.SetFillColor(cNiceBlueDark)
h1f_2A_3.SetLineColor(cNiceBlueDark)
h1f_2A_3.SetFillStyle(3004)
#h1f_2A_2.SetFillColor(kAzure+3)
#h1f_2A_2.SetLineColor(kAzure+3)
#h1f_2A_2.SetFillStyle(30015)
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
#s.Add(h1f_4A_2)
#s.Add(h1f_4A_1)
#s.Add(h1f_4A_0)
s.Add(h1f_4A_other)
#s.Add(h1f_3A_2)
#s.Add(h1f_3A_1)
s.Add(h1f_3A_other)
#s.Add(h1f_2A_2)
s.Add(h1f_2A_other)


s.Draw("hist")
s.SetMaximum(1)
s.GetXaxis().SetTitle('m(a) GeV')
s.GetYaxis().SetTitle('Gen level cat. efficiency')
s.GetYaxis().SetTitleOffset(1)


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

#mg = TMultiGraph()
#mg.SetTitle(" 4 resolved photons -- 3 in acceptance ; m(a) GeV; ");
#mg.SetMaximum(1)
#mg.SetMinimum(0)
#mg.Add(gr_15)
#mg.Add(gr_14)
#mg.Add(gr_13)
#mg.Add(gr_12)
#mg.Add(gr_11)
#mg.Add(gr_10)
#mg.Draw("APL")
               
               

leg = TLegend(0.71245,0.664247,0.89479,0.872958)
#leg = TLegend(0.6, 0.7, 0.89, 0.89)
leg.SetBorderSize(0)
leg.SetHeader("Gen level categories")
#leg.AddEntry(gr_15,"Pt>15","lp")
#leg.AddEntry(gr_14,"Pt>14","lp")
#leg.AddEntry(gr_13,"Pt>13","lp")
#leg.AddEntry(gr_12,"Pt>12","lp")
#leg.AddEntry(gr_11,"Pt>11","lp")
#leg.AddEntry(gr_10,"Pt>10","lp")

#leg.AddEntry(h6f,"Others",'f')
#leg.AddEntry(h1f,"4 resolved ",'f')
leg.AddEntry(h1f_4A_4,"4 resolved: All in acceptance",'f')
leg.AddEntry(h1f_3A_4,"2 resolved + 1 Fat: All in acceptance",'f')
leg.AddEntry(h1f_2A_4,"2 Merged: All in acceptance",'f')

leg.AddEntry(h1f_4A_3,"4 resolved: 1 Missing ",'f')
leg.AddEntry(h1f_3A_3,"2 resolved + 1 Merged: 1 Missing",'f')
leg.AddEntry(h1f_2A_3,"2 Merged: 1 Missing",'f')

#leg.AddEntry(h1f_4A_2,"4 resolved: Other",'f')
#leg.AddEntry(h1f_3A_2,"2 resolved + 1 Fat: Other",'f')
#leg.AddEntry(h1f_2A_2,"2 Fat: Other",'f')

#leg.AddEntry(h1f_4A_1,"4 resolved: 3 Missing",'f')
#leg.AddEntry(h1f_3A_1,"2 resolved + 1 Fat: 3 Missing",'f')

#leg.AddEntry(h1f_4A_0,"4 resolved: 4 Missing",'f')

leg.AddEntry(h1f_4A_other,"4 resolved: Other",'f')



leg.AddEntry(h1f_3A_other,"2 resolved + 1 Merged: Other",'f')



leg.AddEntry(h1f_2A_other,"2 Merged: Other",'f')

#leg.AddEntry(h1f_4A_14,"4 resolved : all in acceptance 14 GeV threshold",'f')
#leg.AddEntry(h1f_4A_13,"4 resolved : all in acceptance 13 GeV threshold",'f')
#leg.AddEntry(h1f_4A_12,"4 resolved : all in acceptance 12 GeV threshold",'f')
#leg.AddEntry(h1f_4A_11,"4 resolved : all in acceptance 11 GeV threshold",'f')
#leg.AddEntry(h1f_4A_10,"4 resolved : all in acceptance 10 GeV threshold",'f')


#leg.AddEntry(h1f_3A,"4 resolved : 3 in acceptance ",'f')
#leg.AddEntry(h1f_other,"4 resolved : Other ",'f')
#leg.AddEntry(h2f,"2 resolved +1 fat",'f')
#leg.AddEntry(h2f_4A,"2 resolved+1 fat:all in acceptance",'f')
#leg.AddEntry(h2f_3A,"2 resolved + 1 fat : 3 in acceptance + 1 Missing",'f')
#leg.AddEntry(h2f_other,"2 resolved +1 fat : Other",'f')
#leg.AddEntry(h3f,"2 fat",'f')
#leg.AddEntry(h3f_4A,"2 fat:all in acceptance",'f')
#leg.AddEntry(h1f_3A,"4 resolved:3 in acceptance ",'f')
#leg.AddEntry(h2f_3A,"2 resolved + 1 fat:1 Missing",'f')
#leg.AddEntry(h1f_other,"4 resolved:Other ",'f')
#leg.AddEntry(h2f_other,"2 resolved +1 fat:Other",'f')
#leg.AddEntry(h3f_other,"2 fat:other",'f')
#leg.AddEntry(h1f,"4 Resolved Photons ",'f')
#leg.AddEntry(h3f,"2 Resolved + 1 Fat Photon",'f')
#leg.AddEntry(h5f,"2 Fat Photons",'f')
leg.SetTextSize(0.02)
leg.SetFillStyle(0)
leg.Draw("same")


#canvas.BuildLegend()
canvas.Update()
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/Higgsto4Gamma/GenLevel/GenCategorization.png")
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/Higgsto4Gamma/GenLevel/GenCategorization.pdf")
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/Higgsto4Gamma/GenLevel/GenCategorization.root")


       
       

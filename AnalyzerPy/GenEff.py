from ROOT import *
from array import array

files = [
         "Mar26_2018/gen0p1.root",
         "Mar26_2018/gen1.root",
         "Mar26_2018/gen5.root",
         "Mar26_2018/gen10.root",
         "Mar26_2018/gen15.root",
         "Mar26_2018/gen20.root",
         "Mar26_2018/gen25.root",
         "Mar26_2018/gen30.root",
         "Mar26_2018/gen35.root",
         "Mar26_2018/gen40.root",
         "Mar26_2018/gen45.root",
         "Mar26_2018/gen50.root",
         "Mar26_2018/gen55.root",
         "Mar26_2018/gen60.root"
         ]

masses = [0.1, 1, 5 , 10, 15, 20, 25, 30 ,35, 40, 45, 50, 55, 60]
#masses = [0.1,1,10,25,40,60]
c1 = []
#c1_4A = []
c1_4A_15 = []
c1_4A_14 = []
c1_4A_13 = []
c1_4A_12 = []
c1_4A_11 = []
c1_4A_10 = []
c1_3A_15 = []
c1_3A_14 = []
c1_3A_13 = []
c1_3A_12 = []
c1_3A_11 = []
c1_3A_10 = []
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
c5 = []
c6 = []
for i, m in enumerate(masses):
       tch = TChain("geninfo")
       tch.AddFile(files[i])
       totevs = tch.Draw("totevs","1>0")
       
       EtaCut_case1 = TCut('abs(p1_eta_case1)<2.5 && abs(p2_eta_case1)<2.5 && abs(p3_eta_case1)<2.5 && abs(p4_eta_case1)<2.5')
       PtCut_case1_4A_15 = TCut('p1_pt_case1 > 15 && p2_pt_case1 > 15 && p3_pt_case1 > 15 && p4_pt_case1 > 15')
       PtCut_case1_3A_15 = TCut('p1_pt_case1 > 15 && p2_pt_case1 > 15 && p3_pt_case1 > 15 && p4_pt_case1 < 15')
       
       PtCut_case1_4A_14 = TCut('p1_pt_case1 > 15 && p2_pt_case1 > 15 && p3_pt_case1 > 14 && p4_pt_case1 > 14')
       PtCut_case1_3A_14 = TCut('p1_pt_case1 > 15 && p2_pt_case1 > 15 && p3_pt_case1 > 14 && p4_pt_case1 < 14')
       
       PtCut_case1_4A_13 = TCut('p1_pt_case1 > 15 && p2_pt_case1 > 15 && p3_pt_case1 > 13 && p4_pt_case1 > 13')
       PtCut_case1_3A_13 = TCut('p1_pt_case1 > 15 && p2_pt_case1 > 15 && p3_pt_case1 > 13 && p4_pt_case1 < 13')
       
       PtCut_case1_4A_12 = TCut('p1_pt_case1 > 15 && p2_pt_case1 > 15 && p3_pt_case1 > 12 && p4_pt_case1 > 12')
       PtCut_case1_3A_12 = TCut('p1_pt_case1 > 15 && p2_pt_case1 > 15 && p3_pt_case1 > 12 && p4_pt_case1 < 12')

       PtCut_case1_4A_11 = TCut('p1_pt_case1 > 15 && p2_pt_case1 > 15 && p3_pt_case1 > 11 && p4_pt_case1 > 11')
       PtCut_case1_3A_11 = TCut('p1_pt_case1 > 15 && p2_pt_case1 > 15 && p3_pt_case1 > 11 && p4_pt_case1 < 11')
        
       PtCut_case1_4A_10 = TCut('p1_pt_case1 > 15 && p2_pt_case1 > 15 && p3_pt_case1 > 10 && p4_pt_case1 > 10')
       PtCut_case1_3A_10 = TCut('p1_pt_case1 > 15 && p2_pt_case1 > 15 && p3_pt_case1 > 10 && p4_pt_case1 < 10')
                
       
       
       EtaCut_case2 = TCut('abs(isopho1_eta_case2)<2.5 && abs(isopho2_eta_case2)<2.5 && abs(fatpho_eta_case2)<2.5')
       PtCut_case2_4A = TCut('fatpho_pt_case2 > 15 && isopho1_pt_case2 > 10 && isopho2_pt_case2 >10')
       PtCut_case2_3A = TCut('fatpho_pt_case2 > 15 && isopho1_pt_case2 > 10 && isopho2_pt_case2 <10')
       
       EtaCut_case3 = TCut('abs(fatpho1_eta_case3)<2.5 && abs(fatpho2_eta_case3)<2.5')
       PtCut_case3_4A = TCut('fatpho1_pt_case3 >15 && fatpho2_pt_case3 > 15')
       
       
       
    
       
       Cut_case1_4A_15 = TCut(EtaCut_case1)
       Cut_case1_4A_15 +=PtCut_case1_4A_15
       Cut_case1_3A_15 = TCut(EtaCut_case1)
       Cut_case1_3A_15 +=PtCut_case1_3A_15

       Cut_case1_4A_14 = TCut(EtaCut_case1)
       Cut_case1_4A_14 +=PtCut_case1_4A_14
       Cut_case1_3A_14 = TCut(EtaCut_case1)
       Cut_case1_3A_14 +=PtCut_case1_3A_14
        
       Cut_case1_4A_13 = TCut(EtaCut_case1)
       Cut_case1_4A_13 +=PtCut_case1_4A_13
       Cut_case1_3A_13 = TCut(EtaCut_case1)
       Cut_case1_3A_13 +=PtCut_case1_3A_13
                
       Cut_case1_4A_12 = TCut(EtaCut_case1)
       Cut_case1_4A_12 +=PtCut_case1_4A_12
       Cut_case1_3A_12 = TCut(EtaCut_case1)
       Cut_case1_3A_12 +=PtCut_case1_3A_12
           
       Cut_case1_4A_11 = TCut(EtaCut_case1)
       Cut_case1_4A_11 +=PtCut_case1_4A_11
       Cut_case1_3A_11 = TCut(EtaCut_case1)
       Cut_case1_3A_11 +=PtCut_case1_3A_11
           
       Cut_case1_4A_10 = TCut(EtaCut_case1)
       Cut_case1_4A_10 +=PtCut_case1_4A_10
       Cut_case1_3A_10 = TCut(EtaCut_case1)
       Cut_case1_3A_10 +=PtCut_case1_3A_10
    
    #Cut_case1_3A = TCut(EtaCut_case1)
       #Cut_case1_3A +=PtCut_case1_3A
       
       Cut_case2_4A = TCut(EtaCut_case2)
       Cut_case2_4A +=PtCut_case2_4A
       
       Cut_case2_3A = TCut(EtaCut_case2)
       Cut_case2_3A +=PtCut_case2_3A
       
       Cut_case3_4A = TCut(EtaCut_case3)
       Cut_case3_4A +=PtCut_case3_4A
       
       tch1 = TChain("H4GGen_case1")
       tch1.AddFile(files[i])
       evs_case1 = tch1.Draw("tp_mass_case1","1>0")
       evs_case1_4A_15 = tch1.Draw("tp_mass_case1",TCut(Cut_case1_4A_15))
       evs_case1_4A_14 = tch1.Draw("tp_mass_case1",TCut(Cut_case1_4A_14))
       evs_case1_4A_13 = tch1.Draw("tp_mass_case1",TCut(Cut_case1_4A_13))
       evs_case1_4A_12 = tch1.Draw("tp_mass_case1",TCut(Cut_case1_4A_12))
       evs_case1_4A_11 = tch1.Draw("tp_mass_case1",TCut(Cut_case1_4A_11))
       evs_case1_4A_10 = tch1.Draw("tp_mass_case1",TCut(Cut_case1_4A_10))
       evs_case1_3A_15 = tch1.Draw("tp_mass_case1",TCut(Cut_case1_3A_15))
       evs_case1_3A_14 = tch1.Draw("tp_mass_case1",TCut(Cut_case1_3A_14))
       evs_case1_3A_13 = tch1.Draw("tp_mass_case1",TCut(Cut_case1_3A_13))
       evs_case1_3A_12 = tch1.Draw("tp_mass_case1",TCut(Cut_case1_3A_12))
       evs_case1_3A_11 = tch1.Draw("tp_mass_case1",TCut(Cut_case1_3A_11))
       evs_case1_3A_10 = tch1.Draw("tp_mass_case1",TCut(Cut_case1_3A_10))
       #evs_case1_3A = tch1.Draw("tp_mass_case1",TCut(Cut_case1_3A))
       
       tch2 = TChain("H4GGen_case2")
       tch2.AddFile(files[i])
       evs_case2 = tch2.Draw("tp_mass_case2","1>0")
       evs_case2_4A = tch2.Draw("tp_mass_case2",TCut(Cut_case2_4A))
       evs_case2_3A = tch2.Draw("tp_mass_case2",TCut(Cut_case2_3A))
       
                                      
       
       tch3 = TChain("H4GGen_case3")
       tch3.AddFile(files[i])
       evs_case3 = tch3.Draw("tp_mass_case3","1>0")
       evs_case3_4A = tch3.Draw("tp_mass_case3",TCut(Cut_case3_4A))
       

       eff_case1 = float(evs_case1)/float(totevs)
       eff_case1_4A_15 = float(evs_case1_4A_15)/float(totevs)
       eff_case1_4A_14 = float(evs_case1_4A_14)/float(totevs)
       eff_case1_4A_13 = float(evs_case1_4A_13)/float(totevs)
       eff_case1_4A_12 = float(evs_case1_4A_12)/float(totevs)
       eff_case1_4A_11 = float(evs_case1_4A_11)/float(totevs)
       eff_case1_4A_10 = float(evs_case1_4A_10)/float(totevs)
       eff_case1_3A_15 = float(evs_case1_3A_15)/float(totevs)
       eff_case1_3A_14 = float(evs_case1_3A_14)/float(totevs)
       eff_case1_3A_13 = float(evs_case1_3A_13)/float(totevs)
       eff_case1_3A_12 = float(evs_case1_3A_12)/float(totevs)
       eff_case1_3A_11 = float(evs_case1_3A_11)/float(totevs)
       eff_case1_3A_10 = float(evs_case1_3A_10)/float(totevs)
       #eff_case1_3A = float(evs_case1_3A)/float(totevs)
       #eff_case1_other = eff_case1 - (eff_case1_4A+eff_case1_3A)
       
       eff_case2 = float(evs_case2)/float(totevs)
       eff_case2_4A = float(evs_case2_4A)/float(totevs)
       eff_case2_3A = float(evs_case2_3A)/float(totevs)
       eff_case2_other = eff_case2 - (eff_case2_4A+eff_case2_3A)
       
       eff_case3 = float(evs_case3)/float(totevs)
       eff_case3_4A = float(evs_case3_4A)/float(totevs)
       eff_case3_other = eff_case3 - eff_case3_4A
       eff_other = 1.0 - (eff_case1+eff_case2+eff_case3)
       #print "case1 ", eff_case1, " case 2 ", eff_case2 , "case 3 ", eff_case3  , "case 4 ", eff_case4 , "case 5 ", eff_case5
       
       c1.append(eff_case1) # efficiency for case1
       c1_4A_15.append(eff_case1_4A_15)
       c1_4A_14.append(eff_case1_4A_14)
       c1_4A_13.append(eff_case1_4A_13)
       c1_4A_12.append(eff_case1_4A_12)
       c1_4A_11.append(eff_case1_4A_11)
       c1_4A_10.append(eff_case1_4A_10)
       c1_3A_15.append(eff_case1_3A_15)
       c1_3A_14.append(eff_case1_3A_14)
       c1_3A_13.append(eff_case1_3A_13)
       c1_3A_12.append(eff_case1_3A_12)
       c1_3A_11.append(eff_case1_3A_11)
       c1_3A_10.append(eff_case1_3A_10)
       #c1_3A.append(eff_case1_3A)
       #c1_other.append(eff_case1_other)
       c2.append(eff_case2) # efficiency for case2
       c2_4A.append(eff_case2_4A)
       c2_3A.append(eff_case2_3A)
       c2_other.append(eff_case2_other)
       c3.append(eff_case3) # efficiency for case3
       c3_4A.append(eff_case3_4A)
       c3_other.append(eff_case3_other)
       #c4.append(eff_case4) # efficiency for case4
       #c5.append(eff_case5) # efficiency for case15
       c6.append(eff_other) # others
       
       print m
       print ""
       #print float(evs_case1)
#print float(evs_case1_4A) , float(evs_case1_3A), float(evs_case1) - (float(evs_case1_4A)+float(evs_case1_3A))
       #print float(evs_case1_3A)
#print float(evs_case1) - (float(evs_case1_4A)+float(evs_case1_3A))
#print c2
#print c3
#print c4
#print c5




canvas = TCanvas( 'canvas', 'gen cat efficiency', 200, 10, 1000, 1000 )
h1f = TH1F( 'h1f', 'case1', 200, 0, 80 )
h1f_4A_15 = TH1F( 'h1f_4A_15', 'case1:4 in acceptance 15 gev', 200, 0, 80 )
h1f_4A_14 = TH1F( 'h1f_4A_14', 'case1:4 in acceptance 14 gev', 200, 0, 80 )
h1f_4A_13 = TH1F( 'h1f_4A_13', 'case1:4 in acceptance 13 gev', 200, 0, 80 )
h1f_4A_12 = TH1F( 'h1f_4A_12', 'case1:4 in acceptance 12 gev', 200, 0, 80 )
h1f_4A_11 = TH1F( 'h1f_4A_11', 'case1:4 in acceptance 11 gev', 200, 0, 80 )
h1f_4A_10 = TH1F( 'h1f_4A_10', 'case1:4 in acceptance 10 gev', 200, 0, 80 )

h1f_3A = TH1F( 'h1f_3A', 'case1:3 in acceptance', 200, 0, 80 )
h1f_other = TH1F( 'h1f_other', 'case1:Others', 200, 0, 80 )
h2f = TH1F( 'h2f', 'case2', 200, 0, 80 )
h2f_4A = TH1F( 'h2f_4A', 'case2:4 in acceptance', 200, 0, 80 )
h2f_3A = TH1F( 'h2f_3A', 'case2:3 in acceptance', 200, 0, 80 )
h2f_other = TH1F( 'h2f', 'case2:Others', 200, 0, 80 )
h3f = TH1F( 'h3f', 'case3', 200, 0, 80 )
h3f_4A = TH1F( 'h3f_4A', 'case3: All in acceptance', 200, 0, 80 )
h3f_other = TH1F( 'h3f_other', 'case3: Other', 200, 0, 80 )


#h6f = TH1F( 'h6f', 'others', 300, 0, 80 )

for i in range(0,14):
    #print c5
    h1f.Fill(masses[i],c1[i])
    h1f_4A_15.Fill(masses[i],c1_4A_15[i])
    h1f_4A_14.Fill(masses[i],c1_4A_14[i])
    h1f_4A_13.Fill(masses[i],c1_4A_13[i])
    h1f_4A_12.Fill(masses[i],c1_4A_12[i])
    h1f_4A_11.Fill(masses[i],c1_4A_11[i])
    h1f_4A_10.Fill(masses[i],c1_4A_10[i])
    #h1f_3A.Fill(masses[i],c1_3A[i])
    #h1f_other.Fill(masses[i],c1_other[i])
    h2f.Fill(masses[i],c2[i])
    h2f_4A.Fill(masses[i],c2_4A[i])
    h2f_3A.Fill(masses[i],c2_3A[i])
    h2f_other.Fill(masses[i],c2_other[i])
    h3f.Fill(masses[i],c3[i])
    h3f_4A.Fill(masses[i],c3_4A[i])
    h3f_other.Fill(masses[i],c3_other[i])
                                      

#h6f.Fill(masses[i],c6[i])


h1f.SetFillColor(kPink-9)
h1f_4A_15.SetFillColor(kBlue+1)
h1f_4A_14.SetFillColor(kAzure+10)
h1f_4A_13.SetFillColor(kViolet-4)
h1f_4A_12.SetFillColor(kMagenta+3)
h1f_4A_11.SetFillColor(kRed)
h1f_4A_10.SetFillColor(kBlack)
#h1f_4A.SetFillStyle(3023)
h1f_3A.SetFillColor(kPink-9)
#h1f_3A.SetFillStyle(3012)
h1f_other.SetFillColor(kOrange+3)
#h1f_other.SetFillStyle(3006)
h2f.SetFillColor(39)
h2f.SetFillStyle(3144)
h2f_4A.SetFillColor(kOrange-4)
h2f_3A.SetFillColor(kYellow-3)
h2f_other.SetFillColor(kSpring-7)
h3f.SetFillColor(kOrange+10)
h3f.SetFillStyle(3088)
h3f_4A.SetFillColor(kCyan-3)
h3f_other.SetFillColor(kCyan+4)
#h4f.SetFillColor(kOrange+2)
#h5f.SetFillColor(kBlue-7)
#h6f.SetFillColor(kBlack)


s = THStack("s","")


#s.Add(h1f)
s.Add(h1f_4A_15)
s.Add(h1f_4A_14)
s.Add(h1f_4A_13)
s.Add(h1f_4A_12)
s.Add(h1f_4A_11)
s.Add(h1f_4A_10)
#s.Add(h1f_3A)
#s.Add(h1f_other)
#s.Add(h2f)
#s.Add(h2f_4A)
#s.Add(h2f_3A)
#s.Add(h2f_other)
#s.Add(h3f)
#s.Add(h3f_4A)

#s.Add(h3f_other)
#s.Add(h6f)

#s.Draw("hist")
#s.SetMaximum(1)
#s.GetXaxis().SetTitle('m(a) GeV')
#s.GetYaxis().SetTitle('Gen level cat. efficiency')
#s.GetYaxis().SetTitleOffset(1)


gr_15 = TGraph(len(masses),array('d',masses),array('d',c1_3A_15))
gr_15.SetLineColor(kBlue+1)
gr_15.SetLineWidth(2)
gr_15.SetMarkerStyle(24)
               
gr_14 = TGraph(len(masses),array('d',masses),array('d',c1_3A_14))
gr_14.SetLineColor(kAzure+10)
gr_14.SetLineWidth(2)
gr_14.SetMarkerStyle(25)
               
gr_13 = TGraph(len(masses),array('d',masses),array('d',c1_3A_13))
gr_13.SetLineColor(kViolet-4)
gr_13.SetLineWidth(2)
gr_13.SetMarkerStyle(26)
               
gr_12 = TGraph(len(masses),array('d',masses),array('d',c1_3A_12))
gr_12.SetLineColor(kMagenta+3)
gr_12.SetLineWidth(2)
gr_12.SetMarkerStyle(27)
               
gr_11 = TGraph(len(masses),array('d',masses),array('d',c1_3A_11))
gr_11.SetLineColor(kRed)
gr_11.SetLineWidth(2)
gr_11.SetMarkerStyle(28)
               
gr_10 = TGraph(len(masses),array('d',masses),array('d',c1_3A_10))
gr_10.SetLineColor(kBlack)
gr_10.SetLineWidth(2)
gr_10.SetMarkerStyle(29)

mg = TMultiGraph()
mg.SetTitle(" 4 resolved photons -- 3 in acceptance ; m(a) GeV; ");
mg.SetMaximum(1)
mg.SetMinimum(0)
mg.Add(gr_15)
mg.Add(gr_14)
mg.Add(gr_13)
mg.Add(gr_12)
mg.Add(gr_11)
mg.Add(gr_10)
mg.Draw("APL")
               
               

leg = TLegend(0.6, 0.7, 0.89, 0.89)
leg.SetBorderSize(0)
leg.SetHeader("Pt threshold on 3rd and 4th photon")
leg.AddEntry(gr_15,"Pt>15","lp")
leg.AddEntry(gr_14,"Pt>14","lp")
leg.AddEntry(gr_13,"Pt>13","lp")
leg.AddEntry(gr_12,"Pt>12","lp")
leg.AddEntry(gr_11,"Pt>11","lp")
leg.AddEntry(gr_10,"Pt>10","lp")

#leg.AddEntry(h6f,"Others",'f')
#leg.AddEntry(h1f,"4 resolved ",'f')
#leg.AddEntry(h1f_4A_15,"4 resolved : all in acceptance 15 GeV threshold",'f')
#leg.AddEntry(h1f_4A_14,"4 resolved : all in acceptance 14 GeV threshold",'f')
#leg.AddEntry(h1f_4A_13,"4 resolved : all in acceptance 13 GeV threshold",'f')
#leg.AddEntry(h1f_4A_12,"4 resolved : all in acceptance 12 GeV threshold",'f')
#leg.AddEntry(h1f_4A_11,"4 resolved : all in acceptance 11 GeV threshold",'f')
#leg.AddEntry(h1f_4A_10,"4 resolved : all in acceptance 10 GeV threshold",'f')


#leg.AddEntry(h1f_3A,"4 resolved : 3 in acceptance ",'f')
#leg.AddEntry(h1f_other,"4 resolved : Other ",'f')
#leg.AddEntry(h2f,"2 resolved +1 fat",'f')
#leg.AddEntry(h2f_4A,"2 resolved +1 fat : all in acceptance",'f')
#leg.AddEntry(h2f_3A,"2 resolved +1 fat : 3 in acceptance",'f')
#leg.AddEntry(h2f_other,"2 resolved +1 fat : Other",'f')
#leg.AddEntry(h3f,"2 fat",'f')
#leg.AddEntry(h3f_4A,"2 fat : all in acceptance",'f')
#leg.AddEntry(h3f_other,"2 fat : other",'f')
#leg.AddEntry(h1f,"4 Resolved Photons ",'f')
#leg.AddEntry(h3f,"2 Resolved + 1 Fat Photon",'f')
#leg.AddEntry(h5f,"2 Fat Photons",'f')

leg.SetFillStyle(0)
leg.Draw("same")

canvas.Update()
canvas.SaveAs("c2.root")
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/H4G_forPrelim/4resolved/3A_ptthresholdstudy.png")
canvas.SaveAs("/afs/cern.ch/user/t/twamorka/www/H4G_forPrelim/4resolved/3A_ptthresholdstudy.pdf")


#print "check ", c[1]
#print "masses ",masses

#for i, m in enumerate(masses):
#print "mass ",mass
#print item[0] for item in c[1]

#cols = [1, 2, 4, 6, kGreen+3]
#CatNames = ["4 resolved #gamma","3 resolved + 1 missing #gamma","2 resolved + 2 merged #gamma","2 merged + 1 resolved + 1 missing #gamma","2 merged + 2 merged #gamma"]
#c0 = TCanvas('a', 'a', 1000, 600)
#c0.SetLogy()
#c0.SetGrid()
#leg = TLegend(0.72, 0.1012, 0.8992, 0.8985)
#leg.SetHeader("Gen Level Categorization")
#leg.SetBorderSize(0)
    
       
       

#!/usr/bin/python

from ROOT import *
import sys, getopt
from array import array

def main(argv):
   inputfiles = ''
   outputfile = 'output.root'
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["inputFiles=","outputFile="])
   except getopt.GetoptError:
      print 'H4GTreeAnalyzer.py -i <inputfile1,inputfile2,inputfile3...> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile1,inputfile2,inputfile3...> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--inputFiles"):
         inputfiles = arg
      elif opt in ("-o", "--outputFile"):
         outputfile = arg

   listOfFiles = inputfiles.split(",")
   print "Number of input files: ", len(listOfFiles)

   tree = TChain("h4gflash/H4GTree")
   for f in listOfFiles:
      print "\t Adding file:", f
      tree.AddFile(f)
   print "Total number of events to be analyzed:", tree.GetEntries()

   outRoot = TFile(outputfile, "RECREATE")
    
 

  
   h_p1_pt = TH1F("h_p1_pt", "p_{T} of Photons; p_{T}(#gamma) [GeV];Events", 100, 0, 650)
   h_p2_pt = TH1F("h_p2_pt", "p_{T} of 2nd photon; p_{T}(#gamma_{2}) [GeV];Events", 100, 0, 650)
   h_p3_pt = TH1F("h_p3_pt", "p_{T} of 3rd photon; p_{T}(#gamma_{3}) [GeV];Events", 100, 0, 650)
   h_p4_pt = TH1F("h_p4_pt", "p_{T} of Photons; p_{T}(#gamma) [GeV];Events", 100, 0, 650)
   h_mggPP1 = TH1F("h_mggPP1", "a1 and a2 :Mass; M(#gamma#gamma) [GeV];Events", 100, 0, 700)
   h_mggPP2 = TH1F("h_mggPP2", "a1 and a2 :Mass; M(#gamma#gamma) [GeV];Events", 100, 0, 700) 
   h_deltam = TH1F("h_deltam","a1 and a2 mass difference; #Delta m [GeV];Events",100,-300,300)
   h_mggPP1pt = TH1F("h_mggPP1pt","a1 and a2: p_{T};p_{T} [GeV];Events",100,0,650)
   h_mggPP2pt = TH1F("h_mggPP2pt","a1 and a2 : p_{T}; p_{T} [GeV];Events",100,0,650)
   h_mgg12 = TH1F("h_mgg12", "DiPhoton Invariant Mass with 1st and 2nd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg13 = TH1F("h_mgg13", "DiPhoton Invariant Mass with 1rd and 3rd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg14 = TH1F("h_mgg14", "DiPhoton Invariant Mass with 1rd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg23 = TH1F("h_mgg23", "DiPhoton Invariant Mass with 2nd and 3rd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg24 = TH1F("h_mgg24", "DiPhoton Invariant Mass with 2nd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg34 = TH1F("h_mgg34", "DiPhoton Invariant Mass with 3rd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgggg = TH1F("X_mgggg", "TetraPhoton Invariant mass; M(#gamma#gamma#gamma#gamma) [Gev]; Events", 100, 300,1200)
   h_n_pho = TH1F("h_n_pho", "Number of photons; Number of Photons; Events", 10, 0, 10)
   h_n_pho_clean = TH1F("h_n_pho_clean", "Number of photons; Number of Photons; Events", 10, 0, 10)
   h_dr = TH1F("h_dr", "dr values; dr; Events",100,0,150)
   h_dr_12=TH1F("h_dr_12","12 dr values;dr12;Events",100,0,6)
   h_dr_13=TH1F("h_dr_13","13 dr values;dr13;Events",100,0,6)
   h_dr_14=TH1F("h_dr_14","14 dr values;dr14;Events",100,0,6)
   h_dr_23=TH1F("h_dr_23","23 dr values;dr23;Events",100,0,6)
   h_dr_24=TH1F("h_dr_24","24 dr values;dr24;Events",100,0,6)
   h_dr_34=TH1F("h_dr_34","34 dr values;dr34;Events",100,0,6)
   h_dr_1=TH1F("h_dr_1","1 dr values;dr1;Events",100,0,150)
   h_dr_2=TH1F("h_dr_2","2 dr values;dr2;Events",100,0,150)
   h_drPdr1=TH1F("h_dr1","1 dr values;dr1;Events",100,0,150)
   h_drPdr2=TH1F("h_dr2","2 dr values;dr2;Events",100,0,150)
   h_mindr=TH1F("h_mindr","Minimum #Delta r;#Delta r;Events",100,0,3)
   h_mgg12_gen = TH1F("h_mgg12_gen", "DiPhoton Invariant Mass with 1st and 2nd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 700)
   h_mgg13_gen = TH1F("h_mgg13_gen", "DiPhoton Invariant Mass with 1rd and 3rd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 700)
   h_mgg14_gen = TH1F("h_mgg14_gen", "DiPhoton Invariant Mass with 1rd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 700)
   h_mgg23_gen = TH1F("h_mgg23_gen", "DiPhoton Invariant Mass with 2nd and 3rd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 700)
   h_mgg24_gen = TH1F("h_mgg24_gen", "DiPhoton Invariant Mass with 2nd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 700)
   h_mgg34_gen = TH1F("h_mgg34_gen", "DiPhoton Invariant Mass with 3rd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 700)
   h_p1_eta = TH1F("h_p1_eta","#eta of photons; #eta(#gamma);Events",100,-2.7,2.7)
   h_p2_eta = TH1F("h_p2_eta","#eta of 2nd photon; #eta(#gamma_{2}));Events",100,-2.7,2.7)
   h_p3_eta = TH1F("h_p3_eta","#eta of 3rd photon; #eta(#gamma_{3}));Events",100,-2.7,2.7)
   h_p4_eta = TH1F("h_p4_eta","#eta of 4th photon; #eta(#gamma_{4}));Events",100,-2.7,2.7)
   h_gen1_eta = TH1F("h_gen1_eta","gen1 eta;#eta;Events",100,-2.5,2.5)
   h_gen2_eta = TH1F("h_gen2_eta","gen2 eta;#eta;Events",100,-2.5,2.5)
   h_gen3_eta = TH1F("h_gen3_eta","gen3 eta;#eta;Events",100,-2.5,2.5)
   h_gen4_eta = TH1F("h_gen4_eta","gen4 eta;#eta;Events",100,-2.5,2.5)
   h_dr_a1 = TH1F("h_dr_a1","#Delta R1 (for a1); #Deltar a_{1};Events",100,0,6)
   h_dr_a2 = TH1F("h_dr_a2","a1 and a2 : #Delta r ; #Deltar;Events",100,0,6)
   h_dphi_a1 = TH1F("h_dphi_a1","a1 and a2 : #Delta #phi ; #Delta #phi; Events", 100,-4,4)
   h_dphi_a2 = TH1F("h_dphi_a2","Delta phi a2;delta phi; Events",100,-4,4)
   h_deta_a1 = TH1F("h_deta_a1","a1 and a2 : #Delta #eta; #Delta #eta; Events", 100,-4,4)
   h_deta_a2 = TH1F("h_deta_a2","Delta eta a2;delta eta; Events",100,-4,4)
   h_mggPP1pz = TH1F("h_mggPP1pz","pz a1;pz a1;Events",100,-900,900)
   h_mggPP2pz = TH1F("h_mggPP2pz","a1 and a2 : p_{z}; p_{z} [GeV];Events",100,-900,900)
   h_gen1_pt = TH1F("h_gen1_pt","gen1 p_{t}; p_{t};Events",100,0,650)
   h_gen2_pt = TH1F("h_gen2_pt","gen2 p_{t}; p_{t};Events",100,0,650)
   h_gen3_pt = TH1F("h_gen3_pt","gen3 p_{t}; p_{t};Events",100,0,650)
   h_gen4_pt = TH1F("h_gen4_pt","gen4 p_{t}; p_{t};Events",100,0,650)
   h_gen1_phi = TH1F("h_gen1_phi","gen1 phi;gen1 phi;events",100,-4,4)
   
   

   triggers = {}
   triggerNames = []
   fraction = []
   
   ptCounter = 0
   evtCounter = 0
   
   #Tree Loop:
   for evt in range(0, tree.GetEntries()):
      if evt%1000 == 0: print "## Analyzing event ", evt
      tree.GetEntry(evt)

      Phos = []

      for p in range(0, tree.n_pho):
#        print "photon #", p, " pt:",tree.v_pho_pt[p]
        p4 = TLorentzVector(0,0,0,0)
        p4.SetPtEtaPhiE( tree.v_pho_pt[p], tree.v_pho_eta[p], tree.v_pho_phi[p], tree.v_pho_e[p])
        minDR = 999
        for Pho in Phos:
           dr = Pho.DeltaR(p4)
           if dr < minDR:
              minDR = dr
        if minDR > 0.01:
           Phos.append(p4)
           

#      print "Number of photons:", tree.n_pho
      if len(Phos) < 4:
         continue
#      if tree.passTrigger == 0:
#         continue

      gen1 = TLorentzVector(0,0,0,0)
      gen2 = TLorentzVector(0,0,0,0)
      gen3 = TLorentzVector(0,0,0,0)
      gen4 = TLorentzVector(0,0,0,0)
      if tree.v_genpho_p4.size() > 0:
         gen1.SetPtEtaPhiE(tree.v_genpho_p4[0].pt(), tree.v_genpho_p4[0].eta(), tree.v_genpho_p4[0].phi(), tree.v_genpho_p4[0].e())
      if tree.v_genpho_p4.size() > 1:
         gen2.SetPtEtaPhiE(tree.v_genpho_p4[1].pt(), tree.v_genpho_p4[1].eta(), tree.v_genpho_p4[1].phi(), tree.v_genpho_p4[1].e())
      if tree.v_genpho_p4.size() > 2:
         gen3.SetPtEtaPhiE(tree.v_genpho_p4[2].pt(), tree.v_genpho_p4[2].eta(), tree.v_genpho_p4[2].phi(), tree.v_genpho_p4[2].e())
      if tree.v_genpho_p4.size() > 3:
         gen4.SetPtEtaPhiE(tree.v_genpho_p4[3].pt(), tree.v_genpho_p4[3].eta(), tree.v_genpho_p4[3].phi(), tree.v_genpho_p4[3].e())
 
         
            
      
      if gen4.Pt() == 0: 
         print "The number of times pt is zero for gen photon 4 is %d" %ptCounter
         ptCounter +=1

      h_gen1_pt.Fill(gen1.Pt())
      h_gen2_pt.Fill(gen2.Pt())
      h_gen3_pt.Fill(gen3.Pt())
      h_gen4_pt.Fill(gen4.Pt())
      #h_gen1_eta.Fill(gen1.Eta())
      #h_gen2_eta.Fill(gen2.Eta())
      #h_gen3_eta.Fill(gen3.Eta())
      #h_gen4_eta.Fill(gen4.Eta())
      h_gen1_phi.Fill(gen1.Phi())
      gen12 = gen1+gen2
      gen13 = gen1+gen3
      gen14 = gen1+gen4
      gen23 = gen2+gen3
      gen24 = gen2+gen4
      gen34 = gen3+gen4
      h_mgg12_gen.Fill(gen12.M())
      h_mgg13_gen.Fill(gen13.M())
      h_mgg14_gen.Fill(gen14.M())
      h_mgg23_gen.Fill(gen23.M())
      h_mgg24_gen.Fill(gen24.M())
      h_mgg34_gen.Fill(gen34.M())
      
      
      

      #true1 = []
      #true2 = []
      #counter = 0
      #if gen12.M() > 59.9 and gen12.M() <60.1
        # true.append(counter)
         #counter =+1
      
     

      h_n_pho.Fill(tree.n_pho)
      h_n_pho_clean.Fill(len(Phos))

      P1 = Phos[0]
      P2 = Phos[1]
      P3 = Phos[2]
      P4 = Phos[3]

      h_p1_pt.Fill(P1.Pt())
      h_p2_pt.Fill(P2.Pt())
      h_p3_pt.Fill(P3.Pt())
      h_p4_pt.Fill(P4.Pt())
      h_dr.Fill(dr)

      h_p1_eta.Fill(P1.Eta())
      h_p2_eta.Fill(P2.Eta())
      h_p3_eta.Fill(P3.Eta())
      h_p4_eta.Fill(P4.Eta())

      P12 = P1 + P2
      h_mgg12.Fill(P12.M())
      h_dr_12.Fill(P1.DeltaR(P2))
      P13 = P1 + P3
      h_dr_13.Fill(P1.DeltaR(P3))
      h_mgg13.Fill(P13.M())
      P14 = P1 + P4
      h_mgg14.Fill(P14.M())
      h_dr_14.Fill(P1.DeltaR(P4))
      P23 = P2 + P3
      h_mgg23.Fill(P23.M())
      h_dr_23.Fill(P2.DeltaR(P3))
      P24 = P2 + P4
      h_mgg24.Fill(P24.M())
      h_dr_24.Fill(P2.DeltaR(P4))
      P34 = P3 + P4
      h_mgg34.Fill(P34.M())
      h_dr_34.Fill(P3.DeltaR(P4))

      diff_12_34 = abs(P12.M() - P34.M())
      diff_13_24 = abs(P13.M() - P24.M())
      diff_14_23 = abs(P14.M() - P23.M())
      
      PP1 = ""
      PP2 = ""
      if diff_12_34 < diff_13_24 and diff_12_34 < diff_14_23:
         PP1 = P12
         PP2 = P34
         h_dr_a1.Fill(P1.DeltaR(P2))
         h_dr_a2.Fill(P3.DeltaR(P4))
         h_dphi_a1.Fill(P1.DeltaPhi(P2))
         h_dphi_a2.Fill(P3.DeltaPhi(P4))
         h_deta_a1.Fill(P1.Eta()-P2.Eta())
         h_deta_a2.Fill(P3.Eta()-P4.Eta())
        
      if diff_13_24 < diff_12_34 and diff_13_24 < diff_14_23:
         PP1 = P13
         PP2 = P24
         h_dr_a1.Fill(P1.DeltaR(P3))
         h_dr_a2.Fill(P2.DeltaR(P4))
         h_dphi_a1.Fill(P1.DeltaPhi(P3))
         h_dphi_a2.Fill(P2.DeltaPhi(P4))
         h_deta_a1.Fill(P1.Eta()-P3.Eta())
         h_deta_a2.Fill(P2.Eta()-P4.Eta()) 

      if diff_14_23 < diff_12_34 and diff_14_23 < diff_13_24:
         PP1 = P14
         PP2 = P23
         h_dr_a1.Fill(P1.DeltaR(P4))
         h_dr_a2.Fill(P2.DeltaR(P3))
         h_dphi_a1.Fill(P1.DeltaPhi(P4))
         h_dphi_a2.Fill(P2.DeltaPhi(P3))
         h_deta_a1.Fill(P1.Eta()-P4.Eta())
         h_deta_a2.Fill(P2.Eta()-P3.Eta())

      #mindr = min(P1.DeltaR(P2), P1.DeltaR(P3), P1.DeltaR(P4), P2.DeltaR(P3), P2.DeltaR(P4), P3.DeltaR(P4))
      h_mindr.Fill(min(P1.DeltaR(P2), P1.DeltaR(P3), P1.DeltaR(P4), P2.DeltaR(P3), P2.DeltaR(P4), P3.DeltaR(P4)))

       
      #if P1.deltaR(P2) < 
      diff_dr_12_34 = abs(P1.DeltaR(P2) - P3.DeltaR(P4))
      diff_dr_13_24 = abs(P1.DeltaR(P3) - P2.DeltaR(P4))
      diff_dr_14_23 = abs(P1.DeltaR(P4) - P2.DeltaR(P3))

      Pdr1 = ""
      Pdr2 = ""
      if diff_dr_12_34 < diff_dr_13_24 and diff_dr_12_34 < diff_dr_14_23:
         Pdr1 = P12
         Pdr2 = P34
         
      if diff_dr_13_24 < diff_dr_12_34 and diff_dr_13_24 < diff_dr_14_23:
         Pdr1 = P13
         Pdr2 = P24
      if diff_dr_14_23 < diff_dr_12_34 and diff_dr_14_23 < diff_dr_13_24:
         Pdr1 = P14
         Pdr2 = P23
      
      

      h_mggPP1.Fill(PP1.M())
      h_mggPP2.Fill(PP2.M())
      h_deltam.Fill(PP1.M()-PP2.M())
      h_mggPP1pt.Fill(PP1.Pt())
      h_mggPP2pt.Fill(PP2.Pt())
      h_mggPP1pz.Fill(PP1.Pz())
      h_mggPP2pz.Fill(PP2.Pz())
    
      #h_drPdr1.Fill(Pdr1.DeltaR())
      #h_drPdr2.Fill(Pdr2.DeltaR())

      Pgggg = P1 + P2 + P3 + P4
      h_mgggg.Fill(Pgggg.M())

      for mt in tree.myTriggerResults:
#         print mt.first, mt.second
         if mt.first in triggers:
            triggers[mt.first] += mt.second
         if mt.first not in triggers:
            triggers[mt.first] = mt.second
      evtCounter += 1

   x = []
   xNames = []
   y = []
   counter = 0
   for tr in triggers:
      x.append(counter)
      y.append(float(triggers[tr])/float(evtCounter))
      xNames.append(tr)
      counter +=1

   X = array("d", x)
   Y = array("d", y)
   gr = TGraph(len(x), X, Y)
   
   grX = gr.GetXaxis()
   print len(xNames), grX.GetNbins()
   for i in x:
      grX.SetBinLabel(grX.FindBin(i), xNames[i])

   outRoot.cd()
   h_p1_pt.Write()
   h_p2_pt.Write()
   h_p3_pt.Write()
   h_p4_pt.Write()
   h_mgg12.Write()
   h_mgg13.Write()
   h_mgg14.Write()
   h_mgg23.Write()
   h_mgg24.Write()
   h_mgg34.Write()
   h_mgggg.Write()
   h_n_pho.Write()
   h_mggPP1.Write()
   h_mggPP2.Write()
   h_dr.Write()
   h_dr_1.Write()
   h_dr_2.Write()
   h_drPdr1.Write()
   h_drPdr2.Write()
   h_dr_12.Write()
   h_dr_13.Write()
   h_dr_14.Write()
   h_dr_23.Write()
   h_dr_24.Write()
   h_dr_34.Write()
   h_n_pho_clean.Write()

   h_mindr.Write()
   gr.Write()
   h_mgg12_gen.Write()
   h_mgg13_gen.Write()
   h_mgg14_gen.Write()
   h_mgg23_gen.Write()
   h_mgg24_gen.Write()
   h_mgg34_gen.Write()
   h_mggPP2pt.Write()
   h_mggPP1pt.Write()
   h_mggPP1pz.Write()
   h_mggPP2pz.Write()
   h_p1_eta.Write()
   h_p2_eta.Write()
   h_p3_eta.Write()
   h_p4_eta.Write()
   h_deltam.Write()
   h_dr_a1.Write()
   h_dr_a2.Write()
   h_dphi_a1.Write()
   h_dphi_a2.Write()
   h_deta_a1.Write()
   h_deta_a2.Write()
   #h_gen1_eta.Write()
   #h_gen2_eta.Write()
   #h_gen3_eta.Write()
   h_gen4_eta.Write()
   h_gen1_phi.Write()
   h_gen1_pt.Write()
   h_gen2_pt.Write()
   h_gen3_pt.Write()
   h_gen4_pt.Write()
   
   gStyle.SetOptStat(0)
   c0 = TCanvas("c", "c", 800, 600)
   h_mggPP2.SetLineColor(4)
   h_mggPP2.SetLineWidth(2)
   h_mggPP2.GetYaxis().SetTitleOffset(1.5)
   h_mggPP2.Draw()
   h_mggPP1.SetLineColor(8)
   h_mggPP1.SetLineWidth(2)
   h_mggPP1.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_mggPP2,"a2 mass","lp")
   legend.AddEntry(h_mggPP1,"a1 mass","lp")
   legend.Draw()
   
   c0.SaveAs("a1a2mass750.pdf")
  
   gStyle.SetOptStat(0)
   c1 = TCanvas("c", "c", 800, 600)
   h_mggPP1pt.SetLineColor(4)
   h_mggPP1pt.SetLineWidth(2)
   h_mggPP1pt.GetYaxis().SetTitleOffset(1.5)
   h_mggPP1pt.Draw()
   h_mggPP2pt.SetLineColor(8)
   h_mggPP2pt.SetLineWidth(2)
   h_mggPP2pt.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_mggPP1pt,"a1 p_{T}","lp")
   legend.AddEntry(h_mggPP2pt,"a2 p_{T}","lp")
   legend.Draw()
   
   c1.SaveAs("a1a2pt750.pdf")

   gStyle.SetOptStat(0)
   c2 = TCanvas("c", "c", 800, 600)
   h_dr_a2.SetLineColor(4)
   h_dr_a2.SetLineWidth(2)
   h_dr_a2.GetYaxis().SetTitleOffset(1.5)
   h_dr_a2.Draw()
   h_dr_a1.SetLineColor(8)
   h_dr_a1.SetLineWidth(2)
   h_dr_a1.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_dr_a2,"a2 #Delta r","lp")
   legend.AddEntry(h_dr_a1,"a1 #Delta r","lp")
   legend.Draw()
   
   c2.SaveAs("a1a2dr750.pdf")
   
   gStyle.SetOptStat(0)
   c3 = TCanvas("c", "c", 800, 600)
   h_p1_eta.SetLineColor(4)
   h_p1_eta.GetYaxis().SetTitleOffset(1.5)
   h_p1_eta.SetLineWidth(2)
   h_p1_eta.Draw()
   h_p2_eta.SetLineColor(8)
   h_p2_eta.SetLineWidth(2)
   h_p2_eta.Draw("same")
   h_p3_eta.SetLineColor(6)
   h_p3_eta.SetLineWidth(2)
   h_p3_eta.Draw("same")
   h_p4_eta.SetLineColor(1)
   h_p4_eta.SetLineWidth(2)
   h_p4_eta.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_p1_eta,"#gamma 1","lp")
   legend.AddEntry(h_p2_eta,"#gamma 2","lp")
   legend.AddEntry(h_p3_eta,"#gamma 3","lp")
   legend.AddEntry(h_p4_eta,"#gamma 4","lp")
   legend.Draw()
   
   c3.SaveAs("combinedeta750.pdf")

   
   gStyle.SetOptStat(0)
   c4 = TCanvas("c", "c", 800, 600)
   h_p4_pt.SetLineColor(4)
   h_p4_pt.GetYaxis().SetTitleOffset(1.5)
   h_p4_pt.SetLineWidth(2)
   h_p4_pt.Draw()
   h_p3_pt.SetLineColor(8)
   h_p3_pt.SetLineWidth(2)
   h_p3_pt.Draw("same")
   h_p2_pt.SetLineColor(6)
   h_p2_pt.SetLineWidth(2)
   h_p2_pt.Draw("same")
   h_p1_pt.SetLineColor(1)
   h_p1_pt.SetLineWidth(2)
   h_p1_pt.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_p4_pt,"#gamma 4","lp")
   legend.AddEntry(h_p3_pt,"#gamma 3","lp")
   legend.AddEntry(h_p2_pt,"#gamma 2","lp")
   legend.AddEntry(h_p1_pt,"#gamma 1","lp")
   legend.Draw()
   
   c4.SaveAs("combinedpt750.pdf")
   

   gStyle.SetOptStat(0)
   c5 = TCanvas("c", "c", 800, 600)
   h_dphi_a1.SetLineColor(4)
   h_dphi_a1.GetYaxis().SetTitleOffset(1.5)
   h_dphi_a1.SetLineWidth(2)
   h_dphi_a1.Draw()
   h_dphi_a2.SetLineColor(8)
   h_dphi_a2.SetLineWidth(2)
   h_dphi_a2.Draw("same")
   
   legend = TLegend(0.85,0.8,0.7,0.9)
   legend.AddEntry(h_dphi_a1,"a1 #Delta #phi","lp")
   legend.AddEntry(h_dphi_a2,"a2 #Delta #phi","lp")
   legend.Draw()
   
   c5.SaveAs("deltaphi750.pdf")
   
   gStyle.SetOptStat()
   c6 = TCanvas("c", "c", 800, 600)
   h_mgggg.SetLineColor(4)
   h_mgggg.GetYaxis().SetTitleOffset(1.5)
   h_mgggg.SetLineWidth(2)
   h_mgggg.Draw()
  
   
   c6.SaveAs("newhiggsmass750.pdf")
   
   gStyle.SetOptStat()
   c7 = TCanvas("c", "c", 800, 600)
   h_deltam.SetLineColor(4)
   h_deltam.GetYaxis().SetTitleOffset(1.5)
   h_deltam.SetLineWidth(2)
   h_deltam.Draw()
  
   
   c7.SaveAs("a1a2massdiff750.pdf")

   gStyle.SetOptStat()
   c8 = TCanvas("c", "c", 800, 600)
   h_mindr.SetLineColor(4)
   h_mindr.GetYaxis().SetTitleOffset(1.5)
   h_mindr.SetLineWidth(2)
   h_mindr.Draw()
  
   
   c8.SaveAs("newmindr750.pdf")

   gStyle.SetOptStat(0)
   c9 = TCanvas("c", "c", 800, 600)
   h_deta_a1.SetLineColor(4)
   h_deta_a1.GetYaxis().SetTitleOffset(1.5)
   h_deta_a1.SetLineWidth(2)
   h_deta_a1.Draw()
   h_deta_a2.SetLineColor(8)
   h_deta_a1.SetLineWidth(2)
   h_deta_a2.Draw("same")

   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_deta_a1,"a1 #Delta #eta","lp")
   legend.AddEntry(h_deta_a2,"a2 #Delta #eta","lp")
   legend.Draw()
   
   c9.SaveAs("deltaeta750.pdf")
   
   
    
   gStyle.SetOptStat(0)
   c10 = TCanvas("c", "c", 800, 600)
   h_mggPP2pz.SetLineColor(4)
   h_mggPP2pz.GetYaxis().SetTitleOffset(1.5)
   h_mggPP2pz.SetLineWidth(2)
   h_mggPP2pz.Draw()
   h_mggPP1pz.SetLineColor(8)
   h_mggPP1pz.SetLineWidth(2)
   h_mggPP1pz.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_mggPP2pz,"a2 p_{z}","lp")
   legend.AddEntry(h_mggPP1pz,"a1 p_{z}","lp")
   legend.Draw()

   c10.SaveAs("a1a2pz.pdf")   

   gStyle.SetOptStat(0)
   c11 = TCanvas("c", "c", 800, 600)
   h_gen1_pt.SetLineColor(4)
   h_gen1_pt.GetYaxis().SetTitleOffset(1.5)
   h_gen1_pt.SetLineWidth(2)
   h_gen1_pt.Draw()
   h_gen2_pt.SetLineColor(8)
   h_gen2_pt.SetLineWidth(2)
   h_gen2_pt.Draw("same")
   h_gen3_pt.SetLineColor(6)
   h_gen3_pt.SetLineWidth(2)
   h_gen3_pt.Draw("same")
   h_gen4_pt.SetLineColor(1)
   h_gen4_pt.SetLineWidth(2)
   h_gen4_pt.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_gen1_pt,"gen#gamma 4","lp")
   legend.AddEntry(h_gen2_pt,"gen#gamma 3","lp")
   legend.AddEntry(h_gen3_pt,"gen#gamma 2","lp")
   legend.AddEntry(h_gen4_pt,"gen#gamma 1","lp")
   legend.Draw()
   
   c11.SaveAs("combinedgenpt.png")

   gStyle.SetOptStat(0)
   c12 = TCanvas("c", "c", 800, 600)
   h_gen1_eta.SetLineColor(4)
   h_gen1_eta.GetYaxis().SetTitleOffset(1.5)
   h_gen1_eta.SetLineWidth(2)
   h_gen1_eta.Draw()
   h_gen2_eta.SetLineColor(8)
   h_gen2_eta.SetLineWidth(2)
   h_gen2_eta.Draw("same")
   h_gen3_eta.SetLineColor(6)
   h_gen3_eta.SetLineWidth(2)
   h_gen3_eta.Draw("same")
   h_gen4_eta.SetLineColor(1)
   h_gen4_eta.SetLineWidth(2)
   h_gen4_eta.Draw("same")
   
   legend = TLegend(0.75,0.8,0.9,0.9)
   legend.AddEntry(h_gen1_eta,"#gamma 1","lp")
   legend.AddEntry(h_gen2_eta,"#gamma 2","lp")
   legend.AddEntry(h_gen3_eta,"#gamma 3","lp")
   legend.AddEntry(h_gen4_eta,"#gamma 4","lp")
   legend.Draw()
   
   c12.SaveAs("gencombinedeta.png")
   
   
   
   

   outRoot.Close()
  # .! rootls -1 myfirstfile.root
	

if __name__ == "__main__":
   main(sys.argv[1:])


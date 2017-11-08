#!/usr/bin/python

from ROOT import *
import sys, getopt
from array import array

def main(argv):
   inputfiles = '/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/test/test.root'
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



   h_gen_mggPP1=TH1F("h_gen_mggPP1", "a1 and a2 :Mass; M(#gamma#gamma) [GeV];Events", 100, 0, 120)
   h_gen_mggPP2=TH1F("h_gen_mggPP2", " gen a1 and a2 :Mass; M(#gamma#gamma) [GeV];Events", 100, 0, 120)
   h_gen_deltam = TH1F("h_gen_deltam","gen a1 and a2 mass difference; #Delta m [GeV];Events",100,-80,80)
   h_gen_mggPP1pt = TH1F("h_gen_mggPP1pt"," gen a1 and a2 :p_{T};p_{T} [GeV];Events",100,0,160)
   h_gen_mggPP2pt = TH1F("h_gen_mggPP2pt"," gen a1 and a2 :p_{T};p_{T} [GeV];Events",100,0,160)
   h_gen_mggPP1pz = TH1F("h_gen_mggPP1pz","a1 pz; p_{z} [GeV];Events",100,-150,150)
   h_gen_mggPP2pz = TH1F("h_gen_mggPP2pz","gen a1 and a2: p_{z}; p_{z} [GeV];Events",100,-150,150)
   h_gen_mgggg = TH1F("h_gen_mgggg", "gen TetraPhoton Invariant mass; M(#gamma#gamma#gamma#gamma) [Gev]; Events", 100, 60,200)
   h_gen_dr_a1=TH1F("h_gen_dr_a1","gena1dr; gena1 dr;Events",100,0,5)
   h_gen_dr_a2=TH1F("h_gen_dr_a2","gen a1 and a2 : #Delta r; #Delta r;Events",100,0,5)
   h_gen_mindr=TH1F("h_gen_mindr","Gen Minimum #Delta r;#Delta r;Events",100,0,3)
   h_mgg12_gen = TH1F("h_mgg12_gen", "DiPhoton Invariant Mass with 1st and 2nd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg13_gen = TH1F("h_mgg13_gen", "DiPhoton Invariant Mass with 1rd and 3rd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg14_gen = TH1F("h_mgg14_gen", "DiPhoton Invariant Mass with 1rd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg23_gen = TH1F("h_mgg23_gen", "DiPhoton Invariant Mass with 2nd and 3rd photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg24_gen = TH1F("h_mgg24_gen", "DiPhoton Invariant Mass with 2nd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_mgg34_gen = TH1F("h_mgg34_gen", "DiPhoton Invariant Mass with 3rd and 4th photons; M(#gamma#gamma) [GeV];Events", 100, 0, 160)
   h_gen1_eta = TH1F("h_gen1_eta","gen1 eta;#eta;Events",100,-2.5,2.5)
   h_gen2_eta = TH1F("h_gen2_eta","gen2 eta;#eta;Events",100,-2.5,2.5)
   h_gen3_eta = TH1F("h_gen3_eta","gen3 eta;#eta;Events",100,-2.5,2.5)
   h_gen4_eta = TH1F("h_gen4_eta","#eta of Gen photons;#eta(#gamma);Events",100,-2.5,2.5)
   h_gen1_phi = TH1F("h_gen1_phi","gen #gamma phi;""#phi;Events",100,-4,4)
   h_gen2_phi = TH1F("h_gen2_phi","gen #gamma phi;""#phi;Events",100,-4,4)
   h_gen3_phi = TH1F("h_gen3_phi","gen #gamma phi;""#phi;Events",100,-4,4)
   h_gen4_phi = TH1F("h_gen4_phi","#phi of Gen photons;#phi(#gamma);Events",100,-4,4)
   h_gen_dphi_a1 = TH1F("h_gen_dphi_a1","gen a1 and a2 : #Delta #phi ; #Delta #phi; Events", 100,-4,4)
   h_gen_dphi_a2 = TH1F("h_gen_dphi_a2","gen a1 and a2 :#Delta #phi;#Delta #phi; Events",100,-4,4)
   h_gen_deta_a1 = TH1F("h_gen_deta_a1","gen a1 and a2 : #Delta #eta; #Delta #eta; Events", 100,-4,4)
   h_gen_deta_a2 = TH1F("h_gen_deta_a2","gen a1 and a2 :#Delta #eta;#Delta #eta; Events",100,-4,4)
   h_gen1_pt = TH1F("h_gen1_pt","gen1 p_{t}; p_{t};Events",100,0,150)
   h_gen2_pt = TH1F("h_gen2_pt","gen2 p_{t}; p_{t};Events",100,0,150)
   h_gen3_pt = TH1F("h_gen3_pt","gen3 p_{t}; p_{t};Events",100,0,150)
   h_gen4_pt = TH1F("h_gen4_pt","p_{t} of Gen photons; p_{t} (#gamma) [GeV];Events",200,0,40)
   h_2d = TH2F("h_2d","h_2d",100,0,150,100,0,150)
   h_len_genphos = TH1F("h_len_genphos","Number of gen phos; # of gen photons;Events",100,0,7)
   triggers = {}
   triggerNames = []
   fraction = []
 
   evtCounter = 0
   #Tree Loop:
   for evt in range(0, tree.GetEntries()):
      if evt%1000 == 0: print "## Analyzing event ", evt
      tree.GetEntry(evt)


      ## loop over GEN photons
      Genphos = []
      number = 0
      for g in range(0,tree.v_genpho_p4.size()):
         #print evt, " photon #", g, " pt: ", tree.v_genpho_p4[g].pt()
         P4 = TLorentzVector(0,0,0,0)
         P4.SetPtEtaPhiE( tree.v_genpho_p4[g].pt(), tree.v_genpho_p4[g].eta(), tree.v_genpho_p4[g].phi(), tree.v_genpho_p4[g].e())
         Genphos.append(P4)
         minDR = 999
         #         number = number+1

         ## check for overlaps
         for genPho in Genphos:
             #Genphos.append(P4)
            dr = genPho.DeltaR(P4)
            if dr < minDR:
               minDR = dr
               #print "dr",dr
               
         ## if no overlaps, add photon to Genphos
         #if minDR > 0.0:
            #Genphos.append(P4)
           # print "number of elements ", len(Genphos)
           # print "max pt : ", max(Genphos[0].pt())
            #number = number+1
            #print evt, " photon #", g, " pt: ", tree.v_genpho_p4[g].pt()
           # sorted(Genphos)   
           # print " ", len(Genphos)
           # print "number", number
      
     
      #print "genphotonpt: ",Genphos[0]
      #def getKey(item)
      #   return item[0]
      #sorted(Genphos, key=getKey)

      ## now sort Genphos by pT
      Genphos.sort(key=lambda x: x.Pt(), reverse=True)
      #      for x in Genphos :
      #         print evt, "Genphos  pt: ", x.Pt() 

      ## add histogrm of len(Genphos)

      print evt, "  #GENphos", len(Genphos)
      h_len_genphos.Fill(len(Genphos))
      if len(Genphos) < 4:
         continue     
     	
      gen1 = TLorentzVector(0,0,0,0)
      gen2 = TLorentzVector(0,0,0,0)
      gen3 = TLorentzVector(0,0,0,0)
      gen4 = TLorentzVector(0,0,0,0)
      
      #print evt ," the number of gen photons ", len(Genphos) 
      # print evt, "max: " , max(Genphos.pt())
      # print "hello ", tree.v_genpho_p4.size(), " ", evt
      if len(Genphos) > 0:
         gen1 = Genphos[0]
      if len(Genphos) > 1:
         gen2 = Genphos[1]
      if len(Genphos) > 2:
         gen3 = Genphos[2]
      if len(Genphos) > 3:
         gen4 = Genphos[3]
         
      #print "gen photon pt ", gen1.Pt(), " ", gen2.Pt(), " ", gen3.Pt(), " ", gen4.Pt()
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
         
      diffgen_12_34 = abs(gen12.M() - gen34.M())
      diffgen_13_24 = abs(gen13.M() - gen24.M())
      diffgen_14_23 = abs(gen14.M() - gen23.M())
      
      genPP1 = ""
      genPP2 = ""
      
      
      if diffgen_12_34 < diffgen_13_24 and diffgen_12_34 < diffgen_14_23:
         genPP1 = gen12
         genPP2 = gen34
         h_gen_dr_a1.Fill(gen1.DeltaR(gen2))
         h_gen_dr_a2.Fill(gen3.DeltaR(gen4))
         h_gen_dphi_a1.Fill(gen1.DeltaPhi(gen2))
         h_gen_dphi_a2.Fill(gen3.DeltaPhi(gen4))
         h_gen_deta_a1.Fill(gen1.Eta()-gen2.Eta())
         h_gen_deta_a2.Fill(gen3.Eta()-gen4.Eta())
         
      if diffgen_13_24 < diffgen_12_34 and diffgen_13_24 < diffgen_14_23:
         genPP1 = gen13
         genPP2 = gen24
         h_gen_dr_a1.Fill(gen1.DeltaR(gen3))
         h_gen_dr_a2.Fill(gen2.DeltaR(gen4))
         h_gen_dphi_a1.Fill(gen1.DeltaPhi(gen3))
         h_gen_dphi_a2.Fill(gen2.DeltaPhi(gen4))
         h_gen_deta_a1.Fill(gen1.Eta()-gen3.Eta())
         h_gen_deta_a2.Fill(gen2.Eta()-gen4.Eta()) 
         
      if diffgen_14_23 < diffgen_12_34 and diffgen_14_23 < diffgen_13_24:
         genPP1 = gen14
         genPP2 = gen23
         h_gen_dr_a1.Fill(gen1.DeltaR(gen4))
         h_gen_dr_a2.Fill(gen2.DeltaR(gen3))
         h_gen_dphi_a1.Fill(gen1.DeltaPhi(gen4))
         h_gen_dphi_a2.Fill(gen2.DeltaPhi(gen3))
         h_gen_deta_a1.Fill(gen1.Eta()-gen4.Eta())
         h_gen_deta_a2.Fill(gen2.Eta()-gen3.Eta())
         
                  #         print "hello "
      #if genPP1 == "":
       #  print "BLAH genPP1 is not assigned! ", diffgen_12_34, " ", diffgen_13_24, " ", diffgen_14_23, " ", tree.v_genpho_p4.size(), " ", evt
        # if genPP2 == "":
         #   print "BLAH genPP2 is not assigned! ", diffgen_12_34, " ", diffgen_13_24, " ", diffgen_14_23, " ", tree.v_genpho_p4.size(), " ", evt
               
                        
      h_gen_mindr.Fill(min(gen1.DeltaR(gen2), gen1.DeltaR(gen3), gen1.DeltaR(gen4), gen2.DeltaR(gen3), gen2.DeltaR(gen4), gen3.DeltaR(gen4)))
      h_gen_mggPP1.Fill(genPP1.M())
      h_gen_mggPP2.Fill(genPP2.M())
      h_gen_deltam.Fill(genPP1.M()-genPP2.M())
      h_gen_mggPP1pt.Fill(genPP1.Pt())
      h_gen_mggPP2pt.Fill(genPP2.Pt())
      h_gen_mggPP1pz.Fill(genPP1.Pz())
      h_gen_mggPP2pz.Fill(genPP2.Pz())

      genPgggg = gen1 + gen2 + gen3 + gen4
      h_gen_mgggg.Fill(genPgggg.M())
      
      
      h_gen1_pt.Fill(gen1.Pt())
      h_gen2_pt.Fill(gen2.Pt())
      h_gen3_pt.Fill(gen3.Pt())
      h_gen4_pt.Fill(gen4.Pt())
      h_gen1_eta.Fill(gen1.Eta())
      h_gen2_eta.Fill(gen2.Eta())
      h_gen3_eta.Fill(gen3.Eta())
      h_gen4_eta.Fill(gen4.Eta())
      h_gen1_phi.Fill(gen1.Phi())
      h_gen2_phi.Fill(gen2.Phi())
      h_gen3_phi.Fill(gen3.Phi())
      h_gen4_phi.Fill(gen4.Phi())
      h_2d.Fill(gen1.Pt(),gen1.DeltaR(gen4))
     
      for mt in tree.myTriggerResults:
#         print mt.first, mt.second
         if mt.first in triggers:
            triggers[mt.first] += mt.second
         if mt.first not in triggers:
            triggers[mt.first] = mt.second
      evtCounter += 1  # print "number", number
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

   #outTree.Fill()
   outRoot.cd()
   h_gen_mggPP1.Write()
   h_gen_mggPP2.Write()
   h_gen_deltam.Write()
   gr.Write()
   h_mgg24_gen.Write()
   h_mgg13_gen.Write()
   h_mgg14_gen.Write()
   h_mgg23_gen.Write()
   h_mgg12_gen.Write()
   h_mgg34_gen.Write()
   h_gen_mggPP2pt.Write()
   h_gen_mggPP1pt.Write()
   h_gen_mggPP1pz.Write()
   h_gen_mggPP2pz.Write()
   h_gen1_eta.Write()
   h_gen2_eta.Write()
   h_gen3_eta.Write()
   h_gen4_eta.Write()
   h_gen1_pt.Write()
   h_gen2_pt.Write()
   h_gen3_pt.Write()
   h_gen4_pt.Write()
   h_gen_dphi_a1.Write()
   h_gen_dphi_a2.Write()
   h_gen_deta_a1.Write()
   h_gen_deta_a2.Write()
   h_gen_dr_a1.Write()
   h_gen_dr_a2.Write()
   h_gen1_phi.Write()
   h_gen2_phi.Write()
   h_gen3_phi.Write()
   h_gen4_phi.Write()
   h_gen_mindr.Write()
   h_gen_mgggg.Write()
   h_2d.Write()
   h_len_genphos.Write()

   outRoot.Close()
  # .! rootls -1 myfirstfile.root


if __name__ == "__main__":
   main(sys.argv[1:])



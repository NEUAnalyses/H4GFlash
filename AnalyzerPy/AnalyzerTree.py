#!/usr/bin/python
import numpy as n
from ROOT import *
import sys, getopt
from array import array

from analyzertools import *

def main(argv):
   #inputfiles = '/eos/cms/store/user/torimoto/physics/4gamma/2018/Signal/sig50.root'
   inputfiles = '/eos/user/t/twamorka/FatPho0p1_Match0p15/sig1.root'
   outputfile = 'test.root'
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

   Genmaker = GenTools()
   outTree = Genmaker.MakeGenTree()
   outTree_case1 = Genmaker.MakeGenTree_case1()
   outTree_case2 = Genmaker.MakeGenTree_case2()
   outTree_case3 = Genmaker.MakeGenTree_case3()

   triggers = {}
   triggerNames = []
   fraction = []



   evtCounter = 0
   Genmaker.totevs[0] = tree.GetEntries()
   #Tree Loop:
   for evt in range(0, tree.GetEntries()):
      if evt%1000 == 0: print "## Analyzing event ", evt
      tree.GetEntry(evt)
      Genphos = []
      number = 0
      for g in range(0,tree.v_photonDaughters_p4.size()):       ## loop over GEN photons
         P4 = TLorentzVector(0,0,0,0)
         P4.SetPtEtaPhiE( tree.v_photonDaughters_p4[g].pt(), tree.v_photonDaughters_p4[g].eta(), tree.v_photonDaughters_p4[g].phi(), tree.v_photonDaughters_p4[g].e())
         
         Genphos.append(P4)
         minDR = 999
      
      Photon1 = TLorentzVector(0,0,0,0)
      Photon2 = TLorentzVector(0,0,0,0)
      Photon3 = TLorentzVector(0,0,0,0)
      Photon4 = TLorentzVector(0,0,0,0)
      
      Photon1 = Genphos[0] # photons 1,2 come from a1; 3,4 come from a2
      Photon2 = Genphos[1]
      Photon3 = Genphos[2]
      Photon4 = Genphos[3]
      
      Genmaker.gen12_mass[0] = (Photon1+Photon2).M()
      Genmaker.gen13_mass[0] = (Photon1+Photon3).M()
      Genmaker.gen14_mass[0] = (Photon1+Photon4).M()
      Genmaker.gen23_mass[0] = (Photon2+Photon3).M()
      Genmaker.gen24_mass[0] = (Photon2+Photon4).M()
      Genmaker.gen34_mass[0] = (Photon3+Photon4).M()
      
      Genmaker.gen12dr[0] = Photon1.DeltaR(Photon2)
      Genmaker.gen13dr[0] = Photon1.DeltaR(Photon3)
      Genmaker.gen14dr[0] = Photon1.DeltaR(Photon4)
      Genmaker.gen23dr[0] = Photon2.DeltaR(Photon3)
      Genmaker.gen24dr[0] = Photon2.DeltaR(Photon4)
      Genmaker.gen34dr[0] = Photon3.DeltaR(Photon4)

      drlist = []
      fatphoton = []
      drlist.append(Photon1.DeltaR(Photon2))
      drlist.append(Photon3.DeltaR(Photon4))
      
      
      Genphos.sort(key=lambda x: x.Pt(), reverse=True) # now sort in pt order and save kinematics
      
      
      
      if len(Genphos) < 4:
         continue

      gen1 = TLorentzVector(0,0,0,0)
      gen2 = TLorentzVector(0,0,0,0)
      gen3 = TLorentzVector(0,0,0,0)
      gen4 = TLorentzVector(0,0,0,0)
      
      
      acc = []
      acceptance = ""
      pho1out = []
      pho2out = []
      pho3out = []
      pho4out = []
      fatphoout = []
      isopho1out = []
      isopho2out = []
      fatpho1out = []
      fatpho2out = []


      if len(Genphos) > 0:
         gen1 = Genphos[0]
      if len(Genphos) > 1:
         gen2 = Genphos[1]
      if len(Genphos) > 2:
         gen3 = Genphos[2]
      if len(Genphos) > 3:
         gen4 = Genphos[3]
      
      
      gen12 = gen1+gen2
      gen13 = gen1+gen3
      gen14 = gen1+gen4
      gen23 = gen2+gen3
      gen24 = gen2+gen4
      gen34 = gen3+gen4

#print gen1.Pt() , gen2.Pt(), gen3.Pt(), gen4.Pt()
      
      Genmaker.gen1_pt[0] = gen1.Pt()
      Genmaker.gen2_pt[0] = gen2.Pt()
      Genmaker.gen3_pt[0] = gen3.Pt()
      Genmaker.gen4_pt[0] = gen4.Pt()
      Genmaker.gen1_eta[0] = gen1.Eta()
      Genmaker.gen2_eta[0] = gen2.Eta()
      Genmaker.gen3_eta[0] = gen3.Eta()
      Genmaker.gen4_eta[0] = gen4.Eta()
      Genmaker.tp_mass[0] = (gen1+gen2+gen3+gen4).M()

      outTree.Fill()
   



      
      for d in drlist:
          if d < 0.1:
             fatphoton.append(1)

      category = ""
      if fatphoton.count(1) == 0:
          category = 4            ## all photons are resolved
      elif fatphoton.count(1) ==1 :
          category = 3            ## 1 merged pair
      elif fatphoton.count(1) ==2:
          category = 2            ## 2 merged pairs
      else : print " i give up"


       
    

      pho1 = ""
      pho2 = ""
      pho3 = ""
      pho4 = ""
      fourpho = []
      threepho = []
      twopho = []
      if category == 4:  # all photons are resolved

         pho1 = gen1
         pho2 = gen2
         pho3 = gen3
         pho4 = gen4
         
         fourpho.append(pho1)
         fourpho.append(pho2)
         fourpho.append(pho3)
         fourpho.append(pho4)
         #print " 4 photon case"
         #print pho1.Pt() , pho2.Pt(), pho3.Pt(), pho4.Pt()
         fourpho.sort(key=lambda x: x.Pt(), reverse=True) # now sort in pt order and save kinematics
         
         pho1 = fourpho[0]
         pho2 = fourpho[1]
         pho3 = fourpho[2]
         pho4 = fourpho[3]
         
         #print pho1.Pt() , pho2.Pt(), pho3.Pt(), pho4.Pt()
         Genmaker.p1_pt_case1[0] = pho1.Pt()
         Genmaker.p2_pt_case1[0] = pho2.Pt()
         Genmaker.p3_pt_case1[0] = pho3.Pt()
         Genmaker.p4_pt_case1[0] = pho4.Pt()
         Genmaker.p1_eta_case1[0] = pho1.Eta()
         Genmaker.p2_eta_case1[0] = pho2.Eta()
         Genmaker.p3_eta_case1[0] = pho3.Eta()
         Genmaker.p4_eta_case1[0] = pho4.Eta()
         Genmaker.p12_dr_case1[0] = pho1.DeltaR(pho2)
         Genmaker.p13_dr_case1[0] = pho1.DeltaR(pho3)
         Genmaker.p14_dr_case1[0] = pho1.DeltaR(pho4)
         Genmaker.p23_dr_case1[0] = pho2.DeltaR(pho3)
         Genmaker.p24_dr_case1[0] = pho2.DeltaR(pho4)
         Genmaker.p34_dr_case1[0] = pho3.DeltaR(pho4)
         Genmaker.p12_mass_case1[0] = (pho1+pho2).M()
         Genmaker.p13_mass_case1[0] = (pho1+pho3).M()
         Genmaker.p14_mass_case1[0] = (pho1+pho4).M()
         Genmaker.p23_mass_case1[0] = (pho2+pho3).M()
         Genmaker.p24_mass_case1[0] = (pho2+pho4).M()
         Genmaker.p34_mass_case1[0] = (pho3+pho4).M()
         Genmaker.tp_mass_case1[0] = (pho1+pho2+pho3+pho4).M()
         
         
         if (pho1.Pt() < 30 or abs(pho1.Eta()) > 2.5):
            pho1out.append(1)
         if (pho2.Pt() < 18 or abs(pho2.Eta()) > 2.5):
            pho2out.append(1)
         if (pho3.Pt() < 10 or abs(pho3.Eta()) > 2.5):
            pho3out.append(1)
         if (pho4.Pt() < 10 or abs(pho4.Eta()) > 2.5):
            pho4out.append(1)
         
         Genmaker.Pho1out[0] = len(pho1out)
         Genmaker.Pho2out[0] = len(pho2out)
         Genmaker.Pho3out[0] = len(pho3out)
         Genmaker.Pho4out[0] = len(pho4out)

         outTree_case1.Fill()

      elif category == 3: # 1 fat (sorry, merged :P) photon
    

           if  Photon1.DeltaR(Photon2) == min(drlist):
               pho1 = Photon1+Photon2
               if Photon3.Pt() > Photon4.Pt():
                  pho2 = Photon3
                  pho3 = Photon4
               elif Photon4.Pt() > Photon3.Pt():
                  pho2 = Photon4
                  pho3 = Photon3
           elif Photon3.DeltaR(Photon4) == min(drlist):
                pho1 = Photon3+Photon4
                if Photon1.Pt() > Photon2.Pt():
                   pho2 = Photon1
                   pho3 = Photon2
                elif Photon2.Pt() > Photon1.Pt():
                   pho2 = Photon2
                   pho3 = Photon1
           threepho.append(pho1)
           threepho.append(pho2)
           threepho.append(pho3)
           threepho.sort(key=lambda x: x.Pt(), reverse=True)
           pho1 = threepho[0]
           pho2 = threepho[1]
           pho3 = threepho[2]
      #print pho1.Pt() , pho2.Pt(), pho3.Pt()
           Genmaker.fatpho_pt_case2[0]  = pho1.Pt()
           Genmaker.isopho1_pt_case2[0] = pho2.Pt()
           Genmaker.isopho2_pt_case2[0] = pho3.Pt()
           Genmaker.fatpho_eta_case2[0] = pho1.Eta()
           Genmaker.isopho1_eta_case2[0] = pho2.Eta()
           Genmaker.isopho2_eta_case2[0] = pho3.Eta()
           Genmaker.fatpho_isopho1_dr_case2[0] = pho1.DeltaR(pho2)
           Genmaker.fatpho_isopho2_dr_case2[0] = pho1.DeltaR(pho3)
           Genmaker.isopho1_isopho2_dr_case2[0] = pho2.DeltaR(pho3)
           Genmaker.fatpho_mass_case2[0] = pho1.M()
           Genmaker.isopho12_mass_case2[0] = (pho2+pho3).M()
           Genmaker.tp_mass_case2[0] = (pho1+pho2+pho3).M()
           
           if (pho1.Pt() < 30 or abs(pho1.Eta()) > 2.5):
              fatphoout.append(1)
           if (pho2.Pt() < 18 or abs(pho2.Eta()) > 2.5):
              isopho1out.append(1)
           if (pho3.Pt() < 10 or abs(pho3.Eta()) > 2.5):
              isopho2out.append(1)
           
           Genmaker.Fatphoout[0] = len(fatphoout)
           Genmaker.Isopho1out[0] = len(isopho1out)
           Genmaker.Isopho2out[0] = len(isopho2out)
           
           outTree_case2.Fill()
 



      elif category == 2:
          
           if Photon1.DeltaR(Photon2) == min(drlist):
              pho1 = Photon1+Photon2
              pho2 = Photon3+Photon4
 
           elif Photon3.DeltaR(Photon4) == min(drlist):
                pho1 = Photon3+Photon4
                pho2 = Photon1+Photon2
           twopho.append(pho1)
           twopho.append(pho2)
           twopho.sort(key=lambda x: x.Pt(), reverse=True)
           pho1 = twopho[0]
           pho2 = twopho[1]
           #print pho1.Pt() , pho2.Pt()
           Genmaker.fatpho1_pt_case3[0] = pho1.Pt()
           Genmaker.fatpho2_pt_case3[0] = pho2.Pt()
           Genmaker.fatpho1_eta_case3[0] = pho1.Eta()
           Genmaker.fatpho2_eta_case3[0] = pho2.Eta()
           Genmaker.fatpho1_fatpho2_dr_case3[0] = pho1.DeltaR(pho2)
           Genmaker.fatpho1_mass_case3[0] = pho1.M()
           Genmaker.fatpho2_mass_case3[0] = pho2.M()
           Genmaker.tp_mass_case3[0] = (pho1+pho2).M()

           if (pho1.Pt() < 30 or abs(pho1.Eta()) > 2.5):
               fatpho1out.append(1)
           if (pho2.Pt() < 18 or abs(pho1.Eta()) > 2.5):
               fatpho2out.append(1)
           
           Genmaker.Fatpho1out[0] = len(fatpho1out)
           Genmaker.Fatpho2out[0] = len(fatpho2out)
           
           outTree_case3.Fill()




      evtCounter += 1

   outRoot.cd()
   outTree.Write()
   outTree_case1.Write()
   outTree_case2.Write()
   outTree_case3.Write()

   
   outRoot.Close()


if __name__ == "__main__":
   main(sys.argv[1:])

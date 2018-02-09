#!/usr/bin/python
import numpy as n
from ROOT import *
import sys, getopt
from array import array
from H4GSkimTools import *
#from H4GSkimTools_3 import *
#from H4GSkimTools_2 import *
def main(argv):
   #inputfiles= '/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/test/test2.root'
   inputfiles = '/eos/user/t/twamorka/2018/Feb2018/sig55.root'
   outputfile = 'Feb9_2018/sig55.root'

   maxEvts = -1
   nfakes = 0
   ntotpho = 4
   try:
      opts, args = getopt.getopt(argv,"hi:o:m:p:f:",["inputFiles=","outputFile=","maxEvents=","nphotons=","nfakes="])
   except getopt.GetoptError:
      print 'H4GTreeAnalyzer.py -i <inputfile1,inputfile2,inputfile3...> -o <outputfile> -m <maxEvts> -p <nphos> -f <nfakes>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile1,inputfile2,inputfile3...> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--inputFiles"):
         inputfiles = arg
      elif opt in ("-o", "--outputFile"):
         outputfile = arg
      elif opt in ("-m", "--maxEvents"):
         maxEvts = long(arg)
      elif opt in ("-p", "--nphotons"):
         ntotpho = int(arg)
      elif opt in ("-f", "--nfakes"):
         nfakes = int(arg)

   listOfFiles = inputfiles.split(",")
   print "Number of input files: ", len(listOfFiles)

   tree = TChain("h4gflash/H4GTree")
   for f in listOfFiles:
      print "\t Adding file:", f
      tree.AddFile(f)
   print "Total number of events to be analyzed:", tree.GetEntries()

   outRoot = TFile(outputfile, "RECREATE")

   treeSkimmer = SkimmedTreeTools()
   outTree_all = treeSkimmer.MakeSkimmedTree_all()
   outTree = treeSkimmer.MakeSkimmedTree()
   outTree_3 = treeSkimmer.MakeSkimmedTree_3()
   outTree_2 = treeSkimmer.MakeSkimmedTree_2()

   triggers = {}
   triggerNames = []
   fraction = []

   evtCounter = 0
   treeSkimmer.initialEvents[0] = tree.GetEntries()
   eventsToRun = min(maxEvts, tree.GetEntries())
   if maxEvts < 0:
      eventsToRun = tree.GetEntries()
   #Tree Loop:
   for evt in range(0,eventsToRun):
      if evt%1000 == 0: print "## Analyzing event ", evt
      tree.GetEntry(evt)

      treeSkimmer.event[0] = tree.event
      treeSkimmer.run[0] = tree.run
      treeSkimmer.lumi[0] = tree.lumi
      treeSkimmer.nvtx[0] = tree.nvtx
      treeSkimmer.npu[0] = tree.npu
      treeSkimmer.genTotalWeight[0] = tree.genTotalWeight
      treeSkimmer.passTrigger[0] = tree.passTrigger
      
      Phos = []
      Phos_id = []
    
      for p in range(0,tree.n_pho ):
        p4 = TLorentzVector(0,0,0,0)
        p4.SetPtEtaPhiM( tree.v_pho_pt[p], tree.v_pho_eta[p], tree.v_pho_phi[p], 0 )
        minDR = 999
        for Pho in Phos:
           dr = Pho.DeltaR(p4)
           if dr < minDR:
              minDR = dr
        if minDR > 0.001:   ## ~~ this is to avoid double counting of photons that have almost overlapping hits in the ECAL SC
           Phos.append(p4)
           Phos_id.append(p)
      
      Phos.sort(key=lambda x: x.Pt(), reverse=True)
      #Make photon selection first because the triggered photons *must* be selected
      sPhos,sPhos_id = treeSkimmer.MakePhotonSelection(Phos, Phos_id, tree.v_pho_mva, tree.v_pho_passElectronVeto)
      
      if nfakes > 0 :
         fPhos, fPhos_id = treeSkimmer.SelectWithFakes(Phos, Phos_id, tree.v_pho_mva, tree.v_pho_passElectronVeto)
         if len(fPhos) < nfakes:
            continue
         if len(sPhos) < ntotpho - nfakes:
            continue
         phomatrix = [[x,y] for x,y in zip(sPhos, sPhos_id)]
         fakematrix = [[x,y] for x,y in zip(fPhos, fPhos_id)]
         phomatrixreduced = phomatrix[:(ntotpho-nfakes)]
         fakematrixreduced = fakematrix[:(nfakes)]
         totmatrix = phomatrixreduced+fakematrixreduced
         totmatrix.sort(key=lambda x: x[0].Pt(), reverse=True)
         sPhos = [x[0] for x in totmatrix]
         sPhos_id = [x[1] for x in totmatrix]

      triggeredDipho = treeSkimmer.MakeTriggerSelection(sPhos, sPhos_id, tree.v_pho_full5x5_r9, tree.v_pho_chargedHadronIso, tree.v_pho_hadronicOverEm, tree.v_pho_hasPixelSeed, tree.v_pho_ecalPFClusterIso, tree.v_pho_sigmaIetaIeta, tree.v_pho_trackIso)
      if triggeredDipho == 0: continue
      treeSkimmer.p_npho[0] = len(sPhos)
      #print "Number of photons " , len(sPhos)
      listdr = []
      for m in range(0, len(sPhos)):
          treeSkimmer.p_pt[0] =  sPhos[m].Pt()
          treeSkimmer.p_M[0] = sPhos[m].M()
          treeSkimmer.p_eta[0] = sPhos[m].Eta()
          treeSkimmer.p_phi[0] = sPhos[m].Phi()
          treeSkimmer.p_mva[0] = tree.v_pho_mva[sPhos_id[m]]
          treeSkimmer.p_r9[0] = tree.v_pho_r9[sPhos_id[m]]
          treeSkimmer.p_full5x5_r9[0] = tree.v_pho_full5x5_r9[sPhos_id[m]]
          treeSkimmer.p_sigmaEtaEta[0] = tree.v_pho_sigmaEtaEta[sPhos_id[m]]
          treeSkimmer.p_full5x5_sigmaEtaEta[0] = tree.v_pho_full5x5_sigmaEtaEta[sPhos_id[m]]
          treeSkimmer.p_full5x5_sigmaIetaIeta[0] = tree.v_pho_full5x5_sigmaIetaIeta[sPhos_id[m]]
          treeSkimmer.p_sigmaIphiIphi[0] = tree.v_pho_sigmaIphiIphi[sPhos_id[m]]
          treeSkimmer.p_genmatch[0] = tree.v_pho_genmatch[sPhos_id[m]]
          for n in range(0, len(sPhos)):
              if (n!=m and n>m):
                 dr = sPhos[m].DeltaR(sPhos[n])
                 listdr.append(dr)
      treeSkimmer.p_drmin[0] = min(listdr)
      treeSkimmer.p_drmax[0] = max(listdr)
 
      outTree_all.Fill()
 ## here write the code to save info of photons irrespective of how many photons there are in the event

## in a separate loop try to calculate mindr here
  

      ## yahan se 3 categories me split ho sakta hai
      if len(sPhos) == 3:
         #triggeredDipho = treeSkimmer.MakeTriggerSelection(sPhos, sPhos_id, tree.v_pho_full5x5_r9, tree.v_pho_chargedHadronIso, tree.v_pho_hadronicOverEm, tree.v_pho_hasPixelSeed, tree.v_pho_ecalPFClusterIso, tree.v_pho_sigmaIetaIeta, tree.v_pho_trackIso)
         #if triggeredDipho == 0: continue
         treeSkimmer.p1_pt_3[0] = sPhos[0].Pt()
         treeSkimmer.p2_pt_3[0] = sPhos[1].Pt()
         treeSkimmer.p3_pt_3[0] = sPhos[2].Pt()
         treeSkimmer.p1_eta_3[0] = sPhos[0].Eta()
         treeSkimmer.p2_eta_3[0] = sPhos[1].Eta()
         treeSkimmer.p3_eta_3[0] = sPhos[2].Eta()
         treeSkimmer.p1_phi_3[0] = sPhos[0].Phi()
         treeSkimmer.p2_phi_3[0] = sPhos[1].Phi()
         treeSkimmer.p3_phi_3[0] = sPhos[2].Phi()
         treeSkimmer.p1_M_3[0] = sPhos[0].M()
         treeSkimmer.p2_M_3[0] = sPhos[1].M()
         treeSkimmer.p3_M_3[0] = sPhos[2].M()
         treeSkimmer.p1_mva_3[0] = tree.v_pho_mva[sPhos_id[0]]
         treeSkimmer.p2_mva_3[0] = tree.v_pho_mva[sPhos_id[1]]
         treeSkimmer.p3_mva_3[0] = tree.v_pho_mva[sPhos_id[2]]
         treeSkimmer.p1_r9_3[0] = tree.v_pho_r9[sPhos_id[0]]
         treeSkimmer.p2_r9_3[0] = tree.v_pho_r9[sPhos_id[1]]
         treeSkimmer.p3_r9_3[0] = tree.v_pho_r9[sPhos_id[2]]
         treeSkimmer.p1_full5x5_r9_3[0] = tree.v_pho_full5x5_r9[sPhos_id[0]]
         treeSkimmer.p2_full5x5_r9_3[0] = tree.v_pho_full5x5_r9[sPhos_id[1]]
         treeSkimmer.p3_full5x5_r9_3[0] = tree.v_pho_full5x5_r9[sPhos_id[2]]

         treeSkimmer.p1_full5x5_sigmaIetaIeta_3[0] = tree.v_pho_full5x5_sigmaIetaIeta[sPhos_id[0]]
         treeSkimmer.p2_full5x5_sigmaIetaIeta_3[0] = tree.v_pho_full5x5_sigmaIetaIeta[sPhos_id[1]]
         treeSkimmer.p3_full5x5_sigmaIetaIeta_3[0] = tree.v_pho_full5x5_sigmaIetaIeta[sPhos_id[2]]

         treeSkimmer.p1_sigmaIphiIphi_3[0] = tree.v_pho_sigmaIphiIphi[sPhos_id[0]]
         treeSkimmer.p2_sigmaIphiIphi_3[0] = tree.v_pho_sigmaIphiIphi[sPhos_id[1]]
         treeSkimmer.p3_sigmaIphiIphi_3[0] = tree.v_pho_sigmaIphiIphi[sPhos_id[2]]

         treeSkimmer.p1_sigmaEtaEta_3[0] = tree.v_pho_sigmaEtaEta[sPhos_id[0]]
         treeSkimmer.p2_sigmaEtaEta_3[0] = tree.v_pho_sigmaEtaEta[sPhos_id[1]]
         treeSkimmer.p3_sigmaEtaEta_3[0] = tree.v_pho_sigmaEtaEta[sPhos_id[2]]

         treeSkimmer.p1_full5x5_sigmaEtaEta_3[0] = tree.v_pho_full5x5_sigmaEtaEta[sPhos_id[0]]
         treeSkimmer.p2_full5x5_sigmaEtaEta_3[0] = tree.v_pho_full5x5_sigmaEtaEta[sPhos_id[1]]
         treeSkimmer.p3_full5x5_sigmaEtaEta_3[0] = tree.v_pho_full5x5_sigmaEtaEta[sPhos_id[2]]

         treeSkimmer.p1_genmatch_3[0] = tree.v_pho_genmatch[sPhos_id[0]]
         treeSkimmer.p2_genmatch_3[0] = tree.v_pho_genmatch[sPhos_id[1]]
         treeSkimmer.p3_genmatch_3[0] = tree.v_pho_genmatch[sPhos_id[2]]
 
         #treeSkimmer.p1_match_3[0] = tree.v_genmatch_int[sPhos_id[0]]
         #treeSkimmer.p2_match_3[0] = tree.v_genmatch_int[sPhos_id[1]]
         #treeSkimmer.p3_match_3[0] = tree.v_genmatch_int[sPhos_id[2]]       
  
         print " Min dr for 3 photon category " , min(sPhos[0].DeltaR(sPhos[1]), sPhos[0].DeltaR(sPhos[2]), sPhos[1].DeltaR(sPhos[2]))
         treeSkimmer.p_mindr_3[0] = min(sPhos[0].DeltaR(sPhos[1]), sPhos[0].DeltaR(sPhos[2]), sPhos[1].DeltaR(sPhos[2]))
         treeSkimmer.p_maxdr_3[0] = max(sPhos[0].DeltaR(sPhos[1]), sPhos[0].DeltaR(sPhos[2]), sPhos[1].DeltaR(sPhos[2]))
         P12 = sPhos[0] + sPhos[1]
         P13 = sPhos[0] + sPhos[2]
         P23 = sPhos[1] + sPhos[2]

         #print "P12 Mass " , P12.M() , "P13 Mass ", P13.M() , "P23 Mass " , P23.M()
 
         treeSkimmer.dphigh_mass_3[0] = P12.M()
         treeSkimmer.p_maxmass_3[0] = max(P12.M(),P13.M(),P23.M()) 
        
         #a1 = ""
         
         #if (P12.M() < P13.M() and P12.M() < P23.M()):
            #a1 = P12
            #treeSkimmer.dp1_dr_3 = sPhos[0].DeltaR(sPhos[1])
         #elif (P13.M() < P12.M() and P13.M() < P23.M()):
            #a1 = P13
            #treeSkimmer.dp1_dr_3 = sPhos[0].DeltaR(sPhos[2])
         #else:
            #a1 = P23
            #treeSkimmer.dp1_dr_3 = sPhos[1].DeltaR(sPhos[2])
     


         #treeSkimmer.dp1_pt_3 = a1.Pt()
         #treeSkimmer.dp1_eta_3 = a1.Eta()
         #treeSkimmer.dp1_phi_3 = a1.Phi()
         #treeSkimmer.dp1_mass_3 = a1.M()
          
         Pgggg = sPhos[0] + sPhos[1] + sPhos[2]
         treeSkimmer.tp_pt_3[0] = Pgggg.Pt()
         treeSkimmer.tp_eta_3[0] = Pgggg.Eta()
         treeSkimmer.tp_phi_3[0] = Pgggg.Phi()
         treeSkimmer.tp_mass_3[0] = Pgggg.M()         
      
         outTree_3.Fill()

      elif len(sPhos) == 2:
         #triggeredDipho = treeSkimmer.MakeTriggerSelection(sPhos, sPhos_id, tree.v_pho_full5x5_r9, tree.v_pho_chargedHadronIso, tree.v_pho_hadronicOverEm, tree.v_pho_hasPixelSeed, tree.v_pho_ecalPFClusterIso, tree.v_pho_sigmaIetaIeta, tree.v_pho_trackIso)
         #if triggeredDipho == 0: continue
         treeSkimmer.p1_pt_2[0] = sPhos[0].Pt()
         treeSkimmer.p2_pt_2[0] = sPhos[1].Pt()
         treeSkimmer.p1_eta_2[0] = sPhos[0].Eta()
         treeSkimmer.p2_eta_2[0] = sPhos[1].Eta()
         treeSkimmer.p1_phi_2[0] = sPhos[0].Phi()
         treeSkimmer.p2_phi_2[0] = sPhos[1].Phi()
         treeSkimmer.p1_M_2[0] = sPhos[0].M()
         treeSkimmer.p2_M_2[0] = sPhos[1].M()
         treeSkimmer.p1_mva_2[0] = tree.v_pho_mva[sPhos_id[0]]
         treeSkimmer.p2_mva_2[0] = tree.v_pho_mva[sPhos_id[1]]
         treeSkimmer.p1_r9_2[0] = tree.v_pho_r9[sPhos_id[0]]
         treeSkimmer.p2_r9_2[0] = tree.v_pho_r9[sPhos_id[1]]
         treeSkimmer.p1_full5x5_r9_2[0] = tree.v_pho_full5x5_r9[sPhos_id[0]]
         treeSkimmer.p2_full5x5_r9_2[0] = tree.v_pho_full5x5_r9[sPhos_id[1]]

         treeSkimmer.p1_full5x5_sigmaIetaIeta_2[0] = tree.v_pho_full5x5_sigmaIetaIeta[sPhos_id[0]]
         treeSkimmer.p2_full5x5_sigmaIetaIeta_2[0] = tree.v_pho_full5x5_sigmaIetaIeta[sPhos_id[1]]

         treeSkimmer.p1_sigmaIphiIphi_2[0] = tree.v_pho_sigmaIphiIphi[sPhos_id[0]]
         treeSkimmer.p2_sigmaIphiIphi_2[0] = tree.v_pho_sigmaIphiIphi[sPhos_id[1]]

         treeSkimmer.p1_sigmaEtaEta_2[0] = tree.v_pho_sigmaEtaEta[sPhos_id[0]]
         treeSkimmer.p2_sigmaEtaEta_2[0] = tree.v_pho_sigmaEtaEta[sPhos_id[1]]

         treeSkimmer.p1_full5x5_sigmaEtaEta_2[0] = tree.v_pho_full5x5_sigmaEtaEta[sPhos_id[0]]
         treeSkimmer.p2_full5x5_sigmaEtaEta_2[0] = tree.v_pho_full5x5_sigmaEtaEta[sPhos_id[1]]

         treeSkimmer.p1_genmatch_2[0] = tree.v_pho_genmatch[sPhos_id[0]]
         treeSkimmer.p2_genmatch_2[0] = tree.v_pho_genmatch[sPhos_id[1]]
     
         treeSkimmer.p_mindr_2[0] = sPhos[0].DeltaR(sPhos[1])
         
         Pgggg = sPhos[0] + sPhos[1]
         treeSkimmer.tp_pt_2[0] = Pgggg.Pt()
         treeSkimmer.tp_eta_2[0] = Pgggg.Eta()
         treeSkimmer.tp_phi_2[0] = Pgggg.Phi()
         treeSkimmer.tp_mass_2[0] = Pgggg.M()
       
         outTree_2.Fill()

      elif len(sPhos) >3: #ntotpho, i.e total number of photons should always be =4
          treeSkimmer.p1_pt[0] = sPhos[0].Pt()
          treeSkimmer.p2_pt[0] = sPhos[1].Pt()
          treeSkimmer.p3_pt[0] = sPhos[2].Pt()
          treeSkimmer.p4_pt[0] = sPhos[3].Pt()
          treeSkimmer.p1_eta[0] = sPhos[0].Eta()
          treeSkimmer.p2_eta[0] = sPhos[1].Eta()
          treeSkimmer.p3_eta[0] = sPhos[2].Eta()
          treeSkimmer.p4_eta[0] = sPhos[3].Eta()
          treeSkimmer.p1_phi[0] = sPhos[0].Phi()
          treeSkimmer.p2_phi[0] = sPhos[1].Phi()
          treeSkimmer.p3_phi[0] = sPhos[2].Phi()
          treeSkimmer.p4_phi[0] = sPhos[3].Phi()
          treeSkimmer.p1_M[0] = sPhos[0].M()
          treeSkimmer.p2_M[0] = sPhos[1].M()
          treeSkimmer.p3_M[0] = sPhos[2].M()
          treeSkimmer.p4_M[0] = sPhos[3].M()


          treeSkimmer.p1_mva[0] = tree.v_pho_mva[sPhos_id[0]]
          treeSkimmer.p2_mva[0] = tree.v_pho_mva[sPhos_id[1]]
	  treeSkimmer.p3_mva[0] = tree.v_pho_mva[sPhos_id[2]]
	  treeSkimmer.p4_mva[0] = tree.v_pho_mva[sPhos_id[3]]

          treeSkimmer.p1_r9[0] = tree.v_pho_r9[sPhos_id[0]]
          treeSkimmer.p2_r9[0] = tree.v_pho_r9[sPhos_id[1]]
          treeSkimmer.p3_r9[0] = tree.v_pho_r9[sPhos_id[2]]
          treeSkimmer.p4_r9[0] = tree.v_pho_r9[sPhos_id[3]]
     
          
          treeSkimmer.p1_full5x5_r9[0] = tree.v_pho_full5x5_r9[sPhos_id[0]]
          treeSkimmer.p2_full5x5_r9[0] = tree.v_pho_full5x5_r9[sPhos_id[1]]
          treeSkimmer.p3_full5x5_r9[0] = tree.v_pho_full5x5_r9[sPhos_id[2]]
          treeSkimmer.p4_full5x5_r9[0] = tree.v_pho_full5x5_r9[sPhos_id[3]]  
      
          treeSkimmer.p1_full5x5_sigmaIetaIeta[0] = tree.v_pho_full5x5_sigmaIetaIeta[sPhos_id[0]]
          treeSkimmer.p2_full5x5_sigmaIetaIeta[0] = tree.v_pho_full5x5_sigmaIetaIeta[sPhos_id[1]]
          treeSkimmer.p3_full5x5_sigmaIetaIeta[0] = tree.v_pho_full5x5_sigmaIetaIeta[sPhos_id[2]]
          treeSkimmer.p4_full5x5_sigmaIetaIeta[0] = tree.v_pho_full5x5_sigmaIetaIeta[sPhos_id[3]]
      
          treeSkimmer.p1_sigmaIphiIphi[0] = tree.v_pho_sigmaIphiIphi[sPhos_id[0]]
          treeSkimmer.p2_sigmaIphiIphi[0] = tree.v_pho_sigmaIphiIphi[sPhos_id[1]]
          treeSkimmer.p3_sigmaIphiIphi[0] = tree.v_pho_sigmaIphiIphi[sPhos_id[2]]
          treeSkimmer.p4_sigmaIphiIphi[0] = tree.v_pho_sigmaIphiIphi[sPhos_id[3]]

          treeSkimmer.p1_sigmaEtaEta[0] = tree.v_pho_sigmaEtaEta[sPhos_id[0]]
          treeSkimmer.p2_sigmaEtaEta[0] = tree.v_pho_sigmaEtaEta[sPhos_id[1]]
          treeSkimmer.p3_sigmaEtaEta[0] = tree.v_pho_sigmaEtaEta[sPhos_id[2]]
          treeSkimmer.p4_sigmaEtaEta[0] = tree.v_pho_sigmaEtaEta[sPhos_id[3]]

          treeSkimmer.p1_full5x5_sigmaEtaEta[0] = tree.v_pho_full5x5_sigmaEtaEta[sPhos_id[0]]
          treeSkimmer.p2_full5x5_sigmaEtaEta[0] = tree.v_pho_full5x5_sigmaEtaEta[sPhos_id[1]]
          treeSkimmer.p3_full5x5_sigmaEtaEta[0] = tree.v_pho_full5x5_sigmaEtaEta[sPhos_id[2]]
          treeSkimmer.p4_full5x5_sigmaEtaEta[0] = tree.v_pho_full5x5_sigmaEtaEta[sPhos_id[3]]      
      
          treeSkimmer.p1_genmatch[0] = tree.v_pho_genmatch[sPhos_id[0]]
          treeSkimmer.p2_genmatch[0] = tree.v_pho_genmatch[sPhos_id[1]]
          treeSkimmer.p3_genmatch[0] = tree.v_pho_genmatch[sPhos_id[2]]
          treeSkimmer.p4_genmatch[0] = tree.v_pho_genmatch[sPhos_id[3]]
   
          treeSkimmer.p_mindr[0] = min( sPhos[0].DeltaR(sPhos[1]), sPhos[0].DeltaR(sPhos[2]), sPhos[0].DeltaR(sPhos[3]), sPhos[1].DeltaR(sPhos[2]), sPhos[1].DeltaR(sPhos[3]), sPhos[2].DeltaR(sPhos[3])) 
          treeSkimmer.p_maxdr[0] = max( sPhos[0].DeltaR(sPhos[1]), sPhos[0].DeltaR(sPhos[2]), sPhos[0].DeltaR(sPhos[3]), sPhos[1].DeltaR(sPhos[2]), sPhos[1].DeltaR(sPhos[3]), sPhos[2].DeltaR(sPhos[3]) )      
          P12 = sPhos[0] + sPhos[1]
          P13 = sPhos[0] + sPhos[2]
          P14 = sPhos[0] + sPhos[3]
          P23 = sPhos[1] + sPhos[2]
          P24 = sPhos[1] + sPhos[3]
          P34 = sPhos[2] + sPhos[3]
   
          treeSkimmer.dphigh_mass[0] = P12.M()
          treeSkimmer.p_maxmass[0] = max((P12.M(),P13.M(),P14.M(),P23.M(),P24.M(),P34.M()))
          pairedDiphos = treeSkimmer.MakePairing(sPhos)
          PP1 = pairedDiphos[0][0]
          PP2 = pairedDiphos[1][0]
     
          treeSkimmer.dp1_p1i[0] = pairedDiphos[0][2]
          treeSkimmer.dp1_p2i[0] = pairedDiphos[0][4]
          treeSkimmer.dp2_p1i[0] = pairedDiphos[1][2]
          treeSkimmer.dp2_p2i[0] = pairedDiphos[1][4]

          if(DEBUG): print pairedDiphos
          treeSkimmer.dp1_dr[0] = pairedDiphos[0][1].DeltaR(pairedDiphos[0][3])
          treeSkimmer.dp2_dr[0] = pairedDiphos[1][1].DeltaR(pairedDiphos[1][3])

          treeSkimmer.dp1_pt[0] = PP1.Pt()
          treeSkimmer.dp1_eta[0] = PP1.Eta()
          treeSkimmer.dp1_phi[0] = PP1.Phi()
          treeSkimmer.dp1_mass[0] = PP1.M()
          treeSkimmer.dp2_pt[0] = PP2.Pt()
          treeSkimmer.dp2_eta[0] = PP2.Eta()
          treeSkimmer.dp2_phi[0] = PP2.Phi()
          treeSkimmer.dp2_mass[0] = PP2.M()

          Pgggg = sPhos[0] + sPhos[1] + sPhos[2] + sPhos[3]
          treeSkimmer.tp_pt[0] = Pgggg.Pt()
          treeSkimmer.tp_eta[0] = Pgggg.Eta()
          treeSkimmer.tp_phi[0] = Pgggg.Phi()
          treeSkimmer.tp_mass[0] = Pgggg.M()
          
          outTree.Fill()
   
      evtCounter += 1

   #end of event loop!

   outRoot.cd()
   outTree_all.Write()
   outTree.Write()
   outTree_3.Write()
   outTree_2.Write()
   outRoot.Close()
   
   #outTree_3.Write()
	

if __name__ == "__main__":
   main(sys.argv[1:])



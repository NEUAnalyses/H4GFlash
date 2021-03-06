#!/usr/bin/python
import numpy as n
from ROOT import *
import sys, getopt
from array import array
from H4GSkimTools import *

def main(argv):
   inputfiles = '/eos/user/t/twamorka/FatPho0p1_Match0p15/sig60.root'
   outputfile = 'test.root'
   maxEvts = -1
   nfakes = 0
   ntotpho = 4
   try:
      opts, args = getopt.getopt(argv,"hi:o:m:",["inputFiles=","outputFile=","maxEvents="])
   except getopt.GetoptError:
      print 'H4GEfficiencies.py -i <inputfile1,inputfile2,inputfile3...> -o <outputfile> -m <maxEvts>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'H4GEfficiencies.py -i <inputfile1,inputfile2,inputfile3...> -o <outputfile> -m <maxEvts>'
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

   treeSkimmer = SkimmedTreeTools()

   outRoot = TFile(outputfile, "RECREATE")

   outTree = TTree("H4GEff", "Tree to calculate efficiencies")
   totevs = n.zeros(1, dtype=float)
   cut0 = n.zeros(1, dtype=float)  #more than 0 photons
   cut1 = n.zeros(1, dtype=float)  #more than 1 photon
   cut2 = n.zeros(1, dtype=float)  #more than 2 photons
   cut3 = n.zeros(1, dtype=float)  #more than 3 photons
   cut4 = n.zeros(1, dtype=float)  # > 0 photons + ID
   cut5 = n.zeros(1, dtype=float)  # > 1 photon + ID
   cut6 = n.zeros(1, dtype=float)  # > 2 photons + ID
   cut7 = n.zeros(1, dtype=float)  # > 3 photons + ID
   cut8 = n.zeros(1, dtype=float)  # all photons have passed the pre-selection
   cut9 = n.zeros(1, dtype=float)  # 3 photon category photons
   cut10 = n.zeros(1, dtype=float) # 2 photon category photons
   cut11 = n.zeros(1, dtype=float) # 4 photon category photons
   cut12 = n.zeros(1, dtype=float)
   cut13 = n.zeros(1, dtype=float)
   cut14 = n.zeros(1, dtype=float)
   cut15 = n.zeros(1, dtype=float)
   cut16 = n.zeros(1, dtype=float)
   cut17 = n.zeros(1, dtype=float)
   cut18 = n.zeros(1, dtype=float)
   cut19 = n.zeros(1, dtype=float)
   cut20 = n.zeros(1, dtype=float)
   cuta = n.zeros(1, dtype=float)
   cutb = n.zeros(1, dtype=float)
   cutc = n.zeros(1, dtype=float)
   cutd = n.zeros(1, dtype=float)
   cute = n.zeros(1, dtype=float)

   outTree.Branch('totevs', totevs, 'totevs/D')
   outTree.Branch('cut0', cut0, 'cut0/D')
   outTree.Branch('cut1', cut1, 'cut1/D')
   outTree.Branch('cut2', cut2, 'cut2/D')
   outTree.Branch('cut3', cut3, 'cut3/D')
   outTree.Branch('cut4', cut4, 'cut4/D')
   outTree.Branch('cut5', cut5, 'cut5/D')
   outTree.Branch('cut6', cut6, 'cut6/D')
   outTree.Branch('cut7', cut7, 'cut7/D')
   outTree.Branch('cut8', cut8, 'cut8/D')
   outTree.Branch('cut9', cut9, 'cut9/D')
   outTree.Branch('cut10', cut10, 'cut10/D')
   outTree.Branch('cut11', cut11, 'cut11/D')
   outTree.Branch('cut12', cut12, 'cut12/D')
   outTree.Branch('cut13', cut13, 'cut13/D')
   outTree.Branch('cut14', cut14, 'cut14/D')
   outTree.Branch('cut15', cut15, 'cut15/D')
   outTree.Branch('cut16', cut16, 'cut16/D')
   outTree.Branch('cut17', cut17, 'cut17/D')
   outTree.Branch('cut18', cut18, 'cut18/D')
   outTree.Branch('cut19', cut19, 'cut19/D')
   outTree.Branch('cut20', cut20, 'cut20/D')
   outTree.Branch('cuta',cuta,'cuta/D')
   outTree.Branch('cutb',cutb,'cutb/D')
   outTree.Branch('cutc',cutc,'cutc/D')
   outTree.Branch('cutd',cutd,'cutd/D')
   outTree.Branch('cute',cute,'cute/D')
   evtCounter = 0
   totevs[0] = tree.GetEntries()

   eventsToRun = min(maxEvts, tree.GetEntries())
   if maxEvts < 0:
      eventsToRun = tree.GetEntries()
   #Tree Loop:
   for evt in range(0, eventsToRun):
      if evt%1000 == 0: print "## Analyzing event ", evt
      tree.GetEntry(evt)

      cut0[0] = 0
      cut1[0] = 0
      cut2[0] = 0
      cut3[0] = 0
      cut4[0] = 0
      cut5[0] = 0
      cut6[0] = 0
      cut7[0] = 0
      cut8[0] = 0
      cut9[0] = 0
      cut10[0] = 0
      cut11[0] = 0
      cut12[0] = 0
      cut13[0] = 0
      cut14[0] = 0
      cut15[0] = 0
      cut16[0] = 0
      cut17[0] = 0
      cut18[0] = 0
      cut19[0] = 0
      cut20[0] = 0
      cuta[0] = 0
      cutb[0] = 0
      cutc[0] = 0
      cutd[0] = 0
      cute[0] = 0
      Phos = []
      Phos_id = []

      for p in range(0, tree.n_pho):
        p4 = TLorentzVector(0,0,0,0)
        p4.SetPtEtaPhiM( tree.v_pho_pt[p], tree.v_pho_eta[p], tree.v_pho_phi[p], 0 )
        minDR = 999
        for Pho in Phos:
           dr = Pho.DeltaR(p4)
           if dr < minDR:
              minDR = dr
        if minDR > 0.001:
           Phos.append(p4)
           Phos_id.append(p)

#if len(Phos) > 0:
#cut0[0] = 1
#if len(Phos) > 1:
#cut1[0] = 1
#if len(Phos) > 2:
#cut2[0] = 1
#if len(Phos) > 3:  ## acceptance for 4g cat
#cut3[0] = 1
#if len(Phos) == 2: ## acceptance for 2g cat
#cut4[0] = 1
#if len(Phos) == 3: ## acceptance for 3g cat
#cut5[0] = 1

      Phos.sort(key=lambda x: x.Pt(), reverse=True)
          #if tree.passTrigger==1:
#cut0[0] = 1

# tPhos,tPhos_id = treeSkimmer.triggerpass(Phos, Phos_id ,tree.passTrigger)
#      if len(tPhos) == 2:
#         cuta[0] = 1
#      elif len(tPhos) == 3:
#         cutb[0] = 1
#         nicematch_1 = []
#         match_1 = 0
#         for g in range(0,tree.v_genmatch_pt.size()):
#             if tree.v_genmatch_pt[g] > 0:
#                match_1 = 1
#                nicematch_1.append(1)
#         if nicematch_1.count(1) == 4:
#            cutc[0] = 1
#         else: cutd[0] = 1
#      elif len(tPhos) > 3:
#         cute[0] = 1
      #print " passtrigger value ", tree.passTrigger   
      sPhos,sPhos_id = treeSkimmer.MakePhotonSelection(Phos, Phos_id, tree.v_pho_mva, tree.v_pho_passElectronVeto)
#     if len(sPhos) >0:
      cut0[0] = 1


#if len(sPhos) > 0:
#cut6[0] = 1
#if len(sPhos) > 1:
#cut7[0] = 1
#if len(sPhos) > 2:
#cut8[0] = 1
#if len(sPhos) > 3: ## MVA for 4g cat
#cut9[0] = 1
#if len(sPhos) == 2: ## MVA for 2g cat
#cut10[0] = 1
#if len(sPhos) == 3: ## MVA for 3g cat
#cut11[0] = 1

      triggeredDipho = treeSkimmer.MakeTriggerSelection(sPhos, sPhos_id, tree.v_pho_full5x5_r9,  tree.v_pho_hadronicOverEm, tree.v_pho_hasPixelSeed, tree.v_pho_ecalPFClusterIso, tree.v_pho_sigmaIetaIeta, tree.v_pho_trackIso)
#      triggeredDipho = treeSkimmer.MakeTriggerSelection(sPhos, sPhos_id, tree.v_pho_full5x5_r9, tree.v_pho_hadronicOverEm, tree.v_pho_hasPixelSeed, tree.v_pho_ecalPFClusterIso, tree.v_pho_sigmaIetaIeta, tree.v_pho_trackIso)
      if triggeredDipho != 0:  #no diphoton triggered
         cut1[0] = 1
#         if len(sPhos)==2:
#            cut3[0] = 1
#         elif len(sPhos)==3:
#            cut4[0] = 1
            #nicematch = []
            #match = 0
            #for g in range(0,tree.v_genmatch_pt.size()):
            #if tree.v_genmatch_pt[g] > 0:
            #match = 1
            #nicematch.append(1)
            #if nicematch.count(1) == 0:
            #cut15[0] = 1
            #elif nicematch.count(1) == 1 :
            #cut16[0] = 1
            #elif nicematch.count(1) == 2:
            #cut17[0] = 1
            #elif nicematch.count(1) ==3 :
            #cut18[0] = 1
            #elif nicematch.count(1) == 4:
            #cut19[0] = 1
         if len(sPhos) > 3:
            cut2[0] = 1

      #print "ratio 2 photon ", cut8/cut11

      evtCounter += 1

      outTree.Fill()
   #end of event loop!

   outRoot.cd()
   outTree.Write()
   outRoot.Close()

	

if __name__ == "__main__":
   main(sys.argv[1:])



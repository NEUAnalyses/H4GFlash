#!/usr/bin/python
import numpy as n
from ROOT import *
import sys, getopt
from array import array
from H4GSkimTools import *
import math as m


def main(argv):
   inputfiles = '/eos/cms/store/user/twamorka/2016_Signal/signal_m_60.root'
   outputfile = 'output.root'
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
   outTree_0 = treeSkimmer.MakeSkimmedTree_0()
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
       #for evt in range(0,eventsToRun):
      if evt%1000 == 0: print "## Analyzing event ", evt
      tree.GetEntry(evt)
      treeSkimmer.event[0] = tree.event
      treeSkimmer.run[0] = tree.run
      treeSkimmer.lumi[0] = tree.lumi
      treeSkimmer.nvtx[0] = tree.nvtx
      treeSkimmer.npu[0] = tree.npu

      Phos = []
      Phos_id = []
      resolvedcount = []
      mergedcount = []
      fatpho1count = []
      fatpho2count = []
      outofptcount = []
      outofetacount = []
      fatphocount_revised = []
      resolvedcount_revised = []
      pho1out = []
      pho2out = []
      pho3out = []
      pho4out = []

      for p in range(0,tree.n_pho ):
        p4 = TLorentzVector(0,0,0,0)
        p4.SetPtEtaPhiM( tree.v_pho_pt[p], tree.v_pho_eta[p], tree.v_pho_phi[p], 0 )
        minDR = 999
        Phos.append(p4)
        Phos_id.append(p)
      Phos.sort(key=lambda x: x.Pt(), reverse=True)

      nPhos,nPhos_id = treeSkimmer.PhotonCollection(Phos,Phos_id)  ## collection of photons with no selection applied

      treeSkimmer.p0_npho[0] = len(nPhos)

      for r in range (0,len(nPhos)):
          treeSkimmer.p0_pt[0] = nPhos[r].Pt()
          treeSkimmer.p0_eta[0] = Phos[r].Eta()
          treeSkimmer.p0_phi[0] = nPhos[r].Phi()
          treeSkimmer.p0_mva[0] = tree.v_pho_mva[nPhos_id[r]]
          treeSkimmer.p0_conversion[0] = tree.v_pho_conversion[nPhos_id[r]]
          treeSkimmer.p0_full5x5_r9[0] = tree.v_pho_full5x5_r9[nPhos_id[r]]
          treeSkimmer.p0_r9[0] = tree.v_pho_r9[nPhos_id[r]]
          treeSkimmer.p0_full5x5_sigmaetaeta[0] = tree.v_pho_full5x5_sigmaIetaIeta[nPhos_id[r]]
          treeSkimmer.p0_sigmaetaeta[0] = tree.v_pho_sigmaIetaIeta[nPhos_id[r]]
          treeSkimmer.p0_genmatchpt[0] = tree.v_genmatch_pt[nPhos_id[r]]
          treeSkimmer.p0_e5x5[0] = tree.v_pho_e5x5[nPhos_id[r]]
          treeSkimmer.p0_fulle5x5[0] = tree.v_pho_full5x5_e5x5[nPhos_id[r]]
          treeSkimmer.p0_passTrigger[0] = tree.passTrigger
          treeSkimmer.p0_passpresel[0] = tree.passpresel


          if tree.v_genmatch_pt[nPhos_id[r]] > 0:
             fatphocount_revised.append(1)
          if tree.v_genmatch_pt[nPhos_id[r]] < 0:
             resolvedcount.append(1)
          if tree.v_genmatch_pt[nPhos_id[r]] > 0:
             mergedcount.append(1)
          if abs(Phos[r].Eta()) > 2.5:
             outofetacount.append(1)

      treeSkimmer.p0_resolvedcount_revised[0] = len(resolvedcount_revised)
      treeSkimmer.p0_resolvedcount[0] = len(resolvedcount)
      treeSkimmer.p0_mergedcount[0] = len(mergedcount)
      treeSkimmer.p0_outofetacount[0] = len(outofetacount)


      if len(nPhos) == 2:
          if nPhos[0].Pt() < 30 or abs(Phos[0].Eta()) > 2.5:
              pho1out.append(1)
          if nPhos[1].Pt() < 18 or abs(Phos[1].Eta()) > 2.5:
              pho2out.append(1)

      elif len(nPhos) == 3:
          if nPhos[0].Pt() < 30 or abs(Phos[0].Eta()) > 2.5:
              pho1out.append(1)
          if nPhos[1].Pt() < 18 or abs(Phos[1].Eta()) > 2.5:
              pho2out.append(1)
          if nPhos[2].Pt() < 10 or abs(Phos[2].Eta()) > 2.5:
              pho3out.append(1)

      elif len(nPhos) > 3:
          if nPhos[0].Pt() < 30 or abs(Phos[0].Eta()) > 2.5:
              pho1out.append(1)
          if nPhos[1].Pt() < 18 or abs(Phos[1].Eta()) > 2.5:
             pho2out.append(1)
          if nPhos[2].Pt() < 10 or abs(Phos[2].Eta()) > 2.5:
             pho3out.append(1)
          if nPhos[3].Pt() < 10 or abs(Phos[3].Eta()) > 2.5:
             pho4out.append(1)


      treeSkimmer.p0_Pho1out[0] = len(pho1out)
      treeSkimmer.p0_Pho2out[0] = len(pho2out)
      treeSkimmer.p0_Pho3out[0] = len(pho3out)
      treeSkimmer.p0_Pho4out[0] = len(pho4out)
      outTree_0.Fill()

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


      if tree.passpresel != 1: continue  ## only continue with pre-selected diphotons
    #   triggeredDipho = treeSkimmer.MakeTriggerSelection(sPhos, sPhos_id)
      #
    #   if triggeredDipho == 0: continue
    #   treeSkimmer.p_npho[0] = len(sPhos)
    #   listdr = []
    #   for m in range(0, len(sPhos)):
      #
    #       treeSkimmer.p_pt[0] =  sPhos[m].Pt()
    #       treeSkimmer.p_M[0] = sPhos[m].M()
    #       treeSkimmer.p_eta[0] = sPhos[m].Eta()
    #       treeSkimmer.p_phi[0] = sPhos[m].Phi()
    #       treeSkimmer.p_mva[0] = tree.v_pho_mva[sPhos_id[m]]
    #       treeSkimmer.p_r9[0] = tree.v_pho_r9[sPhos_id[m]]
    #       treeSkimmer.p_full5x5_r9[0] = tree.v_pho_full5x5_r9[sPhos_id[m]]
    #       treeSkimmer.p_sigmaEtaEta[0] = tree.v_pho_sigmaEtaEta[sPhos_id[m]]
    #       treeSkimmer.p_full5x5_sigmaEtaEta[0] = tree.v_pho_full5x5_sigmaEtaEta[sPhos_id[m]]
    #       treeSkimmer.p_full5x5_sigmaIetaIeta[0] = tree.v_pho_full5x5_sigmaIetaIeta[sPhos_id[m]]
    #       treeSkimmer.p_sigmaIphiIphi[0] = tree.v_pho_sigmaIphiIphi[sPhos_id[m]]
    #       treeSkimmer.p_genmatch[0] = tree.v_pho_genmatch[sPhos_id[m]]
    #       treeSkimmer.p_hadronicOverEm[0] = tree.v_pho_hadronicOverEm[sPhos_id[m]]
    #       treeSkimmer.p_matchpho_pt[0] = tree.v_genmatch_pt[sPhos_id[m]]
    #       treeSkimmer.p_conversion[0] = tree.v_pho_conversion[sPhos_id[m]]
    #       treeSkimmer.p_match[0] = tree.v_matchflag[sPhos_id[m]]
    #       treeSkimmer.p_e5x5[0] = tree.v_pho_e5x5[sPhos_id[m]]
    #       treeSkimmer.p_fulle5x5[0] = tree.v_pho_full5x5_e5x5[sPhos_id[m]]
    #       treeSkimmer.p_passTrigger[0] = tree.passTrigger
      #
    #       for n in range(0, len(sPhos)):
    #           if (n!=m and n>m):
    #              dr = sPhos[m].DeltaR(sPhos[n])
    #              listdr.append(dr)
    #   treeSkimmer.p_drmin[0] = min(listdr)
    #   treeSkimmer.p_drmax[0] = max(listdr)
      #
    #   outTree_all.Fill()

# Split into 3 categories here
      if len(sPhos) == 3:
         nicematch = []
         match = 0
         for g in range(0,tree.v_genmatch_pt.size()):
             if tree.v_genmatch_pt[g] > 0:
                match = 1
                nicematch.append(1)

         if nicematch.count(1) == 0:
            n_genmatch = 0
         elif nicematch.count(1) == 1 :
            n_genmatch = 1
         elif nicematch.count(1) == 2:
            n_genmatch = 2
         elif nicematch.count(1) ==3 :
            n_genmatch = 3
         elif nicematch.count(1) == 4:
            n_genmatch = 4
         elif nicematch.count(1) > 4:
            n_genmatch = 5

         treeSkimmer.genmatch_cat[0] = n_genmatch
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
         treeSkimmer.p1_e5x5_3[0] = tree.v_pho_e5x5[sPhos_id[0]]
         treeSkimmer.p2_e5x5_3[0] = tree.v_pho_e5x5[sPhos_id[1]]
         treeSkimmer.p3_e5x5_3[0] = tree.v_pho_e5x5[sPhos_id[2]]
         treeSkimmer.p1_fulle5x5_3[0] = tree.v_pho_full5x5_e5x5[sPhos_id[0]]
         treeSkimmer.p2_fulle5x5_3[0] = tree.v_pho_full5x5_e5x5[sPhos_id[1]]
         treeSkimmer.p3_fulle5x5_3[0] = tree.v_pho_full5x5_e5x5[sPhos_id[2]]

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

         treeSkimmer.p1_matchpho_pt_3[0] = tree.v_genmatch_pt[sPhos_id[0]]
         treeSkimmer.p2_matchpho_pt_3[0] = tree.v_genmatch_pt[sPhos_id[1]]
         treeSkimmer.p3_matchpho_pt_3[0] = tree.v_genmatch_pt[sPhos_id[2]]

         treeSkimmer.p1_conversion_3[0] = tree.v_pho_conversion[sPhos_id[0]]
         treeSkimmer.p2_conversion_3[0] = tree.v_pho_conversion[sPhos_id[1]]
         treeSkimmer.p3_conversion_3[0] = tree.v_pho_conversion[sPhos_id[2]]

         treeSkimmer.p1_hadronicOverEm_3[0] = tree.v_pho_hadronicOverEm[sPhos_id[0]]
         treeSkimmer.p2_hadronicOverEm_3[0] = tree.v_pho_hadronicOverEm[sPhos_id[1]]
         treeSkimmer.p3_hadronicOverEm_3[0] = tree.v_pho_hadronicOverEm[sPhos_id[2]]

         treeSkimmer.p1_match_3[0] = tree.v_matchflag[sPhos_id[0]]
         treeSkimmer.p2_match_3[0] = tree.v_matchflag[sPhos_id[1]]
         treeSkimmer.p3_match_3[0] = tree.v_matchflag[sPhos_id[2]]

         treeSkimmer.genTotalWeight_3[0] = tree.genTotalWeight

         treeSkimmer.p_mindr_3[0] = min(sPhos[0].DeltaR(sPhos[1]), sPhos[0].DeltaR(sPhos[2]), sPhos[1].DeltaR(sPhos[2]))
         treeSkimmer.p_maxdr_3[0] = max(sPhos[0].DeltaR(sPhos[1]), sPhos[0].DeltaR(sPhos[2]), sPhos[1].DeltaR(sPhos[2]))
         P12 = sPhos[0] + sPhos[1]
         P13 = sPhos[0] + sPhos[2]
         P23 = sPhos[1] + sPhos[2]


         treeSkimmer.dphigh_mass_3[0] = P12.M()
         treeSkimmer.p_maxmass_3[0] = max(P12.M(),P13.M(),P23.M())



         Pgggg = sPhos[0] + sPhos[1] + sPhos[2]
         treeSkimmer.tp_pt_3[0] = Pgggg.Pt()
         treeSkimmer.tp_eta_3[0] = Pgggg.Eta()
         treeSkimmer.tp_phi_3[0] = Pgggg.Phi()
         treeSkimmer.tp_mass_3[0] = Pgggg.M()
         outTree_3.Fill()

      elif len(sPhos) == 2:
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

         treeSkimmer.p1_hadronicOverEm_2[0] = tree.v_pho_hadronicOverEm[sPhos_id[0]]
         treeSkimmer.p2_hadronicOverEm_2[0] = tree.v_pho_hadronicOverEm[sPhos_id[1]]

         treeSkimmer.p1_match_2[0] = tree.v_matchflag[sPhos_id[0]]
         treeSkimmer.p2_match_2[0] = tree.v_matchflag[sPhos_id[1]]

         treeSkimmer.p1_matchpho_pt_2[0] = tree.v_genmatch_pt[sPhos_id[0]]
         treeSkimmer.p2_matchpho_pt_2[0] = tree.v_genmatch_pt[sPhos_id[1]]

         treeSkimmer.p1_conversion_2[0] = tree.v_pho_conversion[sPhos_id[0]]
         treeSkimmer.p2_conversion_2[0] = tree.v_pho_conversion[sPhos_id[1]]

         treeSkimmer.p1_e5x5_2[0] = tree.v_pho_e5x5[sPhos_id[0]]
         treeSkimmer.p2_e5x5_2[0] = tree.v_pho_e5x5[sPhos_id[1]]
         treeSkimmer.p1_fulle5x5_2[0] = tree.v_pho_full5x5_e5x5[sPhos_id[0]]
         treeSkimmer.p2_fulle5x5_2[0] = tree.v_pho_full5x5_e5x5[sPhos_id[1]]

         treeSkimmer.p_mindr_2[0] = sPhos[0].DeltaR(sPhos[1])

         treeSkimmer.genTotalWeight_2[0] = tree.genTotalWeight

         Pgggg = sPhos[0] + sPhos[1]
         treeSkimmer.tp_pt_2[0] = Pgggg.Pt()
         treeSkimmer.tp_eta_2[0] = Pgggg.Eta()
         treeSkimmer.tp_phi_2[0] = Pgggg.Phi()
         treeSkimmer.tp_mass_2[0] = Pgggg.M()

         outTree_2.Fill()

      elif len(sPhos) >3: #ntotpho, i.e total number of photons should always be =4
          mvalist = []

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

          treeSkimmer.p1_matchpho_pt[0] = tree.v_genmatch_pt[sPhos_id[0]]
          treeSkimmer.p2_matchpho_pt[0] = tree.v_genmatch_pt[sPhos_id[1]]
          treeSkimmer.p3_matchpho_pt[0] = tree.v_genmatch_pt[sPhos_id[2]]
          treeSkimmer.p4_matchpho_pt[0] = tree.v_genmatch_pt[sPhos_id[3]]

          mvalist.append(tree.v_pho_mva[sPhos_id[0]])
          mvalist.append(tree.v_pho_mva[sPhos_id[1]])
          mvalist.append(tree.v_pho_mva[sPhos_id[2]])
          mvalist.append(tree.v_pho_mva[sPhos_id[3]])
          mvalist.sort()
          treeSkimmer.mva_max1[0] = mvalist[3]
          treeSkimmer.mva_max2[0] = mvalist[2]
          treeSkimmer.mva_max3[0] = mvalist[1]
          treeSkimmer.mva_max4[0] = mvalist[0]
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

          treeSkimmer.p1_hadronicOverEm[0] = tree.v_pho_hadronicOverEm[sPhos_id[0]]
          treeSkimmer.p2_hadronicOverEm[0] = tree.v_pho_hadronicOverEm[sPhos_id[1]]
          treeSkimmer.p3_hadronicOverEm[0] = tree.v_pho_hadronicOverEm[sPhos_id[2]]
          treeSkimmer.p4_hadronicOverEm[0] = tree.v_pho_hadronicOverEm[sPhos_id[3]]

          treeSkimmer.p1_genmatch[0] = tree.v_pho_genmatch[sPhos_id[0]]
          treeSkimmer.p2_genmatch[0] = tree.v_pho_genmatch[sPhos_id[1]]
          treeSkimmer.p3_genmatch[0] = tree.v_pho_genmatch[sPhos_id[2]]
          treeSkimmer.p4_genmatch[0] = tree.v_pho_genmatch[sPhos_id[3]]

          treeSkimmer.p1_match[0] = tree.v_matchflag[sPhos_id[0]]
          treeSkimmer.p2_match[0] = tree.v_matchflag[sPhos_id[1]]
          treeSkimmer.p3_match[0] = tree.v_matchflag[sPhos_id[2]]
          treeSkimmer.p4_match[0] = tree.v_matchflag[sPhos_id[3]]

          treeSkimmer.p1_conversion[0] = tree.v_pho_conversion[sPhos_id[0]]
          treeSkimmer.p2_conversion[0] = tree.v_pho_conversion[sPhos_id[1]]
          treeSkimmer.p3_conversion[0] = tree.v_pho_conversion[sPhos_id[2]]
          treeSkimmer.p4_conversion[0] = tree.v_pho_conversion[sPhos_id[3]]

          treeSkimmer.p1_e5x5[0] = tree.v_pho_e5x5[sPhos_id[0]]
          treeSkimmer.p2_e5x5[0] = tree.v_pho_e5x5[sPhos_id[1]]
          treeSkimmer.p3_e5x5[0] = tree.v_pho_e5x5[sPhos_id[2]]
          treeSkimmer.p4_e5x5[0] = tree.v_pho_e5x5[sPhos_id[3]]
          treeSkimmer.p1_fulle5x5[0] = tree.v_pho_full5x5_e5x5[sPhos_id[0]]
          treeSkimmer.p2_fulle5x5[0] = tree.v_pho_full5x5_e5x5[sPhos_id[1]]
          treeSkimmer.p3_fulle5x5[0] = tree.v_pho_full5x5_e5x5[sPhos_id[2]]
          treeSkimmer.p4_fulle5x5[0] = tree.v_pho_full5x5_e5x5[sPhos_id[3]]

          treeSkimmer.genTotalWeight[0] = tree.genTotalWeight

          treeSkimmer.p1_passTrigger[0] = tree.passTrigger

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

          ## Cos theta angles
          Boosted_a1 = TLorentzVector(0,0,0,0)
          Boosted_a1.SetPtEtaPhiE(PP1.Pt(),PP1.Eta(),PP1.Phi(),PP1.E())
          Boosted_a2 = TLorentzVector(0,0,0,0)
          Boosted_a2.SetPtEtaPhiE(PP2.Pt(),PP2.Eta(),PP2.Phi(),PP2.E())
          h_forboost = TLorentzVector(0,0,0,0)
          h_forboost.SetPtEtaPhiE(Pgggg.Pt(),Pgggg.Eta(),Pgggg.Phi(),Pgggg.E())
          treeSkimmer.CosTheta_h_a1[0] = treeSkimmer.HelicityCosTheta(h_forboost,Boosted_a1) ## Cos theta b/w a1 and higgs(rest)
          treeSkimmer.CosTheta_h_a2[0] = treeSkimmer.HelicityCosTheta(h_forboost,Boosted_a2) ## Cos theta b/w a2 and higgs(rest)

          Boosted_gamma1 = TLorentzVector(0,0,0,0)
          Boosted_gamma1.SetPtEtaPhiE(pairedDiphos[0][1].Pt(),pairedDiphos[0][1].Eta(),pairedDiphos[0][1].Phi(),pairedDiphos[0][1].E())
          Boosted_gamma2 = TLorentzVector(0,0,0,0)
          Boosted_gamma2.SetPtEtaPhiE(pairedDiphos[0][3].Pt(),pairedDiphos[0][3].Eta(),pairedDiphos[0][3].Phi(),pairedDiphos[0][3].E())
          Boosted_gamma3 = TLorentzVector(0,0,0,0)
          Boosted_gamma3.SetPtEtaPhiE(pairedDiphos[1][1].Pt(),pairedDiphos[1][1].Eta(),pairedDiphos[1][1].Phi(),pairedDiphos[1][1].E())
          Boosted_gamma4 = TLorentzVector(0,0,0,0)
          Boosted_gamma4.SetPtEtaPhiE(pairedDiphos[1][3].Pt(),pairedDiphos[1][3].Eta(),pairedDiphos[1][3].Phi(),pairedDiphos[1][3].E())
          treeSkimmer.CosTheta_a1_gamma1[0] = treeSkimmer.HelicityCosTheta(Boosted_a1,Boosted_gamma1) ## Cos theta b/w gamma1 and a1(rest)
          treeSkimmer.CosTheta_a1_gamma2[0] = treeSkimmer.HelicityCosTheta(Boosted_a1,Boosted_gamma2) ## Cos theta b/w gamma2 and a1(rest)
          treeSkimmer.CosTheta_a2_gamma3[0] = treeSkimmer.HelicityCosTheta(Boosted_a2,Boosted_gamma3) ## Cos theta b/w gamma3 and a2(rest)
          treeSkimmer.CosTheta_a2_gamma4[0] = treeSkimmer.HelicityCosTheta(Boosted_a2,Boosted_gamma4) ## Cos theta b/w gamma4 and a2(rest)
          treeSkimmer.CosTheta_a1_a2[0] = treeSkimmer.HelicityCosTheta(Boosted_a1,Boosted_a2) ## Cos theta b/w a2 and a1(rest)
          treeSkimmer.CosTheta_a2_a1[0] = treeSkimmer.HelicityCosTheta(Boosted_a2,Boosted_a1) ## Cos theta b/w a1 and a2(rest)

          ## Defining a1 and a2 direction
          BoostedHiggs = TVector3(-Pgggg.BoostVector())
          PP1.Boost(BoostedHiggs)
          PP2.Boost(BoostedHiggs)
          PP1_vect = PP1.Vect().Unit()
          PP2_vect = PP2.Vect().Unit()

          Photons= []
          Photons.append(sPhos[0])
          Photons.append(sPhos[1])
          Photons.append(sPhos[2])
          Photons.append(sPhos[3])

          ## Calculate normal to a1 and a2 decay plane
          NormVect = treeSkimmer.norm_planes(Photons,Pgggg)

          ## Calculate phi
          if (abs(PP1_vect.Dot(NormVect[1].Cross(NormVect[0])))) !=0:
             dsign_a1 = PP1_vect.Dot(NormVect[1].Cross(NormVect[0]))/(abs(PP1_vect.Dot(NormVect[1].Cross(NormVect[0]))))
          if (abs(PP2_vect.Dot(NormVect[1].Cross(NormVect[0])))) !=0:
             dsign_a2 = PP2_vect.Dot(NormVect[1].Cross(NormVect[0]))/(abs(PP2_vect.Dot(NormVect[1].Cross(NormVect[0]))))
          if (-1 <= NormVect[0].Dot(NormVect[1]) <= 1):
              treeSkimmer.Phi_a1[0] = dsign_a1*(-1)*m.acos((NormVect[0].Dot(NormVect[1])))
              treeSkimmer.Phi_a2[0] = dsign_a2*(-1)*m.acos((NormVect[0].Dot(NormVect[1])))

          ## Define z direction
          p1 = TLorentzVector(0,0,6500,6500)
          z_vect = TVector3(p1.Vect().Unit())
          ## Calculate the normal of the two diphotons
          zzprime_a1 = TVector3(z_vect.Cross(PP1_vect).Unit())
          zzprime_a2 = TVector3(z_vect.Cross(PP2_vect).Unit())

          ## Calculate Phi1
          if (abs(PP1_vect.Dot(zzprime_a1.Cross(NormVect[0])))) !=0:
             dsignprime_a1 = PP1_vect.Dot(zzprime_a1.Cross(NormVect[0]))/(abs(PP1_vect.Dot(zzprime_a1.Cross(NormVect[0]))))
             treeSkimmer.Phi1_a1[0] = dsignprime_a1*m.acos(zzprime_a1.Dot(NormVect[0]))

          ## Calculate Cos Theta star in the Collins Soper frame
          vec1 = TLorentzVector(0,0,0,0)
          vec2 = TLorentzVector(0,0,0,0)
          vec1.SetPxPyPzE(0,0,6500,6500)
          vec1.SetPxPyPzE(0,0,-6500,6500)
          vec1.Boost(BoostedHiggs)
          vec2.Boost(BoostedHiggs)
          PP1.Boost(BoostedHiggs)
          PP2.Boost(BoostedHiggs)

          CSaxis = TVector3(vec1.Vect().Unit() - vec2.Vect().Unit())
          CSaxis.Unit()

          treeSkimmer.CosThetaStar_CS = m.cos(CSaxis.Angle( PP1.Vect().Unit()))



          outTree.Fill()

      evtCounter += 1

   #end of event loop!

   outRoot.cd()
   outTree_0.Write()
   outTree_all.Write()
   outTree.Write()
   outTree_3.Write()
   outTree_2.Write()
   outRoot.Close()

   #outTree_3.Write()
        #   print dsign_a1
        #   print dsign_a2

if __name__ == "__main__":
   main(sys.argv[1:])

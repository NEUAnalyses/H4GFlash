from ROOT import *
import numpy as n

DEBUG = 0

class SkimmedTreeTools:
   def __init__(self):
      self.p_pt = n.zeros(1, dtype=float)
      self.p_M = n.zeros(1, dtype=float)
      self.p_eta = n.zeros(1, dtype=float)
      self.p_phi = n.zeros(1, dtype=float)
      self.p_mva = n.zeros(1, dtype=float)
      self.p_r9 = n.zeros(1, dtype=float)
      self.p_full5x5_r9 = n.zeros(1, dtype=float)
      self.p_sigmaEtaEta = n.zeros(1, dtype=float)
      self.p_full5x5_sigmaEtaEta = n.zeros(1, dtype=float)
      self.p_full5x5_sigmaIetaIeta = n.zeros(1, dtype=float)
      self.p_sigmaIphiIphi = n.zeros(1, dtype=float)
      self.p_genmatch = n.zeros(1, dtype=float)
      self.p_drmin = n.zeros(1, dtype=float)
      self.p_drmax = n.zeros(1, dtype=float)
      self.p_npho = n.zeros(1, dtype=float)      
      self.p_match = n.zeros(1, dtype=float)
      self.p_hadronicOverEm = n.zeros(1, dtype=float)
      self.p_passTrigger = n.zeros(1, dtype=float)

      self.p1_pt = n.zeros(1, dtype=float)
      self.p2_pt = n.zeros(1, dtype=float)
      self.p3_pt = n.zeros(1, dtype=float)
      self.p4_pt = n.zeros(1, dtype=float)
      self.p1_M = n.zeros(1, dtype=float)
      self.p2_M = n.zeros(1, dtype=float)
      self.p3_M = n.zeros(1, dtype=float)
      self.p4_M = n.zeros(1, dtype=float)
      self.p1_eta = n.zeros(1, dtype=float)
      self.p2_eta = n.zeros(1, dtype=float)
      self.p3_eta = n.zeros(1, dtype=float)
      self.p4_eta = n.zeros(1, dtype=float)
      self.p1_phi = n.zeros(1, dtype=float)
      self.p2_phi = n.zeros(1, dtype=float)
      self.p3_phi = n.zeros(1, dtype=float)
      self.p4_phi = n.zeros(1, dtype=float)
      self.p1_mva = n.zeros(1, dtype=float)
      self.p2_mva = n.zeros(1, dtype=float)
      self.p3_mva = n.zeros(1, dtype=float)
      self.p4_mva = n.zeros(1, dtype=float)
      self.p1_r9 = n.zeros(1, dtype=float)
      self.p2_r9 = n.zeros(1, dtype=float)
      self.p3_r9 = n.zeros(1, dtype=float)
      self.p4_r9 = n.zeros(1, dtype=float)
      self.p1_full5x5_r9 = n.zeros(1, dtype=float)
      self.p2_full5x5_r9 = n.zeros(1, dtype=float)
      self.p3_full5x5_r9 = n.zeros(1, dtype=float)
      self.p4_full5x5_r9 = n.zeros(1, dtype=float)
      self.p1_full5x5_sigmaIetaIeta = n.zeros(1, dtype=float)
      self.p2_full5x5_sigmaIetaIeta = n.zeros(1, dtype=float)
      self.p3_full5x5_sigmaIetaIeta = n.zeros(1, dtype=float)
      self.p4_full5x5_sigmaIetaIeta = n.zeros(1, dtype=float)
      self.p1_sigmaIphiIphi = n.zeros(1, dtype=float)
      self.p2_sigmaIphiIphi = n.zeros(1, dtype=float)
      self.p3_sigmaIphiIphi = n.zeros(1, dtype=float)
      self.p4_sigmaIphiIphi = n.zeros(1, dtype=float)
      self.p1_sigmaEtaEta = n.zeros(1, dtype=float)
      self.p2_sigmaEtaEta = n.zeros(1, dtype=float)
      self.p3_sigmaEtaEta = n.zeros(1, dtype=float)
      self.p4_sigmaEtaEta = n.zeros(1, dtype=float)
      self.p1_full5x5_sigmaEtaEta = n.zeros(1, dtype=float)
      self.p2_full5x5_sigmaEtaEta = n.zeros(1, dtype=float)
      self.p3_full5x5_sigmaEtaEta = n.zeros(1, dtype=float)
      self.p4_full5x5_sigmaEtaEta = n.zeros(1, dtype=float)
      self.p1_genmatch = n.zeros(1, dtype=float)
      self.p2_genmatch = n.zeros(1, dtype=float)
      self.p3_genmatch = n.zeros(1, dtype=float)
      self.p4_genmatch = n.zeros(1, dtype=float)
      self.p1_genmatching = n.zeros(1, dtype=float)
      self.p2_genmatching = n.zeros(1, dtype=float)
      self.p3_genmatching = n.zeros(1, dtype=float)
      self.p4_genmatching = n.zeros(1, dtype=float)
      self.p1_hadronicOverEm = n.zeros(1, dtype=float)
      self.p2_hadronicOverEm = n.zeros(1, dtype=float)
      self.p3_hadronicOverEm = n.zeros(1, dtype=float)
      self.p4_hadronicOverEm = n.zeros(1, dtype=float)
      self.p1_match = n.zeros(1, dtype=float)
      self.p2_match = n.zeros(1, dtype=float)
      self.p3_match = n.zeros(1, dtype=float)
      self.p4_match = n.zeros(1, dtype=float)
      self.p_mindr = n.zeros(1, dtype=float)
      self.p_maxdr = n.zeros(1, dtype=float)
      self.p_maxmass = n.zeros(1, dtype=float)
      self.dp1_pt = n.zeros(1, dtype=float)
      self.dp1_eta = n.zeros(1, dtype=float)
      self.dp1_phi = n.zeros(1, dtype=float)
      self.dp1_mass = n.zeros(1, dtype=float)
      self.dp1_p1i = n.zeros(1, dtype=float)
      self.dp1_p2i = n.zeros(1, dtype=float)
      self.dp2_pt = n.zeros(1, dtype=float)
      self.dp2_eta = n.zeros(1, dtype=float)
      self.dp2_phi = n.zeros(1, dtype=float)
      self.dp2_mass = n.zeros(1, dtype=float)
      self.dp2_p1i = n.zeros(1, dtype=float)
      self.dp2_p2i = n.zeros(1, dtype=float)
      self.dp1_dr = n.zeros(1, dtype=float)
      self.dp2_dr = n.zeros(1, dtype=float)
      self.tp_pt = n.zeros(1, dtype=float)
      self.tp_eta = n.zeros(1, dtype=float)
      self.tp_phi = n.zeros(1, dtype=float)
      self.tp_mass = n.zeros(1, dtype=float)
      self.dphigh_mass = n.zeros(1, dtype=float)
      self.initialEvents = n.zeros(1, dtype=float)
      self.event = n.zeros(1,dtype=int)
      self.run = n.zeros(1,dtype=int)
      self.lumi = n.zeros(1,dtype=int)
      self.nvtx = n.zeros(1,dtype=int)
      self.npu = n.zeros(1,dtype=float)
      self.genTotalWeight = n.zeros(1,dtype=float) 
      self.passTrigger = n.zeros(1, dtype=float)
      self.v_pho_genmatch = n.zeros(1,dtype=float)
      self.v_pho_r9 = n.zeros(1,dtype=float)

      self.p1_pt_3 = n.zeros(1, dtype=float)
      self.p2_pt_3 = n.zeros(1, dtype=float)
      self.p3_pt_3 = n.zeros(1, dtype=float)
      self.p1_M_3 = n.zeros(1, dtype=float)
      self.p2_M_3 = n.zeros(1, dtype=float)
      self.p3_M_3 = n.zeros(1, dtype=float)
      self.p1_eta_3 = n.zeros(1, dtype=float)
      self.p2_eta_3 = n.zeros(1, dtype=float)
      self.p3_eta_3 = n.zeros(1, dtype=float)
      self.p1_phi_3 = n.zeros(1, dtype=float)
      self.p2_phi_3 = n.zeros(1, dtype=float)
      self.p3_phi_3 = n.zeros(1, dtype=float)
      self.p1_mva_3 = n.zeros(1, dtype=float)
      self.p2_mva_3 = n.zeros(1, dtype=float)
      self.p3_mva_3 = n.zeros(1, dtype=float)
      self.p1_r9_3 = n.zeros(1, dtype=float)
      self.p2_r9_3 = n.zeros(1, dtype=float)
      self.p3_r9_3 = n.zeros(1, dtype=float)
      self.p1_full5x5_r9_3 = n.zeros(1, dtype=float)
      self.p2_full5x5_r9_3 = n.zeros(1, dtype=float)
      self.p3_full5x5_r9_3 = n.zeros(1, dtype=float)  
      self.p1_full5x5_sigmaIetaIeta_3 = n.zeros(1, dtype=float)
      self.p2_full5x5_sigmaIetaIeta_3 = n.zeros(1, dtype=float)
      self.p3_full5x5_sigmaIetaIeta_3 = n.zeros(1, dtype=float)
      self.p1_sigmaIphiIphi_3 = n.zeros(1, dtype=float)
      self.p2_sigmaIphiIphi_3 = n.zeros(1, dtype=float)
      self.p3_sigmaIphiIphi_3 = n.zeros(1, dtype=float)
      self.p1_sigmaEtaEta_3 = n.zeros(1, dtype=float)
      self.p2_sigmaEtaEta_3 = n.zeros(1, dtype=float)
      self.p3_sigmaEtaEta_3 = n.zeros(1, dtype=float)  
      self.p1_full5x5_sigmaEtaEta_3 = n.zeros(1, dtype=float)
      self.p2_full5x5_sigmaEtaEta_3 = n.zeros(1, dtype=float)
      self.p3_full5x5_sigmaEtaEta_3 = n.zeros(1, dtype=float)
      self.p1_genmatch_3 = n.zeros(1, dtype=float)
      self.p2_genmatch_3 = n.zeros(1, dtype=float)
      self.p3_genmatch_3 = n.zeros(1, dtype=float) 
      self.p1_match_3 = n.zeros(1, dtype=float)
      self.p2_match_3 = n.zeros(1, dtype=float)
      self.p3_match_3 = n.zeros(1, dtype=float)
      self.p1_hadronicOverEm_3 = n.zeros(1, dtype=float)
      self.p2_hadronicOverEm_3 = n.zeros(1, dtype=float)
      self.p3_hadronicOverEm_3 = n.zeros(1, dtype=float)
      self.p_mindr_3 = n.zeros(1, dtype=float)
      self.p_maxdr_3 = n.zeros(1, dtype=float)
      self.dphigh_mass_3 = n.zeros(1, dtype=float)
      self.p_maxmass_3 = n.zeros(1, dtype=float)
      self.dp1_dr_3 = n.zeros(1, dtype=float)
      self.dp1_pt_3 = n.zeros(1, dtype=float)
      self.dp1_eta_3 = n.zeros(1, dtype=float)
      self.dp1_phi_3 = n.zeros(1, dtype=float)
      self.dp1_mass_3 = n.zeros(1, dtype=float)
      self.tp_pt_3 = n.zeros(1,dtype=float) 
      self.tp_eta_3 = n.zeros(1,dtype=float)
      self.tp_phi_3 = n.zeros(1,dtype=float)
      self.tp_mass_3 = n.zeros(1,dtype=float)
      self.nicematch = n.zeros(1,dtype=float)
      self.genmatch_cat = n.zeros(1,dtype=float)

      self.p1_pt_2 = n.zeros(1, dtype=float)
      self.p2_pt_2 = n.zeros(1, dtype=float)
      self.p1_M_2 = n.zeros(1, dtype=float)
      self.p2_M_2 = n.zeros(1, dtype=float)
      self.p1_eta_2 = n.zeros(1, dtype=float)
      self.p2_eta_2 = n.zeros(1, dtype=float)
      self.p1_phi_2 = n.zeros(1, dtype=float)
      self.p2_phi_2 = n.zeros(1, dtype=float)
      self.p1_mva_2 = n.zeros(1, dtype=float)
      self.p2_mva_2 = n.zeros(1, dtype=float)
      self.p1_r9_2 = n.zeros(1, dtype=float)
      self.p2_r9_2 = n.zeros(1, dtype=float)
      self.p1_full5x5_r9_2 = n.zeros(1, dtype=float)
      self.p2_full5x5_r9_2 = n.zeros(1, dtype=float)
      self.p1_full5x5_sigmaIetaIeta_2 = n.zeros(1, dtype=float)
      self.p2_full5x5_sigmaIetaIeta_2 = n.zeros(1, dtype=float)
      self.p1_sigmaIphiIphi_2 = n.zeros(1, dtype=float)
      self.p2_sigmaIphiIphi_2 = n.zeros(1, dtype=float)
      self.p1_sigmaEtaEta_2 = n.zeros(1, dtype=float)
      self.p2_sigmaEtaEta_2 = n.zeros(1, dtype=float)
      self.p1_full5x5_sigmaEtaEta_2 = n.zeros(1, dtype=float)
      self.p2_full5x5_sigmaEtaEta_2 = n.zeros(1, dtype=float)
      self.p1_genmatch_2 = n.zeros(1, dtype=float)
      self.p2_genmatch_2 = n.zeros(1, dtype=float)
      self.p1_match_2 = n.zeros(1, dtype=float)
      self.p2_match_2 = n.zeros(1, dtype=float)
      self.p1_hadronicOverEm_2 = n.zeros(1, dtype=float)
      self.p2_hadronicOverEm_2 = n.zeros(1, dtype=float)
      self.p_mindr_2 = n.zeros(1,dtype=float)
      self.tp_pt_2 = n.zeros(1,dtype=float)
      self.tp_eta_2 = n.zeros(1,dtype=float)
      self.tp_phi_2 = n.zeros(1,dtype=float)
      self.tp_mass_2 = n.zeros(1,dtype=float)


   def MakeSkimmedTree_all(self):
       outTree_all = TTree("H4GSel_all", "H4G Selected Events:all events ")
       SetOwnership(outTree_all,0)
       outTree_all.Branch('p_pt', self.p_pt, 'p_pt/D')
       outTree_all.Branch('p_M', self.p_M, 'p_M/D')
       outTree_all.Branch('p_eta', self.p_eta, 'p_eta/D')
       outTree_all.Branch('p_phi', self.p_phi, 'p_phi/D')
       outTree_all.Branch('p_mva', self.p_mva, 'p_mva/D')
       outTree_all.Branch('p_r9', self.p_r9, 'p_r9/D')
       outTree_all.Branch('p_full5x5_r9', self.p_full5x5_r9, 'p_full5x5_r9/D')
       outTree_all.Branch('p_sigmaEtaEta', self.p_sigmaEtaEta, 'p_sigmaEtaEta/D')
       outTree_all.Branch('p_full5x5_sigmaEtaEta', self.p_full5x5_sigmaEtaEta, 'p_full5x5_sigmaEtaEta/D')
       outTree_all.Branch('p_full5x5_sigmaIetaIeta', self.p_full5x5_sigmaIetaIeta, 'p_full5x5_sigmaIetaIeta/D')
       outTree_all.Branch('p_sigmaIphiIphi', self.p_sigmaIphiIphi, 'p_sigmaIphiIphi/D')
       outTree_all.Branch('p_genmatch', self.p_genmatch, 'p_genmatch/D')
       outTree_all.Branch('p_match', self.p_match, 'p_match/D')
       outTree_all.Branch('p_drmin', self.p_drmin, 'p_drmin/D')
       outTree_all.Branch('p_drmax', self.p_drmax, 'p_drmax/D')
       outTree_all.Branch('p_npho', self.p_npho, 'p_npho/D')
       outTree_all.Branch('p_hadronicOverEm',self.p_hadronicOverEm,'p_hadronicOverEm/D')
       outTree_all.Branch('p_passTrigger',self.p_passTrigger,'p_passTrigger/D')
       return outTree_all

   def MakeSkimmedTree(self):
      outTree = TTree("H4GSel", "H4G Selected Events")
      SetOwnership(outTree,0)

      outTree.Branch('p1_pt', self.p1_pt, 'p1_pt/D')
      outTree.Branch('p2_pt', self.p2_pt, 'p2_pt/D')
      outTree.Branch('p3_pt', self.p3_pt, 'p3_pt/D')
      outTree.Branch('p4_pt', self.p4_pt, 'p4_pt/D')
      outTree.Branch('p1_M', self.p1_M, 'p1_M/D')
      outTree.Branch('p2_M', self.p2_M, 'p2_M/D')
      outTree.Branch('p3_M', self.p3_M, 'p3_M/D')
      outTree.Branch('p4_M', self.p4_M, 'p4_M/D')
      outTree.Branch('p1_eta', self.p1_eta, 'p1_eta/D')
      outTree.Branch('p2_eta', self.p2_eta, 'p2_eta/D')
      outTree.Branch('p3_eta', self.p3_eta, 'p3_eta/D')
      outTree.Branch('p4_eta', self.p4_eta, 'p4_eta/D')
      outTree.Branch('p1_phi', self.p1_phi, 'p1_phi/D')
      outTree.Branch('p2_phi', self.p2_phi, 'p2_phi/D')
      outTree.Branch('p3_phi', self.p3_phi, 'p3_phi/D')
      outTree.Branch('p4_phi', self.p4_phi, 'p4_phi/D')
      outTree.Branch('p1_mva', self.p1_mva, 'p1_mva/D')
      outTree.Branch('p2_mva', self.p2_mva, 'p2_mva/D')
      outTree.Branch('p3_mva', self.p3_mva, 'p3_mva/D')
      outTree.Branch('p4_mva', self.p4_mva, 'p4_mva/D')
      outTree.Branch('p1_r9', self.p1_r9, 'p1_r9/D')
      outTree.Branch('p2_r9', self.p2_r9, 'p2_r9/D')
      outTree.Branch('p3_r9', self.p3_r9, 'p2_r9/D')
      outTree.Branch('p4_r9', self.p4_r9, 'p4_r9/D')
      outTree.Branch('p1_full5x5_r9', self.p1_full5x5_r9, 'p1_full5x5_r9/D')
      outTree.Branch('p2_full5x5_r9', self.p2_full5x5_r9, 'p2_full5x5_r9/D')
      outTree.Branch('p3_full5x5_r9', self.p3_full5x5_r9, 'p3_full5x5_r9/D')
      outTree.Branch('p4_full5x5_r9', self.p4_full5x5_r9, 'p4_full5x5_r9/D')
      outTree.Branch('p1_sigmaEtaEta',self.p1_sigmaEtaEta, 'p1_sigmaEtaEta/D')
      outTree.Branch('p2_sigmaEtaEta',self.p2_sigmaEtaEta, 'p2_sigmaEtaEta/D') 
      outTree.Branch('p3_sigmaEtaEta',self.p3_sigmaEtaEta, 'p3_sigmaEtaEta/D') 
      outTree.Branch('p4_sigmaEtaEta',self.p4_sigmaEtaEta, 'p4_sigmaEtaEta/D')    
      outTree.Branch('p1_full5x5_sigmaEtaEta',self.p1_full5x5_sigmaEtaEta, 'p1_full5x5_sigmaEtaEta/D')
      outTree.Branch('p2_full5x5_sigmaEtaEta',self.p2_full5x5_sigmaEtaEta, 'p2_full5x5_sigmaEtaEta/D')
      outTree.Branch('p3_full5x5_sigmaEtaEta',self.p3_full5x5_sigmaEtaEta, 'p3_full5x5_sigmaEtaEta/D')
      outTree.Branch('p4_full5x5_sigmaEtaEta',self.p4_full5x5_sigmaEtaEta, 'p4_full5x5_sigmaEtaEta/D')
      outTree.Branch('p1_full5x5_sigmaIetaIeta',self.p1_full5x5_sigmaIetaIeta, 'p1_full5x5_sigmaIetaIeta/D')
      outTree.Branch('p2_full5x5_sigmaIetaIeta',self.p2_full5x5_sigmaIetaIeta, 'p2_full5x5_sigmaIetaIeta/D')
      outTree.Branch('p3_full5x5_sigmaIetaIeta',self.p3_full5x5_sigmaIetaIeta, 'p3_full5x5_sigmaIetaIeta/D')
      outTree.Branch('p4_full5x5_sigmaIetaIeta',self.p4_full5x5_sigmaIetaIeta, 'p4_full5x5_sigmaIetaIeta/D')
      outTree.Branch('p1_sigmaIphiIphi',self.p1_sigmaIphiIphi,'p1_sigmaIphiIphi/D')
      outTree.Branch('p2_sigmaIphiIphi',self.p2_sigmaIphiIphi,'p2_sigmaIphiIphi/D')
      outTree.Branch('p3_sigmaIphiIphi',self.p3_sigmaIphiIphi,'p3_sigmaIphiIphi/D')
      outTree.Branch('p4_sigmaIphiIphi',self.p4_sigmaIphiIphi,'p4_sigmaIphiIphi/D')
      outTree.Branch('p1_genmatch',self.p1_genmatch, 'p1_genmatch/D')
      outTree.Branch('p2_genmatch',self.p2_genmatch, 'p2_genmatch/D')
      outTree.Branch('p3_genmatch',self.p3_genmatch, 'p3_genmatch/D')
      outTree.Branch('p4_genmatch',self.p4_genmatch, 'p4_genmatch/D')
      outTree.Branch('p1_match',self.p1_match, 'p1_match/D')
      outTree.Branch('p2_match',self.p2_match, 'p2_match/D')
      outTree.Branch('p3_match',self.p3_match, 'p3_match/D')
      outTree.Branch('p4_match',self.p4_match, 'p4_match/D')
      outTree.Branch('p1_hadronicOverEm',self.p1_hadronicOverEm,'p1_hadronicOverEm/D')
      outTree.Branch('p2_hadronicOverEm',self.p2_hadronicOverEm,'p2_hadronicOverEm/D')
      outTree.Branch('p3_hadronicOverEm',self.p3_hadronicOverEm,'p3_hadronicOverEm/D')
      outTree.Branch('p4_hadronicOverEm',self.p4_hadronicOverEm,'p4_hadronicOverEm/D')
      outTree.Branch('p_mindr', self.p_mindr, 'p_mindr/D')
      outTree.Branch('p_maxdr', self.p_maxdr, 'p_maxdr/D')
      outTree.Branch('p_maxmass',self.p_maxmass, 'p_maxmass/D')
      outTree.Branch('dp1_pt', self.dp1_pt, 'dp1_pt/D')
      outTree.Branch('dp1_eta', self.dp1_eta, 'dp1_eta/D')
      outTree.Branch('dp1_phi', self.dp1_phi, 'dp1_phi/D')
      outTree.Branch('dp1_mass', self.dp1_mass, 'dp1_mass/D')
      outTree.Branch('dp1_p1i', self.dp1_p1i, 'dp1_p1i/I')
      outTree.Branch('dp1_p2i', self.dp1_p2i, 'dp1_p2i/I')
      outTree.Branch('dp2_pt', self.dp2_pt, 'dp2_pt/D')
      outTree.Branch('dp2_eta', self.dp2_eta, 'dp2_eta/D')
      outTree.Branch('dp2_phi', self.dp2_phi, 'dp2_phi/D')
      outTree.Branch('dp2_mass', self.dp2_mass, 'dp2_mass/D')
      outTree.Branch('dp2_p1i', self.dp2_p1i, 'dp2_p1i/I')
      outTree.Branch('dp2_p2i', self.dp2_p2i, 'dp2_p2i/I')
      outTree.Branch('dp1_dr', self.dp1_dr, 'dp1_dr/D')
      outTree.Branch('dp2_dr', self.dp2_dr, 'dp2_dr/D')
      outTree.Branch('tp_pt', self.tp_pt, 'tp_pt/D')
      outTree.Branch('tp_eta', self.tp_eta, 'tp_eta/D')
      outTree.Branch('tp_phi', self.tp_phi, 'tp_phi/D')
      outTree.Branch('tp_mass', self.tp_mass, 'tp_mass/D')
      outTree.Branch('dphigh_mass', self.dphigh_mass, 'dphigh_mass/D')
      outTree.Branch('initialEvents', self.initialEvents, 'initialEvents/D')
      outTree.Branch('event', self.event, 'event/I')
      outTree.Branch('run', self.run, 'run/I')
      outTree.Branch('lumi', self.lumi, 'lumi/I')
      outTree.Branch('nvtx', self.nvtx, 'nvtx/I')
      outTree.Branch('npu', self.npu, 'npu/D')
      outTree.Branch('genTotalWeight',self.genTotalWeight, 'genTotalWeight/D')
      outTree.Branch('passTrigger',self.passTrigger, 'passTrigger/D')
      #outTree.Branch('nicematch',self.nicematch,'nicematch/D')
      return outTree

   def MakeSkimmedTree_3(self):
      outTree_3 = TTree("H4GSel_3", "H4G Selected Events:3 gamma")
      SetOwnership(outTree_3,0)  
   
      outTree_3.Branch('p1_pt_3', self.p1_pt_3, 'p1_pt_3/D')
      outTree_3.Branch('p2_pt_3', self.p2_pt_3, 'p2_pt_3/D')
      outTree_3.Branch('p3_pt_3', self.p3_pt_3, 'p3_pt_3/D')
      outTree_3.Branch('p1_M_3', self.p1_M_3, 'p1_M_3/D')
      outTree_3.Branch('p2_M_3', self.p2_M_3, 'p2_M_3/D')
      outTree_3.Branch('p3_M_3', self.p3_M_3, 'p3_M_3/D')
      outTree_3.Branch('p1_eta_3', self.p1_eta_3, 'p1_eta_3/D')
      outTree_3.Branch('p2_eta_3', self.p2_eta_3, 'p2_eta_3/D')
      outTree_3.Branch('p3_eta_3', self.p3_eta_3, 'p3_eta_3/D')
      outTree_3.Branch('p1_phi_3', self.p1_phi_3, 'p1_phi_3/D')
      outTree_3.Branch('p2_phi_3', self.p2_phi_3, 'p2_phi_3/D')
      outTree_3.Branch('p3_phi_3', self.p3_phi_3, 'p3_phi_3/D')
      outTree_3.Branch('p1_mva_3', self.p1_mva_3, 'p1_mva_3/D')
      outTree_3.Branch('p2_mva_3', self.p2_mva_3, 'p2_mva_3/D')
      outTree_3.Branch('p3_mva_3', self.p3_mva_3, 'p3_mva_3/D')
      outTree_3.Branch('p1_r9_3', self.p1_r9_3, 'p1_r9_3/D')
      outTree_3.Branch('p2_r9_3', self.p2_r9_3, 'p2_r9_3/D')
      outTree_3.Branch('p3_r9_3', self.p3_r9_3, 'p3_r9_3/D')
      outTree_3.Branch('p1_genmatch_3',self.p1_genmatch_3, 'p1_genmatch_3/D')
      outTree_3.Branch('p2_genmatch_3',self.p2_genmatch_3, 'p2_genmatch_3/D')
      outTree_3.Branch('p3_genmatch_3',self.p3_genmatch_3, 'p3_genmatch_3/D')
      outTree_3.Branch('p1_match_3',self.p1_match_3, 'p1_match_3/D')
      outTree_3.Branch('p2_match_3',self.p2_match_3, 'p2_match_3/D')
      outTree_3.Branch('p3_match_3',self.p3_match_3, 'p3_match_3/D')
      outTree_3.Branch('p1_full5x5_r9_3',self.p1_full5x5_r9_3, 'p1_full5x5_r9_3/D')
      outTree_3.Branch('p2_full5x5_r9_3',self.p2_full5x5_r9_3, 'p2_full5x5_r9_3/D')
      outTree_3.Branch('p3_full5x5_r9_3',self.p3_full5x5_r9_3, 'p3_full5x5_r9_3/D')
      outTree_3.Branch('p1_full5x5_sigmaIetaIeta_3',self.p1_full5x5_sigmaIetaIeta_3,'p1_full5x5_sigmaIetaIeta_3/D')
      outTree_3.Branch('p2_full5x5_sigmaIetaIeta_3',self.p2_full5x5_sigmaIetaIeta_3,'p2_full5x5_sigmaIetaIeta_3/D')
      outTree_3.Branch('p3_full5x5_sigmaIetaIeta_3',self.p3_full5x5_sigmaIetaIeta_3,'p3_full5x5_sigmaIetaIeta_3/D')
      outTree_3.Branch('p1_sigmaIphiIphi_3',self.p1_sigmaIphiIphi_3,'p1_sigmaIphiIphi_3/D')
      outTree_3.Branch('p2_sigmaIphiIphi_3',self.p2_sigmaIphiIphi_3,'p2_sigmaIphiIphi_3/D')
      outTree_3.Branch('p3_sigmaIphiIphi_3',self.p3_sigmaIphiIphi_3,'p3_sigmaIphiIphi_3/D')
      outTree_3.Branch('p1_sigmaEtaEta_3',self.p1_sigmaEtaEta_3,'p1_sigmaEtaEta_3/D')
      outTree_3.Branch('p2_sigmaEtaEta_3',self.p2_sigmaEtaEta_3,'p2_sigmaEtaEta_3/D')
      outTree_3.Branch('p3_sigmaEtaEta_3',self.p3_sigmaEtaEta_3,'p3_sigmaEtaEta_3/D')
      outTree_3.Branch('p1_full5x5_sigmaEtaEta_3',self.p1_full5x5_sigmaEtaEta_3,'p1_full5x5_sigmaEtaEta_3/D')
      outTree_3.Branch('p2_full5x5_sigmaEtaEta_3',self.p2_full5x5_sigmaEtaEta_3,'p2_full5x5_sigmaEtaEta_3/D')
      outTree_3.Branch('p3_full5x5_sigmaEtaEta_3',self.p3_full5x5_sigmaEtaEta_3,'p3_full5x5_sigmaEtaEta_3/D')     
      outTree_3.Branch('p1_hadronicOverEm_3',self.p1_hadronicOverEm_3,'p1_hadronicOverEm_3/D') 
      outTree_3.Branch('p2_hadronicOverEm_3',self.p2_hadronicOverEm_3,'p2_hadronicOverEm_3/D')
      outTree_3.Branch('p3_hadronicOverEm_3',self.p3_hadronicOverEm_3,'p3_hadronicOverEm_3/D')
      outTree_3.Branch('p_mindr_3', self.p_mindr_3, 'p_mindr_3/D')
      outTree_3.Branch('p_maxdr_3', self.p_maxdr_3, 'p_maxdr_3/D')
      outTree_3.Branch('dphigh_mass_3', self.dphigh_mass_3, 'dphigh_mass_3/D')
      outTree_3.Branch('p_maxmass_3', self.p_maxmass_3, 'p_maxmass_3/D')
      outTree_3.Branch('dp1_dr_3',self.dp1_dr_3,'dp1_dr_3/D')
      outTree_3.Branch('dp1_pt_3',self.dp1_pt_3,'dp1_pt_3/D')
      outTree_3.Branch('dp1_eta_3',self.dp1_eta_3,'dp1_eta_3/D')
      outTree_3.Branch('dp1_phi_3',self.dp1_phi_3,'dp1_phi_3/D')
      outTree_3.Branch('dp1_mass_3',self.dp1_mass_3,'dp1_mass_3/D')
      outTree_3.Branch('tp_pt_3',self.tp_pt_3,'tp_pt_3/D')
      outTree_3.Branch('tp_eta_3',self.tp_eta_3,'tp_eta_3/D')
      outTree_3.Branch('tp_phi_3',self.tp_phi_3,'tp_phi_3/D')
      outTree_3.Branch('tp_mass_3',self.tp_mass_3,'tp_mass_3/D')
      outTree_3.Branch('passTrigger',self.passTrigger, 'passTrigger/D')
      outTree_3.Branch('nicematch',self.nicematch,'nicematch/D')
      outTree_3.Branch('genmatch_cat',self.genmatch_cat,'genmatch_cat/D')
      outTree_3.Branch('genTotalWeight',self.genTotalWeight, 'genTotalWeight/D')
      return outTree_3
     
   def MakeSkimmedTree_2(self):
      outTree_2 = TTree("H4GSel_2", "H4G Selected Events:2 gamma")
      SetOwnership(outTree_2,0)

      outTree_2.Branch('p1_pt_2', self.p1_pt_2, 'p1_pt_2/D')
      outTree_2.Branch('p2_pt_2', self.p2_pt_2, 'p2_pt_2/D')
      outTree_2.Branch('p1_M_2', self.p1_M_2, 'p1_M_2/D')
      outTree_2.Branch('p2_M_2', self.p2_M_2, 'p2_M_2/D')
      outTree_2.Branch('p1_eta_2', self.p1_eta_2, 'p1_eta_2/D')
      outTree_2.Branch('p2_eta_2', self.p2_eta_2, 'p2_eta_2/D')
      outTree_2.Branch('p1_phi_2', self.p1_phi_2, 'p1_phi_2/D')
      outTree_2.Branch('p2_phi_2', self.p2_phi_2, 'p2_phi_2/D')
      outTree_2.Branch('p1_mva_2', self.p1_mva_2, 'p1_mva_2/D')
      outTree_2.Branch('p2_mva_2', self.p2_mva_2, 'p2_mva_2/D')
      outTree_2.Branch('p1_r9_2', self.p1_r9_2, 'p1_r9_2/D')
      outTree_2.Branch('p2_r9_2', self.p2_r9_2, 'p2_r9_2/D')
      outTree_2.Branch('p1_genmatch_2',self.p1_genmatch_2, 'p1_genmatch_2/D')
      outTree_2.Branch('p2_genmatch_2',self.p2_genmatch_2, 'p2_genmatch_2/D')
      outTree_2.Branch('p1_match_2',self.p1_match_2, 'p1_match_2/D')
      outTree_2.Branch('p2_match_2',self.p2_match_2, 'p2_match_2/D')
      outTree_2.Branch('p1_full5x5_r9_2',self.p1_full5x5_r9_2, 'p1_full5x5_r9_2/D')
      outTree_2.Branch('p2_full5x5_r9_2',self.p2_full5x5_r9_2, 'p2_full5x5_r9_2/D')
      outTree_2.Branch('p1_full5x5_sigmaIetaIeta_2',self.p1_full5x5_sigmaIetaIeta_2,'p1_full5x5_sigmaIetaIeta_2/D')
      outTree_2.Branch('p2_full5x5_sigmaIetaIeta_2',self.p2_full5x5_sigmaIetaIeta_2,'p2_full5x5_sigmaIetaIeta_2/D')
      outTree_2.Branch('p1_sigmaIphiIphi_2',self.p1_sigmaIphiIphi_2,'p1_sigmaIphiIphi_2/D')
      outTree_2.Branch('p2_sigmaIphiIphi_2',self.p2_sigmaIphiIphi_2,'p2_sigmaIphiIphi_2/D')
      outTree_2.Branch('p1_sigmaEtaEta_2',self.p1_sigmaEtaEta_2,'p1_sigmaEtaEta_2/D')
      outTree_2.Branch('p2_sigmaEtaEta_2',self.p2_sigmaEtaEta_2,'p2_sigmaEtaEta_2/D')
      outTree_2.Branch('p1_full5x5_sigmaEtaEta_2',self.p1_full5x5_sigmaEtaEta_2,'p1_full5x5_sigmaEtaEta_2/D')
      outTree_2.Branch('p2_full5x5_sigmaEtaEta_2',self.p2_full5x5_sigmaEtaEta_2,'p2_full5x5_sigmaEtaEta_2/D')
      outTree_2.Branch('p1_hadronicOverEm_2',self.p1_hadronicOverEm_2,'p1_hadronicOverEm_2/D')
      outTree_2.Branch('p2_hadronicOverEm_2',self.p2_hadronicOverEm_2,'p2_hadronicOverEm_2/D')
      outTree_2.Branch('p_mindr_2',self.p_mindr_2,'p_mindr_2/D')
      outTree_2.Branch('tp_pt_2',self.tp_pt_2,'tp_pt_2/D')
      outTree_2.Branch('tp_eta_2',self.tp_eta_2,'tp_eta_2/D')
      outTree_2.Branch('tp_phi_2',self.tp_phi_2,'tp_phi_2/D')
      outTree_2.Branch('tp_mass_2',self.tp_mass_2,'tp_mass_2/D')
      outTree_2.Branch('passTrigger',self.passTrigger, 'passTrigger/D')
      outTree_2.Branch('genTotalWeight',self.genTotalWeight, 'genTotalWeight/D')
      return outTree_2

   def FillEvent(self, inputTree):

      ObjList = [key.GetName() for key in  inputTree.GetListOfBranches()] 
      #print " ObjList = ", ObjList
      
      for b in ObjList:
        getattr(self, b)[0] = getattr(inputTree, b)
        #setattr(self, b + "[0]", getattr(inputTree, b) ) ---> this does not work!!! Remember! Since [0] will not be interpreted as an operation
   
            

   def triggerpass(self,Phos,Phos_id,Trigger):
       tPhos = []
       tPhos_id = []
       for i,pho in enumerate(Phos):
           if Trigger == 0: continue
           #print Trigger[Phos_id[i]]
           tPhos.append(pho)
           tPhos_id.append(Phos_id[i])
       return tPhos, tPhos_id


   def MakePhotonSelection(self, Phos, Phos_id, MVA, el):
      sPhos = []
      sPhos_id = []
      for i,pho in enumerate(Phos):
         if pho.Pt() < 15:continue
         if abs(pho.Eta()) > 2.5: continue
         #print " I made the pt cut "
         if abs(pho.Eta()) < 1.479 and MVA[Phos_id[i]] < -0.9: continue
         if abs(pho.Eta()) > 1.479 and MVA[Phos_id[i]] < -0.9: continue
         #print " I made the mva cut"
         if el[Phos_id[i]] == 0: continue
         #print " I made the elec cut"
         sPhos.append(pho)
         sPhos_id.append(Phos_id[i])
      return sPhos, sPhos_id

   def MakePhotonSelectionCutBased(self, Phos, Phos_id, rho, chiso, nhiso, phiso, hoe, sieie, el):
      sPhos = []
      sPhos_id = []
      for i,pho in enumerate(Phos):
         if pho.Pt() < 15: continue
         if abs(pho.Eta()) > 2.5: continue
         isCutBasedId = self.PhotonCutBasedId(pho, Phos_id[i], rho, chiso, nhiso, phiso, hoe, sieie, el)
         if isCutBasedId == 0: continue

         sPhos.append(pho)
         sPhos_id.append(Phos_id[i])

      return sPhos, sPhos_id

   def SelectWithFakes(self, Phos, Phos_id, MVA, el):
      fPhos = []
      fPhos_id = []
      for i,pho in enumerate(Phos):
         if pho.Pt() < 15: continue
         if abs(pho.Eta()) > 2.5: continue
         if abs(pho.Eta()) < 1.479 and MVA[Phos_id[i]] > -0.9: continue
         if abs(pho.Eta()) > 1.479 and MVA[Phos_id[i]] > -0.9: continue
         if el[Phos_id[i]] == 0: continue

         fPhos.append(pho)
         fPhos_id.append(Phos_id[i])

      return fPhos, fPhos_id

   def MakeTriggerSelection(self, Phos, Phos_id, R9, HoE, PSeed, ECALIso , SigmaIEtaIEta, trackIso):
      #based on trigger: HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55
      pho1 = 0
      pho1_id = -99
      pho2 = 0
      pho2_id = -99
      #print "Number of photons", len(Phos)
      for i1,p1 in enumerate(Phos):
         for i2,p2 in enumerate(Phos):
            if(i2 <=i1): continue
            if p1.Pt() < 30: continue  # pt of leading photon
            if p2.Pt() < 18: continue  # pt of subleading photon
            if PSeed[Phos_id[i1]] == 1: continue
            if PSeed[Phos_id[i2]] == 1: continue 
            if abs(p1.Eta()) > 1.4442 and abs(p1.Eta()) < 1.566: continue # avoid the EB-EE gap
            if abs(p2.Eta()) > 1.4442 and abs(p2.Eta()) < 1.566: continue
            
            if abs(p1.Eta()) < 1.479 and abs(p2.Eta()) < 1.479: # Case 1 : EB EB
               if R9[Phos_id[i1]] > 0.5 and R9[Phos_id[i2]] > 0.5:
                  if HoE[Phos_id[i1]] < 0.07 and HoE[Phos_id[i2]] < 0.07:
                     if SigmaIEtaIEta[Phos_id[i1]] < 0.0105 and SigmaIEtaIEta[Phos_id[i2]] < 0.0105:
                        if ECALIso[Phos_id[i1]] < 4.0 + 0.012*p1.Pt() and ECALIso[Phos_id[i2]] < 4.0 + 0.012*p2.Pt():
 			   if trackIso[Phos_id[i1]] < 6.0 + 0.012*p1.Pt() and trackIso[Phos_id[i2]] < 6.0 + 0.012*p2.Pt():
                               thisDipho = p1+p2
                               if thisDipho.M() < 55: continue
                               pho1 = p1
                               pho1_id = Phos_id[i1]
                               pho2 = p2
                               pho2_id = Phos_id[i2]
                               break
            elif abs(p1.Eta()) < 1.479  and abs(p2.Eta()) > 1.479: # Case 2 : EB EE
                 if R9[Phos_id[i1]] > 0.85 and R9[Phos_id[i2]] > 0.85:
                    if HoE[Phos_id[i1]] < 0.07 and HoE[Phos_id[i2]] < 0.07:
                       if SigmaIEtaIEta[Phos_id[i1]] < 0.0105 and SigmaIEtaIEta[Phos_id[i2]] < 0.0105:
                          if ECALIso[Phos_id[i1]] < 4.0 + 0.012*p1.Pt() and ECALIso[Phos_id[i2]] < 4.0 + 0.012*p2.Pt():
                             if trackIso[Phos_id[i1]] < 6.0 + 0.012*p1.Pt() and trackIso[Phos_id[i2]] < 6.0 + 0.012*p2.Pt():
                                thisDipho = p1+p2
                                if thisDipho.M() < 55: continue
                                pho1 = p1
                                pho1_id = Phos_id[i1]
                                pho2 = p2
                                pho2_id = Phos_id[i2]
                                break

            elif abs(p1.Eta()) > 1.479 and abs(p2.Eta()) < 1.479: # Case 3 : EE EB
		 #print " EE EB case"
                 if R9[Phos_id[i1]] > 0.85 and R9[Phos_id[i2]] > 0.85:  # Case 3 : EBEE
                    if HoE[Phos_id[i1]] < 0.07 and HoE[Phos_id[i2]] < 0.07:
                       if SigmaIEtaIEta[Phos_id[i1]] < 0.0105 and SigmaIEtaIEta[Phos_id[i2]] < 0.0105:
                          if ECALIso[Phos_id[i1]] < 4.0  + 0.012*p1.Pt() and ECALIso[Phos_id[i2]] < 4.0 + 0.012*p2.Pt():
                             if trackIso[Phos_id[i1]] < 6.0 + 0.012*p1.Pt() and trackIso[Phos_id[i2]] < 6.0 + 0.012*p2.Pt():
                                thisDipho = p1+p2
                                if thisDipho.M() < 55: continue
                                pho1 = p1
                             	pho1_id = Phos_id[i1]
                                pho2 = p2
                                pho2_id = Phos_id[i2]
                                break  
            elif abs(p1.Eta()) > 1.479 and abs(p2.Eta()) > 1.479: # Case 4 : EE EE
		 #print " EE EE case"
                 if R9[Phos_id[i1]] > 0.9 and R9[Phos_id[i2]] > 0.9:  
                    if HoE[Phos_id[i1]] < 0.035 and HoE[Phos_id[i2]] < 0.035:
                       if SigmaIEtaIEta[Phos_id[i1]] < 0.0275 and SigmaIEtaIEta[Phos_id[i2]] < 0.0275:         
                          if ECALIso[Phos_id[i1]] < 4.0 + 0.012*p1.Pt() and ECALIso[Phos_id[i2]] < 4.0 + 0.012*p2.Pt():
                             if trackIso[Phos_id[i1]] < 6.0 + 0.012*p2.Pt() and trackIso[Phos_id[i2]] < 6.0 + 0.012*p2.Pt():
                                thisDipho = p1+p2
                                if thisDipho.M() < 55: continue
                                pho1 = p1
                                pho1_id = Phos_id[i1]
                                pho2 = p2
                                pho2_id = Phos_id[i2]
                                break
         if pho1 !=0 and pho2 != 0: break              

      dipho = pho1+pho2
      if dipho == 0: return 0
      else: return [dipho, pho1, pho1_id, pho2, pho2_id]

   def MakeTriggerSelection_v2(self, Phos, Phos_id, R9, HoE, PSeed, ECALIso , SigmaIEtaIEta, trackIso):
      #based on trigger: HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55
      pho1 = 0
      pho1_id = -99
      pho2 = 0
      pho2_id = -99
      #print "Number of photons", len(Phos)
      for i1,p1 in enumerate(Phos):
         for i2,p2 in enumerate(Phos):
            if(i2 <=i1): continue
            if p1.Pt() < 30: continue  # pt of leading photon
            if p2.Pt() < 18: continue  # pt of subleading photon
            if abs(p1.Eta()) > 1.4442 and abs(p1.Eta()) < 1.566: continue # avoid the EB-EE gap
            if abs(p2.Eta()) > 1.4442 and abs(p2.Eta()) < 1.566: continue

            if abs(p1.Eta()) < 1.479 and abs(p2.Eta()) < 1.479: 
               if R9[Phos_id[i1]] > 0.85 and R9[Phos_id[i2]] > 0.85:  # Case 1 : EB EB (OR path) , when R9 > 0.85
                  if HoE[Phos_id[i1]] < 0.08 and HoE[Phos_id[i2]] < 0.08:
                     if PSeed[Phos_id[i1]] == 1: continue
                     if PSeed[Phos_id[i2]] == 1: continue
                     thisDipho = p1+p2
                     if thisDipho.M() < 55: continue
                     pho1 = p1
                     pho1_id = Phos_id[i1]
                     pho2 = p2
                     pho2_id = Phos_id[i2]
                     break
                  
                  elif SigmaIEtaIEta[Phos_id[i1]] < 0.0105 and SigmaIEtaIEta[Phos_id[i2]] < 0.0105:  #Case 2 : EB EB , R9 > 0.85 (AND path)
                       if HoE[Phos_id[i1]] < 0.08 and HoE[Phos_id[i2]] < 0.08:
                          if ECALIso[Phos_id[i1]] < 6.0 + 0.012*p1.Pt() and ECALIso[Phos_id[i2]] < 6.0 + 0.012*p2.Pt():
                             if trackIso[Phos_id[i1]] < 6.0 + 0.002*p1.Pt() and trackIso[Phos_id[i2]] < 6.0 + 0.002*p2.Pt():
                                 if PSeed[Phos_id[i1]] == 1: continue
                                 if PSeed[Phos_id[i2]] == 1: continue
                                 thisDipho = p1+p2
                                 if thisDipho.M() < 55: continue
                                 pho1 = p1
                                 pho1_id = Phos_id[i1]
                                 pho2 = p2
                                 pho2_id = Phos_id[i2]
                                 break     
               elif R9[Phos_id[i1]] > 0.5 and R9[Phos_id[i1]] < 0.85:  # Case 3 : EB EB (OR path) , when R9 < 0.85
                    if R9[Phos_id[i2]] > 0.5 and R9[Phos_id[i2]] < 0.85:
                       if HoE[Phos_id[i1]] < 0.08 and HoE[Phos_id[i2]] < 0.08:
                          if SigmaIEtaIEta[Phos_id[i1]] < 0.0105 and SigmaIEtaIEta[Phos_id[i2]] < 0.0105:
                             if ECALIso[Phos_id[i1]] < 6.0 + 0.012*p1.Pt() and ECALIso[Phos_id[i2]] < 6.0 + 0.012*p2.Pt():
                                if trackIso[Phos_id[i1]] < 6.0 + 0.002*p1.Pt() and trackIso[Phos_id[i2]] < 6.0 + 0.002*p2.Pt():
                                   if PSeed[Phos_id[i1]] == 1: continue
                                   if PSeed[Phos_id[i2]] == 1: continue
                                   thisDipho = p1+p2
                                   if thisDipho.M() < 55: continue
                                   pho1 = p1
                                   pho1_id = Phos_id[i1]
                                   pho2 = p2
                                   pho2_id = Phos_id[i2]
                                   break
            elif (abs(p1.Eta()) > 1.479 and abs(p2.Eta()) < 1.479) : # Case 4 : EE EB
                 if R9[Phos_id[i1]] > 0.9 and R9[Phos_id[i2]] > 0.85:  
                    if HoE[Phos_id[i1]] < 0.08 and HoE[Phos_id[i2]] < 0.08:
                       if SigmaIEtaIEta[Phos_id[i1]] < 0.0105 and SigmaIEtaIEta[Phos_id[i2]] < 0.0105:
                          if ECALIso[Phos_id[i1]] < 6.0 + 0.012*p1.Pt() and ECALIso[Phos_id[i2]] < 6.0 + 0.012*p2.Pt() :
                             if trackIso[Phos_id[i1]] < 6.0 + 0.002*p1.Pt() and trackIso[Phos_id[i2]] < 6.0 + 0.002*p2.Pt() :
                                if PSeed[Phos_id[i1]] == 1: continue
                                if PSeed[Phos_id[i2]] == 1: continue
                                thisDipho = p1+p2
                                if thisDipho.M() < 55: continue
                                pho1 = p1
                                pho1_id = Phos_id[i1]
                                pho2 = p2
                                pho2_id = Phos_id[i2]
                                break
            elif abs(p1.Eta()) > 1.479 and abs(p2.Eta()) > 1.479: # Case 5 : EE EE (AND path)
                 if R9[Phos_id[i1]] > 0.9 and R9[Phos_id[i2]] > 0.9:
                    if HoE[Phos_id[i1]] < 0.08 and HoE[Phos_id[i2]] < 0.08:
                       if SigmaIEtaIEta[Phos_id[i1]] < 0.035 and SigmaIEtaIEta[Phos_id[i2]] < 0.035:
                          if ECALIso[Phos_id[i1]] < 6.0 + 0.012*p1.Pt() and ECALIso[Phos_id[i2]] < 6.0 + 0.012*p2.Pt():
                             if trackIso[Phos_id[i1]] < 6.0 + 0.002*p1.Pt() and trackIso[Phos_id[i2]] < 6.0 + 0.002*p2.Pt():
                                if PSeed[Phos_id[i1]] == 1: continue
                                if PSeed[Phos_id[i2]] == 1: continue
                                thisDipho = p1+p2
                                if thisDipho.M() < 55: continue
                                pho1 = p1
                                pho1_id = Phos_id[i1]
                                pho2 = p2
                                pho2_id = Phos_id[i2]
                                break
         if pho1 !=0 and pho2 != 0: break

      dipho = pho1+pho2
      if dipho == 0: return 0
      else: return [dipho, pho1, pho1_id, pho2, pho2_id]




   # Phos: a list of 4 (and only 4!) TLorentzVectors
   def MakePairing(self, Phos):
      minDM = 100000
      P1 = 0
      iP1 = -99
      P2 = 0
      iP2 = -99
      P3 = 0
      iP3 = -99
      P4 = 0
      iP4 = -99
      Dipho1 = 0
      Dipho2 = 0
      for i1,p1 in enumerate(Phos):
         for i2,p2 in enumerate(Phos):
            if i2 <= i1: continue
            for i3,p3 in enumerate(Phos):
               if i3 == i2 or i3 == i1: continue
               for i4,p4 in enumerate(Phos):
                  if i4 <= i3: continue
                  if i4==i1 or i4==i2: continue
                  dipho1 = p1+p2
                  dipho2 = p3+p4
                  #Mass = dipho.M()
                  deltaM = abs(dipho1.M() - dipho2.M())
                  if(DEBUG): print deltaM, i1, i2, i3, i4
                  if deltaM < minDM:
                     minDM = deltaM
                     P1 = p1
                     iP1 = i1
                     P2 = p2
                     iP2 = i2
                     P3 = p3
                     iP3 = i3
                     P4 = p4
                     iP4 = i4
                     #print "Photon 1 M : " , p1.M()
                     #Max_mass = max(((p1.M()+p2.M()),(p1.M()+p3.M()),(p1.M()+p4.M()),(p2.M()+p3.M()),(p2.M()+p4.M()),(p3.M()+p4.M())))
                     #print Max_mass
                     Dipho1 = dipho1 if ((p1.Pt() + p2.Pt()) > (p3.Pt() + p4.Pt())) else dipho2
                     Dipho2 = dipho2 if ((p1.Pt() + p2.Pt()) > (p3.Pt() + p4.Pt())) else dipho1
      if(DEBUG): print 'minDr:', abs(Dipho1.M() - Dipho2.M()), iP1, iP2, iP3, iP4
      arr = [[Dipho1, P1, iP1, P2, iP2], [Dipho2, P3, iP3, P4, iP4]]
      return arr


 
   #def MakePairing_3gamma(self, Phos):
      #minDM = 100000
      #P1 = 0
      #iP1 = -99
      #P2 = 0
      #iP2 = -99
      #P3 = 0
      #iP3 = -99
      #Dipho1 = 0
      #for i1,p1 in enumerate(Phos):
         #for i2,p2 in enumerate(Phos):
            #if i2 <= i1: continue
            #for i3,p3 in enumerate(Phos):
               #if i3 == i2 or i3 == i1: continue
                  #dipho12 = p1+p2
                  #dipho13 = p1+p3
                  #dipho23 = p2+p3
                  #Mass = dipho.M()
                  #deltaM_12_13 = abs(dipho12.M() - dipho13.M())
                  #deltaM_12_23 = abs(dipho12.M() - dipho23.M())
                  #if(DEBUG): print deltaM, i1, i2, i3, i4
                  #if deltaM_12_13 < deltaM_12_23:
                     
                     #iP1 = i1
                     #P2 = p2
                     #iP2 = i2
                     #P3 = p3
                     #iP3 = i3
                     #P4 = p4
                     #iP4 = i4
                     #print "Photon 1 M : " , p1.M()
                     #Max_mass = max(((p1.M()+p2.M()),(p1.M()+p3.M()),(p1.M()+p4.M()),(p2.M()+p3.M()),(p2.M()+p4.M()),(p3.M()+p4.M())))
                     #print Max_mass
                     #Dipho1 = dipho1 if ((p1.Pt() + p2.Pt()) > (p3.Pt() + p4.Pt())) else dipho2
                     #Dipho2 = dipho2 if ((p1.Pt() + p2.Pt()) > (p3.Pt() + p4.Pt())) else dipho1
      #if(DEBUG): print 'minDr:', abs(Dipho1.M() - Dipho2.M()), iP1, iP2, iP3, iP4
      #arr = [[Dipho1, P1, iP1, P2, iP2], [Dipho2, P3, iP3, P4, iP4]]
      #return arr



   def PhotonCutBasedId(self, pho, pho_id, rho, chiso, nhiso, phiso, hoe, sieie, el):
      EA = [[0 for x in range(3)] for y in range(7)]
      EA[0][0] = 0.0; EA[0][1] = 0.0599; EA[0][2] = 0.1271;
      EA[1][0] = 0.0; EA[1][1] = 0.0819; EA[1][2] = 0.1101;
      EA[2][0] = 0.0; EA[2][1] = 0.0696; EA[2][2] = 0.0756;
      EA[3][0] = 0.0; EA[3][1] = 0.0360; EA[3][2] = 0.1175;
      EA[4][0] = 0.0; EA[4][1] = 0.0360; EA[4][2] = 0.1498;
      EA[5][0] = 0.0; EA[5][1] = 0.0462; EA[5][2] = 0.1857;
      EA[6][0] = 0.0; EA[6][1] = 0.0656; EA[6][2] = 0.2183;

      feta = abs(pho.Eta())
      whichEA = ""

      if(feta > 0.000 and feta < 1.000 ): whichEA = EA[0]
      if(feta > 1.000 and feta < 1.479 ): whichEA = EA[1]
      if(feta > 1.479 and feta < 2.000 ): whichEA = EA[2]
      if(feta > 2.000 and feta < 2.200 ): whichEA = EA[3]
      if(feta > 2.200 and feta < 2.300 ): whichEA = EA[4]
      if(feta > 2.300 and feta < 2.400 ): whichEA = EA[5]
      if(feta > 2.400 and feta < 10.00 ): whichEA = EA[6]

      nhiso_corr = max(nhiso[pho_id] - rho*whichEA[1], 0)
      phiso_corr = max(nhiso[pho_id] - rho*whichEA[2], 0)

      if feta < 1.5:
         if hoe[pho_id] > 0.05: return 0
         if sieie[pho_id] > 0.0102: return 0
         if chiso[pho_id] > 3.32: return 0
         if nhiso_corr > (1.92 + 0.014*pho.Pt() + 0.000019*pho.Pt()*pho.Pt()): return 0
         if phiso_corr > (0.81 + 0.0053*pho.Pt()): return 0
      if feta > 1.5:
         if hoe[pho_id] > 0.05: return 0
         if sieie[pho_id] > 0.0274: return 0
         if chiso[pho_id] > 1.97: return 0
         if nhiso_corr > (11.86 + 0.0139*pho.Pt() + 0.000025*pho.Pt()*pho.Pt()): return 0
         if phiso_corr > (0.83 + 0.0034*pho.Pt()): return 0

      if el[pho_id] == 0: return 0
      return 1
      


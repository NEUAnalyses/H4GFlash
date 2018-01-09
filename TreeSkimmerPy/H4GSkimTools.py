from ROOT import *
import numpy as n

DEBUG = 0

class SkimmedTreeTools:
   def __init__(self):
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
      self.p_mindr = n.zeros(1, dtype=float)
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
      outTree.Branch('p_mindr', self.p_mindr, 'p_mindr/D')
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
      return outTree


   def FillEvent(self, inputTree):

      ObjList = [key.GetName() for key in  inputTree.GetListOfBranches()] 
      #print " ObjList = ", ObjList
      
      for b in ObjList:
        getattr(self, b)[0] = getattr(inputTree, b)
        #setattr(self, b + "[0]", getattr(inputTree, b) ) ---> this does not work!!! Remember! Since [0] will not be interpreted as an operation
   
            



   def MakePhotonSelection(self, Phos, Phos_id, MVA, el):
      sPhos = []
      sPhos_id = []
      for i,pho in enumerate(Phos):
         if pho.Pt() < 15:continue
         if abs(pho.Eta()) > 2.5: continue
         if abs(pho.Eta()) < 1.479 and MVA[Phos_id[i]] < -0.9: continue
         if abs(pho.Eta()) > 1.479 and MVA[Phos_id[i]] < -0.9: continue
         if el[Phos_id[i]] == 0: continue 
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

   def MakeTriggerSelection(self, Phos, Phos_id, R9, CHIso, HoE, PSeed, ECALIso , SigmaIEtaIEta):
      #based on trigger: HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55
      pho1 = 0
      pho1_id = -99
      pho2 = 0
      pho2_id = -99
      #print "Number of photons", len(Phos)
      for i1,p1 in enumerate(Phos):
         if p1.Pt() < 30 or abs(p1.Eta()) > 1.479: continue
         if (R9[Phos_id[i1]] < 0.5 or abs(p1.Eta()) > 1.479) and (R9[Phos_id[i1]] < 0.8 or abs(p1.Eta()) < 1.479 ): continue 
         #if (HoE[Phos_id[i1]] > 0.1 or abs(p1.Eta()) > 1.479) and (HoE[Phos_id[i1]] > 0.1 or abs(p1.Eta()) < 1.479): continue
         if HoE[Phos_id[i1]] > 0.1: continue
         if ((R9[Phos_id[i1]] < 0.85 or abs(p1.Eta()) > 1.479) and (R9[Phos_id[i1]] < 0.9 or abs(p1.Eta()) < 1.479)) and (ECALIso[Phos_id[i1]] > (6 + 0.012*p1.Pt()) or ((SigmaIEtaIEta[Phos_id[i1]] > 0.015 or abs(p1.Eta()) > 1.479) and (SigmaIEtaIEta[Phos_id[i1]] > 0.035 or abs(p1.Eta()) < 1.479 ))): continue 
         #if R9[Phos_id[i1]] < 0.8 and( ECALIso[Phos_id[i1]] > (6 + 0.012*p1.Pt() or SigmaIEtaIEta[Phos_id[i1]] > 0.015)): continue
         #if CHIso[Phos_id[i1]] > 20 and CHIso[Phos_id[i1]]/p1.Pt() > 0.3: continue
         #if HoE[Phos_id[i1]] > 0.08: continue
         if PSeed[Phos_id[i1]] == 1: continue
         if abs(p1.Eta()) > 1.4442 and abs(p1.Eta()) < 1.566: continue
         
         for i2,p2 in enumerate(Phos):
            if(i2 <= i1): continue
            if p2.Pt() < 20: continue
            if (R9[Phos_id[i2]] < 0.5 or abs(p2.Eta()) > 1.479) and (R9[Phos_id[i2]] < 0.8 or abs(p2.Eta()) < 1.479 ): continue
            #if (HoE[Phos_id[i2]] > 0.1 or abs(p2.Eta()) > 1.479) and (HoE[Phos_id[i2]] > 0.1 or abs(p2.Eta()) < 1.479): continue
            if HoE[Phos_id[i2]] > 0.1: continue
            if ((R9[Phos_id[i2]] < 0.85 or abs(p2.Eta()) > 1.479) and (R9[Phos_id[i2]] < 0.9 or abs(p2.Eta()) < 1.479)) and (ECALIso[Phos_id[i2]] > (6 + 0.012*p2.Pt()) or ((SigmaIEtaIEta[Phos_id[i2]] > 0.015 or abs(p2.Eta()) > 1.479) and (SigmaIEtaIEta[Phos_id[i2]] > 0.035 or abs(p2.Eta()) < 1.479 ))): continue
            #if ((R9[Phos_id[i2] < 0.85 or abs(p2.Eta()) > 1.479) and (R9[Phos_id[i2] < 0.9 or abs(p2.Eta()) < 1.479)) and ((SigmaIEtaIEta[Phos_id[i2] > 0.015 or abs(p2.Eta()) > 1.479) and (SigmaIEtaIEta[Phos_id[i2] > 0.035 or abs(p2.Eta()) < 1.479) or ECALIso[Phos_id[i2] > (6+0.012*p2.Pt())): continue
            #if R9[Phos_id[i2]] < 0.8 and (ECALIso[Phos_id[i2]] > (6 + 0.012*p2.Pt() or SigmaIEtaIEta[Phos_id[i2]] > 0.015)): continue
            #if CHIso[Phos_id[i2]] > 20 and CHIso[Phos_id[i2]]/p2.Pt() > 0.3: continue
            #if HoE[Phos_id[i2]] > 0.08: continue
            if PSeed[Phos_id[i2]] == 1: continue
            if abs(p2.Eta()) > 1.4442 and abs(p2.Eta()) < 1.566: continue
         
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
      


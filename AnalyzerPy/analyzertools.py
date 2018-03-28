from ROOT import *
import numpy as n

DEBUG = 0

class GenTools:

   def __init__(self):
       self.totevs = n.zeros(1, dtype=float)
       self.gen1_pt = n.zeros(1, dtype=float)
       self.gen2_pt = n.zeros(1, dtype=float)
       self.gen3_pt = n.zeros(1, dtype=float)
       self.gen4_pt = n.zeros(1, dtype=float)
       self.gen1_eta = n.zeros(1, dtype=float)
       self.gen2_eta = n.zeros(1, dtype=float)
       self.gen3_eta = n.zeros(1, dtype=float)
       self.gen4_eta = n.zeros(1, dtype=float)
       self.gen12_mass = n.zeros(1, dtype=float)
       self.gen13_mass = n.zeros(1, dtype=float)
       self.gen14_mass = n.zeros(1, dtype=float)
       self.gen23_mass = n.zeros(1, dtype=float)
       self.gen24_mass = n.zeros(1, dtype=float)
       self.gen34_mass = n.zeros(1, dtype=float)
       self.gen12dr = n.zeros(1, dtype=float)
       self.gen13dr = n.zeros(1, dtype=float)
       self.gen14dr = n.zeros(1, dtype=float)
       self.gen23dr = n.zeros(1, dtype=float)
       self.gen24dr = n.zeros(1, dtype=float)
       self.gen34dr = n.zeros(1, dtype=float)
       self.tp_mass = n.zeros(1, dtype=float)
       
       
       self.p1_pt_case1 = n.zeros(1, dtype=float)
       self.p2_pt_case1 = n.zeros(1, dtype=float)
       self.p3_pt_case1 = n.zeros(1, dtype=float)
       self.p4_pt_case1 = n.zeros(1, dtype=float)
       self.p1_eta_case1 = n.zeros(1, dtype=float)
       self.p2_eta_case1 = n.zeros(1, dtype=float)
       self.p3_eta_case1 = n.zeros(1, dtype=float)
       self.p4_eta_case1 = n.zeros(1, dtype=float)
       self.tp_mass_case1 = n.zeros(1, dtype=float)
       
       
       self.fatpho_pt_case2 = n.zeros(1, dtype=float)
       self.isopho1_pt_case2 = n.zeros(1, dtype=float)
       self.isopho2_pt_case2 = n.zeros(1, dtype=float)
       self.fatpho_eta_case2 = n.zeros(1, dtype=float)
       self.isopho1_eta_case2 = n.zeros(1, dtype=float)
       self.isopho2_eta_case2 = n.zeros(1, dtype=float)
       self.tp_mass_case2 = n.zeros(1, dtype=float)
       self.fatpho_dr_case3 = n.zeros(1, dtype=float)

       self.fatpho1_pt_case3 = n.zeros(1, dtype=float)
       self.fatpho1_eta_case3 = n.zeros(1, dtype=float)
       self.fatpho2_pt_case3 = n.zeros(1, dtype=float)
       self.fatpho2_eta_case3 = n.zeros(1, dtype=float)
       self.fatpho1_dr_case3 = n.zeros(1, dtype=float)
       self.fatpho2_dr_case3 = n.zeros(1, dtype=float)
       self.tp_mass_case3 = n.zeros(1, dtype=float)
   
   def MakeGenTree(self):
       outTree = TTree("geninfo","tot evs")
       SetOwnership(outTree,0)
   
       outTree.Branch('totevs',self.totevs,'totevs/D')
       outTree.Branch('gen1_pt',self.gen1_pt,'gen1_pt/D')
       outTree.Branch('gen2_pt',self.gen2_pt,'gen2_pt/D')
       outTree.Branch('gen3_pt',self.gen3_pt,'gen3_pt/D')
       outTree.Branch('gen4_pt',self.gen4_pt,'gen4_pt/D')
       outTree.Branch('gen1_eta',self.gen1_eta,'gen1_eta/D')
       outTree.Branch('gen2_eta',self.gen2_eta,'gen2_eta/D')
       outTree.Branch('gen3_eta',self.gen3_eta,'gen3_eta/D')
       outTree.Branch('gen4_eta',self.gen4_eta,'gen4_eta/D')
       outTree.Branch('gen12_mass',self.gen12_mass,'gen12_mass/D')
       outTree.Branch('gen13_mass',self.gen13_mass,'gen13_mass/D')
       outTree.Branch('gen14_mass',self.gen14_mass,'gen14_mass/D')
       outTree.Branch('gen23_mass',self.gen23_mass,'gen23_mass/D')
       outTree.Branch('gen24_mass',self.gen24_mass,'gen24_mass/D')
       outTree.Branch('gen34_mass',self.gen34_mass,'gen34_mass/D')
       outTree.Branch('gen12dr',self.gen12dr,'gen12dr/D')
       outTree.Branch('gen13dr',self.gen13dr,'gen13dr/D')
       outTree.Branch('gen14dr',self.gen14dr,'gen14dr/D')
       outTree.Branch('gen23dr',self.gen23dr,'gen23dr/D')
       outTree.Branch('gen24dr',self.gen24dr,'gen24dr/D')
       outTree.Branch('gen34dr',self.gen34dr,'gen34dr/D')
       outTree.Branch('tp_mass',self.tp_mass,'tp_mass/D')
       
       return outTree
   
   def MakeGenTree_case1(self):
       outTree_case1 = TTree("H4GGen_case1", "4 resolved")
       SetOwnership(outTree_case1,0)

       outTree_case1.Branch('p1_pt_case1', self.p1_pt_case1, 'p1_pt_case1/D')
       outTree_case1.Branch('p2_pt_case1', self.p2_pt_case1, 'p2_pt_case1/D')
       outTree_case1.Branch('p3_pt_case1', self.p3_pt_case1, 'p3_pt_case1/D')
       outTree_case1.Branch('p4_pt_case1', self.p4_pt_case1, 'p4_pt_case1/D')
       outTree_case1.Branch('p1_eta_case1', self.p1_eta_case1, 'p1_eta_case1/D')
       outTree_case1.Branch('p2_eta_case1', self.p2_eta_case1, 'p2_eta_case1/D')
       outTree_case1.Branch('p3_eta_case1', self.p3_eta_case1, 'p3_eta_case1/D')
       outTree_case1.Branch('p4_eta_case1', self.p4_eta_case1, 'p4_eta_case1/D')
       outTree_case1.Branch('tp_mass_case1', self.tp_mass_case1, 'tp_mass_case1/D')
       #outTree.Branch('a1_dr',self.a1_dr,'a1_dr/D')
       #outTree.Branch('a2_dr',self.a2_dr,'a2_dr/D')
       #outTree.Branch('a1_deta',self.a1_deta,'a1_deta/D')
       #outTree.Branch('a2_deta',self.a2_deta,'a2_deta/D')
       #outTree.Branch('a1_dphi',self.a1_dphi,'a1_dphi/D')
       #outTree.Branch('a2_dphi',self.a2_dphi,'a2_dphi/D')
       #outTree.Branch('a1_mass',self.a1_mass,'a1_mass/D')
       #outTree.Branch('a1_mass',self.a1_mass,'a1_mass/D')
       #outTree.Branch('a1_pt',self.a1_pt,'a1_pt/D')
       #outTree.Branch('a2_pt',self.a2_pt,'a2_pt/D')
       #outTree.Branch('a1_pz',self.a1_pz,'a1_pz/D')
       #outTree.Branch('a2_pz',self.a2_pz,'a2_pz/D')
       #outTree.Branch('tp_mass',self.tp_mass,'tp_mass/D')
       #outTree.Branch('pt_max_4gamma',self.pt_max_4gamma,'pt_max_4gamma/D')
       #outTree.Branch('gen123_pt',self.gen123_pt,'gen123_pt/D')
       #outTree.Branch('gen124_pt',self.gen124_pt,'gen124_pt/D')
       #outTree.Branch('gen134_pt',self.gen134_pt,'gen134_pt/D')
       #outTree.Branch('gen234_pt',self.gen234_pt,'gen234_pt/D')

       return outTree_case1




   def MakeGenTree_case2(self):
       outTree_case2 = TTree("H4GGen_case2", "1 fat + 2 resolved")
       SetOwnership(outTree_case2,0)
   
       outTree_case2.Branch('isopho1_pt_case2', self.isopho1_pt_case2, 'isopho1_pt_case2/D')
       outTree_case2.Branch('isopho2_pt_case2', self.isopho2_pt_case2, 'isopho2_pt_case2/D')
       outTree_case2.Branch('isopho1_eta_case2', self.isopho1_eta_case2, 'isopho1_eta_case2/D')
       outTree_case2.Branch('isopho2_eta_case2', self.isopho2_eta_case2, 'isopho2_eta_case2/D')
       outTree_case2.Branch('fatpho_pt_case2', self.fatpho_pt_case2, 'fatpho_pt_case2/D')
       outTree_case2.Branch('fatpho_eta_case2', self.fatpho_eta_case2, 'fatpho_eta_case2/D')
       outTree_case2.Branch('fatpho_dr_case3',self.fatpho_dr_case3,'fatpho_dr_case3/D')
       outTree_case2.Branch('tp_mass_case2', self.tp_mass_case2, 'tp_mass_case2/D')
   
       return outTree_case2
   

   
   def MakeGenTree_case3(self):
       outTree_case3 = TTree("H4GGen_case3", "2 fat")
       SetOwnership(outTree_case3,0)
       
       outTree_case3.Branch('fatpho1_pt_case3', self.fatpho1_pt_case3, 'fatpho1_pt_case3/D')
       outTree_case3.Branch('fatpho2_pt_case3', self.fatpho2_pt_case3, 'fatpho2_pt_case3/D')
       outTree_case3.Branch('fatpho1_eta_case3', self.fatpho1_eta_case3, 'fatpho1_eta_case3/D')
       outTree_case3.Branch('fatpho2_eta_case3', self.fatpho2_eta_case3, 'fatpho2_eta_case3/D')
       outTree_case3.Branch('fatpho1_dr_case3',self.fatpho1_dr_case3,'fatpho1_dr_case3/D')
       outTree_case3.Branch('fatpho2_dr_case3',self.fatpho2_dr_case3,'fatpho2_dr_case3/D')
       outTree_case3.Branch('tp_mass_case3', self.tp_mass_case3, 'tp_mass_case3/D')
   
       return outTree_case3


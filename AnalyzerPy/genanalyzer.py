#!/usr/bin/python

from ROOT import *
import sys, getopt
from array import array

def main(argv):
   #inputfiles = '/eos/cms/store/user/torimoto/physics/4gamma/2018/Signal/sig50.root'
   inputfiles = '/eos/cms/store/user/twamorka/Feb_2018/Signal/sig60.root'
   outputfile = 'forL1study/gen60.root'
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

   def UnderOverFlow( h):   ## function to show under and over flow bins
       h.SetBinContent(1, h.GetBinContent(0)+h.GetBinContent(1))
       h.SetBinContent(0,0)
       nbins = h.GetNbinsX()
       h.SetBinContent(nbins, h.GetBinContent(nbins)+h.GetBinContent(nbins+1))
       h.SetBinContent(nbins+1,0)
       return

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
   h_gen1_eta = TH1F("h_gen1_eta","gen1 eta;#eta;Events",100,0,3.5)
   h_gen2_eta = TH1F("h_gen2_eta","gen2 eta;#eta;Events",100,0,3.5)
   h_gen3_eta = TH1F("h_gen3_eta","gen3 eta;#eta;Events",100,0,3.5)
   h_gen4_eta = TH1F("h_gen4_eta","#eta of Gen photons;#eta(#gamma);Events",100,0,3.5)
   h_gen1_etaabs = TH1F("h_gen1_etaabs","gen1 |eta|;|#eta|;Events",100,0,3)
   h_gen2_etaabs = TH1F("h_gen2_etaabs","gen2 |eta|;|#eta|;Events",100,0,3)
   h_gen3_etaabs = TH1F("h_gen3_etaabs","gen3 |eta|;|#eta|;Events",100,0,3)
   h_gen4_etaabs = TH1F("h_gen4_etaabs","gen4 |eta|;|#eta|;Events",100,0,3)
   h_gen_maxeta = TH1F("h_gen_maxeta","max gen eta;#eta;Events",100,-3,3)
   h_gen_mineta = TH1F("h_gen_mineta","min gen eta;#eta;Events",100,-3,3)
   h_gen_abs_maxeta = TH1F("h_gen_abs_maxeta","abs max gen eta;#eta;Events",100,-1,3.5)
   h_gen1_phi = TH1F("h_gen1_phi","gen #gamma phi;""#phi;Events",100,-4,4)
   h_gen2_phi = TH1F("h_gen2_phi","gen #gamma phi;""#phi;Events",100,-4,4)
   h_gen3_phi = TH1F("h_gen3_phi","gen #gamma phi;""#phi;Events",100,-4,4)
   h_gen4_phi = TH1F("h_gen4_phi","#phi of Gen photons;#phi(#gamma);Events",100,-4,4)
   h_gen_dphi_a1 = TH1F("h_gen_dphi_a1","gen a1 and a2 : #Delta #phi ; #Delta #phi; Events", 100,-4,4)
   h_gen_dphi_a2 = TH1F("h_gen_dphi_a2","gen a1 and a2 :#Delta #phi;#Delta #phi; Events",100,-4,4)
   h_gen_deta_a1 = TH1F("h_gen_deta_a1","gen a1 and a2 : #Delta #eta; #Delta #eta; Events", 100,-4,4)
   h_gen_deta_a2 = TH1F("h_gen_deta_a2","gen a1 and a2 :#Delta #eta;#Delta #eta; Events",100,-4,4)
   h_gen1_pt = TH1F("h_gen1_pt","gen1 p_{t}; p_{t};Events",100,0,100)
   h_gen2_pt = TH1F("h_gen2_pt","gen2 p_{t}; p_{t};Events",100,0,100)
   h_gen3_pt = TH1F("h_gen3_pt","gen3 p_{t}; p_{t};Events",100,0,100)
   h_gen4_pt = TH1F("h_gen4_pt","p_{t} of Gen photons; p_{t} (#gamma) [GeV];Events",200,0,100)
   h_2d = TH2F("h_2d","h_2d",100,0,150,100,0,150)
   h_len_genphos = TH1F("h_len_genphos","Number of gen phos; # of gen photons;Events",100,0,7)
   h_dr12_gen = TH1F("h_dr12_gen","DeltaR between gen 1 and 2; #Delta r;#Delta r;Events",100,0,5)   
   h_dr13_gen = TH1F("h_dr13_gen","DeltaR between gen 1 and 3; #Delta r;#Delta r;Events",100,0,5)
   h_dr14_gen = TH1F("h_dr14_gen","DeltaR between gen 1 and 4; #Delta r;#Delta r;Events",100,0,5)
   h_dr23_gen = TH1F("h_dr23_gen","DeltaR between gen 2 and 3; #Delta r;#Delta r;Events",100,0,5)
   h_dr24_gen = TH1F("h_dr24_gen","DeltaR between gen 2 and 4; #Delta r;#Delta r;Events",100,0,5)
   h_dr34_gen = TH1F("h_dr34_gen","DeltaR between gen 3 and 4; #Delta r;#Delta r;Events",100,0,5)
   h_len_cat = TH1F("h_len_cat","Occurence of fat photon; blah;b;ah;Events",100,0,5) 
   h_fatpho_pt = TH1F("h_fatpho_pt","Pt of Fat photon in 3 gamma category;p_{T};p_{T};Events",55,0,100)
   h_fatpho_pt_cut1 = TH1F("h_fatpho_pt_cut1","Pt of Fat photon in 3 gamma category;p_{T};p_{T};Events",55,0,100)
   h_fatpho_pt_cut2 = TH1F("h_fatpho_pt_cut2","Pt of Fat photon in 3 gamma category;p_{T};p_{T};Events",55,0,100)
   h_fatpho_eta = TH1F("h_fatpho_eta","Eta of Fat photon in 3 gamma category;#eta;#eta;Events",55,0,3.5)
   h_isopho1_pt = TH1F("h_isopho1_pt","Pt of isolated photon 1 in 3 gamma category;p_{T};p_{T};Events",55,0,100)
   h_isopho1_pt_cut1 = TH1F("h_isopho1_pt_cut1","Pt of isolated photon 1 in 3 gamma category;p_{T};p_{T};Events",55,0,100)
   h_isopho1_pt_cut2 = TH1F("h_isopho1_pt_cut2","Pt of isolated photon 1 in 3 gamma category;p_{T};p_{T};Events",55,0,100)
   h_isopho2_pt = TH1F("h_isopho2_pt","Pt of isolated photon 2 in 3 gamma category;p_{T};p_{T};Events",55,0,100)
   h_isopho2_pt_cut1 = TH1F("h_isopho2_pt_cut1","Pt of isolated photon 2 in 3 gamma category;p_{T};p_{T};Events",55,0,100)
   h_isopho2_pt_cut2 = TH1F("h_isopho2_pt_cut2","Pt of isolated photon 2 in 3 gamma category;p_{T};p_{T};Events",55,0,100)
   h_isopho1_eta = TH1F("h_isopho1_eta","Eta of isolated photon 1 in 3 gamma category;#eta;#eta;Events",55,0,3.5)
   h_isopho2_eta = TH1F("h_isopho2_eta","Eta of isolated photon 2 in 3 gamma category;#eta;#eta;Events",55,0,3.5)
   h_fatpho1_pt = TH1F("h_fatpho1_pt","Pt of Fat Photon 1 in 2 gamma category;p_{T};p_{T};Events",100,0,100)
   h_fatpho2_pt = TH1F("h_fatpho2_pt","Pt of Fat Photon 2 in 2 gamma category;p_{T};p_{T};Events",100,0,100)
   h_fatpho_mass = TH1F("h_fatpho_mass","Mass of Fat photon in 3 gamma category;Mass;Mass[GeV];Events",100,0,120)
   h_isopho1_mass = TH1F("h_isopho1_mass","Mass of Iso photon1 in 3 gamma category;Mass;Mass[GeV];Events",100,0,120)
   h_isopho2_mass = TH1F("h_isopho2_mass","Mass of Iso photon2 in 3 gamma category;Mass;Mass[GeV];Events",100,0,120)
   h_fatpho1_eta = TH1F("h_fatpho1_eta","Eta of Fat Photon 1 in 2 gamma category;#eta;#eta;Events",100,0,3.5)
   h_fatpho2_eta = TH1F("h_fatpho2_eta","Eta of Fat Photon 2 in 2 gamma category;#eta;#eta;Events",100,0,3.5)
   h_fatpho1_mass = TH1F("h_fatpho1_mass","Mass of Fat photon 1 in 2 gamma category;Mass;Mass[GeV];Events",100,0,120)
   h_fatpho2_mass = TH1F("h_fatpho2_mass","Mass of Fat photon 2 in 2 gamma category;Mass;Mass[GeV];Events",100,0,120)
   h_tpmass_3g = TH1F("h_tpmass_3g","Tetraphoton mass in 3 gamma category;Mass;M(#gamma#gamma#gamma)[GeV];Events",100,0,250)
   h_tpmass_2g = TH1F("h_tpmass_2g","Tetraphoton mass in 2 gamma category;Mass;M(#gamma#gamma)[GeV];Events",100,0,250)

   triggers = {}
   triggerNames = []
   fraction = []
 
   evtCounter = 0
   #Tree Loop:
   for evt in range(0,tree.GetEntries()):
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

      h_len_genphos.Fill(len(Genphos))
      if len(Genphos) < 4:
         continue     
     	
      gen1 = TLorentzVector(0,0,0,0)
      gen2 = TLorentzVector(0,0,0,0)
      gen3 = TLorentzVector(0,0,0,0)
      gen4 = TLorentzVector(0,0,0,0)
      
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
      h_mgg12_gen.Fill(gen12.M())
      h_mgg13_gen.Fill(gen13.M())
      h_mgg14_gen.Fill(gen14.M())
      h_mgg23_gen.Fill(gen23.M())
      h_mgg24_gen.Fill(gen24.M())
      h_mgg34_gen.Fill(gen34.M())
        
      h_dr12_gen.Fill(gen1.DeltaR(gen2))
      h_dr13_gen.Fill(gen1.DeltaR(gen3))
      h_dr14_gen.Fill(gen1.DeltaR(gen4))
      h_dr23_gen.Fill(gen2.DeltaR(gen3))
      h_dr24_gen.Fill(gen2.DeltaR(gen4))
      h_dr34_gen.Fill(gen3.DeltaR(gen4))
 
      #print " 12 dr " ,gen1.DeltaR(gen2) 
      drlist = []
      fatphoton = []
      drlist.append(gen1.DeltaR(gen2))
      drlist.append(gen1.DeltaR(gen3))
      drlist.append(gen1.DeltaR(gen4))
      drlist.append(gen2.DeltaR(gen3))
      drlist.append(gen2.DeltaR(gen4))
      drlist.append(gen3.DeltaR(gen4)) 
 
      for d in drlist:
          if d < 0.1:
             fatphoton.append(1)
          
      
      if fatphoton.count(1) == 0:
         category = 4
      elif fatphoton.count(1) ==1 :
         category = 3
      elif fatphoton.count(1) ==2:
         category = 2

      h_len_cat.Fill(category)

      if category==4:
         #print " Number of genphos ", len(Genphos)
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
      
         h_gen1_pt.Fill(gen1.Pt())#,gen1.Pt()>30)
         #UnderOverFlow(h_gen1_pt)
         h_gen2_pt.Fill(gen2.Pt())
         #UnderOverFlow(h_gen2_pt)
         h_gen3_pt.Fill(gen3.Pt())
         #UnderOverFlow(h_gen3_pt)
         h_gen4_pt.Fill(gen4.Pt())
         #UnderOverFlow(h_gen4_pt)
         h_gen1_eta.Fill(abs(gen1.Eta()))
         h_gen1_etaabs.Fill(abs(gen1.Eta()))
         #UnderOverFlow(h_gen1_eta)
         h_gen2_eta.Fill(abs(gen2.Eta()))
         h_gen2_etaabs.Fill(abs(gen2.Eta()))
         #UnderOverFlow(h_gen2_eta)
         h_gen3_eta.Fill(abs(gen3.Eta()))
         h_gen3_etaabs.Fill(abs(gen3.Eta()))
         #UnderOverFlow(h_gen3_eta)
         h_gen4_eta.Fill(abs(gen4.Eta()))
         h_gen4_etaabs.Fill(abs(gen4.Eta()))
         #UnderOverFlow(h_gen4_eta)
         h_gen_maxeta.Fill(max(gen1.Eta(),gen2.Eta(),gen3.Eta(),gen4.Eta()))
         h_gen_mineta.Fill(min(gen1.Eta(),gen2.Eta(),gen3.Eta(),gen4.Eta()))
         h_gen_abs_maxeta.Fill(max(abs(gen1.Eta()),abs(gen2.Eta()),abs(gen3.Eta()),abs(gen4.Eta())))
         #UnderOverFlow(h_gen_abs_maxeta)
         h_gen1_phi.Fill(gen1.Phi())
         h_gen2_phi.Fill(gen2.Phi())
         h_gen3_phi.Fill(gen3.Phi())
         h_gen4_phi.Fill(gen4.Phi())
         h_2d.Fill(gen1.Pt(),gen1.DeltaR(gen4))
    
      
      if category == 3:
         fatpho = ""
         isopho1 = ""
         isopho2 = ""
         if gen1.DeltaR(gen2) < 0.1 and gen1.DeltaR(gen2) == min(drlist):
            fatpho = gen12
            isopho1 = gen3
            isopho2 = gen4
         elif gen1.DeltaR(gen3) < 0.1 and gen1.DeltaR(gen3) == min(drlist):
            fatpho = gen13
            isopho1 = gen2
            isopho2 = gen4
         elif gen1.DeltaR(gen4) < 0.1 and gen1.DeltaR(gen4) == min(drlist):
            fatpho = gen14
            isopho1 = gen2
            isopho2 = gen3
         elif gen2.DeltaR(gen3) < 0.1 and gen2.DeltaR(gen3) == min(drlist):
            fatpho = gen23
            isopho1 = gen1
            isopho2 = gen4
         elif gen2.DeltaR(gen4) < 0.1 and gen2.DeltaR(gen4) == min(drlist):
            fatpho = gen24
            isopho1 = gen1
            isopho2 = gen3
         else:
            fatpho = gen34
            isopho1 = gen1
            isopho2 = gen2
         genPggg = fatpho + isopho1 + isopho2
         h_fatpho_pt.Fill(fatpho.Pt())
         h_fatpho_pt_cut1.Fill(fatpho.Pt(),fatpho.Pt()>14)
         h_fatpho_pt_cut2.Fill(fatpho.Pt(),fatpho.Pt()>18)
         #UnderOverFlow(h_fatpho_pt)
         h_fatpho_eta.Fill(abs(fatpho.Eta()))
         #UnderOverFlow(h_fatpho_eta)
         h_isopho1_pt.Fill(isopho1.Pt())
         h_isopho1_pt_cut1.Fill(isopho1.Pt(),isopho1.Pt()>10)
         h_isopho1_pt_cut2.Fill(isopho1.Pt(),isopho1.Pt()>17)
         #UnderOverFlow(h_isopho1_pt)
         h_isopho2_pt.Fill(isopho2.Pt())
         h_isopho1_pt_cut1.Fill(isopho2.Pt(),isopho2.Pt()>8)
         h_isopho2_pt_cut2.Fill(isopho2.Pt(),isopho2.Pt()>8)
         #UnderOverFlow(h_isopho2_pt)
         h_fatpho_mass.Fill(fatpho.M())
         h_isopho1_mass.Fill(isopho1.M())
         h_isopho2_mass.Fill(isopho2.M())
         h_isopho1_eta.Fill(abs(isopho1.Eta()))
         h_isopho2_eta.Fill(abs(isopho2.Eta()))
         h_tpmass_3g.Fill(genPggg.M())
         #UnderOverFlow(h_isopho1_eta)
         #UnderOverFlow(h_isopho2_eta)

      if category == 2 :
         fatpho1 = ""
         fatpho2 = ""
         if gen1.DeltaR(gen2) < 0.1 and gen1.DeltaR(gen2) == min(drlist):
            fatpho1 = gen12
            fatpho2 = gen34
         elif gen1.DeltaR(gen3) < 0.1 and gen1.DeltaR(gen3) == min(drlist):
            fatpho1 = gen13
            fatpho2 = gen24
         elif gen1.DeltaR(gen4) < 0.1 and gen1.DeltaR(gen4) == min(drlist):
            fatpho1 = gen14
            fatpho2 = gen23
         elif gen2.DeltaR(gen3) < 0.1 and gen2.DeltaR(gen3) == min(drlist):
            fatpho1 = gen23
            fatpho2 = gen14
         elif gen2.DeltaR(gen4) < 0.1 and gen2.DeltaR(gen4) == min(drlist):
            fatpho1 = gen24
            fatpho2 = gen13
         else:
            fatpho1 = gen34
            fatpho2 = gen12
         genPgg = fatpho1 + fatpho2
         h_fatpho1_pt.Fill(fatpho1.Pt())
         h_fatpho2_pt.Fill(fatpho2.Pt())
         h_fatpho1_eta.Fill(abs(fatpho1.Eta()))
         h_fatpho2_eta.Fill(abs(fatpho2.Eta()))
         h_fatpho1_mass.Fill(fatpho1.M())
         h_fatpho2_mass.Fill(fatpho2.M())
         h_tpmass_2g.Fill(genPgg.M())
         #UnderOverFlow(h_fatpho1_pt)
         #UnderOverFlow(h_fatpho2_pt)
         #UnderOverFlow(h_fatpho1_eta)
         #UnderOverFlow(h_fatpho2_eta)
  
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
   h_gen1_etaabs.Write()
   h_gen2_etaabs.Write()
   h_gen3_etaabs.Write()
   h_gen4_etaabs.Write()
   h_gen_maxeta.Write()
   h_gen_mineta.Write()
   h_gen_abs_maxeta.Write()
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
   h_dr12_gen.Write()
   h_dr13_gen.Write()
   h_dr14_gen.Write()
   h_dr23_gen.Write()
   h_dr24_gen.Write()
   h_dr34_gen.Write()
   h_len_cat.Write()
   h_fatpho_pt.Write()
   h_fatpho_pt_cut1.Write()
   h_fatpho_pt_cut2.Write()
   h_fatpho_eta.Write()
   h_isopho1_pt.Write()
   h_isopho1_pt_cut1.Write()
   h_isopho1_pt_cut2.Write()
   h_isopho2_pt.Write()
   h_isopho2_pt_cut1.Write()
   h_isopho2_pt_cut2.Write()
   h_isopho1_eta.Write()
   h_isopho2_eta.Write()
   h_fatpho1_pt.Write()
   h_fatpho2_pt.Write()
   h_fatpho1_eta.Write()
   h_fatpho2_eta.Write()
   h_tpmass_3g.Write()
   h_tpmass_2g.Write()
   h_fatpho_mass.Write()
   h_fatpho1_mass.Write()
   h_fatpho2_mass.Write()

   outRoot.Close()
  # .! rootls -1 myfirstfile.root


if __name__ == "__main__":
   main(sys.argv[1:])



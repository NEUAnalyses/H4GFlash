from ROOT import *
from array import array

files = [
#"FlatTrees/FatPho0p1_Match0p15/eff_m_0p1.root",
#"FlatTrees/FatPho0p1_Match0p15/eff_m_1.root",
#"FlatTrees/FatPho0p1_Match0p15/eff_m_5.root",
"FlatTrees/FatPho0p1_Match0p15/eff_m_10.root",
"FlatTrees/FatPho0p1_Match0p15/eff_m_15.root",
"FlatTrees/FatPho0p1_Match0p15/eff_m_20.root",
"FlatTrees/FatPho0p1_Match0p15/eff_m_25.root",
"FlatTrees/FatPho0p1_Match0p15/eff_m_30.root",
"FlatTrees/FatPho0p1_Match0p15/eff_m_35.root",
"FlatTrees/FatPho0p1_Match0p15/eff_m_40.root",
"FlatTrees/FatPho0p1_Match0p15/eff_m_45.root",
"FlatTrees/FatPho0p1_Match0p15/eff_m_50.root",
"FlatTrees/FatPho0p1_Match0p15/eff_m_55.root",
"FlatTrees/FatPho0p1_Match0p15/eff_m_60.root"
]

masses = [10, 15, 20, 25, 35, 40, 45, 50, 55, 60]
#masses = [0.1, 1, 5, 10, 15, 20, 25, 30, 35, 40, 45,  50, 55, 60]

cuts = [
#["cuta==1", [] ],
#["cutc==1", [] ],
#["cutd==1", [] ],
#["cute==1", [] ]
["cut0==1", [] ],
["cut1==1", [] ],
["cut2==1", [] ],
        #["cut3==1", [] ],
#["cut4==1", [] ],
#["cut5==1", [] ],
#["cut3==1", [] ],
#["cut7==1", [] ],
#["cut8==1", [] ],
        #["cut9==1", [] ],
#["cut7==1", [] ],
#["cut10==1", [] ],
#["cut11==1", [] ],
#["cut9==1", [] ],
#["cut13==1", [] ],
#["cut14==1", [] ],
        #["cut20==1", [] ]
]

for i,m in enumerate(masses):
   for c in cuts:
      tch = TChain("H4GEff")
      tch.AddFile(files[i])
      totevs = tch.Draw("totevs", "1>0")
      thiscut = tch.Draw("totevs", c[0])
      thiseff = float(thiscut)/float(totevs)
      c[1].append(thiseff)


cols = [6, 2, 4]#, 6,kGreen+3,  kOrange+2, 9, 30, 49,]
styls = [ 24,25, 26]#, 27,28, 30, 32, 31, 33]
#cutNames = [ "#events that have passed all pre-selections", "#events with 2 photons", "#events with 3 photons",  "#events with > 3 photons"]#, "4#gamma-id", "4#gamma-id + Offline Trigger like cuts"]
#cutNames = ["=2#gamma","=3#gamma","=>4#gamma","=2#gamma-id",  "=3#gamma-id", "=>4#gamma-id", "=2#gamma-id+Pre-Sel", "=3#gamma-id+Pre-Sel","=>4#gamma-id+Pre-Sel"]
#cutNames = [">=4#gamma+pt+eta",">=4#gamma+pt+eta+MVA",">=4#gamma+pt+eta+MVA+preselections"]
#cutNames = ["==2 #gamma -id ","==3 #gamma -id","=>4  #gamma -id","==2 #gamma -id+preselections","==3 #gamma -id+preselections","=>4 #gamma -id+preselections"]
cutNames = ["Events w/ good photons","Events w/ good photons + pre-selections","Events w/ at least 4 photons"]
#cutNames = ["=>4#gamma","=>4#gamma+ID","=4#gamma+ID+Pre-Sel"]

c0 = TCanvas('a', 'a', 3000, 1500)
#c0.SetLogy()
#c0.SetGrid()
leg = TLegend(0.72, 0.1012, 0.8992, 0.8985)
#leg.SetHeader("Selection Steps")
leg.SetTextSize(0.03)
leg.SetFillStyle(0)
leg.SetBorderSize(0)
for i,c in enumerate(cuts):
   gr = TGraph(len(masses), array('d', masses), array('d', c[1]))
   c.append(gr)
   leg.AddEntry(c[2], cutNames[i], "lp")
   c[2].SetLineColor(cols[i])
   c[2].SetMarkerColor(cols[i])
   c[2].SetMarkerStyle(styls[i])
   c[2].SetMarkerSize(2)
   if( i == 0 ): 
      c[2].Draw("APL")
      c[2].SetMaximum(1.0)
      c[2].SetMinimum(0.0001)
      c[2].GetXaxis().SetLimits(-1, 80)
      c[2].GetYaxis().SetTitle("Selection Efficiency")
      c[2].GetXaxis().SetTitle("Pseudo-Scalar Mass [GeV]")
      c[2].SetTitle()
      c0.Update()
   if( i > 0 ): c[2].Draw("PL")
leg.Draw()
c0.SaveAs("forprelim_eff.pdf")

from PlotterTools import *
from ROOT import *

gStyle.SetOptStat(0)
for v in Vars:
   hists = []
   leg = TLegend(0.6, 0.7, 0.89, 0.89)
   leg.SetBorderSize(0)
   Max = -0.
   for fi,f in enumerate(Files):
      #print "Hello"
      ch = TChain('H4GSel')
      ch.Add(f[0])
      hname = v[1]+'_'+str(fi)
      h = TH1F(hname, v[2], v[3], v[4], v[5])
      ch.Draw(v[0]+'>>'+hname)
      #h.Sumw2()
      total = h.Integral()
      h.Scale(float(f[4])/float(total))
      h.SetLineColor(f[2])
      h.SetLineWidth(3)
      h.SetFillColor(f[3])
      hists.append([h,f[1]])
      if h.GetMaximum() > Max:
         Max = h.GetMaximum()
   print Max

   c0 = TCanvas('a', 'a', 800, 600)
   for fi,hh in enumerate(hists):
      leg.AddEntry(hh[0], hh[1], 'lf')
      hh[0].SetMaximum(Max*1.5)
      hh[0].SetMinimum(0.0001)
      if fi == 0:
         hh[0].Draw('h')
      if fi > 0:
         hh[0].Draw('h same')
   leg.Draw('same')
   c0.SaveAs(outputLoc+v[1]+'.pdf')
   c0.SaveAs(outputLoc+v[1]+'.png')
   c0.SetLogy()
   c0.SaveAs(outputLoc+v[1]+'_log.pdf')
   c0.SaveAs(outputLoc+v[1]+'_log.png')


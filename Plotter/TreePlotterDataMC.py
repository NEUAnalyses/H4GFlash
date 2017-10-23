## code to produce Data MC compariosn plots with signal on top

from PlotterToolsDataMC import *
from ROOT import *
from ROOT import TPad
#gStyle.SetOptStat(0)
#gROOT.SetBatch(kTRUE)
#first loop over all variables
for v in Vars:
   hists = []
   hists2 = []
   leg = TLegend(0.6, 0.8, 0.89, 0.89)
   
   leg.SetBorderSize(0)
   Max = -0.
   Max2 = -0.
   for fi,f in enumerate(MC):  ## get all MC plots, because they have to stacked!
      ch = TChain('H4GSel')
      ch.Add(f[0])
      hname = v[1]+'_'+str(fi)
      h = TH1F(hname, v[2], v[3], v[4], v[5])
      ch.Draw(v[0]+'>>'+hname,TCut(genCut)) ## add cut based on what you want to plot, blind or unblind or anything else
      #total1 = h.Integral
      #print total1
      h.Scale(float(f[4]),"nosw2")
      #h.Scale(1/float(h.Integral()))
      h.SetLineColor(f[2])
      h.SetLineWidth(2)
      h.SetFillColor(f[3])
      h.Sumw2()
      mc_copy = h.Clone("copy")
      hists.append([h,ch,f[1]])
      if h.GetMaximum() > Max:
         Max = h.GetMaximum()
      #hnew = h.Clone("hnew")
      #hnew.Add(hnew)
      #print "Scale Factor",h.Integral()
   #hnew = h[1].Clone("hnew")
   for ai,a in enumerate(hists):
       if ai==0 :
           hnew = a[0].Clone("hnew")
           hnew.Draw()      


 
   for di,d in enumerate(Data):  ## now get data
      ch2 = TChain('H4GSel')
      ch2.Add(d[0])
      hname2 = v[1]+'_'+str(di)
      h2 = TH1F(hname2,v[2],v[3],v[4],v[5])
      ch2.Draw(v[0]+'>>'+hname2,TCut(BlindCut))
      h2.SetMarkerStyle(20)
      h2.GetYaxis().SetTitle('Normalized Yields')
      h2.SetLineColor(1)
      h2.SetLineWidth(2)
      h2.Sumw2()
   for si,s in enumerate(Signal1):   ##plot signal on top
      ch3 = TChain('H4GSel')
      ch3.Add(s[0])
      hname3 = v[1]+'_'+str(si)
      h3 = TH1F(hname3,v[2],v[3],v[4],v[5])
      ch3.Draw(v[0]+'>>'+hname3)#,TCut(genCut))
      #h3.Sumw2()
      #total2 = h3.Integral()
      #print total2
      h3.Scale(float(s[3]))
      #h3.Scale(1/float(total2))
      h3.SetLineColor(s[2])
      #h3.SetFillColor(s[2])
      h3.SetLineWidth(2)
      #h3.SetFillStyle(1001)

   for si2,s2 in enumerate(Signal2):   ##plot signal on top
      ch4 = TChain('H4GSel')
      ch4.Add(s2[0])
      hname4 = v[1]+'_'+str(si2)
      h4 = TH1F(hname4,v[2],v[3],v[4],v[5])
      ch4.Draw(v[0]+'>>'+hname4)#,TCut(genCut))
      #h3.Sumw2()
      total3 = h4.Integral()
      #h4.Scale(1/float(total3))
      h4.Scale(float(s2[3]))
      h4.SetLineColor(s2[2])
      #h3.SetFillColor(s[2])
      h4.SetLineWidth(2)
      #h3.SetFillStyle(1001)
   for si3,s3 in enumerate(Signal3):   ##plot signal on top
      ch5 = TChain('H4GSel')
      ch5.Add(s3[0])
      hname5 = v[1]+'_'+str(si3)
      h5 = TH1F(hname5,v[2],v[3],v[4],v[5])
      ch5.Draw(v[0]+'>>'+hname5)#,TCut(genCut))
      #h3.Sumw2()
      total4 = h5.Integral()
      #h5.Scale(1/float(total4))
      h5.Scale(float(s3[3]))
      h5.SetLineColor(s3[2])
      #h3.SetFillColor(s[2])
      h5.SetLineWidth(2)
      #h3.SetFillStyle(1001)
   for si4,s4 in enumerate(Signal4):   ##plot signal on top
      ch6 = TChain('H4GSel')
      ch6.Add(s4[0])
      hname6 = v[1]+'_'+str(si4)
      h6 = TH1F(hname6,v[2],v[3],v[4],v[5])
      ch6.Draw(v[0]+'>>'+hname6)#,TCut(genCut))
      #h3.Sumw2()
      total5 = h6.Integral()
      #h6.Scale(1/float(total5))
      h6.Scale(float(s4[3]))
      h6.SetLineColor(s4[2])
      #h3.SetFillColor(s[2])
      h6.SetLineWidth(2)
      #h3.SetFillStyle(1001)

 
   c0 = TCanvas('a','a',800,2000)   ##now starts the drawing part, start by stacking all the MC up + add a ratio plot
   SetOwnership(c0,False) ## this takes care of memory leak issues --> segmentation faults
   #p1 = TPad('p1','p1',0,0.25,1,1)
   #SetOwnership(p1,False)
   #p2 = TPad('p2','p2',0,0,1,0.25)
   #SetOwnership(p2,False)

   ## Plot MC + Data +Signal on pad1

   #p1.Draw()
   #p2.Draw()
   
   #p1.cd()
   #p1.SetBottomMargin(0)
   
   s = THStack("s","")
   for fi,hh in enumerate(hists):
      #leg.AddEntry(hh[0], hh[2], 'lf')
      s.Add(hh[0])
      #s.Add(h3)
      hh[0].SetMaximum(Max*1.5)
      hh[0].SetMinimum(0.0001)
      if fi == 0:
         hh[0].Draw('')
      if fi > 0:
         hh[0].Draw('same')
      if fi == 0:
         leg.AddEntry(hh[0],hh[2],'lf')
      if fi == 2:
         leg.AddEntry(hh[0],hh[2],'lf')
      if fi == 5:
         leg.AddEntry(hh[0],hh[2],'lf')
      #h_err = TH1F(h_err, h_err, 35, 100,180)
      #h_err.Add(hh[0])
      #h_err.Add(hh[1])
      #h_err.Add(hh[2])
   #s.Add(h3)   
   s.Draw("hist E1")
   s.GetXaxis().SetTitle(v[6])
   s.GetYaxis().SetTitle('Normalized Yields')
   s.GetYaxis().SetTitleOffset(1.6)
   s.SetMaximum(100000)
   h2.Draw('p same')
   #mc_copy.Draw('same') 
   #ratio.Draw('p')
   #mc_copy.Draw()
   h3.Draw('same')
   h4.Draw('same')
   h5.Draw('same')
   h6.Draw('same')
   ## add text on top of the plot
   #l = TPaveText(-0.9,0.5,0.9,0.95)
   #l.AddText('Blah')
   #l.Draw('same')


   leg.SetNColumns(2)
   
   #leg.AddEntry(h2,"Data",'lp')
   leg.AddEntry(h3,"SigX10 m(a)=60GeV",'lf')
   leg.AddEntry(h4,"SigX10 m(a)=45GeV",'lf')
   leg.AddEntry(h5,"SigX10 m(a)=25GeV",'lf')
   leg.AddEntry(h6,"SigX10 m(a)=10GeV",'lf')

   leg.SetTextFont(42)
   #leg.SetTextSize(0.2)
   leg.SetFillStyle(0)  
   leg.Draw('same')
 
   tlatex = TLatex()  ## Add text like CMS preliminary
   tlatex.SetNDC()
   tlatex.SetTextAngle(0)
   tlatex.SetTextColor(kBlack)
   tlatex.SetTextFont(63)
   tlatex.SetTextAlign(11)
   tlatex.SetTextSize(25)
   tlatex.DrawLatex(0.11,0.91,"CMS")
   tlatex.SetTextFont(53)
   tlatex.DrawLatex(0.18,0.91,"Simulation")
   tlatex.SetTextFont(43)
   tlatex.SetTextSize(23)
   Lumi = "35.87" + " fb^{-1} (13TeV)"
   tlatex.SetTextAlign(31)
   #tlatex.DrawLatex(0.9,0.91,Lumi)
   tlatex.SetTextAlign(11)  
   c0.Update()
   #c0.SetBatch(kTrue) 
   #p1.SetGridx()
   #p2.SetGridy()
   #p2.cd()
   #p2.SetGridy()
   #p2.SetGridx()
   #ratio.Divide(mc_copy)
   #ratio.Draw()
   #ratio.Print("all")
   

   #l = TPaveText(-0.9,0.5,0.9,0.95)
   #l.AddText('Blah')
   #l.Draw('same')
   #p2.Draw()
   #p1.Draw()
   #c0.Update()
   #Save the canvas
   c0.SaveAs(outputLoc+v[1]+'.pdf')
   print "Plot was saved"
   c0.SaveAs(outputLoc+v[1]+'.png')
   print "plot saved again!"
   c0.SetLogy()
   c0.SaveAs(outputLoc+v[1]+'_log.pdf')
   c0.SaveAs(outputLoc+v[1]+'_log.png')

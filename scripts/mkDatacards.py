#!/usr/bin/env python


## 
## code to produce a datacard
## 

import os
import os.path
import optparse
from ROOT import *
import ROOT


if __name__ == '__main__':
  
  print '''
--------------------------------------------------------------------------------------------------

  __ \          |                                 |       \  |         |                
  |   |   _` |  __|   _` |   __|   _` |   __|  _` |      |\/ |   _` |  |  /   _ \   __| 
  |   |  (   |  |    (   |  (     (   |  |    (   |      |   |  (   |    <    __/  |    
 ____/  \__,_| \__| \__,_| \___| \__,_| _|   \__,_|     _|  _| \__,_| _|\_\ \___| _|    
                                                                                
--------------------------------------------------------------------------------------------------
'''    
  
  
  
  usage = 'usage: %prog [options]'
  parser = optparse.OptionParser(usage)
  
  parser.add_option('--tag'                , dest='tag'               , help='Tag used for the shape file name'           , default=None)
  parser.add_option('--sigset'             , dest='sigset'            , help='Signal samples [SM]'                        , default='SM')
  parser.add_option('--outputDirDatacard'  , dest='outputDirDatacard' , help='output directory'                           , default='./')
  parser.add_option('--inputFile'          , dest='inputFile'         , help='input directory'                            , default='./input.root')
  parser.add_option('--structureFile'      , dest='structureFile'     , help='file with datacard configurations'          , default=None )
  parser.add_option('--nuisancesFile'      , dest='nuisancesFile'     , help='file with nuisances configurations'         , default=None )
  parser.add_option('--cutsFile'           , dest='cutsFile'          , help='file with cuts configurations'         , default=None )
  parser.add_option('--samplesFile'        , dest='samplesFile'       , help='file with samples configurations'         , default=None )
        
  (opt, args) = parser.parse_args()
  
  # get the cuts from cuts.py
  cuts = {}
  if opt.cutsFile == None :
     print " Please provide the cuts structure ... it is needed!" 
  elif os.path.exists(opt.cutsFile) :
    handle = open(opt.cutsFile,'r')
    exec(handle)
    handle.close()
  
  for cutName in cuts :
    print "cut = ", cutName, " :: ", cuts[cutName]
  
  
  # ~~~~ get nuisances like lumi blah blah
  nuisances = {}
  if opt.nuisancesFile == None :
     print " Please provide the nuisances structure if you want to add nuisances " 
  elif os.path.exists(opt.nuisancesFile) :
    handle = open(opt.nuisancesFile,'r')
    exec(handle)
    handle.close()
  
  # ~~~~ get samples : the signal and data files you want to work with
  samples = {}
  if opt.samplesFile == None :
     print " Please provide the samples file ... seriously no samples?? " 
  elif os.path.exists(opt.samplesFile) :
    handle = open(opt.samplesFile,'r')
    exec(handle)
    handle.close()
  
  
  #
  # After I got all configurations ...
  #
  
  #
  # ... now let's run ...
  #
  
  # setting up os things --create directory for data card etc
  if not os.path.isdir (opt.outputDirDatacard + "/") :
    os.mkdir(opt.outputDirDatacard + "/")
  
  ## now we go over all the cuts we encountered in the beginning --initiate empty lists --datas,signals,backgrounds for every cut
  #---- loop over "cuts"
  for cutName in cuts :
    
    #datas       = []
    #signals     = ['sig']
    #backgrounds = ['bkg']
    datas       = []
    signals     = []
    backgrounds = []
    

    # calculate yields for data, signal and background
    yieldsSig  = {}   ## these are dictinories (?)
    yieldsBkg  = {}
    yieldsData = {}
  
    #
    # to do it properly :-)
    #
    #yieldsData['data'] = 1.0
    #yieldsBkg['bkg'] = 10.3
    #yieldsSig['sig'] = 100.999
    

    for sampleName, sample in samples.iteritems():  # now going over every sample --this includes data, back and sig
      if sample['isData'] == 1 : ## self explanatory  -- just append data list with data sample name and similarly for back and sig
        datas.append(sampleName)
      elif sample['isSignal'] == 1 :
        signals.append(sampleName)
      elif sample['isSignal'] == 0 :
        backgrounds.append(sampleName)

    #
    # data and background are all merged into 1 single "sample"
    #
    trees_data = {}  ## again initialize dictionary
    for data in datas :  ## for every data sample in "datas" list
      print len(samples[data]['name']) ##  just get the "name" of the root file as input -- very clever python thing and basically just printing out how many files there 
      for itree in range(len(samples[data]['name'])):  ## looping over all the different input data files
        chain = ROOT.TChain('H4GSel')
        chain.Add(samples[data]['name'][itree])
        if 'trees' in trees_data.keys() :
          trees_data['trees'] .append(chain)
          if 'weights' in samples[data].keys() :
            trees_data['weights'].append(samples[data]['weights'][itree])
          else :
            trees_data['weights'].append('1')
        else :
          trees_data['trees'] = []
          trees_data['trees'].append(chain)
          trees_data['weights'] = []
          if 'weights' in samples[data].keys() :
            trees_data['weights'].append(samples[data]['weights'][itree])
          else :
            trees_data['weights'].append('1')
        
    #
    # background can be split into different samples, for some strange reasons ... optimization?
    #     
    
    dict_trees_background = {}
    for background in backgrounds :
      trees_background = {}
      for itree in range(len(samples[background]['name'])):
        chain = ROOT.TChain('H4GSel')
        chain.Add(samples[background]['name'][itree])
        if 'trees' in trees_background.keys() :
          trees_background['trees'] .append(chain)
          trees_background['weights'].append(samples[background]['weights'][itree])
        else :
          trees_background['trees'] = []
          trees_background['trees'].append(chain)
          trees_background['weights'] = []
          trees_background['weights'].append(samples[background]['weights'][itree])
      dict_trees_background[background] = trees_background

    #
    # signals can be split into different samples, since different production mechanisms
    #     
    dict_trees_signal = {}
    for signal in signals :
      trees_signal = {}
      for itree in range(len(samples[signal]['name'])):
        chain = ROOT.TChain('H4GSel')
        chain.Add(samples[signal]['name'][itree])
        if 'trees' in trees_signal.keys() :
          trees_signal['trees'] .append(chain)
          trees_signal['weights'].append(samples[signal]['weights'][itree])
        else :
          trees_signal['trees'] = []
          trees_signal['trees'].append(chain)
          trees_signal['weights'] = []
          trees_signal['weights'].append(samples[signal]['weights'][itree])
      dict_trees_signal[signal] = trees_signal

    
    
 
    #
    # now get the yields
    #

 ## at this step we calculate the yield -- how many events are there in the tree after weights and cuts are applied
    yieldsData['data'] = 0
    for itree in range(len(trees_data['trees'])) :
      yieldsData['data'] += (trees_data['trees'][itree]).GetEntries( '(' + trees_data['weights'][itree] + ') * (' + cuts[cutName] + ')' )
    print "Data Yield  ", yieldsData['data']
    for background in backgrounds :
      yieldsBkg[background] = 0.
      for itree in range(len(dict_trees_background[background]['trees'])) :
        yieldsBkg[background] += (dict_trees_background[background]['trees'][itree]).GetEntries( '(' + dict_trees_background[background]['weights'][itree]   + ') * (' + cuts[cutName] + ')'  )
    print "Background Yield  ", yieldsBkg[background]
    for signal in signals :
      yieldsSig[signal] = 0.
      for itree in range(len(dict_trees_signal[signal]['trees'])) :
        yieldsSig[signal] += (dict_trees_signal[signal]['trees'][itree]).GetEntries( '(' + dict_trees_signal[signal]['weights'][itree]  + ') * (' + cuts[cutName] + ')'   )
      
    print "Signal Yield  ",yieldsSig[signal]
    
    
    
    
    
    #
    # creates the workspaces
    #    source code from https://github.com/NEUAnalyses/H4GFlash/blob/master/bin/AnalysisFits.C
    #
    
    tagNameToAppearInDatacard = cutName
    print tagNameToAppearInDatacard
    if not os.path.isdir (opt.outputDirDatacard + "/" + cutName + "/") :
      os.mkdir(opt.outputDirDatacard + "/" + cutName + "/")
    if not os.path.isdir (opt.outputDirDatacard + "/" + cutName + "/" + "shapes/") :
      os.mkdir(opt.outputDirDatacard + "/" + cutName + "/" + "shapes/")
    
    name_root_file_with_workspace = "/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/t4gamma-supercut/shapes/w_t4gamma-supercut.root"

    root_file_with_workspace = ROOT.TFile (name_root_file_with_workspace, "RECREATE")
    
    w = ROOT.RooWorkspace("w")
    # create the variable
    w.factory( "tp_mass[100, 160]" )
    w.var( "tp_mass" ).SetTitle("tp_mass")
    w.var( "tp_mass" ).setUnit("GeV")
    #w.var( "tp_mass").setRange("reg1",100,115) 
    #w.var( "tp_mass").setRange("reg2",135,180)
    w.factory( "dp1_mass[0,200]" )
    w.factory( "dp2_mass[0,200]" )    
    #w.factory( "mean[4.03336e-02, 0.0001, 10]") 
    # the set of variables
    treeVars = ROOT.RooArgSet()
    treeVars.add( w.var( "tp_mass" ) )
    #frame = w.var( "tp_mass" ).frame()
    treeVars.add( w.var("dp1_mass") )    
    treeVars.add( w.var("dp2_mass") )
    #treeVars.add( w.var("mean") )
    data_RooDataSet = ROOT.RooDataSet( "data", "data", ROOT.RooArgSet( w.var( "tp_mass" ) ) )
    
    #RooArgList *mypdfs
    for itree in range(len(trees_data['trees'])) :
      
      data_RooDataSet_temp = ROOT.RooDataSet( "data", "data", (trees_data['trees'][itree]), treeVars)
      data_RooDataSet.append(data_RooDataSet_temp.reduce('(' + trees_data['weights'][itree] + ') * (' + cuts[cutName] + ')'))
      #c1 = TCanvas('c1','PDF Fits',200,10,700,500)
      #tp_mass = ROOT.RooRealVar("tp_mass","tp_mass",80,160)
      #frame = tp_mass.frame()
      #data.plotOn(frame)






    #signal_RooDataSet = ROOT.RooDataSet( "dataSig", "dataSig", ROOT.RooArgSet(m4g_RooRealVar) )
    #for signal in signals :
      #for itree in range(len(dict_trees_signal[signal]['trees'])) :
        #signal_RooDataSet_temp = ROOT.RooDataSet( "dataSig", "dataSig",  dict_trees_signal[signal]['weights'][itree], treeVars)
        #signal_RooDataSet.append(signal_RooDataSet_temp)

    getattr(w,'import')(data_RooDataSet)
    #getattr(ws,'import')(signal_RooDataSet)
    #ws.import(data_RooDataSet)
    #ws.import(signal_RooDataSet)

    # ~ create null pdf
    #w.factory("GenericPdf:step_pdf("step_pdf","step_pdf","(0.1*tp_mass)",{tp_mass})")  
    leftedge = 115
    rightedge = 135
    #w.factory("GenericPdf:step_pdf(step_pdf,step_pdf,tp_mass*0.1,{tp_mass,leftedge,rightedge))")
    c2 = TCanvas( 'c2', 'Example with Formula', 200, 10, 700, 500 )
    #func1 = TF1( 'func1','((x > 115) ? 0 : 0)',80,160)
    #func1 = TF1(
   # f =  TF1("f", "((x > 2) ? sin(x) : 0)", -10, 10) 
    func1 =  TF1("func1", "1 * ((x > 115 && x < 135) ? 0 : 1)", 80, 160)
    func2 =  TF1("func2", "1 * ((x < 135) ? 0 : 1)", 80, 160)
    func_null = TF1("func_null","func1-func2")
    func1.Draw()
    c2.Update()
    c2.SaveAs("null.png")
    # ~ Bernstein polynomials
    w.factory( "bern1_p0[0.2,-10,10]")
    w.factory( "bern1_p1[0.1,-10,10]")
    treeVars.add( w.var("bern1_p0") )
    treeVars.add( w.var("bern1_p1") )
    w.factory( "Bernstein:bkg_bern1_pdf(tp_mass,{bern1_p0,bern1_p1})")
    
    w.factory( "bern2_p0[0.3,-10,10]")
    w.factory( "bern2_p1[0.2,-10,10]")
    w.factory( "bern2_p2[0.1,-10,10]")    
    treeVars.add( w.var("bern2_p0") )
    treeVars.add( w.var("bern2_p1") )
    treeVars.add( w.var("bern2_p2") )
    w.factory( "Bernstein:bkg_bern2_pdf(tp_mass,{bern2_p0,bern2_p1,bern2_p2})")
    
    w.factory( "bern3_p0[0.3,-10,10]")
    w.factory( "bern3_p1[0.2,-10,10]")
    w.factory( "bern3_p2[0.1,-10,10]")
    w.factory( "bern3_p3[0.1,-10,10]")
    treeVars.add( w.var("bern3_p0") )
    treeVars.add( w.var("bern3_p1") )
    treeVars.add( w.var("bern3_p2") )
    treeVars.add( w.var("bern3_p3") )
    #Fit_bkg_bern3_pdf = ROOT.RooFitResult(w.factory( "Bernstein:bkg_bern3_pdf(tp_mass,{bern3_p0,bern3_p1,bern3_p2,bern3_p3})").fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE)))
    #w.factory( "RooEffProd:bkg_prod_pdf(w.factory( "Bernstein:bkg_bern1_pdf(tp_mass,{bern1_p0,bern1_p1}),w.factory( "Bernstein:bkg_bern2_pdf(tp_mass,{bern2_p0,bern2_p1,bern2_p2}))")    
    #w.factory( "RooEffProd:bkg_prod_pdf(func1,w.factory( "Bernstein:bkg_bern2_pdf(tp_mass,{bern2_p0,bern2_p1,bern2_p2})"))
    w.factory( "RooEffProd:bkg_prod_pdf(func2,func1)")
    w.factory( "bern4_p0[0.4,-10,10]")
    w.factory( "bern4_p1[0.3,-10,10]")
    w.factory( "bern4_p2[0.2,-10,10]")
    w.factory( "bern4_p3[0.1,-10,10]")
    w.factory( "bern4_p4[0.1,-10,10]")
    treeVars.add( w.var("bern4_p0") )
    treeVars.add( w.var("bern4_p1") )
    treeVars.add( w.var("bern4_p2") )
    treeVars.add( w.var("bern4_p3") )
    treeVars.add( w.var("bern4_p4") )
    #Fit_bkg_bern4_pdf = ROOT.RooFitResult(w.factory( "Bernstein:bkg_bern4_pdf(tp_mass,{bern4_p0,bern4_p1,bern4_p2,bern4_p3,bern4_p4})").fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE)))
    w.factory( "Bernstein:bkg_bern4_pdf(tp_mass,{bern4_p0,bern4_p1,bern4_p2,bern4_p3,bern4_p4})")
    
    w.factory( "bern5_p0[0.5,-10,10]")
    w.factory( "bern5_p1[0.4,-10,10]")
    w.factory( "bern5_p2[0.3,-10,10]")
    w.factory( "bern5_p3[0.2,-10,10]")
    w.factory( "bern5_p4[0.1,-10,10]")
    w.factory( "bern5_p5[0.1,-10,10]")
    treeVars.add( w.var("bern5_p0") )
    treeVars.add( w.var("bern5_p1") )
    treeVars.add( w.var("bern5_p2") )
    treeVars.add( w.var("bern5_p3") )
    treeVars.add( w.var("bern5_p4") )
    treeVars.add( w.var("bern5_p5") )
    #Fit_bkg_bern5_pdf = ROOT.RooFitResult(w.factory( "Bernstein:bkg_bern5_pdf(tp_mass,{bern5_p0,bern5_p1,bern5_p2,bern5_p3,bern5_p4,bern5_p5})").fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE)))
    w.factory( "Bernstein:bkg_bern5_pdf(tp_mass,{bern5_p0,bern5_p1,bern5_p2,bern5_p3,bern5_p4,bern5_p5})")

    w.factory( "bern6_p0[0.6,-10,10]")
    w.factory( "bern6_p1[0.5,-10,10]")
    w.factory( "bern6_p2[0.4,-10,10]")
    w.factory( "bern6_p3[0.3,-10,10]")
    w.factory( "bern6_p4[0.2,-10,10]")
    w.factory( "bern6_p5[0.1,-10,10]")
    w.factory( "bern6_p6[0.1,-10,10]")    
    treeVars.add( w.var("bern6_p0") )
    treeVars.add( w.var("bern6_p1") )
    treeVars.add( w.var("bern6_p2") )
    treeVars.add( w.var("bern6_p3") )
    treeVars.add( w.var("bern6_p4") )
    treeVars.add( w.var("bern6_p5") )
    treeVars.add( w.var("bern6_p6") ) 
    #Fit_bkg_bern6_pdf = ROOT.RooFitResult(w.factory( "Bernstein:bkg_bern6_pdf(tp_mass,{bern6_p0,bern6_p1,bern6_p2,bern6_p3,bern6_p4,bern6_p5,bern6_p6})").fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE)))
    w.factory( "Bernstein:bkg_bern6_pdf(tp_mass,{bern6_p0,bern6_p1,bern6_p2,bern6_p3,bern6_p4,bern6_p5,bern6_p6})")
    
    # ~ Chebychev 
    w.factory( "cheb[0.01,-10,10]")
    treeVars.add( w.var("cheb") )
    #w.factory( "Chebychev:bkg_cheb_pdf(tp_mass,cheb)")
    
    # ~ Power Law
    w.factory( "pow[-0.001,-0.01,0.01]")
    treeVars.add( w.var("pow") )

 
    # ~ exponential
    w.factory( "exp1_lambda1[0.1, 0.0001, 100]")
    treeVars.add( w.var("exp1_lambda1"))
    w.factory( "exp1_lambda2[0.1, 0.00001, 100]")
    treeVars.add( w.var("exp1_lambda2"))     
    w.factory( "frac1[0.005, 0.0001, 80.]")
    treeVars.add( w.var("frac1"))
    #w.factory(EXPR::exp(exp1_lambda1*tp_mass)-frac1*exp(exp1_lambda2*tp_mass))
    #w.factory( "frac2[-4.29406e-01, -100, 0.0001]")
    #treeVars.add( w.var("frac2"))    
    #w.factory( "Exponential:bkg_exp2_pdf(tp_mass, a2[4.88218e-01, 0.0001, 10])")
    #w.factory( "Exponential:bkg_exp1_pdf(tp_mass,exp1_lambda)"  )
    #w.factory( "Exponential:bkg_exp2_pdf(tp_mass,exp2_lambda)"  )    
    #w.factory( "SUM:bkg_exp_sum_pdf(frac1*bkg_exp1_pdf,frac2*bkg_exp2_pdf)") 
    #w.factory( "Gaussian:sig_pdf(tp_mass, mass[125, 110, 130], sigma[4, 2, 10])")
    #mypdfs.add(w.factory( "Exponential:bkg_exp_pdf(tp_mass, a1[4.03336e-02, 0.0001, 10])"))
    #mypdfs.add(w.factory( "Exponential:bkg_exp2_pdf(tp_mass, a2[4.88218e-01, 0.0001, 10])"))
    #mypdfs.add(w.factory( "Exponential:bkg_pdf(tp_mass, a[-0.5,-2,-0.2])"  ))
    #print "These are all the pdf's  ", mypdfs
    FitResults = []
    FitResults.append(['bkg_bern1_pdf',"Bernstein:bkg_bern1_pdf(tp_mass,{bern1_p0,bern1_p1})",kBlue])
    FitResults.append(['bkg_bern2_pdf',"Bernstein:bkg_bern2_pdf(tp_mass,{bern2_p0,bern2_p1,bern2_p2})",kMagenta])
    FitResults.append(['bkg_bern3_pdf',"Bernstein:bkg_bern3_pdf(tp_mass,{bern3_p0,bern3_p1,bern3_p2,bern3_p3})",kGreen+1])
    FitResults.append(['bkg_bern4_pdf',"Bernstein:bkg_bern4_pdf(tp_mass,{bern4_p0,bern4_p1,bern4_p2,bern4_p3,bern4_p4})",kOrange+7])
    FitResults.append(['bkg_bern5_pdf',"Bernstein:bkg_bern5_pdf(tp_mass,{bern5_p0,bern5_p1,bern5_p2,bern5_p3,bern5_p4,bern5_p5})",kAzure+10])
    FitResults.append(['bkg_bern6_pdf',"Bernstein:bkg_bern6_pdf(tp_mass,{bern6_p0,bern6_p1,bern6_p2,bern6_p3,bern6_p4,bern6_p5,bern6_p6})",kBlack])
    FitResults.append(['bkg_cheb_pdf', "Polynomial:bkg_cheb_pdf(tp_mass,cheb)",kRed])
    #FitResults.append(['bkg_pow_pdf',  ROOT.RooFitResult(w.factory( "PowerLawSum:bkg_pow_pdf(tp_mass,pow)").fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE)))])
    c1 = TCanvas('c1','PDF Fits',200,10,700,500)
    leg = TLegend(0.5,0.55,0.92,0.88)
    nbins = ROOT.RooBinning(-15,15)
    frame = w.var( "tp_mass" ).frame()
    data_RooDataSet.plotOn(frame)#,CutRange("reg1"))  
    #w.factory("PROD:bern12_pdf(bkg_bern1_pdf,bkg_bern2_pdf)")  
    for fi, f in enumerate(FitResults):
        #stat=f[1].status()
        #minnll=f[1].minNll()
        ROOT.RooFitResult(w.factory( f[1]).fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE)))
        stat = ROOT.RooFitResult(w.factory( f[1]).fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE))).status()
        minnll = ROOT.RooFitResult(w.factory( f[1]).fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE))).minNll()
        w.factory(f[1]).plotOn(frame,RooFit.LineColor(f[2]))
        leg.AddEntry(w.factory(f[1]),f[0],'lf')
    frame.Draw()
    leg.Draw('same')
    c1.SaveAs("test.png")
    cat = ROOT.RooCategory('pdf index','index of the active pdf')

    mypdfs = ROOT.RooArgList()
    mypdfs.add(w.factory( "Bernstein:bkg_bern1_pdf(tp_mass,{bern1_p0,bern1_p1})"))
    mypdfs.add(w.factory( "Bernstein:bkg_bern2_pdf(tp_mass,{bern2_p0,bern2_p1,bern2_p2})"))
    mypdfs.add(w.factory( "Bernstein:bkg_bern3_pdf(tp_mass,{bern3_p0,bern3_p1,bern3_p2,bern3_p3})"))
    mypdfs.add(w.factory( "Bernstein:bkg_bern4_pdf(tp_mass,{bern4_p0,bern4_p1,bern4_p2,bern4_p3,bern4_p4})"))
    mypdfs.add(w.factory( "Bernstein:bkg_bern5_pdf(tp_mass,{bern5_p0,bern5_p1,bern5_p2,bern5_p3,bern5_p4,bern5_p5})"))
    mypdfs.add(w.factory( "Bernstein:bkg_bern6_pdf(tp_mass,{bern6_p0,bern6_p1,bern6_p2,bern6_p3,bern6_p4,bern6_p5,bern6_p6})"))
    multipdf = ROOT.RooMultiPdf("multipdf","all pdfs",cat,mypdfs)  
  
    #frame.Draw()
    #c1.SaveAs("test.png") 
      
    # ~~ Lets talk about signal! -- Sum of Gaussians
    #w.factory( "Gaussian:sig_gaus1_pdf(tp_mass, mass[125, 110, 130], sigma[2, 4, 10])")
    w.factory( "mean[4.03336e-02, 0.0001, 10]") 

      
     
      
    # save the workspace
    w.Write()
    root_file_with_workspace.Close()
    

    
    
    
    
    
    #
    # now write the datacard
    #
    
    
    if not os.path.isdir (opt.outputDirDatacard + "/" + cutName) :
      os.mkdir(opt.outputDirDatacard + "/" + cutName)
    
    
    
    cardPath = opt.outputDirDatacard + "/" + cutName + "/datacard.txt"
    print 'Writing to ' + cardPath 
    card = open( cardPath ,"w")
    card.write('## Parametric shape input card\n')
    
    card.write('imax 1 number of channels\n')
    card.write('jmax * number of background\n')
    card.write('kmax * number of nuisance parameters\n') 
    
    card.write('shapes  bkg      ' + tagNameToAppearInDatacard + '  '  + name_root_file_with_workspace  + '  w:multipdf \n')
    card.write('shapes  sig      ' + tagNameToAppearInDatacard + '  '  + name_root_file_with_workspace  + '  w:sig_pdf \n')
    card.write('shapes  data_obs ' + tagNameToAppearInDatacard + '  '  + name_root_file_with_workspace  + '  w:data \n')
     
    card.write('-'*100+'\n')
    card.write('bin         %s' % tagNameToAppearInDatacard+'\n')    
    card.write('observation -1'+'\n')
    card.write('-'*100+'\n')

   
    totalNumberSamples = len(yieldsSig) + len(yieldsBkg)
    columndef = 10
    
    # adapt column length to long bin names            
    if len(tagNameToAppearInDatacard) >= (columndef - 5) :
      columndef = len(tagNameToAppearInDatacard) + 7
    
    
    card.write('bin'.ljust(80) + ''.join( [tagNameToAppearInDatacard.ljust(columndef) * totalNumberSamples])+'\n')
    
    card.write('process'.ljust(80))
    card.write(''.join([name.ljust(columndef) for name in signals]))
    card.write(''.join([name.ljust(columndef) for name in backgrounds]))
    card.write('\n')
    
    card.write('process'.ljust(80))
    card.write(''.join([('%d' % -iSample   ).ljust(columndef) for iSample in range(len(signals))     ]))
    card.write(''.join([('%d' % (iSample+1)).ljust(columndef) for iSample in range(len(backgrounds)) ]))
    card.write('\n')
    
    card.write('rate'.ljust(80))
    card.write(''.join([('%-.4f' % yieldsSig[name]).ljust(columndef) for name in signals    ]))
    card.write(''.join([('%-.4f' % yieldsBkg[name]).ljust(columndef) for name in backgrounds]))
    card.write('\n')
    
    card.write('-'*100+'\n')
    
    
    
    
    
    
    ## add nuisances
    
    ## first the lnN nuisances
    for nuisanceName, nuisance in nuisances.iteritems():
      
      # check if a nuisance can be skipped because not in this particular cut
      use_this_nuisance = False
      if  'cuts' in nuisance.keys() :
        for Cuts_where_to_use_nuisance  in   nuisance['cuts'] :
          if Cuts_where_to_use_nuisance == cutName :
            # use this niusance
            use_this_nuisance = True
      else :
        # default is use the nuisance everywhere
        use_this_nuisance = True 
      
      if use_this_nuisance :

        if 'type' in nuisance.keys() : # some nuisances may not have "type" ... why?
            #print "nuisance[type] = ", nuisance ['type']
            if nuisance ['type'] == 'lnN' or nuisance ['type'] == 'lnU' :
              card.write((nuisance['name']).ljust(80-20))
              card.write((nuisance ['type']).ljust(20))
              if 'all' in nuisance.keys() and nuisance ['all'] == 1 : # for all samples
                card.write(''.join([(' %s ' % nuisance['value']).ljust(columndef) for name in signals      ]))
                card.write(''.join([(' %s ' % nuisance['value']).ljust(columndef) for name in backgrounds  ]))
                card.write('\n')
              else :
                # apply only to selected samples
                for sampleName in signals:
                  if sampleName in nuisance['samples'].keys() :
                    card.write(('%s' % nuisance['samples'][sampleName]).ljust(columndef))
                  else :
                    card.write(('-').ljust(columndef))
                for sampleName in backgrounds:
                  if sampleName in nuisance['samples'].keys() :
                    card.write(('%s' % nuisance['samples'][sampleName]).ljust(columndef))
                  else :
                    card.write(('-').ljust(columndef))






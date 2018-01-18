#!/usr/bin/env python


## 
## code to produce a datacard
## 

import os
import os.path
import optparse
from ROOT import *
import ROOT
import sys
sys.modules['RooFit'] = ROOT.RooFit
from RooFit import *




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
      print "The number of Data files ",  len(samples[data]['name']) ##  just get the "name" of the root file as input -- very clever python thing and basically just printing out how many files there 
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
      print "The number of backgorunds ", len(samples[background]['name'])
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

    trees_signal = {}  ## again initialize dictionary
    for signal in signals :  ## for every data sample in "datas" list
      print "The number of Signal files ",  len(samples[signal]['name']) ##  just get the "name" of the root file as input -- very clever python thing and basically just printing out how many files there 
      for itree in range(len(samples[signal]['name'])):  ## looping over all the different input data files
        chain = ROOT.TChain('H4GSel')
        chain.Add(samples[signal]['name'][itree])
        if 'trees' in trees_signal.keys() :
          trees_signal['trees'] .append(chain)
          if 'weights' in samples[signal].keys() :
            trees_signal['weights'].append(samples[signal]['weights'][itree])
          else :
            trees_signal['weights'].append('1')
        else :
          trees_signal['trees'] = []
          trees_signal['trees'].append(chain)
          trees_signal['weights'] = []
          if 'weights' in samples[signal].keys() :
            trees_signal['weights'].append(samples[signal]['weights'][itree])
          else :
            trees_signal['weights'].append('1')
    
    
 
    #
    # now get the yields
    #

 ## at this step we calculate the yield -- how many events are there in the tree after weights and cuts are applied
    yieldsData['data'] = 0
    for itree in range(len(trees_data['trees'])) :
      yieldsData['data'] += (trees_data['trees'][itree]).GetEntries( '(' + trees_data['weights'][itree] + ') * (' + cuts[cutName] + ')' )
    print "The Data Yield  ", yieldsData['data']
    for background in backgrounds :
      yieldsBkg[background] = 0.
      for itree in range(len(dict_trees_background[background]['trees'])) :
        yieldsBkg[background] += (dict_trees_background[background]['trees'][itree]).GetEntries( '(' + dict_trees_background[background]['weights'][itree]   + ') * (' + cuts[cutName] + ')'  )
    print "The Background Yield  ", yieldsBkg[background]
    #for signal in signals :
    yieldsSig[signal] = 0.
    for itree in range(len(trees_signal['trees'])) :
      yieldsSig[signal] += (trees_signal['trees'][itree]).GetEntries( '(' + trees_signal['weights'][itree]  + ') * (' + cuts[cutName] + ')'   )
      
    print "The Signal Yield  ",yieldsSig[signal] 
    
    
    
    
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
    
    name_root_file_with_workspace = "/afs/cern.ch/user/t/twamorka/CMSSW_8_1_0/src/HiggsAnalysis/CombinedLimit/t4gamma-supercut/shapes/w_t4gamma-supercut.root"

    root_file_with_workspace = ROOT.TFile (name_root_file_with_workspace, "RECREATE")
    
    w = ROOT.RooWorkspace("w")
    # create the variable
    w.factory( "tp_mass[100, 180]" )
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
    w.factory( "p1_full5x5_r9[0,5]")
    treeVars.add( w.var("p1_full5x5_r9") )
    
    data_RooDataSet = ROOT.RooDataSet( "data", "data", ROOT.RooArgSet( w.var( "tp_mass" ) ) )
    data_RooDataSet_sig = ROOT.RooDataSet( "sig", "sig", ROOT.RooArgSet( w.var("tp_mass" ) ) )
    #RooArgList *mypdfs
    #print "HELLOO", len(trees_data['trees'])
    for itree in range(len(trees_data['trees'])) :
      
      data_RooDataSet_temp = ROOT.RooDataSet( "data", "data", (trees_data['trees'][itree]), treeVars)
      data_RooDataSet.append(data_RooDataSet_temp.reduce('(' + trees_data['weights'][itree] + ') * (' + cuts[cutName] + ')'))
      #data_binnedclone = ROOT.RooDataSet(data_RooDataSet.binnedClone())
    for itree in range(len(trees_signal['trees'])) :

      data_RooDataSet_sig_temp = ROOT.RooDataSet( "signal", "signal", (trees_signal['trees'][itree]), treeVars)
      data_RooDataSet_sig.append(data_RooDataSet_sig_temp.reduce('(' + trees_signal['weights'][itree] + ') * (' + cuts[cutName] + ')'))
      #c1 = TCanvas('c1','PDF Fits',200,10,700,500)
      #tp_mass = ROOT.RooRealVar("tp_mass","tp_mass",80,160)
      #frame = tp_mass.frame()
      #data.plotOn(frame)


    getattr(w,'import')(data_RooDataSet)
    getattr(w,'import')(data_RooDataSet_sig)
    #getattr(ws,'import')(signal_RooDataSet)
    #ws.import(data_RooDataSet)
    #ws.import(signal_RooDataSet)

    # ~ create null pdf
    #w.factory( "high[1.]")
    #treeVars.add( w.var("high") )
    #w.factory( "low[0.]")
    #treeVars.add( w.var("low") )
    #w.factory( "RooFormulaVar:null_pdf(null_pdf,"@0*@1",RooArgList(high,low))")
    #RooFormulaVar = null_pdf("null_pdf","@0*@1",RooArgList(high,low))
    #null_pdf = ROOT.RooFormulaVar("null_pdf","@0*@1",RooArgList(high,low))   
    #x = ROOT.RooRealVar("x","x",-1.0,2.0)
    #stepbld = ROOT.AFitStepFunction(x,"pdf")
    #step = ROOT.RooAbsPdf(stepbld.getPdf())
    #w.factory("GenericPdf:step_pdf("step_pdf","step_pdf","(0.1*tp_mass)",{tp_mass})")  
    #leftedge = 115
    #rightedge = 135
    #w.factory("GenericPdf:step_pdf(step_pdf,step_pdf,tp_mass*0.1,{tp_mass,leftedge,rightedge))")
    #c2 = TCanvas( 'c2', 'Example with Formula', 200, 10, 700, 500 )
    #func1 = TF1( 'func1','((x > 115) ? 0 : 0)',80,160)
    #func1 = TF1(
   # f =  TF1("f", "((x > 2) ? sin(x) : 0)", -10, 10) 
    #func1 =  TF1("func1", "1 * ((x > 115 && x < 135) ? 0 : 1)", 80, 160)
    #func1.Draw()
    #c2.Update()
    #c2.SaveAs("null.png")
    #w.factory( "GenericPdf:bkg_null_pdf(null_pdf,null_pdf,tp_mass *0.1,tp_mass)")
    #w.factory( "GenericPdf:null_pdf(((tp_mass > 115 && tp_mass < 135) ? 0 : 1),tp_mass)")
    #print "HEYYYYYAAAAA"
    # ~ Bernstein polynomials
    w.factory( "bern1_p0[0.2,-5.,5.]")
    w.factory( "bern1_p1[0.2,-5.,5.]")
    treeVars.add( w.var("bern1_p0") )
    treeVars.add( w.var("bern1_p1") )
    w.factory( "Bernstein:bkg_bern1_pdf(tp_mass,{bern1_p0,bern1_p1})")
    #w.factory("RooEffProd:bkg_prod(func1,bkg_bern1_pdf)")
    w.factory( "bern2_p0[0.3,-5.,5.]")
    w.factory( "bern2_p1[0.3,-5.,5.]")
    w.factory( "bern2_p2[0.3,-5.,5.]")    
    treeVars.add( w.var("bern2_p0") )
    treeVars.add( w.var("bern2_p1") )
    treeVars.add( w.var("bern2_p2") )
    w.factory( "Bernstein:bkg_bern2_pdf(tp_mass,{bern2_p0,bern2_p1,bern2_p2})")
    
    #w.factory("RooEffProd:bkg_prod(bkg_bern1_pdf,bkg_bern2_pdf)")   ## ~~ Does this work ???
    #w.factory("RooEffProd:bkg_prod_2(bkg_bern1_pdf,bkg_null_pdf)")     
    w.factory( "bern3_p0[0.4,-5.,5.]")    
    w.factory( "bern3_p1[0.4,-5.,5.]")
    w.factory( "bern3_p2[0.4,-5.,5.]")
    w.factory( "bern3_p3[0.4,-5.,5.]")
    treeVars.add( w.var("bern3_p0") )
    treeVars.add( w.var("bern3_p1") )
    treeVars.add( w.var("bern3_p2") )
    treeVars.add( w.var("bern3_p3") )
    #Fit_bkg_bern3_pdf = ROOT.RooFitResult(w.factory( "Bernstein:bkg_bern3_pdf(tp_mass,{bern3_p0,bern3_p1,bern3_p2,bern3_p3})").fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE)))
    #w.factory( "RooEffProd:bkg_prod_pdf(w.factory( "Bernstein:bkg_bern1_pdf(tp_mass,{bern1_p0,bern1_p1}),w.factory( "Bernstein:bkg_bern2_pdf(tp_mass,{bern2_p0,bern2_p1,bern2_p2}))")    
    #w.factory( "RooEffProd:bkg_prod_pdf(func1,w.factory( "Bernstein:bkg_bern2_pdf(tp_mass,{bern2_p0,bern2_p1,bern2_p2})"))
    #w.factory( "RooEffProd:bkg_prod_pdf(func2,func1)")
    w.factory( "bern4_p0[0.5,-5.,5.]")
    w.factory( "bern4_p1[0.5,-10.,10.]")
    w.factory( "bern4_p2[0.5,-5.,5.]")
    w.factory( "bern4_p3[0.5,-5.,5.]")
    w.factory( "bern4_p4[0.5,-5.,5.]")
    treeVars.add( w.var("bern4_p0") )
    treeVars.add( w.var("bern4_p1") )
    treeVars.add( w.var("bern4_p2") )
    treeVars.add( w.var("bern4_p3") )
    treeVars.add( w.var("bern4_p4") )
    #Fit_bkg_bern4_pdf = ROOT.RooFitResult(w.factory( "Bernstein:bkg_bern4_pdf(tp_mass,{bern4_p0,bern4_p1,bern4_p2,bern4_p3,bern4_p4})").fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE)))
    w.factory( "Bernstein:bkg_bern4_pdf(tp_mass,{bern4_p0,bern4_p1,bern4_p2,bern4_p3,bern4_p4})")
    
    w.factory( "bern5_p0[0.6,-5.,5.]")
    w.factory( "bern5_p1[0.6,-5.,5.]")
    w.factory( "bern5_p2[0.6,-5.,5.]")
    w.factory( "bern5_p3[0.6,-5.,5.]")
    w.factory( "bern5_p4[0.6,-5.,5.]")
    w.factory( "bern5_p5[0.6,-5.,5.]")
    treeVars.add( w.var("bern5_p0") )
    treeVars.add( w.var("bern5_p1") )
    treeVars.add( w.var("bern5_p2") )
    treeVars.add( w.var("bern5_p3") )
    treeVars.add( w.var("bern5_p4") )
    treeVars.add( w.var("bern5_p5") )
    #Fit_bkg_bern5_pdf = ROOT.RooFitResult(w.factory( "Bernstein:bkg_bern5_pdf(tp_mass,{bern5_p0,bern5_p1,bern5_p2,bern5_p3,bern5_p4,bern5_p5})").fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE)))
    w.factory( "Bernstein:bkg_bern5_pdf(tp_mass,{bern5_p0,bern5_p1,bern5_p2,bern5_p3,bern5_p4,bern5_p5})")

    w.factory( "bern6_p0[0.7,-5.,5.]")
    w.factory( "bern6_p1[0.7,-10.,10.]")
    w.factory( "bern6_p2[0.7,-5.,5.]")
    w.factory( "bern6_p3[0.7,-5.,5.]")
    w.factory( "bern6_p4[0.7,-10.,10.]")
    w.factory( "bern6_p5[0.7,-5.,5.]")
    w.factory( "bern6_p6[0.7,-5,5]")    
    treeVars.add( w.var("bern6_p0") )
    treeVars.add( w.var("bern6_p1") )
    treeVars.add( w.var("bern6_p2") )
    treeVars.add( w.var("bern6_p3") )
    treeVars.add( w.var("bern6_p4") )
    treeVars.add( w.var("bern6_p5") )
    treeVars.add( w.var("bern6_p6") ) 
    Fit_bkg_bern6_pdf = ROOT.RooFitResult(w.factory( "Bernstein:bkg_bern6_pdf(tp_mass,{bern6_p0,bern6_p1,bern6_p2,bern6_p3,bern6_p4,bern6_p5,bern6_p6})").fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE)))
    w.factory( "Bernstein:bkg_bern6_pdf(tp_mass,{bern6_p0,bern6_p1,bern6_p2,bern6_p3,bern6_p4,bern6_p5,bern6_p6})")

    
    # ~ Chebychev 
    #w.factory( "cheb[0.01,-10.,10.]")
    #treeVars.add( w.var("cheb") )
    #w.factory( "Chebychev:bkg_cheb_pdf(tp_mass,cheb)")
    #w.factory( "Polynomial:bkg_cheb_pdf(tp_mass,cheb)") 
    w.factory("cheb1[0.01,-10.,10.]")
    w.factory("cheb2[0.01,-10.,10.]") 
    w.factory("cheb3[0.01,-10.,10.]")     
    treeVars.add(w.var("cheb1"))
    treeVars.add(w.var("cheb2"))
    treeVars.add(w.var("cheb3"))
    w.factory("Chebychev:bkg_cheb_pdf(tp_mass,{cheb1,cheb2,cheb3})")

    # ~ Single Exponential
    w.factory ("lambda[-0.001,-0.01,0.01]")
    treeVars.add(w.var("lambda"))
    w.factory("Exponential:bkg_exp_pdf(tp_mass,lambda)")

    # ~ exponential
    w.factory( "lambda1[4.03336e-02, 0.0001, 10]")
    treeVars.add( w.var("lambda1") )
    w.factory( "lambda3[4.88218e-01, 0.0001, 10]")
    treeVars.add( w.var("lambda3") )    
    w.factory("Exponential:bkg_exp1_pdf(tp_mass,lambda1)")
    w.factory("Exponential:bkg_exp2_pdf(tp_mass,lambda3)")
    #w.factory("SUM:bkg_sumexp_pdf(bkg_exp1_pdf, frac2[-4.29406e-03, -100, 0.0001]*bkg_exp2_pdf )")
  
    # ~ Power Law
    w.factory( "pow[2., -10, 10.00001]")
    treeVars.add(w.var("pow"))
    w.factory("PowerLaw:bkg_pow_pdf(tp_mass,pow)")   
 
    #w.factory( "var[-0.001,-0.01,0.01]")
    #treeVars.add( w.var("var"))
    #w.factory("PowerLawSum:bkg_pow_sum_pdf(tp_mass,var)")



 
    FitResults = []
    #FitResults.append(['bkg_bern1_pdf',"Bernstein:bkg_bern1_pdf(tp_mass,{bern1_p0,bern1_p1})",kTeal+3])
    FitResults.append(['bkg_bern2_pdf',"Bernstein:bkg_bern2_pdf(tp_mass,{bern2_p0,bern2_p1,bern2_p2})",kMagenta])
    #FitResults.append(['bkg_bern3_pdf',"Bernstein:bkg_bern3_pdf(tp_mass,{bern3_p0,bern3_p1,bern3_p2,bern3_p3})",kGreen+1])
    #FitResults.append(['bkg_bern4_pdf',"Bernstein:bkg_bern4_pdf(tp_mass,{bern4_p0,bern4_p1,bern4_p2,bern4_p3,bern4_p4})",kOrange+7])
    #FitResults.append(['bkg_bern5_pdf',"Bernstein:bkg_bern5_pdf(tp_mass,{bern5_p0,bern5_p1,bern5_p2,bern5_p3,bern5_p4,bern5_p5})",kAzure+10])
    #FitResults.append(['bkg_bern6_pdf',"Bernstein:bkg_bern6_pdf(tp_mass,{bern6_p0,bern6_p1,bern6_p2,bern6_p3,bern6_p4,bern6_p5,bern6_p6})",kViolet+10])
    #FitResults.append(['bkg_cheb_pdf', "Polynomial:bkg_cheb_pdf(tp_mass,cheb)",kRed])
    #FitResults.append(['bkg_exp_pdf',"Exponential:bkg_exp_pdf(tp_mass,lambda)",kGreen-8])
    #FitResults.append(['bkg_exp1_pdf', "Exponential:bkg_exp1_pdf(tp_mass,lambda1)",kPink])
    #FitResults.append(['bkg_exp2_pdf', "Exponential:bkg_exp2_pdf(tp_mass,lambda3)",kCyan-7])
    #FitResults.append(['bkg_sumexp_pdf',"SUM:bkg_sumexp_pdf(bkg_exp1_pdf, frac2[-4.29406e-03, -100, 0.0001]*bkg_exp2_pdf )",kOrange+5])
    #FitResults.append(['bkg_pow_pdf',  "PowerLaw:bkg_pow_pdf(tp_mass,pow)",kRed])
    FitResults.append(['bkg_cheb_pdf',"Chebychev pol:bkg_cheb_pdf(tp_mass,{cheb1,cheb2,cheb3})",kRed])
    c1 = TCanvas('c1','PDF Fits',200,10,700,500)
    leg = TLegend(0.5,0.55,0.92,0.88)
    tpmass_high = 180
    tpmass_low = 100
    nbins = ROOT.RooBinning(-15,15)
    frame = w.var( "tp_mass" ).frame()
    w.var( "tp_mass").setRange("unblindreg_1",100,115) 
    w.var( "tp_mass").setRange("unblindreg_2",135,180)
    data_RooDataSet.plotOn(frame,RooFit.Binning(tpmass_high-tpmass_low),RooFit.CutRange("unblindreg_1"))
    data_RooDataSet.plotOn(frame,RooFit.Binning(tpmass_high-tpmass_low),RooFit.CutRange("unblindreg_2"))
    #data_RooDataSet.plotOn(frame,RooFit.Binning(tpmass_high-tpmass_low))
    #data2_RooDataSet = ROOT.RooDataSet( "data2", "data2", ROOT.RooArgSet( w.var( "tp_mass" ) ) )
    #data2_RooDataSet = data_RooDataSet.reduce(RooFit.CutRange("reg1"))
    #w.factory("PROD:bern12_pdf(bkg_bern1_pdf,bkg_bern2_pdf)")  
    for fi, f in enumerate(FitResults):
        #stat=f[1].status()
        #minnll=f[1].minNll()
        #ROOT.RooFitResult(w.factory( f[1]).fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE)))
        ROOT.RooFitResult(w.factory( f[1]).fitTo(data_RooDataSet,RooFit.Strategy(1),RooFit.Minimizer("Minuit2","minimize"),RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE)))
        stat = ROOT.RooFitResult(w.factory( f[1]).fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE))).status()
        minnll = ROOT.RooFitResult(w.factory( f[1]).fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE))).minNll()
        w.factory(f[1]).plotOn(frame,RooFit.LineColor(f[2]))
        leg.AddEntry(w.factory(f[1]),f[0],'lf')
        nParams = w.factory(f[1]).getParameters(data_RooDataSet).getSize()
        print "Number of parameters",nParams
        #kolomo = ROOT.RooFitResult(w.factory( f[1]).fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE))).result()
        #Chi2 = ROOT.RooChi2Var('chi2','chi2',w.factory(f[1]),clonedata)
        #params_test = ROOT.RooArgSet()
        #params_test.assignValueOnly(ROOT.RooFitResult(w.factory( f[1]).fitTo(data_RooDataSet,RooFit.Strategy(1),RooFit.Minimizer("Minuit2","minimize"),RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE))).randomizePars())
    #print " THE FIT STATUS IS:  ", stat
    #print " THE minNLL IS:  ",minnll
    #print "HEY BOOIII: ",frame.chiSquare()
    
    frame.Draw()
    tlatex = TLatex()
    tlatex.SetNDC()
    tlatex.SetTextAngle(0)
    tlatex.SetTextColor(kBlack)
    tlatex.SetTextFont(63)
    tlatex.SetTextAlign(11)
    tlatex.SetTextSize(25)
    tlatex.DrawLatex(0.11,0.91,"CMS")
    tlatex.SetTextFont(53)
    tlatex.DrawLatex(0.18,0.91,"Preliminary")
    #Status = ROOT.RooFitResult(w.factory("Bernstein:bkg_bern1_pdf(tp_mass,{bern1_p0,bern1_p1})").fitTo(data_RooDataSet,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE))).status()
    #Status = 0
    #tlatex.DrawLatex(0.7,0.91,Status)
    tlatex.SetTextFont(43)
    tlatex.SetTextSize(23) 
    Lumi = "35.87" + " fb^{-1} (13TeV)"
    tlatex.SetTextAlign(31)
    tlatex.DrawLatex(0.9,0.91,Lumi)
    tlatex.SetTextAlign(11)  
    c1.Update()   
    #leg.Draw('same')
    c1.SaveAs("test.png")
    cat = ROOT.RooCategory('pdf_index','index of the active pdf')

    mypdfs = ROOT.RooArgList()
    #mypdfs.add(w.factory( "Bernstein:bkg_bern1_pdf(tp_mass,{bern1_p0,bern1_p1})"))
    #mypdfs.add(w.factory( "Bernstein:bkg_bern2_pdf(tp_mass,{bern2_p0,bern2_p1,bern2_p2})"))
    #mypdfs.add(w.factory( "Bernstein:bkg_bern3_pdf(tp_mass,{bern3_p0,bern3_p1,bern3_p2,bern3_p3})"))
    #mypdfs.add(w.factory( "Bernstein:bkg_bern4_pdf(tp_mass,{bern4_p0,bern4_p1,bern4_p2,bern4_p3,bern4_p4})"))
    #mypdfs.add(w.factory( "Bernstein:bkg_bern5_pdf(tp_mass,{bern5_p0,bern5_p1,bern5_p2,bern5_p3,bern5_p4,bern5_p5})"))
    #mypdfs.add(w.factory( "Bernstein:bkg_bern6_pdf(tp_mass,{bern6_p0,bern6_p1,bern6_p2,bern6_p3,bern6_p4,bern6_p5,bern6_p6})"))
    mypdfs.add(w.factory( "Exponential:bkg_exp_pdf(tp_mass,lambda)"))
    #mypdfs.add(w.factory( "Exponential:bkg_exp1_pdf(tp_mass,lambda1)"))
    #mypdfs.add(w.factory( "Exponential:bkg_exp2_pdf(tp_mass,lambda3)"))
    #mypdfs.add(w.factory( "SUM:bkg_sumexp_pdf(bkg_exp1_pdf, frac2[-4.29406e-03, -100, 0.0001]*bkg_exp2_pdf )"))
    #mypdfs.add(w.factory( "Polynomial:bkg_cheb_pdf(tp_mass,cheb)"))
    mypdfs.add(w.factory("Chebychev:bkg_cheb_pdf(tp_mass,cheb1,cheb2,cheb3)"))
    multipdf = ROOT.RooMultiPdf("multipdf","multipdf",cat,mypdfs)  
    #w.import(multipdf) 
    frame.Draw()
    #c1.SaveAs("test.png") 
    #c3 = TCanvas('c3','c3',200,10,700,500)   
    #data_RooDataSet.plotOn(frame)
    #w.factory( "Bernstein:bkg_bern1_pdf(tp_mass,{bern1_p0,bern1_p1})").plotOn(frame)
    #frame.Draw()   
    # ~~ Lets talk about signal! --Build Sum of Gaussians
    #w.factory("dm[0.1,-3.,3.]")
    #treeVars.add(w.var("dm"))
    forceFracUnity_ = False    
    recursive_ = False
    ngaussians = 10
    gaussians = ROOT.RooArgList() 
    coeffs = ROOT.RooArgList()
    for g in range(0,ngaussians):
      print "Gaussian number " ,g
      w.factory("dm[0.1,-3.,3.]")
      treeVars.add(w.var("dm"))
      w.factory("mean[125,110,130]")   ## FIX ME -- Should mean values be different?
      treeVars.add(w.var("mean"))
      w.factory("sigma[2.,0.4,20.]")
      treeVars.add(w.var("sigma"))
      w.factory( "Gaussian:gaus(tp_mass, mean, sigma)")

      gaussians.add(w.factory( "Gaussian:gaus(tp_mass, mean, sigma)"))
     
      if g < ngaussians - 1:
         print "CHECK CHECK"
         w.factory("frac[0.1,0.01,0.99]")
         treeVars.add(w.var("frac"))
         coeffs.add(w.factory("frac[0.1,0.01,0.99]"))
    
      #if (g == ngaussians - 1):# FIX ME -- and forceFracUnity_ == 1) :   
         #w.factory("recfrac[0.1,0.01,0.99]")
         #treeVars.add(w.var("recfrac"))
         #coeffs.add(w.factory("recfrac[0.1,0.01,0.99]"))
    
    
      
     
    #w.factory( "RooAddPdf:sig_pdf(gaus,gaus,kTrue)")
    #sig = ROOT.RooAddPdf("total","total",ROOT.RooArgList(gaussians),ROOT.RooArgList(coeffs),ROOT.kTRUE)
      #dm = ROOT.RooRealVar(Form("dm_g%d"),Form("dm_g%d"),0.1,-3.,3.)           
      #w.factory( "dm[0.1,-3.,3..]")
      #treeVars.add(w.var("dm"))
      #w.factory( "sum:mean(125,dm)")
      #treeVars.add(w.var("mean"))      
     

    w.factory( "Gaussian:sig_gaus1_pdf(tp_mass, mass1[125, 120, 128], sigma1[3.0,0.5,8.0])")
    w.factory( "Gaussian:sig_gaus2_pdf(tp_mass, mass2[125, 110, 130], sigma2[3, 0.5, 8.0])")
    w.factory( "Gaussian:sig_gaus3_pdf(tp_mass, mass3[125, 110, 130], sigma3[3, 0.5, 18.0])")
    w.factory( "SUM:sig_sum_gaus12_pdf(ng1[0.5,0.01,0.99]*sig_gaus1_pdf,ng2[0.3,0.01,0.99]*sig_gaus2_pdf)")
    w.factory( "SUM:sig_pdf(ng3[0.66, 0.01, 0.99]*sig_sum_gaus12_pdf,sig_gaus3_pdf)")
    w.factory( "mean[4.03336e-02, 0.0001, 10]") 
    Sig_gaus_3 = ROOT.RooFitResult(w.factory("SUM:sig_pdf(ng3[0.66, 0.01, 0.99]*sig_sum_gaus12_pdf,sig_gaus3_pdf)").fitTo(data_RooDataSet_sig,RooFit.SumW2Error(kTRUE), RooFit.Save(kTRUE))) 
    sig_nll = Sig_gaus_3.minNll()
    print " The signal nll value : " , sig_nll  
    c2 = TCanvas('c2','Signal Gaussian Fits',200,10,700,500)  
    frame = w.var( "tp_mass" ).frame()
    data_RooDataSet_sig.plotOn(frame)
    w.factory("Gaussian:sig_pdf(tp_mass, mass1[125, 120, 128], sigma1[3.0,0.5,8.0])").plotOn(frame,RooFit.LineColor(kOrange))
    w.factory("SUM:sig_pdf(ng3[0.66, 0.01, 0.99]*sig_sum_gaus12_pdf,sig_gaus3_pdf)").plotOn(frame,RooFit.LineColor(kOrange))
    w.factory("SUM:sig_pdf(ng3[0.66, 0.01, 0.99]*sig_sum_gaus12_pdf,sig_gaus3_pdf)").plotOn(frame,RooFit.Components("sig_gaus1_pdf"),RooFit.LineColor(209))
    w.factory("SUM:sig_pdf(ng3[0.66, 0.01, 0.99]*sig_sum_gaus12_pdf,sig_gaus3_pdf)").plotOn(frame,RooFit.Components("sig_gaus2_pdf"),RooFit.LineColor(222))
    w.factory("SUM:sig_pdf(ng3[0.66, 0.01, 0.99]*sig_sum_gaus12_pdf,sig_gaus3_pdf)").plotOn(frame,RooFit.Components("sig_gaus3_pdf"),RooFit.LineColor(kRed))
    frame.Draw()
    c2.SaveAs("sig.png")

    getattr(w,'import')(cat) 
    getattr(w,'import')(multipdf)  
    #getattr(w,'import')(sig)
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
            if nuisance ['type'] == 'lnN' or nuisance ['type'] == 'lnU' or nuisance['type'] == 'discrete':
              card.write('pdf_index'.ljust(80))
              card.write('discrete'.ljust(20))
              card.write('\n')
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






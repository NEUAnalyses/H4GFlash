#!/usr/bin/env python


## 
## code to produce a datacard
## 

import os
import os.path
import optparse
#from ROOT import *
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
  
  
  cuts = {}
  if opt.cutsFile == None :
     print " Please provide the cuts structure ... it is needed!" 
  elif os.path.exists(opt.cutsFile) :
    handle = open(opt.cutsFile,'r')
    exec(handle)
    handle.close()
  
  for cutName in cuts :
    print "cut = ", cutName, " :: ", cuts[cutName]
  
  
  # ~~~~
  nuisances = {}
  if opt.nuisancesFile == None :
     print " Please provide the nuisances structure if you want to add nuisances " 
  elif os.path.exists(opt.nuisancesFile) :
    handle = open(opt.nuisancesFile,'r')
    exec(handle)
    handle.close()
  
  # ~~~~
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
  
  if not os.path.isdir (opt.outputDirDatacard + "/") :
    os.mkdir(opt.outputDirDatacard + "/")
  
  #---- loop over "cuts"
  for cutName in cuts :
    
    #datas       = []
    #signals     = ['sig']
    #backgrounds = ['bkg']
    datas       = []
    signals     = []
    backgrounds = []
    
    # calculate yields for data, signal and background
    yieldsSig  = {}
    yieldsBkg  = {}
    yieldsData = {}
  
    #
    # to do it properly :-)
    #
    #yieldsData['data'] = 1.0
    #yieldsBkg['bkg'] = 10.3
    #yieldsSig['sig'] = 100.999
    
    for sampleName, sample in samples.iteritems():
      if sample['isData'] == 1 :
        datas.append(sampleName)
      elif sample['isSignal'] == 1 :
        signals.append(sampleName)
      elif sample['isSignal'] == 0 :
        backgrounds.append(sampleName)

    #
    # data and background are all merged into 1 single "sample"
    #
    trees_data = {}
    for data in datas :
      for itree in range(len(samples[data]['name'])):
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
    yieldsData['data'] = 0
    for itree in range(len(trees_data['trees'])) :
      yieldsData['data'] += (trees_data['trees'][itree]).GetEntries( '(' + trees_data['weights'][itree] + ') * (' + cuts[cutName] + ')' )
    
    for background in backgrounds :
      yieldsBkg[background] = 0.
      for itree in range(len(dict_trees_background[background]['trees'])) :
        yieldsBkg[background] += (dict_trees_background[background]['trees'][itree]).GetEntries( '(' + dict_trees_background[background]['weights'][itree]   + ') * (' + cuts[cutName] + ')'  )

    for signal in signals :
      yieldsSig[signal] = 0.
      for itree in range(len(dict_trees_signal[signal]['trees'])) :
        yieldsSig[signal] += (dict_trees_signal[signal]['trees'][itree]).GetEntries( '(' + dict_trees_signal[signal]['weights'][itree]  + ') * (' + cuts[cutName] + ')'   )
      
    
    
    
    
    
    
    #
    # creates the workspaces
    #    source code from https://github.com/NEUAnalyses/H4GFlash/blob/master/bin/AnalysisFits.C
    #
    
    tagNameToAppearInDatacard = cutName

    if not os.path.isdir (opt.outputDirDatacard + "/" + cutName + "/") :
      os.mkdir(opt.outputDirDatacard + "/" + cutName + "/")
    if not os.path.isdir (opt.outputDirDatacard + "/" + cutName + "/" + "shapes/") :
      os.mkdir(opt.outputDirDatacard + "/" + cutName + "/" + "shapes/")
    
    name_root_file_with_workspace = opt.outputDirDatacard + "/" + cutName + "/shapes/w_" + tagNameToAppearInDatacard + ".root"

    root_file_with_workspace = ROOT.TFile (name_root_file_with_workspace, "RECREATE")
    
    w = ROOT.RooWorkspace("w")
    # create the variable
    w.factory( "tp_mass[80, 160]" )
    w.var( "tp_mass" ).SetTitle("tp_mass")
    w.var( "tp_mass" ).setUnit("GeV")
   
    w.factory( "dp1_mass[0,200]" )
    
 
    # the set of variables
    treeVars = ROOT.RooArgSet()
    treeVars.add( w.var( "tp_mass" ) )
    treeVars.add( w.var("dp1_mass") )    
    
    data_RooDataSet = ROOT.RooDataSet( "data", "data", ROOT.RooArgSet( w.var( "tp_mass" ) ) )
    print "HEYYYY",trees_data['trees']
    for itree in range(len(trees_data['trees'])) :
      
      data_RooDataSet_temp = ROOT.RooDataSet( "data", "data", (trees_data['trees'][itree]), treeVars)
      data_RooDataSet.append(data_RooDataSet_temp.reduce('(' + trees_data['weights'][itree] + ') * (' + cuts[cutName] + ')'))






    #signal_RooDataSet = ROOT.RooDataSet( "dataSig", "dataSig", ROOT.RooArgSet(m4g_RooRealVar) )
    #for signal in signals :
      #for itree in range(len(dict_trees_signal[signal]['trees'])) :
        #signal_RooDataSet_temp = ROOT.RooDataSet( "dataSig", "dataSig",  dict_trees_signal[signal]['weights'][itree], treeVars)
        #signal_RooDataSet.append(signal_RooDataSet_temp)

    getattr(w,'import')(data_RooDataSet)
    #getattr(ws,'import')(signal_RooDataSet)
    #ws.import(data_RooDataSet)
    #ws.import(signal_RooDataSet)

      
      #TChain* treeTemp = new TChain("H4GSel");
      #treeTemp->AddFile(TString(rootName));
      
      
      #TTree* tree = (TTree*) treeTemp->CopyTree(std::string(selection + " && " + categoriesCuts[cat]).c_str() );
      #std::cout << "Reading file: " << rootName << "\n\t with " << tree->GetEntries() << " entries \n\t Making the following cut: " << categoriesCuts[cat] << std::endl;
      #RooDataSet* data = new RooDataSet( "data", "data", tree, *treeVars);
          
      #//Get signal distribution from file
      #TChain* treeTempSig = new TChain("H4GSel");
      #treeTempSig->AddFile(TString(signal_File));
      #std::string toCut = selection + " && " + categoriesCuts[cat];
      #if(TString(categoriesCuts[cat]).Contains("< 0")) toCut = selection;
      #TTree* treeSig = (TTree*) treeTempSig->CopyTree( toCut.c_str() );
      #std::cout << "Reading signal file: " << signal_File << "\n\t with " << treeSig->GetEntries() << " entries \n\t Making the following cut: " << categoriesCuts[cat] << std::endl;
#//      RooDataSet* dataSig = new RooDataSet( "dataSig", "dataSig", treeSig, *treeVars, cut.c_str(), "evWeight" );
      #RooDataSet* dataSig = new RooDataSet( "dataSig", "dataSig", treeSig, *treeVars);
        
      #w->import(*data);
      #w->import(*dataSig);
      

    #ws.factory( "RooFormulaVar:meanSigCB1('meanG1*mH/125.09', {meanG1[125, 120, 128], mH[125.09]})"  )
    
      #for ( unsigned int f = 0; f < signal_Functions.size(); f++){
          #TString thisFunction(signal_Functions[f]);
          #std::cout << "Signal function added: " << thisFunction << std::endl;
          #w->factory( thisFunction.Data() );
      #}
    
    #ws.factory( "RooBernstein:Bern2_tp_mass(tp_mass, {mod_b2_p0_mgg_bb, mod_b2_p1_mgg_bb, mod_b2_p2_mgg_bb} )"  )
    w.factory( "Exponential:bkg_pdf(tp_mass, a[-0.5,-2,-0.2])"  )
    w.factory( "Gaussian:sig_pdf(tp_mass, mass[125, 110, 130], sigma[4, 2, 10])");

    
    
    
      #//Initialize all needed PDFs for background
      #for ( unsigned int f = 0; f < functions.size(); f++){
        #TString thisFunction(functions[f]);
        #std::cout << "Function added: " << thisFunction << std::endl;
        #w->factory( thisFunction.Data() );
      #}
      
      
      
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
    
    card.write('shapes  bkg      ' + tagNameToAppearInDatacard + '  '  + name_root_file_with_workspace  + '  w:bkg_pdf \n')
    card.write('shapes  sig      ' + tagNameToAppearInDatacard + '  '  + name_root_file_with_workspace  + '  w:sig_pdf \n')
    card.write('shapes  data_obs ' + tagNameToAppearInDatacard + '  '  + name_root_file_with_workspace  + '  w:data \n')
     
    card.write('-'*100+'\n')
    card.write('bin         %s' % tagNameToAppearInDatacard+'\n')    
    card.write('observation %.0f\n' % yieldsData['data'])
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






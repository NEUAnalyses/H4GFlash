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
    chain_data = TChain('H4GSel')
    for data in datas :
      for tree in samples[data]['name']:
        chain_data.Add(tree)

    #
    # background can be split into different samples, for some strange reasons ... optimization?
    #     
    
    chains_background = {}
    for background in backgrounds :
      chain_background = TChain('H4GSel')
      for tree in samples[background]['name']:
        chain_background.Add(tree)
      chains_background[background] = chain_background

    #
    # signals can be split into different samples, since different production mechanisms
    #     
    chains_signal = {}
    for signal in signals :
      chain_signal = TChain('H4GSel')
      for tree in samples[signal]['name']:
        chain_signal.Add(tree)
      chains_signal[signal] = chain_signal
 
    #
    # now get the yields
    #
    yieldsData['data'] = chain_data.GetEntries()
    for background in backgrounds :
      yieldsBkg[background] = chains_background[background].GetEntries()
    for signal in signals :
      yieldsSig[signal] = chains_signal[signal].GetEntries()
    
    
    
    
    #
    # now write the datacard
    #
    
    
    if not os.path.isdir (opt.outputDirDatacard + "/" + cutName) :
      os.mkdir(opt.outputDirDatacard + "/" + cutName)
    
    tagNameToAppearInDatacard = cutName
    
    
    cardPath = opt.outputDirDatacard + "/" + cutName + "/datacard.txt"
    print 'Writing to ' + cardPath 
    card = open( cardPath ,"w")
    card.write('## Parametric shape input card\n')
    
    card.write('imax 1 number of channels\n')
    card.write('jmax * number of background\n')
    card.write('kmax * number of nuisance parameters\n') 
    
    card.write('-'*100+'\n')
    card.write('bin         %s' % tagNameToAppearInDatacard+'\n')
    
    card.write('observation %.0f\n' % yieldsData['data'])
    
    card.write('shapes  *           * '+
               'shapes/histos_' + tagNameToAppearInDatacard + ".root" +
               '     histo_$PROCESS histo_$PROCESS_$SYSTEMATIC' + '\n')
    
    card.write('shapes  data_obs           * '+
               'shapes/histos_' + tagNameToAppearInDatacard + ".root" +
               '     histo_Data' + '\n')
    
    #   shapes  *           * shapes/hww-19.36fb.mH125.of_vh2j_shape_mll.root     histo_$PROCESS histo_$PROCESS_$SYSTEMATIC
    #   shapes  data_obs    * shapes/hww-19.36fb.mH125.of_vh2j_shape_mll.root     histo_Data
    
    
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










       
        ##if nuisanceName != 'stat' : # 'stat' has a separate treatment, it's the MC/data statistics
          
          ##if 'type' in nuisance.keys() : # some nuisances may not have "type" ... why?
            ###print "nuisance[type] = ", nuisance ['type']
            ##if nuisance ['type'] == 'lnN' or nuisance ['type'] == 'lnU' :
              ##card.write((nuisance['name']).ljust(80-20))
              ##card.write((nuisance ['type']).ljust(20))
              ##if 'all' in nuisance.keys() and nuisance ['all'] == 1 : # for all samples
                ###card.write(''.join([('%-.4f' % nuisance['value']).ljust(columndef) for name in signals      ]))
                ###card.write(''.join([('%-.4f' % nuisance['value']).ljust(columndef) for name in backgrounds  ]))
                ##card.write(''.join([(' %s ' % nuisance['value']).ljust(columndef) for name in signals      ]))
                ##card.write(''.join([(' %s ' % nuisance['value']).ljust(columndef) for name in backgrounds  ]))
                ##card.write('\n')
              ##else :
                ### apply only to selected samples
                ##for sampleName in signals:
                  ##if sampleName in nuisance['samples'].keys() :
                    ###card.write(('%-.4f' % nuisance['samples'][sampleName]).ljust(columndef))
                    ##card.write(('%s' % nuisance['samples'][sampleName]).ljust(columndef))
                  ##else :
                    ##card.write(('-').ljust(columndef))
                ##for sampleName in backgrounds:
                  ##if sampleName in nuisance['samples'].keys() :
                    ###card.write(('%-.4f' % nuisance['samples'][sampleName]).ljust(columndef))
                    ##card.write(('%s' % nuisance['samples'][sampleName]).ljust(columndef))
                  ##else :
                    ##card.write(('-').ljust(columndef))
                     
            ##elif nuisance ['type'] == 'shape' :
              ##card.write(("CMS_" + (nuisance['name'])).ljust(80-20))
              ##if 'AsLnN' in nuisance.keys() and  float(nuisance ['AsLnN']) >= 1:
                ##print ">>>>>", nuisance['name'], " was derived as a shape uncertainty but is being treated as a lnN"
                ##card.write(('lnN').ljust(20))
                ##allSelectedSamples = signals + backgrounds  
                ##for sampleName in allSelectedSamples:
                  ##if ('all' in nuisance.keys() and nuisance ['all'] == 1) or \
                     ##sampleName in nuisance['samples'].keys() :  
                    ##histo     = _getHisto(cutName+"/"+variableName+'/', 
                                               ##'histo_' + sampleName)
                    ##histoUp   = _getHisto(cutName+"/"+variableName+'/', 
                                               ##'histo_' + sampleName + '_' + (nuisance['name']) + "Up") 
                    ##histoDown = _getHisto(cutName+"/"+variableName+'/',
                                               ##'histo_' + sampleName + '_' + (nuisance['name']) + "Down")
    
                    ##histoIntegral = histo.Integral()
                    ##histoUpIntegral = histoUp.Integral()
                    ##histoDownIntegral = histoDown.Integral()
                    ##if histoIntegral > 0:
                      ##diffUp = (histoUpIntegral - histoIntegral)/histoIntegral/float(nuisance ['AsLnN'])
                      ##diffDo = (histoDownIntegral - histoIntegral)/histoIntegral/float(nuisance ['AsLnN'])
                    ##else: 
                      ##diffUp = 0.
                      ##diffDo = 0.
    
                    ##lnNUp = 1. + diffUp
                    ##lnNDo = 1. + diffDo
                      
                    ##card.write((('%-.4f' % lnNUp)+"/"+('%-.4f' % lnNDo)).ljust(columndef))
                  ##else:
                    ##card.write(('-').ljust(columndef)) 
    
              ##else:  
                ##card.write((nuisance ['type']).ljust(20))
                ##if 'all' in nuisance.keys() and nuisance ['all'] == 1 : # for all samples
                  ##card.write(''.join([('1.000').ljust(columndef) for name in signals      ]))
                  ##card.write(''.join([('1.000').ljust(columndef) for name in backgrounds  ]))
                  ##card.write('\n')
                ##else :
                  ### apply only to selected samples
                  ##for sampleName in signals:
                    ##if sampleName in nuisance['samples'].keys() :
                      ##card.write(('1.000').ljust(columndef))                          
                      ### save the nuisance histograms in the root file
                      ##_saveHisto(cutName+"/"+variableName+'/',
                                       ##'histo_' + sampleName + '_' + (nuisance['name']) + "Up",
                                       ##'histo_' + sampleName + '_CMS_' + (nuisance['name']) + "Up"
                                       ##)
                      ##_saveHisto(cutName+"/"+variableName+'/',
                                       ##'histo_' + sampleName + '_' + (nuisance['name']) + "Down",
                                       ##'histo_' + sampleName + '_CMS_' + (nuisance['name']) + "Down"
                                       ##)
                    ##else :
                      ##card.write(('-').ljust(columndef))
                  ##for sampleName in backgrounds:
                    ##if sampleName in nuisance['samples'].keys() :
                      ##card.write(('1.000').ljust(columndef))
                      ### save the nuisance histograms in the root file
                      ##_saveHisto(cutName+"/"+variableName+'/',
                                       ##'histo_' + sampleName + '_' + (nuisance['name']) + "Up",
                                       ##'histo_' + sampleName + '_CMS_' + (nuisance['name']) + "Up"
                                       ##)
                      ##_saveHisto(cutName+"/"+variableName+'/',
                                       ##'histo_' + sampleName + '_' + (nuisance['name']) + "Down",
                                       ##'histo_' + sampleName + '_CMS_' + (nuisance['name']) + "Down"
                                       ##)
                    ##else :
                      ##card.write(('-').ljust(columndef))
              
            ### new line at the end of any nuisance that is *not* stat ... because in that case it's already done on its own
          ##card.write('\n')
                   
    #card.write('-'*100+'\n')
  
    #card.write('\n')
    #card.close()
  
  
    
  ##first loop over all variables
  #for v in Vars:
     #hists = []
     #hists2 = []
     #leg = TLegend(0.6, 0.7, 0.89, 0.89)
     #leg.SetBorderSize(0)
     #Max = -0.
     #Max2 = -0.
     #for fi,f in enumerate(MC):  ## get all MC plots, because they have to stacked!
        #ch = TChain('H4GSel')
        #ch.Add(f[0])
        #hname = v[1]+'_'+str(fi)
        #h = TH1F(hname, v[2], v[3], v[4], v[5])
        #ch.Draw(v[0]+'>>'+hname,TCut(BlindCut)) ## add cut based on what you want to plot, blind or unblind or anything else
        #h.Scale(float(f[4]),"nosw2")
        #h.SetLineColor(f[2])
        #h.SetLineWidth(2)
        #h.SetFillColor(f[3])
        #hists.append([h,ch,f[1]])
        #if h.GetMaximum() > Max:
           #Max = h.GetMaximum()
     ##print "I AM MC MAX",Max
   
     #for di,d in enumerate(Data):  ## now get data
        #ch2 = TChain('H4GSel')
        #ch2.Add(d[0])
        #hname2 = v[1]+'_'+str(di)
        #h2 = TH1F(hname2,v[2],v[3],v[4],v[5])
        #ch2.Draw(v[0]+'>>'+hname2,TCut(Blind))
        #h2.SetMarkerStyle(20)
        #h2.GetYaxis().SetTitle('Normalized Yields')
        #h2.SetLineColor(1)
        #h2.SetLineWidth(2)
        #h2.Sumw2()
     #for si,s in enumerate(Signal):   ##plot signal on top
        #ch3 = TChain('H4GSel')
        #ch3.Add(s[0])
        #hname3 = v[1]+'_'+str(si)
        #h3 = TH1F(hname3,v[2],v[3],v[4],v[5])
        #ch3.Draw(v[0]+'>>'+hname3)
        ##h3.Sumw2()
        ##total2 = h3.Integral()
        #h3.Scale(float(s[3]))
        #h3.SetLineColor(s[2])
        #h3.SetLineWidth(2)
        ##h3.Sumw2()
        ##hists2.append([h3,ch3,s[1]])
        
        #if h3.GetMaximum() > Max2:
          #Max2 = h3.GetMaximum()
     ##print "I AM SIGNAL MAX", Max2
  
     #c0 = TCanvas('a','a',800,1000)   ##now starts the drawing part, start by stacking all the MC up
     #s = THStack("s","")
     #for fi,hh in enumerate(hists):
        #leg.AddEntry(hh[0], hh[2], 'lf')
        #s.Add(hh[0])
        #hh[0].SetMaximum(Max*1.5)
        #hh[0].SetMinimum(0.0001)
        #if fi == 0:
           #hh[0].Draw('')
        #if fi > 0:
           #hh[0].Draw('same')
        
     #s.Draw("hist")
     #s.GetXaxis().SetTitle(v[6])
     #s.GetYaxis().SetTitle('Normalized Yields')
     #s.GetYaxis().SetTitleOffset(1.6);
  
     #h2.Draw('p same')
     #h3.Draw('h same')
     #leg.SetNColumns(3)
     #leg.AddEntry(h2,"Data",'lp')
     #leg.AddEntry(h3,"SigX10  m(a)=55GeV",'l')  
     #leg.Draw('same')
  
     ##c0.Update()
     #c0.SaveAs(outputLoc+v[1]+'.pdf')
     #c0.SaveAs(outputLoc+v[1]+'.png')
     #c0.SetLogy()
     #c0.SaveAs(outputLoc+v[1]+'_log.pdf')
     #c0.SaveAs(outputLoc+v[1]+'_log.png')

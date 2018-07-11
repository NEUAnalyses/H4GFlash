






samples['data']  = {  

            'isData': 1,
            
            'name': [
              '/tmp/twamorka/Data_all.root',
              ],
            
           }
  
  

samples['sig']  = {  

            'isData': 0,
            'isSignal': 1,

            'name': [
              '/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/FlatTrees/FatPho0p1_Match0p15/signal_m_60.root',
                     #'/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/for4Gamma_ver2/sig45.root',
                     #'/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/for4Gamma_ver2/sig25.root',
              ],
            
            'weight' : '1',  
            
            'weights' :  [
                       '36*0.001*1000/198014', 
                       '36*0.001*1000/198033',
                       '36*0.001*1000/200000',
                       '36*0.001*1000/195505',
                        ],
           }
  
 
 

samples['bkg']  = {  

            'isData': 0,
            'isSignal': 0,

            'name': [
              '/eos/cms/store/user/twamorka/FlatTrees/DiPhoJets80toInf.root',
              '/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/TreeSkimmerPy/FlatTrees/QCD40toInf.root',
              '/eos/cms/store/user/twamorka/FlatTrees/GJets20to40.root',
              '/eos/cms/store/user/twamorka/FlatTrees/GJets20toInf.root',
              '/eos/cms/store/user/twamorka/FlatTrees/GJets40toInf.root',
              '/eos/cms/store/user/twamorka/FlatTrees/QCD30to40.root',
              '/eos/cms/store/user/twamorka/FlatTrees/DiPho40to80.root',
              '/eos/cms/store/user/twamorka/FlatTrees/QCD30toInf.root',
              ],
            
            'weight' : '1',  
            
            'weights' :  [
                       '197.866',
                       '3.030',
                       '0.316',
                       '3.106',
                       '0.423',
                       '44.197',
                       '0.111',
                       '249.667', 
                        ],
           }
  
  
    
  


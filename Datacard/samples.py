






samples['data']  = {  

            'isData': 1,
            
            'name': [
              '/eos/cms/store/user/twamorka/4gamma/skimtrees/data.root',
              'file2.root',
              ],
            
           }
  
  

samples['sig']  = {  

            'isData': 0,
            'isSignal': 1,

            'name': [
              '/eos/cms/store/user/twamorka/4gamma/skimtrees/sig60_skim.root',
              '/eos/cms/store/user/twamorka/4gamma/skimtrees/sig45_skim.root',
              '/eos/cms/store/user/twamorka/4gamma/skimtrees/sig25_skim.root',
              '/eos/cms/store/user/twamorka/4gamma/skimtrees/sig10_skim.root',
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
              '/eos/cms/store/user/twamorka/4gamma/skimtrees/DiphoJets80_Inf_gen.root',
              '/eos/cms/store/user/twamorka/4gamma/skimtrees/DiphoJets40_80_gen.root',
              '/eos/cms/store/user/twamorka/4gamma/skimtrees/GJets20_40_gen.root',
              '/eos/cms/store/user/twamorka/4gamma/skimtrees/GJets20_Inf_gen.root',
              '/eos/cms/store/user/twamorka/4gamma/skimtrees/GJets40_Inf_gen.root',
              '/eos/cms/store/user/twamorka/4gamma/skimtrees/QCD30_40_gen.root',
              '/eos/cms/store/user/twamorka/4gamma/skimtrees/QCD40_Inf_gen.root',
              '/eos/cms/store/user/twamorka/4gamma/skimtrees/QCD30_Inf_gen.root',
              ],
            
            'weight' : '1',  
            
            'weights' :  [
                       '0.111', 
                       '3.030',
                       '0.316',
                       '3.106',
                       '0.423',
                       '44.197',
                       '197.866',
                       '249.667', 
                        ],
           }
  
  
    
  


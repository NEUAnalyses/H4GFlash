## script for calculating weights on MC events -- Thanks Rafael!
import json, os

eosOutput = '/eos/cms/store/user/twamorka/'

GJets20to40 = ['GJets20to40',
'/GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_backup_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

GJets20toInf = ['GJets20toInf',
'/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

GJets40toInf = ['GJets40toInf',
'/GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

QCD30toInf = ['QCD30toInf',
'/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

QCD30to40 = ['QCD30to40',
'/QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

QCD40toInf = ['QCD40toInf',
'/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

DYJets = ['DYJets',
'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1-74c0514daa3d87bd951f57782e8afcd5/USER'
]


bkgSample = GJets40toInf

#localDir = os.getcwd()

data_file_location = '/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg//MetaData/data/RunIISummer16-2_4_1-25ns_Moriond17/datasets.json'
# if 'crovelli' in bkgSample[1] or 'musella' in bkgSample[1]:
# 	data_file_location = localDir + '/../MetaData/data/microAODdatasets/Spring15BetaV2_MetaV3/bkgPasquale.json'

data_file = open(data_file_location)
data = json.load(data_file)

dataFiles = data[bkgSample[1]]['files']

totalWeight = 0
totalEvents = 0

for files in dataFiles:
	if int(files['nevents']) == 0: continue
	print files['name'], files['nevents']#, files['weights']
	totalWeight += float(files['weights'])
	totalEvents += float(files['nevents'])



print "#################################################################"
print "## Dataset        ## Sum of events        ## Sum of Weights    ##"
print "## ",bkgSample[0],"    ##", totalEvents, "    ##", format(totalWeight, 'f'), " ##"
print "#################################################################"

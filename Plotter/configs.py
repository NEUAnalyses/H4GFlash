##################################################
##################################################
## Configuration parameters to run MakeStack.py ##
##################################################
##################################################

doBlind = False
doSignalRegion = True

isPhoCR = False
addHiggs = True
hideData = False
#addbbH = True
#dyjets = False

#do pile up reweighting
doPUweight = True

year = ""

doSignal = True


#Luminosity to normalize backgrounds
lumi = 35900#pb
#MCSF = 1.0
#signalFactor = 1
#List of datasets to be used (cross section information defined there)
data_file = open("datasets/datasets.json")

#number of bins in histograms
nbin = 30
dr = "sqrt( (leadingPhoton.Eta() - subleadingPhoton.Eta())*(leadingPhoton.Eta() - subleadingPhoton.Eta()) + (leadingPhoton.Phi() - subleadingPhoton.Phi())*(leadingPhoton.Phi() - subleadingPhoton.Phi()) )"

#plots will be saved in dirName
prefix = ""
dirSuffix = "ttHMVA/"
dirPrefix = "/afs/cern.ch/work/m/mgouzevi/private/LIMITS/CLEAN_EPS_GGBB_UPDATE/CMSSW_8_0_28/src/flashgg/bbggTools/stackPlots/"
dirName = dirPrefix + dirSuffix

#Location of root files for each invidivual samples. Name of the root files is defined in datasets/datasets(76).json
#loc = '/eos/cms/store/group/phys_higgs/resonant_HH/RunII/FlatTrees/2016/May2_Mjj70to190_NewCatMVA'
loc = '/eos/cms/store/user/twamorka/FlatTrees_2016/'
bkgLocation = loc + '/Background/'
signalLocation = loc + '/Signal/'
dataLocation = loc + '/Data/'


#plots to be made
plots = []
##plots.append(["dicandidate_Mass", "diHiggsCandidate.M()", "m_{#gamma#gamma jj} [GeV]", 34, 150, 1000])
plots.append(["MXprime", "diHiggsCandidate.M() - dijetCandidate.M() - diphotonCandidate.M() + 250.", "#tilde{M}_{X} [GeV]", 30, 250, 1150])
plots.append(["diPho_Mass", "diphotonCandidate.M()", "m_{#gamma#gamma} [GeV]", 80, 100, 140])
plots.append(["diJet_Mass", "dijetCandidate.M()", "m_{jj} [GeV]", 24, 70, 190])
plots.append(["HHTagger", "HHTagger", "Classification MVA", 54, -1.08, 1.08])
plots.append(["ttHTagger", "ttHTagger", "Classification MVA", 54, -1.08, 1.08])
plots.append(["CosTheta_gg", "fabs(CosTheta_gg)", "| cos #theta_{#gamma#gamma} |", 10, 0, 1])
plots.append(["CosTheta_bb", "fabs(CosTheta_bb)", "| cos #theta_{jj} |", 10, 0, 1])
plots.append(["CosThetaStar_CS", "fabs(CosThetaStar_CS)", "| cos #theta^{CS}_{HH} |", 10, 0, 1])



#cuts to be used to make plots
Cut = " isSignal && diphotonCandidate.M() > 100 && diphotonCandidate.M() < 180 "
Cut += " && dijetCandidate.M() > 70 && dijetCandidate.M() < 190 "

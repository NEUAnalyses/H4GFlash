import FWCore.ParameterSet.Config as cms
import flashgg.Taggers.flashggTags_cff as flashggTags

process = cms.Process("h4gflash")
process.load("flashgg.H4GFlash.H4GFlash_cfi")

process.h4gflash.rho = cms.InputTag('fixedGridRhoAll')
process.h4gflash.vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")
process.h4gflash.puInfo=cms.InputTag("slimmedAddPileupInfo")

process.h4gflash.lumiWeight = cms.double(1.0)
process.h4gflash.intLumi = cms.double(1.0)
process.h4gflash.puReWeight=cms.bool(True)

process.h4gflash.puBins=cms.vdouble()
process.h4gflash.dataPu=cms.vdouble()
process.h4gflash.mcPu=cms.vdouble()

process.h4gflash.vtxTag = cms.untracked.InputTag("goodPrimaryVertices");
print "I'M HERE 1"

print "1.01"

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring("test.root")
)

print "1.1"

process.TFileService = cms.Service("TFileService",
      fileName = cms.string("out.root"),
      closeFileFast = cms.untracked.bool(True)
  )

print "2"

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 2000 )

print "2.1"

# to check which triggers are present ---remove if not needed
#process.TriggerAnalyzer = cms.EDAnalyzer("MiniAODTriggerAnalyzer",
      #bits = cms.InputTag("TriggerResults","","HLT")
      #)
#process.TriggerAnalyzerPath = cms.Path(process.TriggerAnalyzer)

# ----------

# import flashgg customization
from flashgg.MetaData.JobConfig import customize
import FWCore.ParameterSet.VarParsing as VarParsing
# set default options if needed
customize.setDefault("maxEvents",-1)
customize.setDefault("targetLumi",2.58e+3)

print "2.2"

customize.register('PURW',
				True,
				VarParsing.VarParsing.multiplicity.singleton,
				VarParsing.VarParsing.varType.bool,
				"Do PU reweighting?")


# call the customization
customize(process)

print "3"
#vtxTag              = cms.InputTag("goodPrimaryVertices")
process.h4gflash.puReWeight=cms.bool( customize.PURW )
if customize.PURW == False:
	process.h4gflash.puTarget = cms.vdouble()

maxEvents = 5
if customize.maxEvents:
        maxEvents = int(customize.maxEvents)

if customize.inputFiles:
        inputFile = customize.inputFiles

if customize.outputFile:
        outputFile = customize.outputFile

print "4"

if customize.processId == "Data":
        from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel
        process.hltHighLevel= hltHighLevel.clone(HLTPaths = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v*",
                                                                "HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v*",
                                                                "HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v*"
                                                                ))
        process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

        process.load('RecoMET.METFilters.eeBadScFilter_cfi')
        process.eeBadScFilter.EERecHitSource = cms.InputTag("reducedEgamma","reducedEERecHits") # Saved MicroAOD Collection (data only)

        process.dataRequirements = cms.Sequence()
        process.dataRequirements += process.hltHighLevel
        process.dataRequirements += process.eeBadScFilter


process.load("flashgg.Taggers.flashggTags_cff")
process.h4gflash.OutFileName = cms.untracked.string(outputFile)

print "5"

process.p = cms.Path(flashggTags.flashggUnpackedJets*process.h4gflash)

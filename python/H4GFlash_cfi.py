import FWCore.ParameterSet.Config as cms

h4gflash = cms.EDAnalyzer('H4GFlash',

	diphotons = cms.untracked.InputTag("flashggDiPhotons"),
	genphotons = cms.untracked.InputTag("flashggGenPhotons"),
        genparticles = cms.untracked.InputTag("flashggPrunedGenParticles"),
	myTriggers = cms.untracked.vstring(#"HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15",
					   #"HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15",
					   #"HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95",
					   #"HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixel",
					   #"HLT_Diphoton30PV",
					   #"HLT_Diphoton30_18_Solid",
					   #"HLT_Diphoton30EB"
					   "HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v7",
                                           "HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v7"
                                          ),
	triggerTag = cms.InputTag("TriggerResults", "", "HLT")
)

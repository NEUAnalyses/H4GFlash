// Written by Tanvi Wamorkar
// for incorporating 2016 Diphoton preselection


#include <memory>

#include "flashgg/H4GFlash/interface/H4GTools.h"
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

//my includes
#include <memory>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <utility>
#include <cmath>
#include "TTree.h"
#include "TFile.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "flashgg/H4GFlash/interface/H4GTools.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "flashgg/Taggers/interface/GlobalVariablesDumper.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

//FLASHgg files
#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/DataFormats/interface/SinglePhotonView.h"
#include "flashgg/DataFormats/interface/Photon.h"
#include "flashgg/DataFormats/interface/Jet.h"
#include "flashgg/Taggers/interface/GlobalVariablesDumper.h"

bool DEBUG = 0;

bool H4GTools::passLowMassHggPreselection (const flashgg::DiPhotonCandidate * dipho){
    bool isPreselected = false;
    if ( ( dipho->leadingPhoton()->full5x5_r9() > 0.8
            || dipho->leadingPhoton()->egChargedHadronIso() < 20
            || dipho->leadingPhoton()->egChargedHadronIso()/dipho->leadingPhoton()->pt() < 0.3 )
          &&
          ( dipho->subLeadingPhoton()->full5x5_r9() > 0.8
            || dipho->subLeadingPhoton()->egChargedHadronIso() < 20
            || dipho->subLeadingPhoton()->egChargedHadronIso()/dipho->subLeadingPhoton()->pt() < 0.3)

          && ( ((fabs(dipho->leadingPhoton()->superCluster()->eta()) < 1.4442 && dipho->leadingPhoton()->hadronicOverEm() < 0.07)
          ||(fabs(dipho->leadingPhoton()->superCluster()->eta()) > 1.566 && dipho->leadingPhoton()->hadronicOverEm ()< 0.035)) && ((fabs(dipho->subLeadingPhoton()->superCluster()->eta()) < 1.4442 &&  dipho->subLeadingPhoton()->hadronicOverEm() < 0.07)
          ||(fabs(dipho->subLeadingPhoton()->superCluster()->eta()) > 1.566 && dipho->subLeadingPhoton()->hadronicOverEm() < 0.035) ) )

          && (dipho->leadingPhoton()->pt() >30.0 && dipho->subLeadingPhoton()->pt() > 18.0)
          && (fabs(dipho->leadingPhoton()->superCluster()->eta()) < 2.5 && fabs(dipho->subLeadingPhoton()->superCluster()->eta()) < 2.5)
          && (fabs(dipho->leadingPhoton()->superCluster()->eta()) < 1.4442 || fabs(dipho->leadingPhoton()->superCluster()->eta()) > 1.566 )
          && (fabs(dipho->subLeadingPhoton()->superCluster()->eta()) < 1.4442 || fabs(dipho->subLeadingPhoton()->superCluster()->eta()) > 1.566)
          && ( (fabs(dipho->leadingPhoton()->superCluster()->eta()) < 1.4442 && fabs(subLeadingPhoton()->superCluster()->eta()) < 1.4442)
          || (fabs(dipho->leadingPhoton()->superCluster()->eta()) < 1.4442 && dipho->leadingPhoton()->full5x5_r9()>0.85 && fabs(dipho->subLeadingPhoton()->superCluster()->eta()) > 1.566 && dipho->subLeadingPhoton()->full5x5_r9()>0.90 )
          || (fabs(dipho->leadingPhoton()->superCluster()->eta()) > 1.566 && dipho->leadingPhoton()->full5x5_r9()>0.90 && fabs(dipho->subLeadingPhoton()->superCluster()->eta()) < 1.4442 && dipho->subLeadingPhoton()->full5x5_r9()>0.85 )
          || (fabs(dipho->leadingPhoton()->superCluster()->eta()) > 1.566 && dipho->leadingPhoton()->full5x5_r9()>0.90 && fabs(dipho->subLeadingPhoton()->superCluster()->eta()) > 1.566 && dipho->subLeadingPhoton()->full5x5_r9()>0.90 ) )
          && dipho->mass() > 55
          && (dipho->leadingPhoton()->pt() > 0.47*dipho->mass() && dipho->subLeadingPhoton()->pt() > 0.28*dipho->mass())
          && (!dipho->leadingPhoton()->hasPixelSeed()) && (!dipho->subLeadingPhoton()->hasPixelSeed())
          && (dipho->leadPhotonId() > -0.9 && dipho->subLeadPhotonId() > -0.9)

        ) {
 	    isPreselected = true;
      if (isPreselected) return true;
      else return false;
}
std::vector<flashgg::DiPhotonCandidate> H4GTools::DiPhotonPreselection(vector<flashgg::DiPhotonCandidate> diphoCol)
{
    std::vector<flashgg::DiPhotonCandidate> selDiPhos;

    for ( unsigned int dp = 0; dp < diphoCol.size(); dp++)
    {
      flashgg::DiPhotonCandidate dipho = diphoCol[dp];

      if (passLowMassHggPreselection(&dipho)){
	selDiPhos.push_back(dipho);
	continue;
      }
    }

    return selDiPhos;
}
}

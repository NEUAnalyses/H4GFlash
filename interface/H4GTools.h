
//FLASHgg files
// #include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
// #include "flashgg/DataFormats/interface/SinglePhotonView.h"
// #include "flashgg/DataFormats/interface/Photon.h"
// #include "flashgg/DataFormats/interface/Jet.h"
// #include "DataFormats/VertexReco/interface/Vertex.h"
// #include "DataFormats/Math/interface/LorentzVector.h"
// #include "FWCore/Common/interface/TriggerNames.h"
// #include "DataFormats/Common/interface/TriggerResults.h"
// #include "flashgg/DataFormats/interface/Electron.h"
// #include "flashgg/DataFormats/interface/Muon.h"


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
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"

#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/DataFormats/interface/SinglePhotonView.h"
#include "flashgg/DataFormats/interface/Photon.h"
#include "flashgg/DataFormats/interface/Jet.h"
// #include "flashgg/Taggers/interface/GlobalVariablesDumper.h"

namespace H4GTools {

      typedef math::XYZTLorentzVector LorentzVector;

      struct H4G_DiPhoton{
        LorentzVector p4;
        int ip1;
        int ip2;
	float SumPt;
      };

      struct H4G_TetraPhoton{
        LorentzVector p4;
        int ip1;
        int ip2;
        int ip3;
        int ip4;
        int idp1;
        int idp2;
	float SumPt;
      };
      // bool passLowMassHggPreselection(const flashgg::DiPhotonCandidate * dipho);
      // std::vector<flashgg::DiPhotonCandidate> DiPhotonPreselection( vector<flashgg::DiPhotonCandidate> diphoCol );

      


      std::map<std::string,int> TriggerSelection(std::vector<std::string> myTriggers, const edm::TriggerNames &names, edm::Handle<edm::TriggerResults> triggerBits)
      {
         std::map<std::string,int> triggerResults;
         for(unsigned int j = 0; j < myTriggers.size(); j++)
         {
            int accepted = 0;
            for ( unsigned int i = 0; i < triggerBits->size(); i++)
            {
            //if(DEBUG) std::cout << "[H4GTools::TriggerSelection] Trigger name: " << names.triggerName(i) << " \t Decision: " << triggerBits->accept(i) << std::endl;
               if((names.triggerName(i)).find(myTriggers[j]) != std::string::npos )
               {
                  if(triggerBits->accept(i) == 1){
                     accepted = 1;
                  }
               }
            }
//        triggerResults.push_back(accepted);
            triggerResults[myTriggers[j]] = accepted;
         }
          return triggerResults;
      };


}

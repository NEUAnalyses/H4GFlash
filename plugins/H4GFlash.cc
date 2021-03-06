// -*- C++ -*-
//
// Package:    H4G/H4GFlash
// Class:      H4GFlash
//
/**\class H4GFlash H4GFlash.cc H4G/H4GFlash/plugins/H4GFlash.cc
 Description: [one line class summary]
 Implementation:
 [Notes on implementation]
 */
//
// Original Author:  Rafael Teixeira De Lima
//         Created:  Sat, 26 Mar 2016 16:30:02 GMT
//
//
// system include files
#include <memory>

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

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.
class H4GFlash : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
public:
    explicit H4GFlash(const edm::ParameterSet&);
    ~H4GFlash();

    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

    //Selector elements:
    typedef math::XYZTLorentzVector LorentzVector;
    edm::EDGetTokenT<edm::View<flashgg::DiPhotonCandidate> > diphotonsToken_;
    edm::EDGetTokenT<edm::View<flashgg::DiPhotonCandidate> > AfterSelectionDiPhotonToken_;
    edm::EDGetTokenT<edm::View<pat::PackedGenParticle> > genPhotonsToken_;
    //edm::EDGetTokenT<edm::View<reco::GenParticle> > genPhotonsToken_;
    edm::EDGetTokenT<edm::View<reco::GenParticle> > genParticlesToken_;
    edm::EDGetTokenT<GenEventInfoProduct> genInfoToken_;
    edm::EDGetTokenT<edm::TriggerResults> triggerToken_;
    edm::InputTag genInfoInputTag_;
    //edm::EDGetTokenT<SinglePhotonView> singlephotonviewToken_;
    edm::InputTag vtxTag_;
    edm::EDGetTokenT<reco::Vertex> vtxHT_;
    edm::EDGetTokenT<edm::View<reco::Vertex> > vertexToken_;

    long int counter;

    flashgg::GlobalVariablesDumper* globVar_;

    //Out tree elements:
    edm::Service<TFileService> fs;
    TTree* outTree;
    int n_pho, n_pho_presel, run, lumi, evtnum, passTrigger, nicematch, passpresel, passMVA, cat_flag, preselcat_flag, n_dipho, n_preseldipho;
    double rho;
    std::vector<H4GTools::H4G_DiPhoton> v_h4g_diphos;
    std::vector<H4GTools::H4G_TetraPhoton> v_h4g_tetraphos;
    std::vector<LorentzVector> v_pho_p4;
    std::vector<LorentzVector> v_genpho_p4;
    std::vector<LorentzVector> v_preseldipho;
    std::vector<float> v_genpho_p4_pt;
    std::vector<LorentzVector> v_genpho2_p4;
    std::vector<int> v_genpho_p4_momid;
    std::vector<float> v_genpho_p4_mommass;
    std::vector<int> v_genpho_motherpdgid;
    std::vector<float> v_pho_pt;
    std::vector<float> v_pho_eta;
    std::vector<float> v_pho_phi;
    std::vector<float> v_pho_e;

    std::vector<LorentzVector> v_genlep_p4;
    std::vector<LorentzVector> v_genmatch_p4;
    std::vector<LorentzVector> v_fatpho1_p4;
    std::vector<float> v_fatpho1_pt;
    std::vector<float> v_gen_a_mass;
    std::vector<float> v_gen_a_id;
    std::vector<float> v_gen_a_pt;
    std::vector<float> v_gen_a_eta;
    std::vector<float> v_gen_a_phi;

    std::vector<float> v_gen_X_mass;
    std::vector<float> v_gen_X_id;
    std::vector<float> v_gen_X_pt;
    std::vector<float> v_gen_X_eta;
    std::vector<float> v_gen_X_phi;


    //---- Inputs defined here:
    //     http://cmslxr.fnal.gov/lxr/source/DataFormats/PatCandidates/interface/Photon.h
    //     http://cmslxr.fnal.gov/lxr/source/DataFormats/PatCandidates/src/Photon.cc
    // photon ids and cluster variables
    std::vector<float> v_pho_hadronicOverEm;
    //       std::vector<float> v_pho_chargedHadronIso;
    //       std::vector<float> v_pho_neutralHadronIso;
    //       std::vector<float> v_pho_photonIso;
    std::vector<float> v_pho_passElectronVeto;
    std::vector<float> v_pho_hasPixelSeed;
    //       std::vector<float> v_pho_ecalPFClusterIso;
    //       std::vector<float> v_pho_hcalPFClusterIso;
    std::vector<float> v_pho_eMax;
    std::vector<float> v_pho_e3x3;
    std::vector<float> v_pho_subClusRawE1;
    //       std::vector<float> v_pho_subClusDPhi1;
    //       std::vector<float> v_pho_subClusDEta1;
    std::vector<float> v_pho_subClusRawE2;
    //       std::vector<float> v_pho_subClusDPhi2;
    //       std::vector<float> v_pho_subClusDEta2;
    std::vector<float> v_pho_subClusRawE3;
    //       std::vector<float> v_pho_subClusDPhi3;
    //       std::vector<float> v_pho_subClusDEta3;
    std::vector<float> v_pho_iPhi;
    std::vector<float> v_pho_iEta;
    std::vector<float> v_pho_r9;
    std::vector<float> v_pho_full5x5_r9;

    std::vector<float> v_pho_sigmaIetaIeta;
    std::vector<float> v_pho_sigmaIphiIphi;
    std::vector<float> v_pho_dr03HcalTowerSumEt;
    std::vector<float> v_pho_dr03EcalRecHitSumEt;
    std::vector<float> v_pho_dr03TkSumPt;

    //---- from http://cmslxr.fnal.gov/lxr/source/DataFormats/PatCandidates/interface/Photon.h


    std::vector<float> v_pho_e2nd                 ;
    std::vector<float> v_pho_eTop                 ;
    std::vector<float> v_pho_eBottom              ;
    std::vector<float> v_pho_eLeft                ;
    std::vector<float> v_pho_eRight               ;
    std::vector<float> v_pho_see                  ;
    std::vector<float> v_pho_spp                  ;
    std::vector<float> v_pho_sep                  ;
    std::vector<float> v_pho_maxDR                ;
    std::vector<float> v_pho_maxDRDPhi            ;
    std::vector<float> v_pho_maxDRDEta            ;
    std::vector<float> v_pho_maxDRRawEnergy       ;
    //std::vector<float> v_pho_subClusRawE1         ;
    //std::vector<float> v_pho_subClusRawE2         ;
    //std::vector<float> v_pho_subClusRawE3         ;
    std::vector<float> v_pho_subClusDPhi1         ;
    std::vector<float> v_pho_subClusDPhi2         ;
    std::vector<float> v_pho_subClusDPhi3         ;
    std::vector<float> v_pho_subClusDEta1         ;
    std::vector<float> v_pho_subClusDEta2         ;
    std::vector<float> v_pho_subClusDEta3         ;
    std::vector<float> v_pho_cryPhi               ;
    std::vector<float> v_pho_cryEta               ;
    std::vector<float> v_pho_ecalPFClusterIso     ;
    std::vector<float> v_pho_hcalPFClusterIso     ;
    std::vector<float> v_pho_caloIso              ;
    std::vector<float> v_pho_hcalIso              ;
    std::vector<float> v_pho_ecalIso              ;
    std::vector<float> v_pho_trackIso             ;
    std::vector<float> v_pho_genmatch             ;
    std::vector<float> v_pho_recomatch            ;
    std::vector<float>  v_pho_matchedgenphoton    ;
    std::vector<float> v_matchflag                ;
    //---- from http://cmslxr.fnal.gov/lxr/source/RecoEgamma/EgammaTools/interface/EcalRegressionData.h
    std::vector<float> v_pho_scRawEnergy          ;
    std::vector<float> v_pho_scCalibEnergy        ;
    std::vector<float> v_pho_scPreShowerEnergy    ;
    //       std::vector<float> v_pho_scEta                ;
    //       std::vector<float> v_pho_scPhi                ;
    //       std::vector<float> v_pho_scEtaWidth           ;
    //       std::vector<float> v_pho_scPhiWidth           ;
    //       std::vector<float> v_pho_seedClusEnergy       ;
    //
    //       std::vector<float> v_pho_sigmaIEtaIEta        ;
    //       std::vector<float> v_pho_sigmaIEtaIPhi        ;
    //       std::vector<float> v_pho_sigmaIPhiIPhi        ;
    //
    std::vector<float> v_pho_scPreShowerEnergyOverSCRawEnergy     ;
    //       std::vector<float> v_pho_scSeedR9                             ;
    //       std::vector<float> v_pho_seedClusEnergyOverSCRawEnergy        ;
    //       std::vector<float> v_pho_eMaxOverSCRawEnergy                  ;
    //       std::vector<float> v_pho_e2ndOverSCRawEnergy                  ;
    //       std::vector<float> v_pho_seedLeftRightAsym                    ;
    //       std::vector<float> v_pho_seedTopBottomAsym                    ;
    //       std::vector<float> v_pho_maxSubClusDRRawEnergyOverSCRawEnergy ;
    //
    //       std::vector<float> v_pho_subClusRawEnergyOverSCRawEnergy_0   ;
    //       std::vector<float> v_pho_subClusRawEnergy_0                  ;
    //       std::vector<float> v_pho_subClusDPhi_0                       ;
    //       std::vector<float> v_pho_subClusDEta_0                       ;
    //
    //       std::vector<float> v_pho_subClusRawEnergyOverSCRawEnergy_1   ;
    //       std::vector<float> v_pho_subClusRawEnergy_1                  ;
    //       std::vector<float> v_pho_subClusDPhi_1                       ;
    //       std::vector<float> v_pho_subClusDEta_1                       ;
    //
    //       std::vector<float> v_pho_subClusRawEnergyOverSCRawEnergy_2   ;
    //       std::vector<float> v_pho_subClusRawEnergy_2                  ;
    //       std::vector<float> v_pho_subClusDPhi_2                       ;
    //       std::vector<float> v_pho_subClusDEta_2                       ;

    //---- from https://cmssdt.cern.ch/SDT/doxygen/CMSSW_8_0_11/doc/html/df/d55/EgammaCandidates_2interface_2Photon_8h_source.html

    std::vector<float>  v_pho_e1x5   ;
    std::vector<float>  v_pho_e2x5   ;
    //       std::vector<float>  e3x3   ;
    std::vector<float>  v_pho_e5x5   ;
    std::vector<float>  v_pho_maxEnergyXtal   ;
    std::vector<float>  v_pho_sigmaEtaEta   ;
    //std::vector<float>  v_pho_full5x5_sigmaPhiPhi ;
    //       std::vector<float>  sigmaIetaIeta   ;
    std::vector<float>  v_pho_r1x5    ;
    std::vector<float>  v_pho_r2x5    ;
    //       std::vector<float>  r9    ;

    std::vector<float>  v_pho_full5x5_e1x5   ;
    std::vector<float>  v_pho_full5x5_e2x5   ;
    std::vector<float>  v_pho_full5x5_e3x3   ;
    std::vector<float>  v_pho_full5x5_e5x5   ;
    std::vector<float>  v_pho_full5x5_maxEnergyXtal   ;
    std::vector<float>  v_pho_full5x5_sigmaEtaEta   ;
    std::vector<float>  v_pho_full5x5_sigmaIetaIeta   ;
    std::vector<float>  v_pho_full5x5_r1x5    ;
    std::vector<float>  v_pho_full5x5_r2x5    ;
    //       std::vector<float>  full5x5_r9    ;


    std::vector<float>  v_pho_mipChi2   ;
    std::vector<float>  v_pho_mipTotEnergy   ;
    std::vector<float>  v_pho_mipSlope   ;
    std::vector<float>  v_pho_mipIntercept   ;
    std::vector<int>    v_pho_mipNhitCone   ;
    std::vector<int>    v_pho_mipIsHalo   ;


    std::vector<float>  v_pho_ecalRecHitSumEtConeDR04   ;
    std::vector<float>  v_pho_hcalTowerSumEtConeDR04   ;
    std::vector<float>  v_pho_hcalDepth1TowerSumEtConeDR04   ;
    std::vector<float>  v_pho_hcalDepth2TowerSumEtConeDR04   ;
    std::vector<float>  v_pho_hcalTowerSumEtBcConeDR04   ;
    std::vector<float>  v_pho_hcalDepth1TowerSumEtBcConeDR04   ;
    std::vector<float>  v_pho_hcalDepth2TowerSumEtBcConeDR04   ;
    //  Track pT sum
    std::vector<float>  v_pho_trkSumPtSolidConeDR04   ;
    //As above, excluding the core at the center of the cone
    std::vector<float>  v_pho_trkSumPtHollowConeDR04   ;
    //Returns number of tracks in a cone of dR
    std::vector<int>    v_pho_nTrkSolidConeDR04   ;
    //As above, excluding the core at the center of the cone
    std::vector<int>    v_pho_nTrkHollowConeDR04   ;
    //
    std::vector<float>  v_pho_ecalRecHitSumEtConeDR03   ;
    std::vector<float>  v_pho_hcalTowerSumEtConeDR03   ;
    std::vector<float>  v_pho_hcalDepth1TowerSumEtConeDR03   ;
    std::vector<float>  v_pho_hcalDepth2TowerSumEtConeDR03   ;
    std::vector<float>  v_pho_hcalTowerSumEtBcConeDR03   ;
    std::vector<float>  v_pho_hcalDepth1TowerSumEtBcConeDR03   ;
    std::vector<float>  v_pho_hcalDepth2TowerSumEtBcConeDR03   ;
    //  Track pT sum c
    std::vector<float>  v_pho_trkSumPtSolidConeDR03   ;
    //As above, excluding the core at the center of the cone
    std::vector<float>  v_pho_trkSumPtHollowConeDR03   ;
    //Returns number of tracks in a cone of dR
    std::vector<int>    v_pho_nTrkSolidConeDR03   ;
    //As above, excluding the core at the center of the cone
    std::vector<int>    v_pho_nTrkHollowConeDR03   ;

    std::vector<float>  v_pho_chargedHadronIso   ;
    std::vector<float>  v_pho_chargedHadronIsoWrongVtx   ;
    std::vector<float>  v_pho_neutralHadronIso   ;
    std::vector<float>  v_pho_photonIso   ;
    std::vector<float>  v_pho_sumChargedParticlePt   ;
    std::vector<float>  v_pho_sumNeutralHadronEtHighThreshold   ;
    std::vector<float>  v_pho_sumPhotonEtHighThreshold   ;
    std::vector<float>  v_pho_sumPUPt   ;
    std::vector<float>  v_dr_genreco;

    std::vector<int>    v_pho_nClusterOutsideMustache   ;
    std::vector<float>  v_pho_etOutsideMustache   ;
    std::vector<float>  v_pho_pfMVA   ;
    std::vector<float>  v_pho_conversion ;
    std::vector<LorentzVector>  v_reco_genmatch;
    std::vector<LorentzVector>  v_reco_notgenmatch;
    std::vector<float>  v_genpho_pt;
    std::vector<float>  v_gen_pdgid;
    std::vector<float>  v_genmom_pdgid;
    std::vector<float>  v_genreco_dR;
    std::vector<float> v_genreco_ptdiff;
    std::vector<std::vector<float>> v_pho_dr;
    std::vector<std::vector<float>> v_genpho_dr;
    //    std::vector<float> v_genpho_pt;
    std::vector<std::vector<float>> v_pho_dphi;
    std::vector<std::vector<float>> v_pho_deta;
    std::vector<std::map<std::string, int>> v_pho_cutid;
    std::vector<float> v_pho_mva;
    std::map<std::string, int> myTriggerResults;
    std::vector<float> v_fatpho_number;
    std::vector<float> v_matchreco_count;
    std::vector<float> v_genmatch_full5x5_r9;
    std::vector<float> v_genmatch_chargedHadronIso;
    std::vector<float> v_genmatch_hadronicOverEm;
    std::vector<float> v_genmatch_hasPixelSeed;
    std::vector<float> v_genmatch_ecalPFClusterIso;
    std::vector<float> v_genmatch_sigmaIetaIeta;
    std::vector<float> v_genmatch_passElectronVeto;
    std::vector<float> v_notgenmatch_passElectronVeto;
    std::vector<float> phosTemp;
    std::vector<float> phosTemp_presel;
    std::vector<float> v_genmatch_pt;
    std::vector<float> v_genmatch_mva;
    std::vector<float> v_genmatch_eta;
    std::vector<float> v_genmatch_phi;
    std::vector<float> v_genmatch_trackIso;
    std::vector<float> v_genmatching;
    std::vector<float> v_genmatch_int;
    std::vector<float> v_nicematch;
    std::vector<float> v_genpho_id;
    std::vector<float>  v_genrecoPt_ratio;
    // gen mother information
    std::vector<LorentzVector> v_genmother_p4;
    std::vector<float> v_genmother_pt;
    std::vector<float> v_genmother_eta;
    std::vector<float> v_genmother_phi;
    std::vector<float> v_mother_id;
    std::vector<float> v_daughter_id;
    std::vector<LorentzVector> v_daughter_p4;
    std::vector<LorentzVector> v_4case;
    std::vector<LorentzVector> v_daughterofa_p4;
    std::vector<LorentzVector> v_photonDaughters_p4;
    std::vector<LorentzVector> v_mergedpho_p4;
    std::vector<LorentzVector> v_fatpho_p4;
    std::vector<LorentzVector> v_genlevelphoton_p4;
    std::vector<LorentzVector> v_fatpho_collection;
    std::vector<float> v_reco_genmatchcount;
    std::vector<float> v_fatpho_energy;
    std::vector<float> v_genmatch_ver2;
    std::vector<int> v_resolvedcount;

    double genTotalWeight;
    //Parameters
    std::vector<std::string> myTriggers;

    std::map<std::string, int> triggerStats;
    TFile* outFile;

private:
    virtual void beginJob() override;
    virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
    virtual void endJob() override;

    // ----------member data ---------------------------

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
H4GFlash::H4GFlash(const edm::ParameterSet& iConfig):
diphotonsToken_( consumes<edm::View<flashgg::DiPhotonCandidate> >( iConfig.getUntrackedParameter<edm::InputTag> ( "diphotons", edm::InputTag( "flashggDiPhotons" ) ) ) ),
genPhotonsToken_( consumes<edm::View<pat::PackedGenParticle> >( iConfig.getUntrackedParameter<edm::InputTag>( "genphotons", edm::InputTag( "flashggGenPhotons" ) ) ) ),
genParticlesToken_( consumes<edm::View<reco::GenParticle> >( iConfig.getUntrackedParameter<edm::InputTag>( "genparticles", edm::InputTag( "flashggPrunedGenParticles" ) ) ) ),
//singlephotonviewToken_( ( iConfig.getUntrackedParameter<edm::InputTag> ("singlephotonview", edm::InputTag("flashggSinglePhotonView" ) ) ) )
//vtxTag_ = iConfig.getParameter<edm::InputTag>("vtxTag");
//vtxHT_( consumes<reco::VertexCollection>(vtxTag_));
vertexToken_(consumes<edm::View<reco::Vertex> >(iConfig.getUntrackedParameter<edm::InputTag> ("vertex",edm::InputTag("offlineSlimmedPrimaryVertices"))))

{
  AfterSelectionDiPhotonToken_ = consumes<edm::View<flashgg::DiPhotonCandidate> >( iConfig.getUntrackedParameter<edm::InputTag> ( "PreselectedDiPhotons", edm::InputTag( "flashggPreselectedDiPhotonsLowMass" ) ) );

    //now do what ever initialization is needed
    genInfoInputTag_ = iConfig.getUntrackedParameter<edm::InputTag>( "genInfo", edm::InputTag("generator") );
    genInfoToken_ = consumes<GenEventInfoProduct>( genInfoInputTag_ );
    vtxTag_ = iConfig.getUntrackedParameter<edm::InputTag>("vtxTag");
    vtxHT_  = consumes<reco::Vertex> (vtxTag_);
    //singlephotonviewToken_ = iConfig.getUntrackedParameter<edm::InputTag> ("singlephotonview", edm::InputTag("flashggSinglePhotonView" ) );
    //singlephotonviewToken_ = consumes<SinglePhotonView>(singlephotonviewTag_);
    globVar_ = new flashgg::GlobalVariablesDumper(iConfig, consumesCollector() );
    double lumiWeight_ = ( iConfig.getParameter<double>( "lumiWeight" ) );
    globVar_->dumpLumiFactor(lumiWeight_);
    //double maxGenDeltaR_ = (iConfig.getParameter<double> ("maxGenDeltaR"));
    usesResource("TFileService");
    //   edm::Service<TFileService> fs;
    outTree = fs->make<TTree> ("H4GTree", "Tree for h->4g analysis");
    outTree->Branch("run", &run, "run/I");
    outTree->Branch("lumi", &lumi, "lumi/I");
    outTree->Branch("evtnum", &evtnum, "evtnum/I");

    outTree->Branch("rho", &rho, "rho/D");
    outTree->Branch("passTrigger", &passTrigger, "passTrigger/I");
    outTree->Branch("passpresel", &passpresel, "passpresel/I");
    outTree->Branch("passMVA", &passMVA, "passMVA/I");
    outTree->Branch("nicematch", &nicematch, "rho/I");
    outTree->Branch("v_h4g_diphos", &v_h4g_diphos);
    //outTree->Branch("v_h4g_tetraphos", &v_h4g_tetraphos);
    outTree->Branch("cat_flag", &cat_flag, "cat_flag/I");
    outTree->Branch("preselcat_flag", &preselcat_flag, "preselcat_flag/I");
    outTree->Branch("v_preseldipho", &v_preseldipho);
    outTree->Branch("n_pho", &n_pho, "n_pho/I");
    outTree->Branch("n_pho_presel", &n_pho_presel, "n_pho_presel/I");
    outTree->Branch("n_dipho", &n_dipho, "n_dipho/I");
    outTree->Branch("n_preseldipho", &n_preseldipho, "n_preseldipho/I");
    outTree->Branch("v_pho_p4", &v_pho_p4);
    outTree->Branch("v_genpho_p4", &v_genpho_p4);
    outTree->Branch("v_genpho_p4_pt",&v_genpho_p4_pt);
    outTree->Branch("v_genpho2_p4", &v_genpho2_p4);
    outTree->Branch("v_genpho_motherpdgid", &v_genpho_motherpdgid);
    outTree->Branch("v_pho_pt", &v_pho_pt);
    outTree->Branch("v_pho_eta", &v_pho_eta);
    outTree->Branch("v_pho_phi", &v_pho_phi);
    outTree->Branch("v_pho_e", &v_pho_e);

    outTree->Branch("v_pho_hadronicOverEm",   &v_pho_hadronicOverEm  );
    //    outTree->Branch("v_pho_chargedHadronIso", &v_pho_chargedHadronIso);
    //    outTree->Branch("v_pho_neutralHadronIso", &v_pho_neutralHadronIso);
    outTree->Branch("v_pho_photonIso",        &v_pho_photonIso );
    outTree->Branch("v_pho_passElectronVeto", &v_pho_passElectronVeto);
    outTree->Branch("v_pho_hasPixelSeed",     &v_pho_hasPixelSeed );
    //    outTree->Branch("v_pho_ecalPFClusterIso", &v_pho_ecalPFClusterIso);
    //    outTree->Branch("v_pho_hcalPFClusterIso", &v_pho_hcalPFClusterIso);
    outTree->Branch("v_pho_eMax",             &v_pho_eMax );
    outTree->Branch("v_pho_e3x3",             &v_pho_e3x3 );
    //    outTree->Branch("v_pho_subClusRawE1",     &v_pho_subClusRawE1 );
    //    outTree->Branch("v_pho_subClusDPhi1",     &v_pho_subClusDPhi1 );
    //    outTree->Branch("v_pho_subClusDEta1",     &v_pho_subClusDEta1 );
    //    outTree->Branch("v_pho_subClusRawE2",     &v_pho_subClusRawE2 );
    //    outTree->Branch("v_pho_subClusDPhi2",     &v_pho_subClusDPhi2 );
    //    outTree->Branch("v_pho_subClusDEta2",     &v_pho_subClusDEta2 );
    //    outTree->Branch("v_pho_subClusRawE3",     &v_pho_subClusRawE3 );
    //    outTree->Branch("v_pho_subClusDPhi3",     &v_pho_subClusDPhi3 );
    //    outTree->Branch("v_pho_subClusDEta3",     &v_pho_subClusDEta3 );
    outTree->Branch("v_pho_iPhi",             &v_pho_iPhi );
    outTree->Branch("v_pho_iEta",             &v_pho_iEta );
    outTree->Branch("v_pho_r9",               &v_pho_r9 );
    outTree->Branch("v_pho_full5x5_r9",       &v_pho_full5x5_r9 );

    //---- more photon id variables

    outTree->Branch("v_pho_sigmaIetaIeta"        ,     &v_pho_sigmaIetaIeta );
    outTree->Branch("v_pho_sigmaIphiIphi"        ,     &v_pho_sigmaIphiIphi );
    //outTree->Branch("v_pho_full5x5_sigmaPhiPhi"  ,     &v_pho_full5x5_sigmaPhiPhi   );
    outTree->Branch("v_pho_dr03HcalTowerSumEt"   ,     &v_pho_dr03HcalTowerSumEt );
    outTree->Branch("v_pho_dr03EcalRecHitSumEt"  ,     &v_pho_dr03EcalRecHitSumEt );
    outTree->Branch("v_pho_dr03TkSumPt"          ,     &v_pho_dr03TkSumPt );

    //---- from http://cmslxr.fnal.gov/lxr/source/DataFormats/PatCandidates/interface/Photon.h
    outTree->Branch("v_pho_e2nd"                 ,     &v_pho_e2nd );
    outTree->Branch("v_pho_eTop"                 ,     &v_pho_eTop );
    outTree->Branch("v_pho_eBottom"              ,     &v_pho_eBottom );
    outTree->Branch("v_pho_eLeft"                ,     &v_pho_eLeft );
    outTree->Branch("v_pho_eRight"               ,     &v_pho_eRight );
    outTree->Branch("v_pho_see"                  ,     &v_pho_see );
    outTree->Branch("v_pho_spp"                  ,     &v_pho_spp );
    outTree->Branch("v_pho_sep"                  ,     &v_pho_sep );
    outTree->Branch("v_pho_maxDR"                ,     &v_pho_maxDR );
    outTree->Branch("v_pho_maxDRDPhi"            ,     &v_pho_maxDRDPhi );
    outTree->Branch("v_pho_maxDRDEta"            ,     &v_pho_maxDRDEta );
    outTree->Branch("v_pho_maxDRRawEnergy"       ,     &v_pho_maxDRRawEnergy );
    outTree->Branch("v_pho_subClusRawE1"         ,     &v_pho_subClusRawE1 );
    outTree->Branch("v_pho_subClusRawE2"         ,     &v_pho_subClusRawE2 );
    outTree->Branch("v_pho_subClusRawE3"         ,     &v_pho_subClusRawE3 );
    outTree->Branch("v_pho_subClusDPhi1"         ,     &v_pho_subClusDPhi1 );
    outTree->Branch("v_pho_subClusDPhi2"         ,     &v_pho_subClusDPhi2 );
    outTree->Branch("v_pho_subClusDPhi3"         ,     &v_pho_subClusDPhi3 );
    outTree->Branch("v_pho_subClusDEta1"         ,     &v_pho_subClusDEta1 );
    outTree->Branch("v_pho_subClusDEta2"         ,     &v_pho_subClusDEta2 );
    outTree->Branch("v_pho_subClusDEta3"         ,     &v_pho_subClusDEta3 );
    outTree->Branch("v_pho_cryPhi"               ,     &v_pho_cryPhi );
    outTree->Branch("v_pho_cryEta"               ,     &v_pho_cryEta );
    outTree->Branch("v_pho_ecalPFClusterIso"     ,     &v_pho_ecalPFClusterIso );
    outTree->Branch("v_pho_hcalPFClusterIso"     ,     &v_pho_hcalPFClusterIso );
    outTree->Branch("v_pho_caloIso"              ,     &v_pho_caloIso );
    outTree->Branch("v_pho_hcalIso"              ,     &v_pho_hcalIso );
    outTree->Branch("v_pho_ecalIso"              ,     &v_pho_ecalIso );
    outTree->Branch("v_pho_trackIso"             ,     &v_pho_trackIso );



    //---- from http://cmslxr.fnal.gov/lxr/source/RecoEgamma/EgammaTools/interface/EcalRegressionData.h
    outTree->Branch("v_pho_scRawEnergy"                              ,          &v_pho_scRawEnergy );
    //    outTree->Branch("v_pho_scCalibEnergy"                            ,          &v_pho_scCalibEnergy );
    //    outTree->Branch("v_pho_scPreShowerEnergy"                        ,          &v_pho_scPreShowerEnergy );
    //    outTree->Branch("v_pho_scEta"                                    ,          &v_pho_scEta );
    //    outTree->Branch("v_pho_scPhi"                                    ,          &v_pho_scPhi );
    //    outTree->Branch("v_pho_scEtaWidth"                               ,          &v_pho_scEtaWidth );
    //    outTree->Branch("v_pho_scPhiWidth"                               ,          &v_pho_scPhiWidth );
    //    outTree->Branch("v_pho_seedClusEnergy"                           ,          &v_pho_seedClusEnergy );
    //    outTree->Branch("v_pho_sigmaIEtaIEta"                            ,          &v_pho_sigmaIEtaIEta );
    //    outTree->Branch("v_pho_sigmaIEtaIPhi"                            ,          &v_pho_sigmaIEtaIPhi );
    //    outTree->Branch("v_pho_sigmaIPhiIPhi"                            ,          &v_pho_sigmaIPhiIPhi );
    //    outTree->Branch("v_pho_scPreShowerEnergyOverSCRawEnergy"         ,          &v_pho_scPreShowerEnergyOverSCRawEnergy );
    //    outTree->Branch("v_pho_scSeedR9"                                 ,          &v_pho_scSeedR9 );
    //    outTree->Branch("v_pho_seedClusEnergyOverSCRawEnergy"            ,          &v_pho_seedClusEnergyOverSCRawEnergy );
    //    outTree->Branch("v_pho_eMaxOverSCRawEnergy"                      ,          &v_pho_eMaxOverSCRawEnergy );
    //    outTree->Branch("v_pho_e2ndOverSCRawEnergy"                      ,          &v_pho_e2ndOverSCRawEnergy );
    //    outTree->Branch("v_pho_seedLeftRightAsym"                        ,          &v_pho_seedLeftRightAsym );
    //    outTree->Branch("v_pho_seedTopBottomAsym"                        ,          &v_pho_seedTopBottomAsym );
    //    outTree->Branch("v_pho_maxSubClusDRRawEnergyOverSCRawEnergy"     ,          &v_pho_maxSubClusDRRawEnergyOverSCRawEnergy );
    //
    //    outTree->Branch("v_pho_subClusRawEnergyOverSCRawEnergy_0"        ,          &v_pho_subClusRawEnergyOverSCRawEnergy_0 );
    //    outTree->Branch("v_pho_subClusRawEnergy_0"                       ,          &v_pho_subClusRawEnergy_0 );
    //    outTree->Branch("v_pho_subClusDPhi_0"                            ,          &v_pho_subClusDPhi_0 );
    //    outTree->Branch("v_pho_subClusDEta_0"                            ,          &v_pho_subClusDEta_0 );
    //
    //    outTree->Branch("v_pho_subClusRawEnergyOverSCRawEnergy_1"        ,          &v_pho_subClusRawEnergyOverSCRawEnergy_1 );
    //    outTree->Branch("v_pho_subClusRawEnergy_1"                       ,          &v_pho_subClusRawEnergy_1 );
    //    outTree->Branch("v_pho_subClusDPhi_1"                            ,          &v_pho_subClusDPhi_1 );
    //    outTree->Branch("v_pho_subClusDEta_1"                            ,          &v_pho_subClusDEta_1 );
    //
    //    outTree->Branch("v_pho_subClusRawEnergyOverSCRawEnergy_2"        ,          &v_pho_subClusRawEnergyOverSCRawEnergy_2 );
    //    outTree->Branch("v_pho_subClusRawEnergy_2"                       ,          &v_pho_subClusRawEnergy_2 );
    //    outTree->Branch("v_pho_subClusDPhi_2"                            ,          &v_pho_subClusDPhi_2 );
    //    outTree->Branch("v_pho_subClusDEta_2"                            ,          &v_pho_subClusDEta_2 );
    //


    outTree->Branch("v_pho_e1x5"                                ,      &v_pho_e1x5                 );
    outTree->Branch("v_pho_e2x5"                                ,      &v_pho_e2x5                 );
    outTree->Branch("v_pho_e5x5"                                ,      &v_pho_e5x5                 );
    outTree->Branch("v_pho_maxEnergyXtal"                       ,      &v_pho_maxEnergyXtal                 );
    outTree->Branch("v_pho_sigmaEtaEta"                         ,      &v_pho_sigmaEtaEta                 );
    outTree->Branch("v_pho_r1x5"                                ,      &v_pho_r1x5                 );
    outTree->Branch("v_pho_r2x5"                                ,      &v_pho_r2x5                 );
    outTree->Branch("v_pho_full5x5_e1x5"                        ,      &v_pho_full5x5_e1x5                 );
    outTree->Branch("v_pho_full5x5_e2x5"                        ,      &v_pho_full5x5_e2x5                 );
    outTree->Branch("v_pho_full5x5_e3x3"                        ,      &v_pho_full5x5_e3x3                 );
    outTree->Branch("v_pho_full5x5_e5x5"                        ,      &v_pho_full5x5_e5x5                 );
    outTree->Branch("v_pho_full5x5_maxEnergyXtal"               ,      &v_pho_full5x5_maxEnergyXtal                 );
    outTree->Branch("v_pho_full5x5_sigmaEtaEta"                 ,      &v_pho_full5x5_sigmaEtaEta                 );
    outTree->Branch("v_pho_full5x5_sigmaIetaIeta"               ,      &v_pho_full5x5_sigmaIetaIeta                 );
    outTree->Branch("v_pho_full5x5_r1x5"                        ,      &v_pho_full5x5_r1x5                 );
    outTree->Branch("v_pho_full5x5_r2x5"                        ,      &v_pho_full5x5_r2x5                 );
    outTree->Branch("v_pho_mipChi2"                             ,      &v_pho_mipChi2                 );
    outTree->Branch("v_pho_mipTotEnergy"                        ,      &v_pho_mipTotEnergy                 );
    outTree->Branch("v_pho_mipSlope"                            ,      &v_pho_mipSlope                 );
    outTree->Branch("v_pho_mipIntercept"                        ,      &v_pho_mipIntercept                 );
    outTree->Branch("v_pho_mipNhitCone"                         ,      &v_pho_mipNhitCone                 );
    outTree->Branch("v_pho_mipIsHalo"                           ,      &v_pho_mipIsHalo                 );
    outTree->Branch("v_pho_ecalRecHitSumEtConeDR04"             ,      &v_pho_ecalRecHitSumEtConeDR04                 );
    outTree->Branch("v_pho_hcalTowerSumEtConeDR04"              ,      &v_pho_hcalTowerSumEtConeDR04                 );
    outTree->Branch("v_pho_hcalDepth1TowerSumEtConeDR04"        ,      &v_pho_hcalDepth1TowerSumEtConeDR04                 );
    outTree->Branch("v_pho_hcalDepth2TowerSumEtConeDR04"        ,      &v_pho_hcalDepth2TowerSumEtConeDR04                 );
    outTree->Branch("v_pho_hcalTowerSumEtBcConeDR04"            ,      &v_pho_hcalTowerSumEtBcConeDR04                 );
    outTree->Branch("v_pho_hcalDepth1TowerSumEtBcConeDR04"      ,      &v_pho_hcalDepth1TowerSumEtBcConeDR04                 );
    outTree->Branch("v_pho_hcalDepth2TowerSumEtBcConeDR04"      ,      &v_pho_hcalDepth2TowerSumEtBcConeDR04                 );
    outTree->Branch("v_pho_trkSumPtSolidConeDR04"               ,      &v_pho_trkSumPtSolidConeDR04                 );
    outTree->Branch("v_pho_trkSumPtHollowConeDR04"              ,      &v_pho_trkSumPtHollowConeDR04                 );
    outTree->Branch("v_pho_nTrkSolidConeDR04"                   ,      &v_pho_nTrkSolidConeDR04                 );
    outTree->Branch("v_pho_nTrkHollowConeDR04"                  ,      &v_pho_nTrkHollowConeDR04                 );
    outTree->Branch("v_pho_ecalRecHitSumEtConeDR03"             ,      &v_pho_ecalRecHitSumEtConeDR03                 );
    outTree->Branch("v_pho_hcalTowerSumEtConeDR03"              ,      &v_pho_hcalTowerSumEtConeDR03                 );
    outTree->Branch("v_pho_hcalDepth1TowerSumEtConeDR03"        ,      &v_pho_hcalDepth1TowerSumEtConeDR03                 );
    outTree->Branch("v_pho_hcalDepth2TowerSumEtConeDR03"        ,      &v_pho_hcalDepth2TowerSumEtConeDR03                 );
    outTree->Branch("v_pho_hcalTowerSumEtBcConeDR03"            ,      &v_pho_hcalTowerSumEtBcConeDR03                 );
    outTree->Branch("v_pho_hcalDepth1TowerSumEtBcConeDR03"      ,      &v_pho_hcalDepth1TowerSumEtBcConeDR03                 );
    outTree->Branch("v_pho_hcalDepth2TowerSumEtBcConeDR03"      ,      &v_pho_hcalDepth2TowerSumEtBcConeDR03                 );
    outTree->Branch("v_pho_trkSumPtSolidConeDR03"               ,      &v_pho_trkSumPtSolidConeDR03                 );
    outTree->Branch("v_pho_trkSumPtHollowConeDR03"              ,      &v_pho_trkSumPtHollowConeDR03                 );
    outTree->Branch("v_pho_nTrkSolidConeDR03"                   ,      &v_pho_nTrkSolidConeDR03                 );
    outTree->Branch("v_pho_nTrkHollowConeDR03"                  ,      &v_pho_nTrkHollowConeDR03                 );
    outTree->Branch("v_pho_chargedHadronIso"                    ,      &v_pho_chargedHadronIso                 );
    outTree->Branch("v_pho_chargedHadronIsoWrongVtx"            ,      &v_pho_chargedHadronIsoWrongVtx                 );
    outTree->Branch("v_pho_neutralHadronIso"                    ,      &v_pho_neutralHadronIso                 );
    outTree->Branch("v_pho_photonIso"                           ,      &v_pho_photonIso                 );
    outTree->Branch("v_pho_sumChargedParticlePt"                ,      &v_pho_sumChargedParticlePt                 );
    outTree->Branch("v_pho_sumNeutralHadronEtHighThreshold"     ,      &v_pho_sumNeutralHadronEtHighThreshold                 );
    outTree->Branch("v_pho_sumPhotonEtHighThreshold"            ,      &v_pho_sumPhotonEtHighThreshold                 );
    outTree->Branch("v_pho_sumPUPt"                             ,      &v_pho_sumPUPt                 );
    outTree->Branch("v_pho_nClusterOutsideMustache"             ,      &v_pho_nClusterOutsideMustache                 );
    outTree->Branch("v_pho_etOutsideMustache"                   ,      &v_pho_etOutsideMustache                 );
    outTree->Branch("v_pho_pfMVA"                               ,      &v_pho_pfMVA                 );
    outTree->Branch("v_pho_genmatch"                            ,      &v_pho_genmatch              );
    outTree->Branch("v_pho_conversion"                          ,      &v_pho_conversion            );
    outTree->Branch("v_pho_recomatch"                           ,      &v_pho_recomatch             );
    outTree->Branch("v_pho_matchedgenphoton"                    ,      &v_pho_matchedgenphoton      );
    outTree->Branch("v_matchflag"                               ,      &v_matchflag                 );
    outTree->Branch("v_reco_genmatch"                           ,      &v_reco_genmatch             );
    outTree->Branch("v_genpho_pt"                               ,      &v_genpho_pt                 );
    outTree->Branch("v_reco_notgenmatch"                        ,      &v_reco_notgenmatch          );
    // Reco level  Variables of gen matched photons
    outTree->Branch("v_genmatch_full5x5_r9" , &v_genmatch_full5x5_r9 );
    outTree->Branch("v_genmatch_chargedHadronIso", &v_genmatch_chargedHadronIso);
    outTree->Branch("v_genmatch_hadronicOverEm", &v_genmatch_hadronicOverEm);
    outTree->Branch("v_genmatch_hasPixelSeed", &v_genmatch_hasPixelSeed);
    outTree->Branch("v_genmatch_ecalPFClusterIso", &v_genmatch_ecalPFClusterIso);
    outTree->Branch("v_genmatch_sigmaIetaIeta", &v_genmatch_sigmaIetaIeta);
    outTree->Branch("v_genmatch_passElectronVeto",&v_genmatch_passElectronVeto);
    outTree->Branch("v_notgenmatch_passElectronVeto",&v_notgenmatch_passElectronVeto);
    outTree->Branch("phosTemp",&phosTemp);
    outTree->Branch("phosTemp_presel",&phosTemp_presel);
    outTree->Branch("v_genmatch_pt",&v_genmatch_pt);
    outTree->Branch("v_genmatch_mva",&v_genmatch_mva);
    outTree->Branch("v_genmatch_eta",&v_genmatch_eta);
    outTree->Branch("v_genmatch_phi",&v_genmatch_phi);
    outTree->Branch("v_genmatch_trackIso",&v_genmatch_trackIso);
    //---- gen level variables
    outTree->Branch("v_genreco_dR",&v_genreco_dR);
    outTree->Branch("v_genreco_ptdiff",&v_genreco_ptdiff);
    outTree->Branch("v_genmatch_p4", &v_genmatch_p4);
    outTree->Branch("v_fatpho1_p4", &v_fatpho1_p4);
    outTree->Branch("v_fatpho1_pt", &v_fatpho1_pt);
    outTree->Branch("v_genlep_p4", &v_genlep_p4);
    outTree->Branch("v_genpho_p4_momid",&v_genpho_p4_momid);
    outTree->Branch("v_genpho_p4_mommass",&v_genpho_p4_mommass);
    outTree->Branch("v_gen_a_mass",           &v_gen_a_mass );
    outTree->Branch("v_gen_a_id",             &v_gen_a_id );
    outTree->Branch("v_gen_a_pt",             &v_gen_a_pt );
    outTree->Branch("v_gen_a_eta",            &v_gen_a_eta );
    outTree->Branch("v_gen_a_phi",            &v_gen_a_phi );
    outTree->Branch("v_gen_X_mass",           &v_gen_X_mass );
    outTree->Branch("v_gen_X_id",             &v_gen_X_id );
    outTree->Branch("v_gen_X_pt",             &v_gen_X_pt );
    outTree->Branch("v_gen_X_eta",            &v_gen_X_eta );
    outTree->Branch("v_gen_X_phi",            &v_gen_X_phi );
    outTree->Branch("v_gen_pdgid",            &v_gen_pdgid );
    outTree->Branch("v_genmom_pdgid",         &v_genmom_pdgid );
    outTree->Branch("v_pho_dr", &v_pho_dr);
    outTree->Branch("v_pho_dphi", &v_pho_dphi);
    outTree->Branch("v_pho_deta", &v_pho_deta);
    outTree->Branch("v_pho_cutid", &v_pho_cutid);
    outTree->Branch("v_pho_mva", &v_pho_mva);
    outTree->Branch("genTotalWeight", &genTotalWeight, "genTotalWeight/D");
    outTree->Branch("v_genpho_dr", &v_genpho_dr);
    outTree->Branch("myTriggerResults", &myTriggerResults);
    outTree->Branch("v_fatpho_number", &v_fatpho_number);
    outTree->Branch("v_matchreco_count", &v_matchreco_count);
    outTree->Branch("v_dr_genreco",&v_dr_genreco);
    outTree->Branch("v_genmatching",&v_genmatching);
    outTree->Branch("v_genmatch_int",&v_genmatch_int);
    outTree->Branch("v_nicematch",&v_nicematch);
    outTree->Branch("v_genrecoPt_ratio",&v_genrecoPt_ratio);
    outTree->Branch("v_genmother_p4",&v_genmother_p4);
    outTree->Branch("v_genmother_pt",&v_genmother_pt);
    outTree->Branch("v_genmother_eta",&v_genmother_eta);
    outTree->Branch("v_genmother_phi",&v_genmother_phi);
    outTree->Branch("v_genpho_id",&v_genpho_id);
    outTree->Branch("v_mother_id",&v_mother_id);
    outTree->Branch("v_daughter_id",&v_daughter_id);
    outTree->Branch("v_daughter_p4",&v_daughter_p4);
    outTree->Branch("v_4case",&v_4case);
    outTree->Branch("v_daughterofa_p4",&v_daughterofa_p4);
    outTree->Branch("v_photonDaughters_p4",&v_photonDaughters_p4);
    outTree->Branch("v_genlevelphoton_p4",&v_genlevelphoton_p4);
    outTree->Branch("v_mergedpho_p4",&v_mergedpho_p4);
    outTree->Branch("v_fatpho_p4",&v_fatpho_p4);
    outTree->Branch("v_fatpho_energy",&v_fatpho_energy);
    outTree->Branch("v_genmatch_ver2",&v_genmatch_ver2);
    outTree->Branch("v_reco_genmatchcount",&v_reco_genmatchcount);
    outTree->Branch("v_resolvedcount",&v_resolvedcount);
    //outTree->Branch("v_preselectedphoton_size",&v_preselectedphoton_size/D);
    std::map<std::string, std::string> replacements;
    globVar_->bookTreeVariables(outTree, replacements);

    counter = 0;

    //Get parameters
    std::vector<std::string> def_myTriggers;
    triggerToken_ = consumes<edm::TriggerResults>( iConfig.getParameter<edm::InputTag>( "triggerTag" ) );
    myTriggers = iConfig.getUntrackedParameter<std::vector<std::string> >("myTriggers", def_myTriggers);
    std::cout << "Analyzing events with the following triggers:" << std::endl;
    for ( size_t i = 0; i < myTriggers.size(); i++)
        std::cout << "\t" << myTriggers[i] << std::endl;
}


H4GFlash::~H4GFlash()
{

    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
H4GFlash::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    if(counter%1000 == 0) std::cout << "[H4GFlash::analyzer] Analyzing event #" << counter << std::endl;
    counter++;

    using namespace edm;

    globVar_->fill(iEvent);
    const double rhoFixedGrd = globVar_->valueOf(globVar_->indexOf("rho"));
    rho = rhoFixedGrd;

    edm::Handle<edm::View<flashgg::DiPhotonCandidate> > diphotons;
    iEvent.getByToken(diphotonsToken_, diphotons);

    edm::Handle<edm::View<flashgg::DiPhotonCandidate> > PreselectedDiPhotons;
    iEvent.getByToken(AfterSelectionDiPhotonToken_, PreselectedDiPhotons);

    edm::Handle<reco::Vertex> vtxH;
    iEvent.getByToken(vtxHT_,vtxH);

    edm::Handle<edm::View<reco::Vertex> > vertex;
    iEvent.getByToken(vertexToken_, vertex);

    std::vector<flashgg::DiPhotonCandidate> preseldipho;

    // Calculate  MC Weights here
    edm::Handle<GenEventInfoProduct> genEvtInfo;
    if( ! iEvent.isRealData() ) {
        iEvent.getByToken(genInfoToken_, genEvtInfo);
        genTotalWeight = genEvtInfo->weight();
    } else {
        genTotalWeight = 1;
    }
    //Trigger
    myTriggerResults.clear();
    if (myTriggers.size() > 0){
        Handle<edm::TriggerResults> trigResults;
        iEvent.getByToken(triggerToken_, trigResults);
        const edm::TriggerNames &names = iEvent.triggerNames(*trigResults);
        myTriggerResults = H4GTools::TriggerSelection(myTriggers, names, trigResults);
    }

    int acceptedTriggers = 0;
    for (std::map<std::string, int>::iterator it = myTriggerResults.begin(); it != myTriggerResults.end(); it++){
        if (DEBUG) std::cout << "Trigger name: " << it->first << "\n \t Decision: " << it->second << std::endl;
        if (it->second) acceptedTriggers++;
        std::map<std::string, int>::iterator finder;
        finder = triggerStats.find(it->first);
        if ( finder != triggerStats.end() )
            triggerStats[it->first] += it->second;
        if ( finder == triggerStats.end() )
            triggerStats[it->first] =  it->second;
    }
    if (acceptedTriggers) passTrigger = 1;
    if (!acceptedTriggers) passTrigger = 0;

    //Initialize tree variables
    genTotalWeight = 1.0;
    passpresel = -999;
    n_pho = 0;
    n_pho_presel = 0;
    //n_dipho = 0;
    //n_preseldipho = 0;
    //npho_before = 0;
    //npho_after = 0;
    v_pho_p4.clear();
    v_genpho_p4.clear();
    v_genpho2_p4.clear();
    v_pho_pt.clear();
    v_pho_eta.clear();
    v_pho_phi.clear();
    v_pho_e.clear();
    v_pho_dr.clear();
    v_pho_dphi.clear();
    v_pho_deta.clear();
    v_pho_cutid.clear();
    v_pho_mva.clear();
    v_h4g_diphos.clear();
    //v_h4g_tetraphos.clear();
    v_genpho_dr.clear();
    v_pho_hadronicOverEm.clear();
    //    v_pho_chargedHadronIso.clear();
    //    v_pho_neutralHadronIso.clear();
    //    v_pho_photonIso.clear();
    v_pho_passElectronVeto.clear();
    v_pho_hasPixelSeed.clear();
    //    v_pho_ecalPFClusterIso.clear();
    //    v_pho_hcalPFClusterIso.clear();
    v_pho_eMax.clear();
    v_pho_e3x3.clear();
    //    v_pho_subClusRawE1.clear();
    //    v_pho_subClusDPhi1.clear();
    //    v_pho_subClusDEta1.clear();
    //    v_pho_subClusRawE2.clear();
    //    v_pho_subClusDPhi2.clear();
    //    v_pho_subClusDEta2.clear();
    //    v_pho_subClusRawE3.clear();
    //    v_pho_subClusDPhi3.clear();
    //    v_pho_subClusDEta3.clear();
    v_pho_iPhi.clear();
    v_pho_iEta.clear();
    v_pho_r9.clear();
    v_pho_full5x5_r9.clear();
    v_pho_sigmaIetaIeta.clear();
    v_pho_sigmaIphiIphi.clear();
    v_pho_dr03HcalTowerSumEt.clear();
    v_pho_dr03EcalRecHitSumEt.clear();
    v_pho_dr03TkSumPt.clear();
    v_pho_e2nd                 .clear();
    v_pho_eTop                 .clear();
    v_pho_eBottom              .clear();
    v_pho_eLeft                .clear();
    v_pho_eRight               .clear();
    v_pho_see                  .clear();
    v_pho_spp                  .clear();
    v_pho_sep                  .clear();
    v_pho_maxDR                .clear();
    v_pho_maxDRDPhi            .clear();
    v_pho_maxDRDEta            .clear();
    v_pho_maxDRRawEnergy       .clear();
    v_pho_subClusRawE1         .clear();
    v_pho_subClusRawE2         .clear();
    v_pho_subClusRawE3         .clear();
    v_pho_subClusDPhi1         .clear();
    v_pho_subClusDPhi2         .clear();
    v_pho_subClusDPhi3         .clear();
    v_pho_subClusDEta1         .clear();
    v_pho_subClusDEta2         .clear();
    v_pho_subClusDEta3         .clear();
    v_pho_cryPhi               .clear();
    v_pho_cryEta               .clear();
    v_pho_ecalPFClusterIso     .clear();
    v_pho_hcalPFClusterIso     .clear();
    v_pho_caloIso              .clear();
    v_pho_hcalIso              .clear();
    v_pho_ecalIso              .clear();
    v_pho_trackIso             .clear();
    v_pho_genmatch             .clear();
    v_pho_conversion           .clear();
    v_pho_recomatch            .clear();
    v_pho_matchedgenphoton     .clear();
    v_pho_scRawEnergy          .clear();
    //    v_pho_scCalibEnergy        .clear();
    //    v_pho_scPreShowerEnergy    .clear();
    //    v_pho_scEta                .clear();
    //    v_pho_scPhi                .clear();
    //    v_pho_scEtaWidth           .clear();
    //    v_pho_scPhiWidth           .clear();
    //    v_pho_seedClusEnergy       .clear();
    //
    //    v_pho_sigmaIEtaIEta        .clear();
    //    v_pho_sigmaIEtaIPhi        .clear();
    //    v_pho_sigmaIPhiIPhi        .clear();
    //
    //    v_pho_scPreShowerEnergyOverSCRawEnergy     .clear();
    //    v_pho_scSeedR9                             .clear();
    //    v_pho_seedClusEnergyOverSCRawEnergy        .clear();
    //    v_pho_eMaxOverSCRawEnergy                  .clear();
    //    v_pho_e2ndOverSCRawEnergy                  .clear();
    //    v_pho_seedLeftRightAsym                    .clear();
    //    v_pho_seedTopBottomAsym                    .clear();
    //    v_pho_maxSubClusDRRawEnergyOverSCRawEnergy .clear();
    //
    //    v_pho_subClusRawEnergyOverSCRawEnergy_0   .clear();
    //    v_pho_subClusRawEnergy_0                  .clear();
    //    v_pho_subClusDPhi_0                       .clear();
    //    v_pho_subClusDEta_0                       .clear();
    //
    //    v_pho_subClusRawEnergyOverSCRawEnergy_1   .clear();
    //    v_pho_subClusRawEnergy_1                  .clear();
    //    v_pho_subClusDPhi_1                       .clear();
    //    v_pho_subClusDEta_1                       .clear();
    //
    //    v_pho_subClusRawEnergyOverSCRawEnergy_2   .clear();
    //    v_pho_subClusRawEnergy_2                  .clear();
    //    v_pho_subClusDPhi_2                       .clear();
    //    v_pho_subClusDEta_2                       .clear();


    v_pho_e1x5.clear();
    v_pho_e2x5.clear();
    v_pho_e5x5.clear();
    v_pho_maxEnergyXtal.clear();
    v_pho_sigmaEtaEta.clear();
    //v_pho_full5x5_sigmaPhiPhi.clear();
    v_pho_r1x5.clear();
    v_pho_r2x5.clear();
    v_pho_full5x5_e1x5.clear();
    v_pho_full5x5_e2x5.clear();
    v_pho_full5x5_e3x3.clear();
    v_pho_full5x5_e5x5.clear();
    v_pho_full5x5_maxEnergyXtal.clear();
    v_pho_full5x5_sigmaEtaEta.clear();
    v_pho_full5x5_sigmaIetaIeta.clear();
    v_pho_full5x5_r1x5.clear();
    v_pho_full5x5_r2x5.clear();
    v_pho_mipChi2.clear();
    v_pho_mipTotEnergy.clear();
    v_pho_mipSlope.clear();
    v_pho_mipIntercept.clear();
    v_pho_mipNhitCone.clear();
    v_pho_mipIsHalo.clear();
    v_pho_ecalRecHitSumEtConeDR04.clear();
    v_pho_hcalTowerSumEtConeDR04.clear();
    v_pho_hcalDepth1TowerSumEtConeDR04.clear();
    v_pho_hcalDepth2TowerSumEtConeDR04.clear();
    v_pho_hcalTowerSumEtBcConeDR04.clear();
    v_pho_hcalDepth1TowerSumEtBcConeDR04.clear();
    v_pho_hcalDepth2TowerSumEtBcConeDR04.clear();
    v_pho_trkSumPtSolidConeDR04.clear();
    v_pho_trkSumPtHollowConeDR04.clear();
    v_pho_nTrkSolidConeDR04.clear();
    v_pho_nTrkHollowConeDR04.clear();
    v_pho_ecalRecHitSumEtConeDR03.clear();
    v_pho_hcalTowerSumEtConeDR03.clear();
    v_pho_hcalDepth1TowerSumEtConeDR03.clear();
    v_pho_hcalDepth2TowerSumEtConeDR03.clear();
    v_pho_hcalTowerSumEtBcConeDR03.clear();
    v_pho_hcalDepth1TowerSumEtBcConeDR03.clear();
    v_pho_hcalDepth2TowerSumEtBcConeDR03.clear();
    v_pho_trkSumPtSolidConeDR03.clear();
    v_pho_trkSumPtHollowConeDR03.clear();
    v_pho_nTrkSolidConeDR03.clear();
    v_pho_nTrkHollowConeDR03.clear();
    v_pho_chargedHadronIso.clear();
    v_pho_chargedHadronIsoWrongVtx.clear();
    v_pho_neutralHadronIso.clear();
    v_pho_photonIso.clear();
    v_pho_sumChargedParticlePt.clear();
    v_pho_sumNeutralHadronEtHighThreshold.clear();
    v_pho_sumPhotonEtHighThreshold.clear();
    v_pho_sumPUPt.clear();
    v_pho_nClusterOutsideMustache.clear();
    v_pho_etOutsideMustache.clear();
    v_pho_pfMVA.clear();
    v_reco_genmatch.clear();
    v_reco_notgenmatch.clear();
    v_genpho_p4_mommass.clear();
    v_genpho_p4_momid.clear();
    v_genpho_p4_pt.clear();
    v_genlep_p4.clear();
    v_genpho_pt.clear();
    v_genpho_id.clear();
    v_gen_a_mass.clear();
    v_gen_a_id.clear();
    v_gen_a_pt.clear();
    v_gen_a_eta.clear();
    v_gen_a_phi.clear();
    v_gen_X_mass.clear();
    v_gen_X_id.clear();
    v_gen_X_pt.clear();
    v_gen_X_eta.clear();
    v_gen_X_phi.clear();
    v_matchflag.clear();
    v_dr_genreco.clear();
    v_gen_pdgid.clear();
    v_genmom_pdgid.clear();
    v_genmatch_p4.clear();
    v_fatpho1_p4.clear();
    v_fatpho1_pt.clear();
    v_fatpho_number.clear();
    v_matchreco_count.clear();
    v_genreco_dR.clear();
    v_genreco_ptdiff.clear();
    v_genmatch_passElectronVeto.clear();
    v_notgenmatch_passElectronVeto.clear();
    v_genmatch_full5x5_r9.clear();
    v_genmatch_chargedHadronIso.clear();
    v_genmatch_hadronicOverEm.clear();
    v_genmatch_hasPixelSeed.clear();
    v_genmatch_ecalPFClusterIso.clear();
    v_genmatch_sigmaIetaIeta.clear();
    phosTemp.clear();
    phosTemp_presel.clear();
    v_genmatch_pt.clear();
    v_genmatch_mva.clear();
    v_genmatch_eta.clear();
    v_genmatch_phi.clear();
    v_genmatch_trackIso.clear();
    v_genmatching.clear();
    v_genmatch_int.clear();
    v_genrecoPt_ratio.clear();
    v_nicematch.clear();
    v_genmother_p4.clear();
    v_genmother_pt.clear();
    v_genmother_eta.clear();
    v_genmother_phi.clear();
    v_mother_id.clear();
    v_daughter_id.clear();
    v_daughter_p4.clear();
    v_4case.clear();
    v_reco_genmatchcount.clear();
    v_daughterofa_p4.clear();
    v_photonDaughters_p4.clear();
    v_genlevelphoton_p4.clear();
    v_mergedpho_p4.clear();
    v_fatpho_p4.clear();
    v_fatpho_energy.clear();
    v_genmatch_ver2.clear();
    v_resolvedcount.clear();
    //Create a list pf photons from diphotons
    std::vector<const flashgg::Photon*> phosTemp;
    std::vector<const flashgg::Photon*> phosTemp_presel;
    std::vector<const flashgg::Photon*> extra;
    std::vector<const flashgg::Photon*> fat1;
    edm ::Ptr<reco::Vertex> vtx;
    edm::Ptr<reco::Vertex> vtx_to_use;
    vtx_to_use = vertex->ptrAt(0);

    n_dipho = diphotons->size();
    n_preseldipho = PreselectedDiPhotons->size();
    //std::cout << " number of diphotons " <<  diphotons->size() << " preselected diphotons " << PreselectedDiPhotons->size() << std::endl;
    for (size_t i = 0; i < (diphotons->size()); ++i){
      edm::Ptr<flashgg::DiPhotonCandidate> dipho = diphotons->ptrAt(i);
      vtx = diphotons->ptrAt(i)->vtx();
      const flashgg::Photon * Pho1 = dipho->leadingPhoton();
      const flashgg::Photon * Pho2 = dipho->subLeadingPhoton();
      if ( phosTemp.size() == 0 ){
        phosTemp.push_back(Pho1);
        phosTemp.push_back(Pho2);
        n_pho+=2;
        continue;
      }
      else {
        float minDR1 = 999, minDR2 = 999;
        for ( size_t p = 0; p < phosTemp.size(); p++){
          float deltar1 = deltaR(phosTemp[p]->p4(), Pho1->p4());
          if(deltar1 < minDR1) minDR1 = deltar1;

          float deltar2 = deltaR(phosTemp[p]->p4(), Pho2->p4());
          if(deltar2 < minDR2) minDR2 = deltar2;
        }
        if ( minDR1 > 0.0001){
          n_pho++;
          phosTemp.push_back(Pho1);
        }
        if ( minDR2 > 0.0001){
          n_pho++;
          phosTemp.push_back(Pho2);
        }
      }
    }

    for (size_t i1 = 0; i1 < (PreselectedDiPhotons->size()); ++i1){
      edm::Ptr<flashgg::DiPhotonCandidate> dipho_presel = PreselectedDiPhotons->ptrAt(i1);
      vtx = PreselectedDiPhotons->ptrAt(i1)->vtx();
      const flashgg::Photon * pho1 = dipho_presel->leadingPhoton();
      const flashgg::Photon * pho2 = dipho_presel->subLeadingPhoton();
      if ( phosTemp_presel.size() == 0 ){
        phosTemp_presel.push_back(pho1);
        phosTemp_presel.push_back(pho2);
        n_pho_presel+=2;
        continue;
      }
      else {
        float minDR1 = 999, minDR2 = 999;
        for ( size_t p1 = 0; p1 < phosTemp_presel.size(); p1++){
          float deltar1 = deltaR(phosTemp_presel[p1]->p4(), pho1->p4());
          if(deltar1 < minDR1) minDR1 = deltar1;

          float deltar2 = deltaR(phosTemp_presel[p1]->p4(), pho2->p4());
          if(deltar2 < minDR2) minDR2 = deltar2;
        }
        if ( minDR1 > 0.0001){
          n_pho_presel++;
          phosTemp_presel.push_back(pho1);
        }
        if ( minDR2 > 0.0001){
          n_pho_presel++;
          phosTemp_presel.push_back(pho2);
        }
      }
    }
    for (int index1 = 0; index1 < (int)phosTemp.size(); ++index1) {
      int smallestindex = index1;
      for (int index2 = index1+1; index2 < (int)phosTemp.size(); ++index2){
         if (phosTemp[index1]->pt() < phosTemp[index2]->pt()){
           smallestindex  = index2;
           std::swap(phosTemp[index1],phosTemp[smallestindex]);
         }
      }
    }
    // for (int index3 = 0; index3 < (int)phosTemp.size(); ++index3) {
    //   int smallestindex2 = index3;
    //   for (int index4= index3+1; index4 < (int)phosTemp.size(); ++index4){
    //      if (phosTemp[index4]->pt() < phosTemp[index4]->pt()){
    //        smallestindex2  = index4;
    //        std::swap(phosTemp[index3],phosTemp[smallestindex2]);
    //      }
    //   }
    // }

    // trigger preselection on diphoton candidates
    if (diphotons->size() > 0 && PreselectedDiPhotons->size() > 0 ){
      passpresel = 1;
    }
   if (diphotons->size() > 0 && PreselectedDiPhotons->size() == 0){
      passpresel = 0;
    }
    // if (n_pho_presel < 2 ){
    //   passpresel = 0;
    // }
    // if (n_pho_presel > 1 ){
    //   passpresel = 1;
    // }

    // std::cout << "number of diphotons " << diphotons->size() << " preselected " << PreselectedDiPhotons->size() << " presel value " << passpresel << std::endl;
    // std::cout << " number of photons " << n_pho << " preselected " << n_pho_presel << std::endl;
    //std::cout << " phostemp size " << phosTemp.size() << " preselectedphotons size " << phosTemp_presel.size() << std::endl;

    // for (int i = 0; i < (int)phosTemp.size(); ++i) {
    //     const flashgg::Photon * pho = phosTemp[i];
    //     std::cout << " photon pt "<< pho->pt() << std::endl;
    //   }
    //   for (int i1 = 0; i1 < (int)phosTemp_presel.size(); ++i1) {
    //       const flashgg::Photon * preselpho = phosTemp_presel[i1];
    //       std::cout << " preselected photon pt "<< preselpho->pt() << std::endl;
    //     }

    // the following block must be commented for background MC and Data

//     std::vector<int> mylist;
//     std::vector<int> mylistfat;
//     std::vector<int> fatcount;
//     std::vector<int> matchreco_count;
//     std::vector<int> reco_fat_count;
//     std::vector<int> resolvedcount;
//     std::vector<int> preselectcount;
//
//     edm::Handle<edm::View<reco::GenParticle> > genParticles;
//     iEvent.getByToken(genParticlesToken_,genParticles);
//
//     if( ! iEvent.isRealData() ) {
//         for(size_t g=0; g < genParticles->size(); g++) {
//             auto gen = genParticles->ptrAt(g);
//             if( gen->isPromptFinalState() == 0 ) continue;
//             if( gen->pdgId() != 22) continue;
//             if( gen->mother(0)->pdgId() == 25 || gen->mother(0)->pdgId() == 54)  // for matching -- this is the pseudoscalar "a"
//             {
//                 v_genpho_p4.push_back( gen->p4() );
//             }
//         }
//         for (size_t gp=0; gp<genParticles->size(); gp++) {
//             auto gen = genParticles->ptrAt(gp);
//             int type = gen->pdgId();
//             if ( abs(type) == 25 || abs(type) == 54 ){ //---- pseudoscalar "a"
//                 v_gen_a_mass .push_back(gen->mass());
//                 v_gen_a_pt .push_back(gen->pt());
//                 v_gen_a_phi.push_back(gen->phi());
//                 v_gen_a_eta.push_back(gen->eta());
//                 v_gen_a_id .push_back(1. * type);
//                 v_genlevelphoton_p4.push_back(gen->daughter(0)->p4());  // v_genlevelphoton_p4 is collection of the 4 final state photons
//                 v_genlevelphoton_p4.push_back(gen->daughter(1)->p4());
//             }
//             if ( abs(type) == 35 ) { //---- X
//                 v_gen_X_mass .push_back(gen->mass());
//                 v_gen_X_pt .push_back(gen->pt());
//                 v_gen_X_phi.push_back(gen->phi());
//                 v_gen_X_eta.push_back(gen->eta());
//                 v_gen_X_id .push_back(1. * type);
//             }
//             if (( abs(type) == 11 || abs(type) == 13 || abs(type) == 15 ) && (gen->isPromptFinalState() == 1)) {//---- leptons (only prompt)
//                 v_genlep_p4.push_back( gen->p4() );
//             }
//         }
//
//     // identifying merged photons @ Gen-level
//     float deltar_a1 = 0;
//     float deltar_a2 = 0;
//     deltar_a1 =  deltaR(v_genlevelphoton_p4[0],v_genlevelphoton_p4[1]);
//     deltar_a2 =  deltaR(v_genlevelphoton_p4[2],v_genlevelphoton_p4[3]);
//     if (deltar_a1 < 0.15)
//       { LorentzVector fatpho1 = v_genlevelphoton_p4[0] + v_genlevelphoton_p4[1];
//         v_fatpho_p4.push_back(fatpho1);
//         fatcount.push_back(1);
//       }
//     if (deltar_a2 < 0.15)
//       { LorentzVector fatpho2 = v_genlevelphoton_p4[2] + v_genlevelphoton_p4[3];
//         v_fatpho_p4.push_back(fatpho2);
//         fatcount.push_back(1);
//       }
//     v_fatpho_number.push_back(fatcount.size());
// // now that we have identified merged photons @ gen-level, we can start identifying reco photons
//    unsigned int bestgenfat = INT_MAX;
//    for( size_t f = 0; f < v_fatpho_p4.size(); f++) {
//        LorentzVector fatpho_temp = v_fatpho_p4[f];
//        float maxDeltaR = 0.15;
//        float bestdRdiff = 99e15;
//        unsigned int bestreco = INT_MAX;
//        for (int i=0; i< (int)phosTemp.size(); ++i) {
//            const flashgg::Photon * pho = phosTemp[i];
//            float dR = deltaR(*pho,fatpho_temp);
//            if (dR > maxDeltaR){continue;}
//            matchreco_count.push_back(1);
//            if (dR < bestdRdiff) {
//               bestdRdiff = dR;
//               bestreco = i;   // best is the index of the reco photon that matches with the gen-level fat photon
//               bestgenfat = f;
//               v_genrecoPt_ratio.push_back(pho->pt()/fatpho_temp.pt());
//            }
//        }
//        mylist.push_back(bestreco);
//        mylistfat.push_back(bestgenfat);
//    }
//    v_matchreco_count.push_back(matchreco_count.size());  // counts the number of reco photons that are within a cone of deltar < 0.15 of the gen level fat photon
//
//    // now saving information of the matched reco photon
//    for (int r = 0; r < (int)phosTemp.size(); ++r) {
//        const flashgg::Photon * phomatch = phosTemp[r];
//        bool found = (std::find(mylist.begin(), mylist.end(), r) != mylist.end());
//        v_matchflag.push_back(found);
//        if(found == 1) {
//            v_genmatch_pt.push_back( phomatch->pt() );
//            v_genmatch_p4.push_back(phomatch->p4()); // this reco photon is fat
//            v_genmatch_eta.push_back(phomatch->eta());
//        }
//        else {
//            resolvedcount.push_back(1);
//            v_genmatch_pt.push_back(-999); // this reco photon is resolved
//            v_genmatch_eta.push_back(-999);}
//    }
//    // now doing matching the other way around, i.e start from reco photons and look for a fat photon within a cone of deltar < 0.15
//    v_resolvedcount.push_back(resolvedcount.size());
//    for (int s = 0; s < (int)phosTemp.size(); ++s) {
//      const flashgg::Photon * pho_temp = phosTemp[s];
//      for( size_t f1 = 0; f1 < v_fatpho_p4.size(); f1++) {
//        LorentzVector fatpho_temp1 = v_fatpho_p4[f1];
//        if (deltaR(*pho_temp,fatpho_temp1) < 0.15){
//            reco_fat_count.push_back(1); // how many times is there a fat photon within dR < 0.15 of a reco photon ?
//        }
//      }
//    }
//    v_reco_genmatchcount.push_back(reco_fat_count.size());
// }
    if (passpresel == 1 ) {
    for (int i = 0; i < (int)phosTemp.size(); ++i) {
        const flashgg::Photon * pho = phosTemp[i];
        //if (passpresel != 1 )continue;
        //std::cout << " photon pt " << pho->pt() << std::endl;
        v_pho_genmatch.push_back(pho->hasUserInt("genMatchType")  );
        v_pho_matchedgenphoton.push_back(pho->hasUserCand("matchedGenPhoton") );
        v_pho_pt.push_back( pho->pt() );
        v_pho_eta.push_back( pho->superCluster()->eta() );
        v_pho_phi.push_back( pho->superCluster()->phi() );
        v_pho_e.push_back( pho->energy() );
        math::PtEtaPhiELorentzVectorD tmpVec;
        tmpVec.SetPt( pho->pt() );
        tmpVec.SetEta( pho->superCluster()->eta() );
        tmpVec.SetPhi( pho->superCluster()->phi() );
        tmpVec.SetE( pho->energy() );
        LorentzVector thisPhoV4( tmpVec );
        v_pho_p4.push_back( thisPhoV4 );
        v_pho_mva.push_back(pho->phoIdMvaDWrtVtx(vtx_to_use));
        v_pho_hadronicOverEm.push_back    ( pho->hadronicOverEm() );
        v_pho_passElectronVeto.push_back  ( pho->passElectronVeto() );
        v_pho_hasPixelSeed.push_back      ( pho->hasPixelSeed() );
        v_pho_eMax.push_back              ( pho->eMax() );
        v_pho_e3x3.push_back              ( pho->e3x3() );
        v_pho_iPhi.push_back              ( pho->iPhi() );
        v_pho_iEta.push_back              ( pho->iEta() );
        v_pho_r9.push_back                ( pho->old_r9() );
        v_pho_full5x5_r9.push_back        ( pho->full5x5_r9() );
        v_pho_sigmaIetaIeta        .push_back(  pho-> sigmaIetaIeta       ()  );
        v_pho_sigmaIphiIphi        .push_back(  pho->  showerShapeVariables() . sigmaIphiIphi       );
        v_pho_e2nd                 .push_back(  pho-> e2nd                ()  );
        v_pho_eTop                 .push_back(  pho-> eTop                ()  );
        v_pho_eBottom              .push_back(  pho-> eBottom             ()  );
        v_pho_eLeft                .push_back(  pho-> eLeft               ()  );
        v_pho_eRight               .push_back(  pho-> eRight              ()  );
        v_pho_see                  .push_back(  pho-> see                 ()  );
        v_pho_spp                  .push_back(  pho-> spp                 ()  );
        v_pho_sep                  .push_back(  pho-> sep                 ()  );
        v_pho_maxDR                .push_back(  pho-> maxDR               ()  );
        v_pho_maxDRDPhi            .push_back(  pho-> maxDRDPhi           ()  );
        v_pho_maxDRDEta            .push_back(  pho-> maxDRDEta           ()  );
        v_pho_maxDRRawEnergy       .push_back(  pho-> maxDRRawEnergy      ()  );
        v_pho_subClusRawE1         .push_back(  pho-> subClusRawE1        ()  );
        v_pho_subClusRawE2         .push_back(  pho-> subClusRawE2        ()  );
        v_pho_subClusRawE3         .push_back(  pho-> subClusRawE3        ()  );
        v_pho_subClusDPhi1         .push_back(  pho-> subClusDPhi1        ()  );
        v_pho_subClusDPhi2         .push_back(  pho-> subClusDPhi2        ()  );
        v_pho_subClusDPhi3         .push_back(  pho-> subClusDPhi3        ()  );
        v_pho_subClusDEta1         .push_back(  pho-> subClusDEta1        ()  );
        v_pho_subClusDEta2         .push_back(  pho-> subClusDEta2        ()  );
        v_pho_subClusDEta3         .push_back(  pho-> subClusDEta3        ()  );
        v_pho_cryPhi               .push_back(  pho-> cryPhi              ()  );
        v_pho_cryEta               .push_back(  pho-> cryEta              ()  );
        v_pho_ecalPFClusterIso     .push_back(  pho-> ecalPFClusterIso    ()  );
        v_pho_hcalPFClusterIso     .push_back(  pho-> hcalPFClusterIso    ()  );
        v_pho_caloIso              .push_back(  pho-> caloIso             ()  );
        v_pho_hcalIso              .push_back(  pho-> hcalIso             ()  );
        v_pho_ecalIso              .push_back(  pho-> ecalIso             ()  );
        v_pho_trackIso             .push_back(  pho-> trackIso            ()  );
        v_pho_conversion           .push_back(  pho->hasConversionTracks  ()  );
        v_pho_e1x5                                        .push_back(  pho->   e1x5                                    ()    );
        v_pho_e2x5                                        .push_back(  pho->   e2x5                                    ()    );
        v_pho_e5x5                                        .push_back(  pho->   e5x5                                    ()    );
        v_pho_maxEnergyXtal                               .push_back(  pho->   maxEnergyXtal                           ()    );
        v_pho_sigmaEtaEta                                 .push_back(  pho->   sigmaEtaEta                             ()    );
        v_pho_r1x5                                        .push_back(  pho->   r1x5                                    ()    );
        v_pho_r2x5                                        .push_back(  pho->   r2x5                                    ()    );
        v_pho_full5x5_e1x5                                .push_back(  pho->   full5x5_e1x5                            ()    );
        v_pho_full5x5_e2x5                                .push_back(  pho->   full5x5_e2x5                            ()    );
        v_pho_full5x5_e3x3                                .push_back(  pho->   full5x5_e3x3                            ()    );
        v_pho_full5x5_e5x5                                .push_back(  pho->   full5x5_e5x5                            ()    );
        v_pho_full5x5_maxEnergyXtal                       .push_back(  pho->   full5x5_maxEnergyXtal                   ()    );
        v_pho_full5x5_sigmaEtaEta                         .push_back(  pho->   full5x5_sigmaEtaEta                     ()    );
        v_pho_full5x5_sigmaIetaIeta                       .push_back(  pho->   full5x5_sigmaIetaIeta                   ()    );
        v_pho_full5x5_r1x5                                .push_back(  pho->   full5x5_r1x5                            ()    );
        v_pho_full5x5_r2x5                                .push_back(  pho->   full5x5_r2x5                            ()    );
        v_pho_mipChi2                                     .push_back(  pho->   mipChi2                                 ()    );
        v_pho_mipTotEnergy                                .push_back(  pho->   mipTotEnergy                            ()    );
        v_pho_mipSlope                                    .push_back(  pho->   mipSlope                                ()    );
        v_pho_mipIntercept                                .push_back(  pho->   mipIntercept                            ()    );
        v_pho_mipNhitCone                                 .push_back(  pho->   mipNhitCone                             ()    );
        v_pho_mipIsHalo                                   .push_back(  pho->   mipIsHalo                               ()    );
        v_pho_ecalRecHitSumEtConeDR04                     .push_back(  pho->   ecalRecHitSumEtConeDR04                 ()    );
        v_pho_hcalTowerSumEtConeDR04                      .push_back(  pho->   hcalTowerSumEtConeDR04                  ()    );
        v_pho_hcalDepth1TowerSumEtConeDR04                .push_back(  pho->   hcalDepth1TowerSumEtConeDR04            ()    );
        v_pho_hcalDepth2TowerSumEtConeDR04                .push_back(  pho->   hcalDepth2TowerSumEtConeDR04            ()    );
        v_pho_hcalTowerSumEtBcConeDR04                    .push_back(  pho->   hcalTowerSumEtBcConeDR04                ()    );
        v_pho_hcalDepth1TowerSumEtBcConeDR04              .push_back(  pho->   hcalDepth1TowerSumEtBcConeDR04          ()    );
        v_pho_hcalDepth2TowerSumEtBcConeDR04              .push_back(  pho->   hcalDepth2TowerSumEtBcConeDR04          ()    );
        v_pho_trkSumPtSolidConeDR04                       .push_back(  pho->   trkSumPtSolidConeDR04                   ()    );
        v_pho_trkSumPtHollowConeDR04                      .push_back(  pho->   trkSumPtHollowConeDR04                  ()    );
        v_pho_nTrkSolidConeDR04                           .push_back(  pho->   nTrkSolidConeDR04                       ()    );
        v_pho_nTrkHollowConeDR04                          .push_back(  pho->   nTrkHollowConeDR04                      ()    );
        v_pho_ecalRecHitSumEtConeDR03                     .push_back(  pho->   ecalRecHitSumEtConeDR03                 ()    );
        v_pho_hcalTowerSumEtConeDR03                      .push_back(  pho->   hcalTowerSumEtConeDR03                  ()    );
        v_pho_hcalDepth1TowerSumEtConeDR03                .push_back(  pho->   hcalDepth1TowerSumEtConeDR03            ()    );
        v_pho_hcalDepth2TowerSumEtConeDR03                .push_back(  pho->   hcalDepth2TowerSumEtConeDR03            ()    );
        v_pho_hcalTowerSumEtBcConeDR03                    .push_back(  pho->   hcalTowerSumEtBcConeDR03                ()    );
        v_pho_hcalDepth1TowerSumEtBcConeDR03              .push_back(  pho->   hcalDepth1TowerSumEtBcConeDR03          ()    );
        v_pho_hcalDepth2TowerSumEtBcConeDR03              .push_back(  pho->   hcalDepth2TowerSumEtBcConeDR03          ()    );
        v_pho_trkSumPtSolidConeDR03                       .push_back(  pho->   trkSumPtSolidConeDR03                   ()    );
        v_pho_trkSumPtHollowConeDR03                      .push_back(  pho->   trkSumPtHollowConeDR03                  ()    );
        v_pho_nTrkSolidConeDR03                           .push_back(  pho->   nTrkSolidConeDR03                       ()    );
        v_pho_nTrkHollowConeDR03                          .push_back(  pho->   nTrkHollowConeDR03                      ()    );
        v_pho_chargedHadronIso                            .push_back(  pho->   chargedHadronIso                        ()    );
        v_pho_chargedHadronIsoWrongVtx                    .push_back(  pho->   chargedHadronIsoWrongVtx                ()    );
        v_pho_neutralHadronIso                            .push_back(  pho->   neutralHadronIso                        ()    );
        v_pho_photonIso                                   .push_back(  pho->   photonIso                               ()    );
        v_pho_sumChargedParticlePt                        .push_back(  pho->   sumChargedParticlePt                    ()    );
        v_pho_sumNeutralHadronEtHighThreshold             .push_back(  pho->   sumNeutralHadronEtHighThreshold         ()    );
        v_pho_sumPhotonEtHighThreshold                    .push_back(  pho->   sumPhotonEtHighThreshold                ()    );
        v_pho_sumPUPt                                     .push_back(  pho->   sumPUPt                                 ()    );
        v_pho_nClusterOutsideMustache                     .push_back(  pho->   nClusterOutsideMustache                 ()    );
        v_pho_etOutsideMustache                           .push_back(  pho->   etOutsideMustache                       ()    );
        v_pho_pfMVA                                       .push_back(  pho->   pfMVA                                   ()    );


    }
  }
    // Save delta r between selected photons
    for( size_t p = 0; p < v_genpho_p4.size(); p++) {

        LorentzVector pho = v_genpho_p4[p];
        std::vector<float> vecDR;
        std::vector<float> vecDPhi;
        std::vector<float> vecDEta;

        for ( size_t p2 = 0; p2 < v_genpho_p4.size(); p2++) {
            LorentzVector pho2 = v_genpho_p4[p2];
            float deltar = 0;
            float deltaphi = 0;
            float deltaeta = 0;
            if( p2 == p ) {
                deltar = -999;
                deltaphi = -999;
                deltaeta = -999;
            }
            if( p2 != p ) {
                deltar = deltaR(pho, pho2);
                deltaphi = deltaPhi(pho.phi(), pho2.phi());
                deltaeta = fabs(pho.eta() - pho2.eta());
            }

            if( p2 > p ){
                H4GTools::H4G_DiPhoton thisH4GDipho;
                LorentzVector Sum = pho+pho2;
                thisH4GDipho.p4 = Sum;
                thisH4GDipho.ip1 = p;
                thisH4GDipho.ip2 = p2;
                thisH4GDipho.SumPt = pho.pt() + pho2.pt();
                if( pho.pt() < pho2.pt()){
                    thisH4GDipho.ip1 = p2;
                    thisH4GDipho.ip2 = p;
                }
                // ---- save all possible combinations,
                //                 // ---- but of course only once, then we require p2 > p
                v_h4g_diphos.push_back(thisH4GDipho);
            }

            vecDR.push_back(deltar);
            vecDPhi.push_back(deltaphi);
            vecDEta.push_back(deltaeta);

        }
        //---- vector of the distances between the photon and all other photons in the event
        v_pho_dr.push_back(vecDR);
        v_pho_dphi.push_back(vecDPhi);
        v_pho_deta.push_back(vecDEta);
    }
    // ---- Make tetraphotons

    for ( size_t q1 = 0; q1 < v_h4g_diphos.size(); q1++) {
        H4GTools::H4G_DiPhoton Dipho1 = v_h4g_diphos[q1];
        for ( size_t q2 = q1+1; q2 < v_h4g_diphos.size(); q2++) {


            H4GTools::H4G_DiPhoton Dipho2 = v_h4g_diphos[q2];
            // ---- check that we don't use photons twice
            if ( Dipho1.ip1 == Dipho2.ip1
                || Dipho1.ip1 == Dipho2.ip2
                || Dipho1.ip2 == Dipho2.ip1
                || Dipho1.ip2 == Dipho2.ip2 ) continue;
            H4GTools::H4G_TetraPhoton thisTetra;
            thisTetra.p4 = Dipho1.p4 + Dipho2.p4;
            thisTetra.idp1 = q1;
            thisTetra.idp2 = q2;
            thisTetra.ip1 = Dipho1.ip1;
            thisTetra.ip2 = Dipho1.ip2;
            thisTetra.ip3 = Dipho2.ip1;
            thisTetra.ip4 = Dipho2.ip2;
            thisTetra.SumPt = Dipho1.SumPt + Dipho2.SumPt;
            if ( Dipho1.p4.pt() < Dipho2.p4.pt()) {
                thisTetra.idp1 = q2;
                thisTetra.idp2 = q1;
                thisTetra.ip1 = Dipho2.ip1;
                thisTetra.ip2 = Dipho2.ip2;
                thisTetra.ip3 = Dipho1.ip1;
                thisTetra.ip4 = Dipho1.ip2;
            }
            //v_h4g_tetraphos.push_back(thisTetra);
        }

    }




    // Save the info
    outTree->Fill();

}


// ------------ method called once each job just before starting event loop  ------------
void
H4GFlash::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
H4GFlash::endJob()
{

    std::cout << "============== Job stats ==============" << std::endl;
    std::cout << "\t Total number of events: " << counter << std::endl;
    std::cout << "\t Trigger stats: " << std::endl;
    for( std::map<std::string, int>::iterator it = triggerStats.begin(); it != triggerStats.end(); it++)
        std::cout << "\t  - " << it->first << " \t - Accepted events: " << it->second << std::endl;

}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
H4GFlash::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}


//define this as a plug-in
DEFINE_FWK_MODULE(H4GFlash);

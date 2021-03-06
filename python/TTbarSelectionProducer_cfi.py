import FWCore.ParameterSet.Config as cms

ttbarselectionproducer = cms.EDProducer("TTbarSelectionProducer",
                                        verbose          = cms.int32(0),
                                        triggerColl      = cms.InputTag("TriggerResults","","HLT"),
                                        #cf https://twiki.cern.ch/twiki/bin/view/CMS/TopTrigger
                                        trigNamesToSel   = cms.vstring('HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v',
                                                                       'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v',
                                                                       'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v',
                                                                       'HLT_IsoMu20_eta2p1_v2'
                                                                       ),
                                        trigChannels     = cms.vint32(11*13,
                                                                      11*13,
                                                                      11*11,
                                                                      13*13),
                                        doTrigSel        = cms.bool(True),
                                        electronColl     = cms.InputTag("slimmedElectrons"),
                                        conversions      = cms.InputTag("reducedEgamma:reducedConversions"),
                                        electronIdMap    = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-medium"),
                                        electron_cut_pt  = cms.double(20),
                                        electron_cut_eta = cms.double(2.5),
                                        electron_cut_iso = cms.double(0.15),
                                        muonColl         = cms.InputTag("slimmedMuons"),
                                        muon_cut_pt      = cms.double(20),
                                        muon_cut_eta     = cms.double(2.4),
                                        muon_cut_iso     = cms.double(0.12),
                                        jetColl          = cms.InputTag("slimmedJets"),
                                        jet_cut_pt       = cms.double(20),
                                        jet_cut_eta      = cms.double(2.5),
                                        metColl          = cms.InputTag("slimmedMETs"),
                                        met_cut          = cms.double(0)
                                        )

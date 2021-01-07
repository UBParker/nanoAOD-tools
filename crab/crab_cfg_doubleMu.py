from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config
#, getUsernameFromSiteDB

config = Configuration()

config.section_("General")
config.General.requestName = 'NanoPostprocessorLFVtest_DoubleEG_B_2017_Jan6_4perJob'
config.General.transferLogs = True
config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.outputFiles = [ 'tree_Skim.root','output_hists.root' ]
config.JobType.scriptExe = 'crab_scriptdata.sh'
# hadd nano will not be needed once nano tools are in cmssw
config.JobType.inputFiles = ['crab_script_testdata.py', '../scripts/haddnano.py', "/afs/cern.ch/user/a/asparker/public/LFVTopCode_MyFork/nano_cmssw_mc_try2/CMSSW_10_6_4/src/data/TopLFV/input/RoccoR2017.txt","/afs/cern.ch/user/a/asparker/public/LFVTopCode_MyFork/nano_cmssw_mc_try2/CMSSW_10_6_4/src/data/TopLFV/include/MyAnalysis.h", "/afs/cern.ch/user/a/asparker/public/LFVTopCode_MyFork/nano_cmssw_mc_try2/CMSSW_10_6_4/src/data/TopLFV/lib/main.so", "testMC.txt"  ]

config.JobType.sendPythonFolder = True
config.section_("Data")
config.Data.inputDataset = '/DoubleEG/piedavid-Run2017B-31Mar2018-v1_TopNanoAODv6-1-1_2017-9721c24ccc7f925c513e24ff74941177/USER'#'/DoubleMuon/piedavid-Run2017B-31Mar2018-v1_TopNanoAODv6-1-1_2017-9721c24ccc7f925c513e24ff74941177/USER'
config.Data.inputDBS = 'phys03'
#config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 4 #180
#config.Data.totalUnits = 10

config.Data.outLFNDirBase = '/store/user/%s/NanoPosttest_Jan5_doubleEG2017B' % ( 'asparker' )
# getUsernameFromSiteDB())
config.Data.publication = False
#config.Data.outputDatasetTag = 'NanoTestPost_doubleMu_2017B'
config.section_("Site")
#config.Site.storageSite = "T2_DE_DESY"

config.Site.storageSite = "T2_CH_CERN"
# config.section_("User")
#config.User.voGroup = 'dcms'
config.JobType.allowUndistributedCMSSW = True

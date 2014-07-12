import gensim
import numpy as np
import matplotlib.pyplot as plt
import os
import io
import nltk
import logging

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

'''Displays similar terms to an input term.'''

def main():
    print "\nLoading Word2Vec model...\n"
    # 4 GB input file, uses about 20 GB of memory when loaded
    model = gensim.models.Word2Vec.load_word2vec_format("../../PubMed/BioNLP/wikipedia-pubmed-and-PMC-w2v.bin", binary = True)
    model.init_sims(replace=True)
    vocab = model.index2word

    while True:
        line = raw_input('\nprompt> ')
        if line in vocab:
            print "\nSimilar words:"
            print "______________"
            sims = model.most_similar(positive=[line.split()[0]])
            for p in sims:
                print p
        else:
            print "Sorry: not in vocabulary!"
            
if __name__ == '__main__':
    main()
    
    
'''
Behavior:

prompt> tDCS

Similar words:
______________
(u'rTMS', 0.8524664044380188)
(u'cathodal', 0.8008538484573364)
(u'anodal', 0.7848386168479919)
(u'cTBS', 0.7710281610488892)
(u'tACS', 0.7492803335189819)
(u'excitability-diminishing', 0.744255781173706)
(u'excitability-enhancing', 0.7432180643081665)
(u'tsDCS', 0.7424830794334412)
(u'TMS', 0.7370374798774719)
(u'TDCS', 0.7321546673774719)

prompt> microcircuit

Similar words:
______________
(u'microcircuits', 0.8897331953048706)
(u'microcircuitry', 0.8424049615859985)
(u'thalamocortical', 0.7728371620178223)
(u'DG-CA3', 0.7646147012710571)
(u'entorhinal-hippocampal', 0.7464720010757446)
(u'circuitry', 0.7403584122657776)
(u'thalamo-cortical', 0.7362979650497437)
(u'neuromodulated', 0.736114501953125)
(u'pattern-generating', 0.7261242270469666)
(u'cortico-thalamic', 0.7259366512298584)

prompt> STDP     

Similar words:
______________
(u'Hebbian', 0.8346817493438721)
(u'iSTDP', 0.8191224932670593)
(u'anti-Hebbian', 0.8104883432388306)
(u'Anti-Hebbian', 0.774303138256073)
(u'LTP/LTD', 0.7693324089050293)
(u'spike-time-dependent', 0.7624968886375427)
(u'Hebbian-like', 0.7592620253562927)
(u'spike-timing', 0.7520999908447266)
(u'hebbian', 0.7517502307891846)
(u'non-Hebbian', 0.7425894141197205)

prompt> purkinjie
Sorry: not in vocabulary!

prompt> purkinje

Similar words:
______________
(u'Purkinje', 0.874071478843689)
(u'Purkinge', 0.6978480219841003)
(u'non-Purkinje', 0.6936492919921875)
(u'mitral/tufted', 0.687702476978302)
(u'Calretinin-immunopositive', 0.6871809363365173)
(u'Pukinje', 0.6819372177124023)
(u'basket/stellate', 0.6769469976425171)
(u'Purkinje-like', 0.6735796928405762)
(u'granule', 0.6669027805328369)
(u'GluRdelta2(+/Lc)', 0.6632756590843201)

prompt> sequencing-by-ligation

Similar words:
______________
(u'5500xl', 0.7578691244125366)
(u'454/Roche', 0.7468917965888977)
(u'sequencing-by-synthesis', 0.743279218673706)
(u'Roche-454', 0.7393358945846558)
(u'454-FLX', 0.7208085060119629)
(u'Solexa/Illumina', 0.7157059907913208)
(u'SOLEXA', 0.7135040163993835)
(u'SOLiD', 0.7078325748443604)
(u'Illumina/Solexa', 0.705757200717926)
(u'ABI/SOLiD', 0.7055375576019287)

prompt> pseudo-telepathy

Similar words:
______________
(u'graphity', 0.6225616931915283)
(u'-player', 0.6212465763092041)
(u'TDEXX', 0.591554582118988)
(u'continuous-variable', 0.5862028002738953)
(u'three-player', 0.5849363207817078)
(u'discrete-variable', 0.5828121304512024)
(u'tic-tac-toe', 0.5750041604042053)
(u'perfect-information', 0.5709482431411743)
(u'SF-SCF', 0.5708451271057129)
(u'Hawk-Dove', 0.5707070827484131)

prompt> hidden-variable

Similar words:
______________
(u'renormalizable', 0.7471596002578735)
(u'random-matrix', 0.743245005607605)
(u'reparametrization', 0.7407134175300598)
(u'finite-order', 0.7403596639633179)
(u'quasi-deterministic', 0.7392038702964783)
(u'parametrizing', 0.7357470989227295)
(u'ICSEk', 0.7338249087333679)
(u'indeterministic', 0.7331994771957397)
(u'martingales', 0.7315749526023865)
(u'worldsheet', 0.7296195030212402)

prompt> DNA-origami 

Similar words:
______________
(u'3.9-nm', 0.683306872844696)
(u'RIDC3', 0.6641777157783508)
(u'nanowire-nanotube', 0.6547878980636597)
(u'd(A15G15)', 0.651665985584259)
(u'nanocrown', 0.6516061425209045)
(u'MLV-GUV', 0.6509178876876831)
(u'nanometer-scaled', 0.6493244767189026)
(u'micro-assemblies', 0.6464407444000244)
(u'microbowl', 0.645066499710083)
(u'nano-well', 0.6431269645690918)

prompt> SST

Similar words:
______________
(u'SSTs', 0.6336500644683838)
(u'sea-surface', 0.5527259111404419)
(u'R_age0', 0.5177354216575623)
(u'WSST', 0.5134069323539734)
(u'SSHA', 0.4979604184627533)
(u'BBT', 0.4940464496612549)
(u'ULNTT', 0.48894286155700684)
(u'fAPARe', 0.48677128553390503)
(u'monthly-mean', 0.48629283905029297)
(u'LST', 0.4842722415924072)

prompt> host-guest

Similar words:
______________
(u'supramolecular', 0.8009198904037476)
(u'Host-guest', 0.800398051738739)
(u'noncovalent', 0.7842929363250732)
(u'non-covalent', 0.7686740159988403)
(u'host/guest', 0.7682664394378662)
(u'metal-ligand', 0.7569376826286316)
(u'guest-host', 0.7384780645370483)
(u'self-assemblies', 0.7337920069694519)
(u'supramolecules', 0.733771562576294)
(u'protein-surfactant', 0.7323499917984009)

prompt> intravascular

Similar words:
______________
(u'intra-vascular', 0.8323153257369995)
(u'Intravascular', 0.7860449552536011)
(u'intravasal', 0.7582016587257385)
(u'coagulation(DIC)', 0.6470015048980713)
(u'DIVC', 0.6429858803749084)
(u'Non-overt', 0.6308848857879639)
(u'(DIC).', 0.6194186210632324)
(u'disease/disseminated', 0.6092827916145325)
(u'intrasvascular', 0.607906699180603)
(u'pre-disseminated', 0.6043370962142944)

prompt> quantitative phase microscopy
Sorry: not in vocabulary!

prompt> DIC

Similar words:
______________
(u'Nomarski', 0.6346431374549866)
(u'brightfield', 0.6131829023361206)
(u'bright-field', 0.6092953085899353)
(u'interference-contrast', 0.5937526822090149)
(u'Epi-fluorescence', 0.5780161619186401)
(u'phase-contrast', 0.5739066004753113)
(u'differential-interference', 0.5727100968360901)
(u'IR-DIC', 0.5691530108451843)
(u'Spinning-disk', 0.5672113299369812)
(u'Nomarsky', 0.5671278834342957)

prompt> spinning-disk

Similar words:
______________
(u'spinning-disc', 0.8962848782539368)
(u'laser-scanning', 0.8382167220115662)
(u'TCS-SL', 0.8355540037155151)
(u'LSM700', 0.8344143629074097)
(u'epi-fluorescence', 0.830013632774353)
(u'TCS-SP5', 0.8279765248298645)
(u'LSM710', 0.8209614157676697)
(u'widefield', 0.8203139305114746)
(u'TCS-SP', 0.8203009963035583)
(u'TCS-SP2', 0.8179222941398621)

prompt> C. elegans
Sorry: not in vocabulary!

prompt> C.elegans

Similar words:
______________
(u'D.melanogaster', 0.7808642387390137)
(u'Drosophila', 0.7406141757965088)
(u'Caenohabditis', 0.7330749034881592)
(u'drosophila', 0.7143757939338684)
(u'Caenhorhabditis', 0.7136931419372559)
(u'Drosphila', 0.7130506634712219)
(u'Caernorhabditis', 0.7107883095741272)
(u'Caenorrhabditis', 0.7080975770950317)
(u'Caenorhaditis', 0.7065104246139526)
(u'ce10', 0.7042290568351746)

prompt> connectome

Similar words:
______________
(u'connectomes', 0.7538338303565979)
(u'connectomics', 0.7271997928619385)
(u'phenome', 0.6334644556045532)
(u'multi-omics', 0.6211690902709961)
(u'physiome', 0.6201737523078918)
(u'connectivity', 0.6198800802230835)
(u'neuroinformatics', 0.6161473393440247)
(u'neuroinformatic', 0.615900456905365)
(u'paleogenomics', 0.6131301522254944)
(u'brain-wide', 0.6037588715553284)

prompt> osmium

Similar words:
______________
(u'OsO4', 0.8469041585922241)
(u'Osmium', 0.8384340405464172)
(u'tetroxide', 0.7909336686134338)
(u'postfixation', 0.7579689025878906)
(u'tetraoxide', 0.7437511086463928)
(u'glutaraldehyde', 0.7186528444290161)
(u'postfixed', 0.7152538299560547)
(u'gluteraldehyde', 0.7001497745513916)
(u'OSO4', 0.690950870513916)
(u'post-fixation', 0.6904089450836182)

prompt> nanobubble

Similar words:
______________
(u'nanobubbles', 0.7259963154792786)
(u'nanodroplet', 0.7045518159866333)
(u'nanochannel', 0.7029339075088501)
(u'polymer/solvent', 0.6893505454063416)
(u'polymer-nanoparticle', 0.6877922415733337)
(u'water-toluene', 0.6876121163368225)
(u'monoglyceride-based', 0.6872311234474182)
(u'nanoaggregate', 0.6865259408950806)
(u'nano-particle', 0.6804802417755127)
(u'micro-mixing', 0.6800671219825745)

prompt> backscatter

Similar words:
______________
(u'backscattered', 0.7774629592895508)
(u'backscattering', 0.7541754245758057)
(u'back-scattered', 0.6863366961479187)
(u'reflectivity', 0.6722930073738098)
(u'scattering', 0.6605265736579895)
(u'lidar', 0.6556425094604492)
(u'spatially-resolved', 0.6511934995651245)
(u'photoacoustic', 0.650908887386322)
(u'back-scattering', 0.6490159034729004)
(u'Time-domain', 0.6444695591926575)

prompt> ADAR1

Similar words:
______________
(u'ADAR', 0.8010864853858948)
(u'ADAR2', 0.7735375761985779)
(u'ADARs', 0.726050615310669)
(u'E319A', 0.7193240523338318)
(u'ADAR3', 0.7192800045013428)
(u'RNA-editing', 0.6473779678344727)
(u'pri-mir-376a2', 0.645708441734314)
(u'APOBEC-1', 0.6450561285018921)
(u'Prp8', 0.6447651386260986)
(u'APOBEC1', 0.6438855528831482)

prompt> immunoregulatory

Similar words:
______________
(u'immuno-regulatory', 0.855791449546814)
(u'immune-regulatory', 0.8476027250289917)
(u'immune-modulatory', 0.7817468643188477)
(u'immunoregulation', 0.7668118476867676)
(u'immuno-modulatory', 0.7589092254638672)
(u'immunomodulatory', 0.7558903694152832)
(u'immune-suppressive', 0.7542456984519958)
(u'disease-promoting', 0.7350339293479919)
(u'immunoinhibitory', 0.7265671491622925)
(u'down-regulatory', 0.7073224186897278)

prompt> Treg

Similar words:
______________
(u'Tregs', 0.9393182396888733)
(u'T(reg)', 0.9153534173965454)
(u'nTreg', 0.9090198874473572)
(u'T-reg', 0.8903014063835144)
(u'Foxp3+', 0.8830138444900513)
(u'reg', 0.8720570206642151)
(u'TReg', 0.8692123293876648)
(u'T-regulatory', 0.8654361963272095)
(u'FoxP3+', 0.8639062643051147)
(u'CD4+CD25+', 0.8630605936050415)

prompt> autoantigen-specific

Similar words:
______________
(u'islet-reactive', 0.8845388293266296)
(u'autoreactive', 0.8575700521469116)
(u'auto-reactive', 0.8545098304748535)
(u'Ag-specific', 0.8503217697143555)
(u'MBP-specific', 0.8482874631881714)
(u'alloreactive', 0.8477950692176819)
(u'myelin-reactive', 0.8441157341003418)
(u'antigen-specific', 0.8393238186836243)
(u'alloantigen-specific', 0.8375391960144043)
(u'self-antigen-specific', 0.8346645832061768)

prompt> thymus

Similar words:
______________
(u'spleen', 0.7856139540672302)
(u'thymuses', 0.7003498673439026)
(u'thymic', 0.6994088888168335)
(u'thymi', 0.67829430103302)
(u'testis', 0.6359335780143738)
(u'MLNs', 0.635832667350769)
(u'adrenals', 0.6288015246391296)
(u'thymocytes', 0.628328263759613)
(u'MLN', 0.6190166473388672)
(u'testes', 0.618057131767273)

prompt> NOD

Similar words:
______________
(u'NOD/Lt', 0.7864229679107666)
(u'B6.H2g7', 0.7808311581611633)
(u'NOD.Idd3', 0.7762904167175293)
(u'MRL/lpr', 0.7752621173858643)
(u'TNF-alpha-NOD', 0.7631634473800659)
(u'C57BL/KsJ', 0.7628995776176453)
(u'4.1-NOD', 0.7615660429000854)
(u'RIP-GP', 0.7605341076850891)
(u'8.3-TCR-beta-transgenic', 0.7598447203636169)
(u'NOD.scid', 0.7586204409599304)

prompt> CD20 

Similar words:
______________
(u'CD19', 0.8985385298728943)
(u'CD5', 0.8886458277702332)
(u'CD79a', 0.8747891783714294)
(u'CD7', 0.869798481464386)
(u'CD56', 0.8610313534736633)
(u'CD138', 0.8579594492912292)
(u'CD45', 0.8564658761024475)
(u'CD3', 0.8507461547851562)
(u'CD43', 0.8482075333595276)
(u'CD21', 0.8380001187324524)

prompt> monoclonal

Similar words:
______________
(u'polyclonal', 0.886044979095459)
(u'Monoclonal', 0.8782506585121155)
(u'Mab', 0.8591514229774475)
(u'mAb', 0.8436859846115112)
(u'MoAb', 0.8421968817710876)
(u'mAbs', 0.838129460811615)
(u'mAB', 0.8333730697631836)
(u'antibody', 0.8327054977416992)
(u'anti-MUC1', 0.8316301703453064)
(u'MAb', 0.8284293413162231)

prompt> GRIN

Similar words:
______________
(u'gradient-index', 0.7914174795150757)
(u'collimating', 0.7414436936378479)
(u'Selfoc', 0.7366790175437927)
(u'GRIN-rod', 0.7314081192016602)
(u'variable-focus', 0.7216536998748779)
(u'telecentric', 0.7074366807937622)
(u'lens-based', 0.706377387046814)
(u'Gradient-index', 0.7052550911903381)
(u'aberration-free', 0.699813961982727)
(u'three-mirror', 0.6972783207893372)

prompt> fiber-bundle

Similar words:
______________
(u'phase-screen', 0.7027356028556824)
(u'butt-coupling', 0.700380802154541)
(u'five-layer', 0.6957000494003296)
(u'zero-thickness', 0.6880347728729248)
(u'beam-forming', 0.6862413883209229)
(u'quasi-three-dimensional', 0.6807047128677368)
(u'millimeter-scale', 0.6803610920906067)
(u'ray-trace', 0.6793121695518494)
(u'quasi-isotropic', 0.6788274049758911)
(u'space-invariant', 0.6786760091781616)

prompt> super-resolution

Similar words:
______________
(u'superresolution', 0.8803644180297852)
(u'Super-resolution', 0.8022908568382263)
(u'multispectral', 0.7899445295333862)
(u'video-rate', 0.7759106159210205)
(u'structured-illumination', 0.7685712575912476)
(u'nanoscopy', 0.759961724281311)
(u'FLIM', 0.7569429874420166)
(u'episcopic', 0.7521911859512329)
(u'multi-photon', 0.750573456287384)
(u'subdiffraction', 0.7501491904258728)

prompt> array-tomography
Sorry: not in vocabulary!

prompt> ultrathin-sectioned

Similar words:
______________
(u'thin-sections', 0.7502503395080566)
(u'negatively-stained', 0.7474088668823242)
(u'thin-sectioned', 0.7420254945755005)
(u'negative-stained', 0.7402969002723694)
(u'cryo-fixed', 0.7330671548843384)
(u'permanganate-fixed', 0.7314386367797852)
(u'rotary-replicated', 0.7259163856506348)
(u'metal-shadowed', 0.7186503410339355)
(u'reembedded', 0.7165279388427734)
(u'Resin-embedded', 0.7111867666244507)

prompt> vitrified

Similar words:
______________
(u'vitrified-warmed', 0.8241201043128967)
(u'vitrification', 0.7862972617149353)
(u'pronucleate', 0.7646970152854919)
(u'vitrified/warmed', 0.752212405204773)
(u'blastocysts', 0.7492651343345642)
(u'failed-matured', 0.7463165521621704)
(u'vitro-matured', 0.746229350566864)
(u'morulae', 0.743812084197998)
(u'2PN', 0.7314016222953796)
(u'zygotes', 0.724366307258606)

'''

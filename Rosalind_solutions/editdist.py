def editdistance(word1,word2):
    d=[]
    for i in range(len(word1)+1):
        d.append([0]*(len(word2)+1))

    for i in range(len(word1)+1):
        d[i][0]=i
    for i in range(len(word2)+1):
        d[0][i]=i

    for i in range(1,len(word1)+1):
        for j in range(1,len(word2)+1):
            disthor = d[i][j-1] + 1
            distvert = d[i-1][j] + 1
            if word1[i-1] == word2[j-1]:
                distdiag=d[i-1][j-1]
            else:
                distdiag=d[i-1][j-1]+1
            d[i][j] = min(disthor,distvert,distdiag)
    return d[-1][-1]


print(editdistance("DFQINIIWHMEYFIDARKVIFGITAHKPQKVRNHNRADDKIASMNGFVQFSYCKIAKALTCWSVQRKTLTTPHWCTTEWDEQQTIDQGISRRTNAMYLMSANAFVNNIVTYHMTMLGAWELWCECFMIDVDPFQPCVNTKYMWGCANIARRSTDDMSYLIFGMNVATCKEVLWEIKQFGAINPFSGANPIINPKECRHEFYWFNQNCQSWSEDSWIANAKCYKFKWNHWGSPEPQFYRFVATSNTMCVFTNHFGLEKRDPQIHKREIANLTVRCWADIKINLPHRASIHTIEYNFMLTPNRGICDPRDSFFHVGFHNKIFIEVVMYPSFYSTMRDHYCIDNVGWLYVHMRGLQHYWYNEMHTKRNMRWFFVWKMDMFACQQLGLDCGDFTGHNNIFNMPDMDKNLVIQQFVKVMEHENHIDKNLNCGEIYTPAVHRVNTDAQTKKHGRQPHAPLLIACRSYAQMDMPMEEYQSAWIYSECTHHDMRCHHKPIEQRITKDGDKVQQQKIYRRYHCRAQKNDTITELDMKTQTWEIDLFLMYLSCPQPLWFRFTGRMDGLNDEPQFKSHSYWTMPCDRHVNENSQWWHVQICRGNISNHKKLHAFTSVEDLCMPNQASVYYICYSNNTFMTKRYYEAEMPKHGPQVITHYHMRSAYGPSEGGNTQRKNCCARPELFDCWPEASMKALYDPTNRWFPDQFMYLEAYLLCAGAAMHWMLSLMKHKFYPWAYFSHICYVVKVIGGMHMDVDNLCGWIMSRLQCPYTKDGMWIFVRREMFDGRTNWEAHCYMEFQPQCLVYWDGVSRILKYGIAWWYKHNQEHTAQPYHADCMHFNLVLEWVGIRWVDTAKPEEPEMCCFNSAFFPIEWTQAKRSVKSGEQLYCWMIGVYPQTWNLASVNMIRNLAPWPFPSPPDYNGTGGKNMQPDKLFMPSYFFNQLTYWQLPMACCVPRVTAMSCLRMSDDHYSWESKYGGYQKDHVMWITTNKKGPSVIGYFCEGEKVYQLIQDDSDDDWGILNHWHMRMFMMFWLNLDFSEDCMCWSVWLFFSWNAYSFYRDKTHMDRMMEYYALGVPIVDCAQDRNPTMIQLFVGKYQRLPEAKCNGKTQFEMCICIAHGGTPYAIQSFEWDYPQGLNTVTYSPVKMSMGISWKDYLRGEYTVHKWIGLWPNKGRFRESNVPKARFHYNALYHGDIEDQWFNAKFPMLHRIKMDFYTMDDNCLAQTRGCDTNQRPIFFDKPVYHLTGLTLHWWHLHICDPYPYKARCDGFLRREQMQMASNMTPPFWTRNVPKNHDESCICKNSIVLPLSRYPQVFRTCTMDRNGIFAGQSEDLTFSNKINMLFIPHTISSWKGRPNYEQLSSRFRLNPYRIYMKMNHILTWQEPMRFHMVGEFHKCPLPEYSMWHANVPVWDWFPVTTDLYQWDNDETAEFTWETRLDYNFGCGLNTEDRQAQYVFHRNKPINGIGAQRPQYTTANWCAWWCYTSDWFLESSWKGFIRKLTSSTEKWYKPVTYYSTHDIEYINDVSSYTDTHCRLLEHQWANTMYEFLSSRSMCALLLRIHNDNPEYVKDPIMASLRCQWCSGEIYQWRQQGDYQECWRNPDYQRRHHCLTRKHSYMLSWWKKIYWREADNSNFFFMGVSYNVEAKWVNEHTDHMTCVYYALDMPIFDATYPKKCQCHAQQWFSIYNSNTDDPGAESQAGIQQFWHKHHVVCNAKKVFRSQTRELYDIWMYAASRCKRCLRESKIAKLTRPDHHFSVCWCEQKLSTTPRKKWGMAEACLKTSVYAFGVRLVTRPKVLEPEIEVASSYWYDWQAMDRAPFCWPREKMSVHWWGWRHFNSNCSTEPKAFNQATWGSFWGHTEKSGDIKLVLASEWVEPEIESMNPQIEEVWTPNDNECEWTSDKKFVRIRSIFMFKIQKHMADSFKQHTENIAFDQRPSSHNCMKLSKMDQYTGNLDAQGANKTCPHQQFMSHHSAIACCMGTKWICSWKMMCFDTGQLSGTYHEKEEGFEKQDRMVGKTCNYSFNYHVSCNQGRTPVDILTTMHPYHDDQANYMREFGNFKPDYKGYECIPIENHLTLMYGLWHVACNIIYRTNNQQDIQGWCVVCWGAMPPWPEVYNLPCVATEKCMLRFNFKAFTHHYHRMSSWDYERHTFNPYLSAWQIKWYMHPVGDQRLTRWSFWSSCRNLALGYEYLWDMITSIHCCDLWALMISLPVPCSTMISSEVNELIVKCWEMLMNKNTAVGCRMSANEIIPWVMSWCEQVHEKMPYYEWPYSPGYIFHAEILRHDESFPFQPMESDVQTEDEDLRYLYSSGRSDHKCVCSSKMDCYWFVQGVLTGHQYHHSMSLAASWLVRPKMRGMDVAEVEHNADMHQTEKTKLRMHGKYMHVSRNEPIGEGNNDLDMCIEAYWRFHVWGLGYVRRQEHGGTYLGPFIMWVGCRAEPFPQMNPLVTHMTPHYNCREERVTKAGDSECRKFCWQYAERQSQNTECNMAERIIGCMIKVWEFWRVDTGHTPKICCRVARNTWYLGKTKIRLNAQGWAWHAMYSSFWNYCPRPAAVQKDIQKKYKEASMMGCGWHAQRNPFLFNLEYVSICLVCTDAKYWQAFDDMSQSVDIFSNVLCKNHVGGYIQMCFDLRWHCKSINNYRLNSWYDWWVCNIKQAPVWRKFSIPDQSHQMERCVLAMIGQLLGGNHTAMQFVLLLNVLAQLYTCIFMTFYNHDNLAWDVSGEPNLGVGYYHTKPQMIPEPFTYHHTFYQEQMISKPCVDVAGQHTKMAEQKMCDANSAQKEPMMFPPTGWQRAMWIMVDRYSRYRDMEYFLNSPSGMSACILRIIMRNMVHSRFCEFDGMWKIGMICPCRGVGTFWERSWMSRFSKLDKVNIPASYSTGDNWRYHYPGIERFNHTHGSLSGKAQCYWEACVTISDEEWFVLIQNMPHILPHPMHNWDGWWTIGEAEGWNPSHEMVRDDNGDFGNPFLSWPSWLGRWMETNQVMSLLVTTRKWPVFGTYYRWVTEAMAMTRTEAWSGHDLGRWAEVCCMSAFRHHHAQAGWHHLWCTDQAEVLFMHQLFLDGQKQVMLGDTWFMMWILEERGYVMMRVWNNAKVSLVVGWGPPVATQRNDCPQFNRNRQHSECHDHGSSDHCVQFWDQDSSNPDFWQASLNYAYYGYTYTQQMMKWLWEPYQLRYIPKIFCKYSIGAAMPFPNIYNITKDKKNCMHKDTECPTGYWTCTLYWHYTSQCYRFHDAIGIDWDLRANIHEESEVSCNALKDYSRDNFIWMMYQFYWRYDGPPILHAEASRHENRPKINPEESVLYCLSLLQQFPVRYENQKCHSEAQCWRVSNIDGPHAMKWSFSPACTKTHMTISKAIQCTIWETIAFHSHGEEWALSHEWWMATDGPNMKWQWNFFFKTRSLMNTNIQWHMPCLESKYQNTEQYLFWDKKHMKKTQTPPDMPWASHCDCVIRPYPNAVIHNENRCLVLTTPWMQMTRKQEWMIFQMEWVFCFANLQYVEIEHWIDQRNGRQIQCSSKMWDHIFFTPRFHWYMKWMEWWPAPIKHQEYQNLMPEQDMFDIEFFNQNARSGITVTGDNWKYMMQAWMNNSMFASKLDKQCYFVNLRIHAQESRPSGGEDDWGCRMFFSHMACSIKWD","DFQINRIWHMEYFIDERYVIFGITAHKPADDKACSYCKIAKADVNRYTQHFEGAGHPYARMQSEEHWETWSDGHNYPAQHLISHRTNAMYLLSAVTAWFDVFWNWPHKQCECFMIWVPGQSTRKVNTDYHMTDDWSYLIFGMNVATCKEVLWEIKQNPIINCSHSFYWFLQNCQSWSESSWIARRKINFLVNRIKFKWNHWGSPEPQTSCTECVFTNTFSGEKRDPQIHKREIANLINLMHRASIHTIEYNFMLTPNNSWFYRDPRDSFEHVFHNKIFQEVVMCPSFYSYPSENRRMRPQETTWCKDAFCGWLYENMRGLQHYWYNEMYTNRDNYNTRNMRWFFVWKMDMFACQQLGLDCGDFRDVWWMKSWGHSNIFNEMDKRLVEQVFVINAEAVHRVNLFAQTKKHGRQPHAPLHEAAMNIACRSYAQMDMPQIEDKIRIMYSECTHHDRITKDGDKVQQQKIYHCRAQKNDTMMKTQTWDQPLPFRFTQCARRMDKSHTMPCDRHQNHPSTLDCWWAHWIVKDKHAQCVLCGDSIDRTMIHPSKHKFTSVEDLCMPNQASVYYWYAWGFQFHCYTNNYNMSLGCMTKRFYLMVFALPMMWNEVAYPSEGGNTQRKNCCARPEFWLFIHKFDCWRWFPDQAAMYWMLNLEPWAYFSHFFKAWTMTCYCFDFVKVIWGMHMDVKNLCGWIMSRLQCPYDGYWIFVGRTNWEAHHYMEFQGQCWDNWYSFHGLEYYHWRAVGWIYFMLVQEHTAQPYHLDCMHFMLVGIRWVDTAKMEPETCCFNIAFFPIEWTQSHGKKRCYCSIGVYPQTWTLNICLNLAQVNMIFNWPFPPPIYNGTGGKNMQPDSYQGGQKCWEQLPMICCVWGLHYRAMSCSWESKYGGYQKDAVMWTTSRTAQGVCYFCTGEKIYQLIQARIKWRSIMQECVMQYDDEGILNHWDPPYNMCWRMFMMFWLNLDDSEDCMCWSVWVNSSFFSYSFYRGKTDFMMEYYALGVRHTQADINIQIGGWNIQLFGPNYEYNGGKYQGKTQTGQNMPTLLILIAVGGTPYAIQSQAMWMGANNKRWDYPQGLNTVKMSIENHPYSMNISWKDWLRGQHWHLPHNVHKPWNIGLWPNKGRHWKRAIRARNALYHGDIEDQWFNAKHRIKMQLCWFTMDDNCGARTRGCDTNQRPIFFDKPVYHGTGLGLSMVEFNGWYSKENNMEFAHLHICDPYPYKARCDGFLRMQEMYRWPWTRNVPKNHDSQHSECICKNSIVNPLSRYPQVFRTCTFAGQSEDMDTTATYIFDSNKHNDSSPFYTIPYSWKGRPNYEQLSSRFREGPYRTYMKMNHILTLQEPMRFVMFQDFMRDMVDPFHICPLPEYEMYHWFPVTTDLYDIDETAEFSWETGPISTKNLDYNFGCGLNTEDRQAQTVFHGVSSAACLNKPINGIHAQRGYQYTTTNWCHWWCYTSDWFLESSWRKNTSSTKPVPWSYSTHYHYNQPEMVSSYTLYTGYISHCRILEHQWTNTMYEFLSSRSMCALLLRVMRGMFILDNPEYVKDPIMASLDHDVSCQWCSQFDYQECWRNTDYQRRHKRKHSYSLSTLLKKKKIDIFWREADHSNFFFMGVSYNVEAKWVNEHTDHIVTQVYYALDMPMDWNKFDATYELWAFQQWFSPVMNMITNPRGNTDDPGAEWQAGIQQFWHKHHVVCNMKKVQRSGMFPSERELYDVWMKQLKKVKRCCCVARESKIKNEILQKLTRPDHHFSVCWIHQKLSTTPRKSMWGPAACLKTSVYAHLVTRPKVLEPEIEVVYKSSYQQMRQSYEGIWFEAYDWQAMLRAPFVWPRKMSVHWYWFMDYWRHFNPNCSTEPKAQATWGSFWGHTLKSGDIKLVLASEWVIPEIWIVMNPQIEEVWTPNDGECEWGSDKKFVRIYSIFMWQLKIQKHMADSFKQPSSPMIVSAENCIFRSKEFDQYTGNLEMMNKTCPHQQFMHSAIACCMDTKWICSWKMMIFDHNIGFNGRFLSGTPHCKPYEGFEKQDRMVGKTCAYSFNYQGRTPVDIMNRIHQEVTMREFGPDYKGYECAAGQYIPIENHNTSMYGLWHVACNIPYRDNNQQDIQGQCVVCWGAMPPQPFVYNLYEAARFGVDTEKCMLRFNEKALHMPKATHHYHRMSSWDYERHTFNPYLGDPQEFPAAWQIKWYMHPVGDQRLTRWACRRNISLYHLHLALGYEYQWDMITSIKPSCNYSNRPLSVPCSTMISSEDMHHNTLIVKCWEMLMNRNTAVGCRMSANEQMACCAWREMIWWQVHEMQMPHYEWPYSPGDIFHAEILRGDESFPFQPMESGRSDHKVCSSKMDHNCDSEEYVFVQILRVLTGHQYHHSMSWAINLKPWLVMPLMRPWNAWQSLGMVLGPVTDMHQTEKWVEYETWSKHGYMHECEVLSFNEMIGEGNNDLEQSWTRSQPRGVFCRNRECEAYWRFHVWGLGYVRRNYMHGGTKLGPFIFPQMHSFIGWFPLVQSCSHMGPHVNCREERENECVMMTNEHNWFPAGTIIFDSCWQYSERWFMHSSQNTECNMAERIPCCMIKVWWFWRVDQGHTARNTWHYLGKTYFLIIMIIRLGAQGWAWHAMYSSFWAAMQKEIQKKYKLQALPVQEGWHAGYPIYFWRNPFLNIATWYWQAFDDMSQSVDIFCTARHSYYSNFDAYWLCKNHIGGIMQMCFIWNVVLRWSKSINNYRHGSPMTKQAPVWRKSDYDRCASIPDQSHQERCVLAMIGNHMQMWHRRSVILLNLAQLYTCIFMTGKEEASTFAWDDSGEPNGGVGYYHTKPQMIPEPFTYTTEAHTCACPFLYQEQLHDQISKCCVDVAGCDTKMSMCMMCDANEPMMFPPTGWQKAVWIMVHRSSQYRKMILNGMSACILRIIMRNMVHSRFCEFDGMWKIGMICPCRGVEKTFECPDCERPIRSWMSRPSKLDKVISVNIQATETGWCDSMQPMCANVRYPGIERFNHTHGWEACWWLVTISDEEWFILIQNMHHILPHKMHNYDGWWTIGEAEGWNPSHEMVRDDNGDFGNPFLSWPSWLGRWMETNQVMSTVKMLVRKWPVFGTVYRWLGFLEAMAMDIYGYAVDCRNEAWSAGWHHLGVVFCTDQAEVLFMGWCFGPPREQLFLDKHVMLGDTWFCCIYMTEERGQVYTMAKVSLVVPWGPTVAHEDTPHRQRNDDPQFNRNRQHSECHDHGSSDHHALSQQKQFWPVGAKCNTFWQASLNYAYYGYTSTQQMMKWWYIPKIFCYYKDKKNDTECRQEIRFRFPTGYWTCTFMKWQIEQACMRFHDAIGIDWDLRHEEHEPSCPALKDYSRDNFIKMMYQFYWRYPGPPILHAHASRHENRPKIMWCETQVDAPEESVLDCLSLLQRKPVRRENQKCHSEDYELWTVCCWQVVSNYDGPHNMKSSFSATTRACTKTHKCDTTTIKPSAIQCHSHGEEWALSKEWWMATDGPNMAWQWLFFFKTHSTMNTNIQWHFGVPCLESKTEQSLVVMNINYIKEQTPPTMKIHWDCVIRPYPNTIPQRDMMSVIHPWKEKIRKENRCLVLTTQWMQMTRKQEWMIFQMEWGEVWQLCIANLQYTWVWICEFEHWIDNIHIFFDDTVAGIPWMFDIEFFNQNARSGITVTGISPIYFSNWPTMMLAWMNISSINEYFVNLRIRAKESRPSGGEDDWGCRDFFSHMYCSIKHD"))
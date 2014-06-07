
# returns the current list of known stations
import operator

def getStations(sortingKey):
    #{
    #    "Name":"HayFM",
    #    "Url":"http://hayfm.am:8000/",
    #    "Icon":""
    #},
    #cityfm, http://www.cityfm.am/
    #radio vem, http://www.vem.am/
    resp = [
            { # verified
                "Name":     "Ar Radio Intercontinental",
                "Url":      "http://199.195.194.92:8029",
                "Icon":     "http://www.arradio.am/images/m_01.gif",
                "Email":    "aa@arradio.am",
                "Country":  "Armenia",
                "Address":  "0025 Yerevan, Alex Manoogian 5 str",
                "Phone":    "+374-10-55-11-43",
                "Director": "Armen Amiryan",
                "WebPage":  "http://www.arradio.am"
            },
            {
                "Name":     "Armenian Bible Study",
                "Url":      "http://sc7.mystreamserver.com:8036/",
                "Icon":     "http://www.armenianbiblestudy.com/img/abslogo.png",
                "Email":    "feedback@armenianbiblestudy.com",
                "Country":  "",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://www.armenianbiblestudy.com/"
            },
            {
                "Name":     "Armenian Christian Radio",
                "Url":      "http://fire.wavestreamer.com:5643",
                "Icon":     "http://bashde.org/images/logo-4e.png",
                "Email":    "info@bashde.org",
                "Country":  "USA",
                "Address":  "405 Waltham St. Lexington, MA 02421-7954",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://bashde.org/"
            },
            {
                "Name":     "Armenian Independent Broadcasting of Boston",
                "Url":      "http://ws.irib.ir/player/mediaplayer/player.swf",
                "Icon":     "http://armenianradioboston.com/images/ABB-Bannerad.jpg",
                "Email":    "Yevgine@aol.com",
                "Country":  "USA",
                "Address":  "PO Box 46, Watertown, Massachusetts 02471",
                "Phone":    "+1-617-926-6268",
                "Director": "Yevgine Gharibian",
                "WebPage":  "http://armenianradioboston.com/"
            },
            {
                "Name":     "Armenian Net Radio",
                "Url":      "http://50.117.8.242:1126/Live",
                "Icon":     "http://www.armnetradio.com/images/logosmall.png",
                "Email":    "",
                "Country":  "Armenia",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://www.armnetradio.com/"
            },
            {
                "Name":     "Armenian Patriotic Radio",
                "Url":      "http://5.35.246.210:8001/stream",
                "Icon":     "http://www.imarmenian.com/association2/wp-content/uploads/2011/12/ARF-Logo-Red.png",
                "Email":    "radioyan@imarmenian.com",
                "Country":  "France",
                "Address":  "Maraash Street, Harboyan Building, 1203 Bourj Hammoud, Al-Metn, Lebanon",
                "Phone":    "+961-3-274-847",
                "Director": "",
                "WebPage":  "http://radioyan.com/"
            },
            {
                "Name":     "Armenian Pulse Radio",
                "Url":      "http://50.7.96.210:8134/",
                "Icon":     "http://www.armenianpulse.com/wp-content/themes/eGamer/images/radiopage/pulse_radio.jpg",
                "Email":    "content@armenianpulse.com",
                "Country":  "",
                "Address":  "",
                "Phone":    "",
                "Director": "Harout Kalandjian",
                "WebPage":  "http://www.armenianpulse.com/"
            },
            {
                "Name":     "Armenian Voice",
                "Url":      "http://50.7.77.114:8111/autodj",
                "Icon":     "http://www.armenianvoice.com/SiteImages/ArmenianVoice.jpg",
                "Email":    "info@Armenianvoice.com",
                "Country":  "",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://www.armenianvoice.com/"
            },
            {
                "Name":     "Lav Radio(FM-107)",
                "Url":      "http://streams4.museter.com:8218/",
                "Icon":     "http://www.fm107.am/images/logo.jpg",
                "Email":    "",
                "Country":  "Armenia",
                "Address":  "",
                "Phone":    "+374-10-36-86-45",
                "Director": "",
                "WebPage":  "http://www.fm107.am/"
            },
            {
                "Name":     "Lav Radio Mix",
                "Url":      "http://195.154.181.100:8000/stream",
                "Icon":     "http://www.lavradio.am/img/big_logo.png",
                "Email":    "info@lavradio.am",
                "Country":  "Armenia",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://www.lavradio.am/"
            },
            {
                "Name":     "Nor Radyo",
                "Url":      "http://norradyo.com:8000/live",
                "Icon":     "http://www.ermenikultur.org/wp-content/uploads/2013/10/Nor_Radyo__g_rsel.jpg",
                "Email":    "info@norradyo.com",
                "Country":  "Turkey",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://www.norradyo.com/"
            },
            {
                "Name":     "Public Radio of Armenia",
                "Url":      "http://195.154.181.100:8052/",
                "Icon":     "http://www.armradio.am/hy/wp-content/uploads/2012/09/logo_up_arm.png",
                "Email":    "aa@arradio.am",
                "Country":  "Armenia",
                "Address":  "Yerevan 25, Aleq Manukyan 5",
                "Phone":    "+374-10-55-11-43",
                "Director": "Armen Amiryan",
                "WebPage":  "http://www.armradio.am/"
            },
            {
                "Name":     "Radio A",
                "Url":      "http://91.121.62.121:7250/",
                "Icon":     "http://votreradiosurlenet.com/player/img/radioa.gif",
                "Email":    "radio.a@wanadoo.fr",
                "Country":  "France",
                "Address":  "32 rue Pompery, 26500 Bourg-les-Valence",
                "Phone":    "00-33-4-75-56-18-33",
                "Director": "",
                "WebPage":  "http://radioa.net/"
            },
            {
                "Name":     "Radio Ardzaganq",
                "Url":      "http://www.ardzagank.com/home.swf",
                "Icon":     "http://www.ardzagank.com/img/logo_3.jpg",
                "Email":    "ardzagank@ardzagank.com",
                "Country":  "Armenia",
                "Address":  "Frunze 13, Yerevan, Armenia",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://www.ardzagank.com/"
            },
            {
                "Name":     "Radio Fama",
                "Url":      "http://195.154.181.100:8036/",
                "Icon":     "http://www.radiofama.am/wp-content/uploads/lg8.png",
                "Email":    "",
                "Country":  "Armenia",
                "Address":  "375010, Yerevan, Tigran Mec 17",
                "Phone":    "+3741-59-70-00",
                "Director": "",
                "WebPage":  "http://radiofama.am"
            },
            {
                "Name":     "Radio Gayan",
                "Url":      "http://radiogayan.com:8000",
                "Icon":     "",
                "Email":    "",
                "Country":  "",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://radiogayan.com/"
            },
            {
                "Name":     "Radio Spyurq",
                "Url":      "http://192.184.9.79:8174/",
                "Icon":     "http://d1i6vahw24eb07.cloudfront.net/s195991q.png",
                "Email":    "http://static.wixstatic.com/media/9badce_2edb315888ac483287408d2d6d0d3d48.jpg_srz_p_171_87_75_22_0.50_1.20_0.00_jpg_srz",
                "Country":  "Lebanon",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://www.radiospurk.com/"
            },
            {
                "Name":     "Radio Arax",
                "Url":      "http://www.radioarax.com/programas/RadioArax-727-DO-20140601.mp3",
                "Icon":     "http://www.radioarax.com/logo.jpg",
                "Email":    "armenia@adinet.com.uy",
                "Country":  "Uruguay",
                "Address":  "",
                "Phone":    "+598-90-09-69-09",
                "Director": "",
                "WebPage":  "http://www.radioarax.com/"
            },
            {
                "Name":     "Radio Arc",
                "Url":      "http://radioarc.serverroom.us:4082",
                "Icon":     "http://www.radioarc.com/images/logo-anim.gif",
                "Email":    "info@radioarc.com",
                "Country":  "",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://www.radioarc.com/"
            },
            {
                "Name":     "Radio Armenia",
                "Url":      "http://radioarmenia.com/radio2/radio.swf",
                "Icon":     "http://radioarmenia.com/radio2/images/small_logo.jpg",
                "Email":    "info@armenianmusic.com",
                "Country":  "",
                "Address":  "",
                "Phone":    "+323-664-3365",
                "Director": "",
                "WebPage":  "http://radioarmenia.com/"
            },
            {
                "Name":     "Radio Armenie",
                "Url":      "http://radioarmenie.relay-network.com:8032/",
                "Icon":     "http://www.radioarmenie.com/templates/theme475/images/logo.gif",
                "Email":    "",
                "Country":  "France",
                "Address":  "4 rue Marcellin Berthelot 69150 DECINES FRANCE",
                "Phone":    "04-78-49-52-74",
                "Director": "",
                "WebPage":  "http://www.radioarmenie.com/"
            },
            {
                "Name":     "Radio AVOL",
                "Url":      "http://64.150.176.192:8250/stream",
                "Icon":     "http://radioavol.org/uploads/donates/donate1x1.png",
                "Email":    "info@radioavol.org",
                "Country":  "Lebanon",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://radioavol.org/"
            },
            {
                "Name":     "Radio Avrora",
                "Url":      "http://www.radioaurora.am/hdvideo/",
                "Icon":     "http://www.radioaurora.am/images/white_logo.png",
                "Email":    "radioaurora@radioaurora.am",
                "Country":  "Armenia",
                "Address":  "Yerevan, Nairi Zaryan 22, 0051",
                "Phone":    "+374-10-25-10-07",
                "Director": "",
                "WebPage":  "http://www.radioaurora.am/"
            },
            {
                "Name":     "Radio AYP",
                "Url":      "http://stric6.streamakaci.com/radioayp.mp3",
                "Icon":     "http://radio-aypfm.com/images/bientot_en_direct.jpg",
                "Email":    "",
                "Country":  "France",
                "Address":  "41 rue des ecolses, 94140 Alfortville",
                "Phone":    "01-43-53-19-90",
                "Director": "",
                "WebPage":  "http://radio-aypfm.com/"
            },
            {
                "Name":     "Radio Hay (starfm)",
                "Url":      "http://mix.am:8000/starfm",
                "Icon":     "http://live.mix.am/templates/live/img/2.png",
                "Email":    "",
                "Country":  "Armenia",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://live.mix.am/"
            },
            {
                "Name":     "Radio Hay (mixfm)",
                "Url":      "http://mix.am:8000/mixfm",
                "Icon":     "http://live.mix.am/templates/live/img/3.png",
                "Email":    "",
                "Country":  "Armenia",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://live.mix.am/"
            },
            {
                "Name":     "Radio Hay (Hay FM)",
                "Url":      "http://mix.am:8000/radiohyfm",
                "Icon":     "http://live.mix.am/templates/live/img/4.png",
                "Email":    "",
                "Country":  "Armenia",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://live.mix.am/"
            },
            {
                "Name":     "Radio Hay (Anr)",
                "Url":      "http://mix.am:8000/anr24",
                "Icon":     "http://live.mix.am/templates/live/img/5.png",
                "Email":    "",
                "Country":  "Arcax",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://live.mix.am/"
            },
            {
                "Name":     "Radio Hay (Smile)",
                "Url":      "http://mix.am:8000/smile",
                "Icon":     "http://live.mix.am/templates/live/img/6.png",
                "Email":    "",
                "Country":  "Armenia",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://live.mix.am/"
            },
            {
                "Name":     "Radio Hay (5 achok)",
                "Url":      "http://mix.am:8000/5achok",
                "Icon":     "",
                "Email":    "",
                "Country":  "Armenia",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://live.mix.am/"
            },
            {
                "Name":     "Radio Hay(Yerevan)",
                "Url":      "http://mix.am:8000/rhyerevan",
                "Icon":     "",
                "Email":    "",
                "Country":  "Armenia",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://radiohay.am/"
            },
            {
                "Name":     "Radio Jan",
                "Url":      "http://streams4.museter.com:8216/",
                "Icon":     "http://www.arm-radio.com/wp-content/uploads/2014/02/radio-jan-logo.png",
                "Email":    "info@radiojan.am",
                "Country":  "Armenia",
                "Address":  "",
                "Phone":    "+374-96-01-08-55",
                "Director": "",
                "WebPage":  "http://www.radiojan.am/"
            },
            {
                "Name":     "Radio Jazz",
                "Url":      "http://radiojazz.am/wp-content/themes/ari/mp3Player2.sw",
                "Icon":     "http://radiojazz.am/wp-content/themes/ari/images/logo.png",
                "Email":    "",
                "Country":  "Armenia",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://radiojazz.am/"
            },
            {
                "Name":     "Radio Toot",
                "Url":      "http://87.117.201.159:8110/",
                "Icon":     "http://radiotoot.com/eng/wp-content/uploads/2013/06/logosmall32.png",
                "Email":    "",
                "Country":  "Armenia",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://radiotoot.com/"
            },
            {
                "Name":     "Radio Sevan",
                "Url":      "http://sevan.bitwize.me:8018/",
                "Icon":     "http://cdn9.staztic.com/app/a/991/991430/radio-sevan-live-1-0-s-156x156.jpg",
                "Email":    "",
                "Country":  "Lebanon",
                "Address":  "Beirut, Khatchadurian Street, Khederlarian Building, Ground Floor",
                "Phone":    "+961-1-567161/2/3",
                "Director": "",
                "WebPage":  "http://www.radiosevan.com/"
            },
            {
                "Name":     "Radio Van",
                "Url":      "http://radiovan.am:8000/32_stereo",
                "Icon":     "http://www.radiovan.am/assets/pictures/logo.png",
                "Email":    "radiovan@radiovan.am",
                "Country":  "Armenia",
                "Address":  "Yerevan, Xandjyan 13a",
                "Phone":    "+374-10-54-00-01",
                "Director": "",
                "WebPage":  "http://radiovan.am"
            },
            {
                "Name":     "Radio YAN ARMENIAN",
                "Url":      "http://5.35.246.210:8000/stream",
                "Icon":     "http://www.imarmenian.com/association2/wp-content/uploads/2011/11/radioyan-300x97.jpg",
                "Email":    "radioyan@imarmenian.com",
                "Country":  "France",
                "Address":  "Maraash Street, Harboyan Building, 1203 Bourj Hammoud, Al-Metn, Lebanon",
                "Phone":    "+961-3-274-847",
                "Director": "",
                "WebPage":  "http://www.radioyan.com/"
            },
            {
                "Name":     "Radio YAN FOLK",
                "Url":      "http://5.35.246.210:8002/stream",
                "Icon":     "http://old.hooys.com/banasdeghzootyoon/55_P20_Dare_Zadooroghli_a.jpg",
                "Email":    "radioyan@imarmenian.com",
                "Country":  "France",
                "Address":  "Maraash Street, Harboyan Building, 1203 Bourj Hammoud, Al-Metn, Lebanon",
                "Phone":    "+961-3-274-847",
                "Director": "",
                "WebPage":  "http://www.radioyan.com/"
            },
            {
                "Name":     "Radio Yeraz",
                "Url":      "http://50.7.173.162:8233/",
                "Icon":     "http://radioyeraz.com/yeraz/wp-content/uploads/2013/12/radiologo.png",
                "Email":    "radioyan@imarmenian.com",
                "Country":  "",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://radioyeraz.com/"
            },
            {
                "Name":     "Trik Trak",
                "Url":      "http://64.118.88.39:8010/",
                "Icon":     "http://triktrak.ca/wp-content/uploads/2011/09/triklogo31.jpg",
                "Email":    "",
                "Country":  "",
                "Address":  "",
                "Phone":    "",
                "Director": "",
                "WebPage":  "http://triktrak.ca/"
            },
             {
                "Name":     "Vem Radio",
                "Url":      "http://vem.am//upload/February_Musical%20pearls_1361952495544.mp3",
                "Icon":     "http://www.vem.am/img/logo_pop.gifg",
                "Email":    "",
                "Country":  "Armenia",
                "Address":  "19 Koriun Street,Yerevan 0009",
                "Phone":    "+374-10-54-15-95",
                "Director": "",
                "WebPage":  "http://www.vem.am/"
            },
            {
                "Name":     "Voice of Van",
                "Url":      "http://www.voiceofvan.net/player/player.swf",
                "Icon":     "http://www.voiceofvan.net/sites/all/themes/layout6/images/header-object.png",
                "Email":    "",
                "Country":  "Lebanon",
                "Address":  "",
                "Phone":    "+961-1-241-199 ",
                "Director": "",
                "WebPage":  "http://www.voiceofvan.net/"
            },
            {
                "Name":     "Yerevan Nights",
                "Url":      "mms://radio.yerevannights.com/YerevanNights",
                "Icon":     "http://t2.gstatic.com/images?q=tbn:ANd9GcT_gI2q43Rgxs0Exa6JcZr9X3usmX5fGs2Do6_JDDmSrJ2sva3o",
                "Email":    "info@yerevannights.com",
                "Country":  "USA",
                "Address":  "3200 Wilshire Blvd. Ste 902NT, Los Angeles, CA, United States 90010",
                "Phone":    "+1-877-220-8951",
                "Director": "",
                "WebPage":  "http://www.yerevannights.com/"
            }
    ]
    resp.sort(key=operator.itemgetter(sortingKey))
    return resp

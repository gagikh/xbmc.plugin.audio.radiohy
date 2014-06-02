
# returns the current list of known stations

def getStations():
    #{
    #    "Name":"HayFM",
    #    "Url":"http://hayfm.am:8000/",
    #    "Icon":""
    #},
    resp = [
            {
                "Name":     "Ar Radio Intercontinental",
                "Url":      "http://199.195.194.92:8029",
                "Icon":     "http://www.arradio.am/images/m_01.gif",
                "Email":    "aa@arradio.am",
                "Country":  "Armenia",
                "Phone":    "+374-10-55-11-43",
                "WebPage":  "http://www.arradio.am"
            },
            {
                "Name":     "Armenian Christian Radio",
                "Url":      "http://fire.wavestreamer.com:5643",
                "Icon":     "http://bashde.org/images/logo-4e.png",
                "Email":    "info@bashde.org",
                "Country":  "",
                "Phone":    "",
                "WebPage":  "http://bashde.org/"
            },
            {
                "Name":     "Armenian Patriotic Radio",
                "Url":      "http://5.35.246.210:8001/stream",
                "Icon":     "http://www.imarmenian.com/association2/wp-content/uploads/2011/12/ARF-Logo-Red.png",
                "Email":    "radioyan@imarmenian.com",
                "Country":  "France",
                "Phone":    "+961-3-274-847",
                "WebPage":  "http://radioyan.com/"
            },
            {
                "Name":     "Armenian Pulse Radio",
                "Url":      "http://50.7.96.210:8134/",
                "Icon":     "http://www.armenianpulse.com/wp-content/themes/eGamer/images/radiopage/pulse_radio.jpg",
                "Email":    "content@armenianpulse.com",
                "Country":  "",
                "Phone":    "",
                "WebPage":  "http://www.armenianpulse.com/"
            },
            {
                "Name":     "Lav Radio(FM-107)",
                "Url":      "http://streams4.museter.com:8218/",
                "Icon":     "http://www.fm107.am/images/logo.jpg",
                "Email":    "",
                "Country":  "Armenia",
                "Phone":    "+374-10-36-86-45",
                "WebPage":  "http://www.fm107.am/"
            },
            {
                "Name":     "Nor Radyo",
                "Url":      "http://norradyo.com:8000/live",
                "Icon":     "http://www.ermenikultur.org/wp-content/uploads/2013/10/Nor_Radyo__g_rsel.jpg",
                "Email":    "",
                "Country":  "Turkey",
                "Phone":    "",
                "WebPage":  "http://www.norradyo.com/"
            },
            {
                "Name":     "Radio A",
                "Url":      "http://91.121.62.121:7250/",
                "Icon":     "http://votreradiosurlenet.com/player/img/radioa.gif",
                "Email":    "radio.a@wanadoo.fr",
                "Country":  "France",
                "Phone":    "00-33-4-75-56-18-33",
                "WebPage":  "http://radioa.net/"
            },
            {
                "Name":     "Radio Aga",
                "Url":      "http://50.7.77.114:8111/autodj",
                "Icon":     "http://www.armenianvoice.com/SiteImages/ArmenianVoice.jpg",
                "Email":    "info@Armenianvoice.com",
                "Country":  "",
                "Phone":    "",
                "WebPage":  "http://www.armenianvoice.com/"
            },
            {
                "Name":     "Radio Arax",
                "Url":      "http://radioarmenie.relay-network.com:8032/",
                "Icon":     "http://www.radioarax.com/logo.jpg",
                "Email":    "armenia@adinet.com.uy",
                "Country":  "Uruguay",
                "Phone":    "+598-90-09-69-09",
                "WebPage":  "http://www.radioarax.com/"
            },
            {
                "Name":     "Radio Arc",
                "Url":      "http://radioarc.serverroom.us:4082",
                "Icon":     "http://www.radioarc.com/images/logo-anim.gif",
                "Email":    "info@radioarc.com",
                "Country":  "",
                "Phone":    "",
                "WebPage":  "http://www.radioarc.com/"
            },
            {
                "Name":     "Radio Armenie",
                "Url":      "http://radioarmenie.relay-network.com:8032/",
                "Icon":     "http://www.radioarmenie.com/templates/theme475/images/logo.gif",
                "Email":    "",
                "Country":  "France",
                "Phone":    "04-78-49-52-74",
                "WebPage":  "http://www.radioarmenie.com/"
            },
            {
                "Name":     "Radio AVOL",
                "Url":      "http://64.150.176.192:8250/stream",
                "Icon":     "http://radioavol.org/uploads/donates/donate1x1.png",
                "Email":    "info@radioavol.org",
                "Country":  "Lebanon",
                "Phone":    "",
                "WebPage":  "http://radioavol.org/"
            },
            {
                "Name":     "Radio Avrora",
                "Url":      "http://www.radioaurora.am/hdvideo/",
                "Icon":     "http://www.radioaurora.am/images/white_logo.png",
                "Email":    "radioaurora@radioaurora.am",
                "Country":  "Armenia",
                "Phone":    "+374-10-25-10-07",
                "WebPage":  "http://www.radioaurora.am/"
            },
            {
                "Name":     "Radio AYP",
                "Url":      "http://stric6.streamakaci.com/radioayp.mp3",
                "Icon":     "http://radio-aypfm.com/images/bientot_en_direct.jpg",
                "Email":    "",
                "Country":  "France",
                "Phone":    "01-43-53-19-90",
                "WebPage":  "http://radio-aypfm.com/"
            },
            {
                "Name":     "NOP",
                "Url":      "http://ws.irib.ir/player/mediaplayer/player.swf",
                "Icon":     "NOP",
                "Email":    "NOP",
                "Country":  "NOP",
                "Phone":    "NOP",
                "WebPage":  "http://armenianradioboston.com/"
            },
            {
                "Name":     "Radio Hay (5 achok)",
                "Url":      "http://mix.am:8000/5achok",
                "Icon":     "",
                "Email":    "",
                "Country":  "Armenia",
                "Phone":    "",
                "WebPage":  "http://live.mix.am/"
            },
            {
                "Name":     "Radio Hay(Yerevan)",
                "Url":      "http://mix.am:8000/rhyerevan",
                "Icon":     "",
                "Email":    "",
                "Country":  "Armenia",
                "Phone":    "",
                "WebPage":  "http://radiohay.am/"
            },
            {
                "Name":     "Radio Jan",
                "Url":      "http://streams4.museter.com:8216/",
                "Icon":     "http://www.arm-radio.com/wp-content/uploads/2014/02/radio-jan-logo.png",
                "Email":    "info@radiojan.am",
                "Country":  "Armenia",
                "Phone":    "+374-96-01-08-55",
                "WebPage":  "http://www.radiojan.am/"
            },
            {
                "Name":     "Radio Jazz",
                "Url":      "NOP",
                "Icon":     "http://radiojazz.am/wp-content/themes/ari/images/logo.png",
                "Email":    "",
                "Country":  "Armenia",
                "Phone":    "",
                "WebPage":  "http://radiojazz.am/"
            },
            {
                "Name":     "Radio Toot",
                "Url":      "http://87.117.201.159:8110/",
                "Icon":     "http://radiotoot.com/eng/wp-content/uploads/2013/06/logosmall32.png",
                "Email":    "",
                "Country":  "Armenia",
                "Phone":    "",
                "WebPage":  "http://radiotoot.com/"
            },
            {
                "Name":     "Radio Sevan",
                "Url":      "http://sevan.bitwize.me:8018/",
                "Icon":     "http://cdn9.staztic.com/app/a/991/991430/radio-sevan-live-1-0-s-156x156.jpg",
                "Email":    "",
                "Country":  "Beirut",
                "Phone":    "+961-1-567161/2/3",
                "WebPage":  "http://www.radiosevan.com/"
            },
            {
                "Name":     "Radio Van",
                "Url":      "http://radiovan.am:8000/32_stereo",
                "Icon":     "http://www.radiovan.am/assets/pictures/logo.png",
                "Email":    "radiovan@radiovan.am",
                "Country":  "Armenia",
                "Phone":    "+374-10-54-00-01",
                "WebPage":  "http://radiovan.am"
            },
            {
                "Name":     "Radio YAN ARMENIAN",
                "Url":      "http://5.35.246.210:8000/stream",
                "Icon":     "http://www.imarmenian.com/association2/wp-content/uploads/2011/11/radioyan-300x97.jpg",
                "Email":    "radioyan@imarmenian.com",
                "Country":  "France",
                "Phone":    "+961-3-274-847",
                "WebPage":  "http://www.radioyan.com/"
            },
            {
                "Name":     "Radio YAN FOLK",
                "Url":      "http://5.35.246.210:8002/stream",
                "Icon":     "http://old.hooys.com/banasdeghzootyoon/55_P20_Dare_Zadooroghli_a.jpg",
                "Email":    "radioyan@imarmenian.com",
                "Country":  "France",
                "Phone":    "+961-3-274-847",
                "WebPage":  "http://www.radioyan.com/"
            },
            {
                "Name":     "Radio Yeraz",
                "Url":      "http://50.7.173.162:8233/",
                "Icon":     "http://radioyeraz.com/yeraz/wp-content/uploads/2013/12/radiologo.png",
                "Email":    "radioyan@imarmenian.com",
                "Country":  "Armenia",
                "Phone":    "",
                "WebPage":  "http://radioyeraz.com/"
            },
            {
                "Name":     "Voice of Van",
                "Url":      "http://www.voiceofvan.net/player/player.swf",
                "Icon":     "http://www.voiceofvan.net/sites/all/themes/layout6/images/header-object.png",
                "Email":    "",
                "Country":  "Lebanon",
                "Phone":    "+961-1-241-199 ",
                "WebPage":  "http://www.voiceofvan.net/"
            },
            {
                "Name":     "Yerevan Nights",
                "Url":      "mms://radio.yerevannights.com/YerevanNights",
                "Icon":     "http://t2.gstatic.com/images?q=tbn:ANd9GcT_gI2q43Rgxs0Exa6JcZr9X3usmX5fGs2Do6_JDDmSrJ2sva3o",
                "Email":    "info@yerevannights.com",
                "Country":  "Armenia",
                "Phone":    "",
                "WebPage":  "http://www.yerevannights.com/"
            }
    ]
    return resp


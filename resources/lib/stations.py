
# returns the current list of known stations
import operator

# TODO: verify stations
#{
#    "Name":"HayFM",
#    "Url":"http://hayfm.am:8000/",
#    "Icon":""
#},
#cityfm, http://www.cityfm.am/
#radio vem, http://www.vem.am/

# crontab TIME format: 
# * * * * * *
# | | | | | | 
# | | | | | +-- Year              (range: 1900-3000)
# | | | | +---- Day of the Week   (range: 1-7, 1 standing for Monday)
# | | | +------ Month of the Year (range: 1-12)
# | | +-------- Day of the Month  (range: 1-31)
# | +---------- Hour              (range: 0-23)
# +------------ Minute            (range: 0-59)

def getStations(sortingKey):
    resp = [
            {
                # Thursday 8:00pm to 9:00pm, duration 1h
                "Address":  "21 Smith Street Fitzroy 3065,Melbourne",
                "Country":  "Australia",
                "Director": "James McKenzie",
                "Email":    "stationmanager@3cr.org.au",
                "Icon":     "http://www.3cr.org.au/sites/default/files/images/building/3crfront_light.jpg",
                "Name":     "3CR",
                "Phone":    "(03) 9419 0155",
                "Time":     "[[[0,20,4,-1,-1,-1],[0,21,4,-1,-1,-1]]]",
                "Url":      "",
                "WebPage":  "http://www.3cr.org.au/armenian"
                },
            {
                # Tuesday 5:00pm to 6:00pm, duration 1h, Tuesday 8:00pm to 9:00pm, duration 1h
                "Address":  "Sydney, Locked Bag 028,Crows Nest, NSW 1585",
                "Country":  "Australia",
                "Director": "",
                "Email":    "armenian.program@sbs.com.au",
                "Icon":     "http://www.sbs.com.au/sales/resize/index/id/252/w/294/h/220/",
                "Name":     "SBS Radio",
                "Phone":    "(02) 9430 2828",
                "Time":     "[[[[0,17,2,-1,-1,-1],[0,18,2,-1,-1,-1]],[[0,20,2,-1,-1,-1],[0,21,2,-1,-1,-1]]]]",
                "Url":      "",
                "WebPage":  "http://www.sbs.com.au/yourlanguage/armenian/"
                },
            {
                # 17:00pm to 18:00pm, duration 1H
                "Address":  "1397 Nicosia, Cyprus",
                "Country":  "Cyprus",
                "Director": "",
                "Email":    "armenian@cybc.com.cy",
                "Icon":     "",
                "Name":     "",
                "Phone":    "+357 22862000",
                "Time":     "[[[0,17,-1,-1,-1,-1],[0,18,-1,-1,-1,-1]]]",
                "Url":      "",
                "WebPage":  "http://www.cybc.com.cy"
                },
            {
                # not defined
                "Address":  "",
                "Country":  "Hungary",
                "Director": "",
                "Email":    "huttereri@yahoo.com",
                "Icon":     "",
                "Name":     "",
                "Phone":    "361 302 809 767",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "",
                "WebPage":  ""
                },
            {
                "Address":  "",
                "Country":  "Hungary",
                "Director": "",
                "Email":    "eranyak.oganova@gmail.com",
                "Icon":     "",
                "Name":     "",
                "Phone":    "0036 20 378 47 96",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "",
                "WebPage":  "http://bolgar.radio.hu/"
                },
            {
                "Address":  "",
                "Country":  "Germany",
                "Director": "",
                "Email":    "Aram_a@msn.com",
                "Icon":     "http://www.hayfm.de/wp-content/uploads/2013/03/slider-3-914x374.jpg",
                "Name":     "Hay FM",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "",
                "WebPage":  "http://www.hayfm.de/"
                },
            {
                "Address":  "",
                "Country":  "Vatikan",
                "Director": "",
                "Email":    "",
                "Icon":     "http://hy.radiovaticana.va/img/h_02.gif",
                "Name":     "Voice of Vatikan",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "",
                "WebPage":  "http://www.radiovaticana.org/arm/index.asp"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "",
                "Icon":     "http://www.am680.com.ar/images/RM1.jpg",
                "Name":     "Voice of Vatikan",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "",
                "WebPage":  "http://www.am680.com.ar/"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "",
                "Icon":     "http://www.amerikayidzayn.com/App_Themes/VOA_hy-AM-VOA/img/top_logo.gif",
                "Name":     "Voice of Amerika",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "",
                "WebPage":  "http://www.amerikayidzayn.com/"
                },
            { # verified
                "Address":  "0025 Yerevan, Alex Manoogian 5 str",
                "Country":  "Armenia",
                "Director": "Armen Amiryan",
                "Email":    "aa@arradio.am",
                "Icon":     "http://www.arradio.am/images/m_01.gif",
                "Name":     "Ar Radio Intercontinental",
                "Phone":    "+374-10-55-11-43",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://199.195.194.92:8029",
                "WebPage":  "http://www.arradio.am"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "feedback@armenianbiblestudy.com",
                "Icon":     "http://www.armenianbiblestudy.com/img/abslogo.png",
                "Name":     "Armenian Bible Study",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://sc7.mystreamserver.com:8036/",
                "WebPage":  "http://www.armenianbiblestudy.com/"
                },
            {
                "Address":  "405 Waltham St. Lexington, MA 02421-7954",
                "Country":  "USA",
                "Director": "",
                "Email":    "info@bashde.org",
                "Icon":     "http://bashde.org/images/logo-4e.png",
                "Name":     "Armenian Christian Radio",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://fire.wavestreamer.com:5643",
                "WebPage":  "http://bashde.org/"
                },
            {
                "Address":  "Los Angeles, California",
                "Country":  "USA",
                "Director": "",
                "Email":    "",
                "Icon":     "http://armenianglobalradio.com/wp-content/themes/agrtheme/images/header1.jpg",
                "Name":     "Armenian Global Radio",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://50.7.77.114:8304/",
                "WebPage":  "http://armenianglobalradio.com/"
                },
            {
                "Address":  "PO Box 46, Watertown, Massachusetts 02471",
                "Country":  "USA",
                "Director": "Yevgine Gharibian",
                "Email":    "Yevgine@aol.com",
                "Icon":     "http://armenianradioboston.com/images/ABB-Bannerad.jpg",
                "Name":     "Armenian Independent Broadcasting of Boston",
                "Phone":    "+1-617-926-6268",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://armenianradioboston.com/audio/player.swf",
                "WebPage":  "http://armenianradioboston.com/"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "",
                "Icon":     "http://www.armnetradio.com/images/logosmall.png",
                "Name":     "Armenian Net Radio",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://50.117.8.242:1126/Live",
                "WebPage":  "http://www.armnetradio.com/"
                },
            {
                "Address":  "Maraash Street, Harboyan Building, 1203 Bourj Hammoud, Al-Metn, Lebanon",
                "Country":  "France",
                "Director": "",
                "Email":    "radioyan@imarmenian.com",
                "Icon":     "http://www.imarmenian.com/association2/wp-content/uploads/2011/12/ARF-Logo-Red.png",
                "Name":     "Armenian Patriotic Radio",
                "Phone":    "+961-3-274-847",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://5.35.246.210:8001/stream",
                "WebPage":  "http://radioyan.com/"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "Harout Kalandjian",
                "Email":    "content@armenianpulse.com",
                "Icon":     "http://www.armenianpulse.com/wp-content/themes/eGamer/images/radiopage/pulse_radio.jpg",
                "Name":     "Armenian Pulse Radio",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://50.7.96.210:8134/",
                "WebPage":  "http://www.armenianpulse.com/"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "info@Armenianvoice.com",
                "Icon":     "http://www.armenianvoice.com/SiteImages/ArmenianVoice.jpg",
                "Name":     "Armenian Voice",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://50.7.77.114:8111/autodj",
                "WebPage":  "http://www.armenianvoice.com/"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "",
                "Icon":     "http://crazyradiyo.listen2myshow.com/bannerimages/567/93/022931984224filebaner.jpg",
                "Name":     "Crazy Radio Armenia",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "",
                "WebPage":  "http://crazyradio.do.am/"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "",
                "Icon":     "http://www.fm107.am/images/logo.jpg",
                "Name":     "Lav Radio(FM-107)",
                "Phone":    "+374-10-36-86-45",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://streams4.museter.com:8218/",
                "WebPage":  "http://www.fm107.am/"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "info@lavradio.am",
                "Icon":     "http://www.lavradio.am/img/big_logo.png",
                "Name":     "Lav Radio Mix",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://195.154.181.100:8000/stream",
                "WebPage":  "http://www.lavradio.am/"
                },
            {
                "Address":  "",
                "Country":  "Turkey",
                "Director": "",
                "Email":    "info@norradyo.com",
                "Icon":     "http://www.ermenikultur.org/wp-content/uploads/2013/10/Nor_Radyo__g_rsel.jpg",
                "Name":     "Nor Radyo",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://norradyo.com:8000/live",
                "WebPage":  "http://www.norradyo.com/"
                },
            {
                "Address":  "Yerevan 25, Aleq Manukyan 5",
                "Country":  "Armenia",
                "Director": "Armen Amiryan",
                "Email":    "aa@arradio.am",
                "Icon":     "http://www.armradio.am/hy/wp-content/uploads/2012/09/logo_up_arm.png",
                "Name":     "Public Radio of Armenia",
                "Phone":    "+374-10-55-11-43",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://195.154.181.100:8052/",
                "WebPage":  "http://www.armradio.am/"
                },
            {
                "Address":  "32 rue Pompery, 26500 Bourg-les-Valence",
                "Country":  "France",
                "Director": "",
                "Email":    "radio.a@wanadoo.fr",
                "Icon":     "http://votreradiosurlenet.com/player/img/radioa.gif",
                "Name":     "Radio A",
                "Phone":    "00-33-4-75-56-18-33",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://91.121.62.121:7250/",
                "WebPage":  "http://radioa.net/"
                },
            {
                "Address":  "Frunze 13, Yerevan, Armenia",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "ardzagank@ardzagank.com",
                "Icon":     "http://www.ardzagank.com/img/logo_3.jpg",
                "Name":     "Radio Ardzaganq",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://de1.fananoon.com:7000",
                "WebPage":  "http://www.ardzagank.com/"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "atendimento@armeniaeterna.com.br",
                "Icon":     "",
                "Name":     "Radio Armenia Eterna",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "",
                "WebPage":  "http://armeniaeterna.com.br/"
                },
            {
                "Address":  "375010, Yerevan, Tigran Mec 17",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "",
                "Icon":     "http://www.radiofama.am/wp-content/uploads/lg8.png",
                "Name":     "Radio Fama",
                "Phone":    "+3741-59-70-00",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://195.154.181.100:8036/",
                "WebPage":  "http://radiofama.am"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "",
                "Icon":     "",
                "Name":     "Radio Gayan",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://radiogayan.com:8000",
                "WebPage":  "http://radiogayan.com/"
                },
            {
                "Address":  "",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "http://static.wixstatic.com/media/9badce_2edb315888ac483287408d2d6d0d3d48.jpg_srz_p_171_87_75_22_0.50_1.20_0.00_jpg_srz",
                "Icon":     "http://d1i6vahw24eb07.cloudfront.net/s195991q.png",
                "Name":     "Radio Spyurq",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://192.184.9.79:8174/",
                "WebPage":  "http://www.radiospurk.com/"
                },
            {
                "Address":  "",
                "Country":  "Uruguay",
                "Director": "",
                "Email":    "armenia@adinet.com.uy",
                "Icon":     "http://www.radioarax.com/logo.jpg",
                "Name":     "Radio Arax",
                "Phone":    "+598-90-09-69-09",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://www.radioarax.com/programas/RadioArax-727-DO-20140601.mp3",
                "WebPage":  "http://www.radioarax.com/"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "info@radioarc.com",
                "Icon":     "http://www.radioarc.com/images/logo-anim.gif",
                "Name":     "Radio Arc",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://radioarc.serverroom.us:4082",
                "WebPage":  "http://www.radioarc.com/"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "info@armenianmusic.com",
                "Icon":     "http://radioarmenia.com/radio2/images/small_logo.jpg",
                "Name":     "Radio Armenia",
                "Phone":    "+323-664-3365",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://radioarmenia.com/radio2/radio.swf",
                "WebPage":  "http://radioarmenia.com/"
                },
            {
                "Address":  "4 rue Marcellin Berthelot 69150 DECINES FRANCE",
                "Country":  "France",
                "Director": "",
                "Email":    "",
                "Icon":     "http://www.radioarmenie.com/templates/theme475/images/logo.gif",
                "Name":     "Radio Armenie",
                "Phone":    "04-78-49-52-74",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://radioarmenie.relay-network.com:8032/",
                "WebPage":  "http://www.radioarmenie.com/"
                },
            {
                "Address":  "",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "info@radioavol.org",
                "Icon":     "http://radioavol.org/uploads/donates/donate1x1.png",
                "Name":     "Radio AVOL",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://64.150.176.192:8250/stream",
                "WebPage":  "http://radioavol.org/"
                },
            {
                "Address":  "Yerevan, Nairi Zaryan 22, 0051",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "radioaurora@radioaurora.am",
                "Icon":     "http://www.radioaurora.am/images/white_logo.png",
                "Name":     "Radio Avrora",
                "Phone":    "+374-10-25-10-07",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://www.radioaurora.am/hdvideo/",
                "WebPage":  "http://www.radioaurora.am/"
                },
            {
                "Address":  "41 rue des ecolses, 94140 Alfortville",
                "Country":  "France",
                "Director": "",
                "Email":    "",
                "Icon":     "http://radio-aypfm.com/images/bientot_en_direct.jpg",
                "Name":     "Radio AYP",
                "Phone":    "01-43-53-19-90",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://stric6.streamakaci.com/radioayp.mp3",
                "WebPage":  "http://radio-aypfm.com/"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "",
                "Icon":     "http://live.mix.am/templates/live/img/2.png",
                "Name":     "Radio Hay (starfm)",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://mix.am:8000/starfm",
                "WebPage":  "http://live.mix.am/"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "",
                "Icon":     "http://live.mix.am/templates/live/img/3.png",
                "Name":     "Radio Hay (mixfm)",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://mix.am:8000/mixfm",
                "WebPage":  "http://live.mix.am/"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "",
                "Icon":     "http://live.mix.am/templates/live/img/4.png",
                "Name":     "Radio Hay (Hay FM)",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://mix.am:8000/radiohyfm",
                "WebPage":  "http://live.mix.am/"
                },
            {
                "Address":  "",
                "Country":  "Arcax",
                "Director": "",
                "Email":    "",
                "Icon":     "http://live.mix.am/templates/live/img/5.png",
                "Name":     "Radio Hay (Anr)",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://mix.am:8000/anr24",
                "WebPage":  "http://live.mix.am/"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "",
                "Icon":     "http://live.mix.am/templates/live/img/6.png",
                "Name":     "Radio Hay (Smile)",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://mix.am:8000/smile",
                "WebPage":  "http://live.mix.am/"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "",
                "Icon":     "",
                "Name":     "Radio Hay (5 achok)",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://mix.am:8000/5achok",
                "WebPage":  "http://live.mix.am/"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "",
                "Icon":     "",
                "Name":     "Radio Hay(Yerevan)",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://mix.am:8000/rhyerevan",
                "WebPage":  "http://radiohay.am/"
                },
            {
                "Address":  "1617Colorado Blvd. Ste#2, Los Angeles, CA 90041",
                "Country":  "USA",
                "Director": "JOSEPH KRIKORIAN",
                "Email":    "josephkmusic@gmail.com",
                "Icon":     "http://www.josephkmusic.com/wp-content/themes/theme1418/images/logo.png",
                "Name":     "Radio Hayeren",
                "Phone":    "+1 818 355 0603",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://199.189.111.28:8303/stream",
                "WebPage":  "http://www.josephkmusic.com/"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "info@radiojan.am",
                "Icon":     "http://www.arm-radio.com/wp-content/uploads/2014/02/radio-jan-logo.png",
                "Name":     "Radio Jan",
                "Phone":    "+374-96-01-08-55",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://streams4.museter.com:8216/",
                "WebPage":  "http://www.radiojan.am/"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "",
                "Icon":     "http://radiojazz.am/wp-content/themes/ari/images/logo.png",
                "Name":     "Radio Jazz",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://radiojazz.am/wp-content/themes/ari/mp3Player2.sw",
                "WebPage":  "http://radiojazz.am/"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "",
                "Icon":     "http://radiotoot.com/eng/wp-content/uploads/2013/06/logosmall32.png",
                "Name":     "Radio Toot",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://87.117.201.159:8110/",
                "WebPage":  "http://radiotoot.com/"
                },
            {
                "Address":  "Beirut, Khatchadurian Street, Khederlarian Building, Ground Floor",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "",
                "Icon":     "http://cdn9.staztic.com/app/a/991/991430/radio-sevan-live-1-0-s-156x156.jpg",
                "Name":     "Radio Sevan",
                "Phone":    "+961-1-567161/2/3",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://sevan.bitwize.me:8018/",
                "WebPage":  "http://www.radiosevan.com/"
                },
            {
                "Address":  "Yerevan, Xandjyan 13a",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "radiovan@radiovan.am",
                "Icon":     "http://www.radiovan.am/assets/pictures/logo.png",
                "Name":     "Radio Van",
                "Phone":    "+374-10-54-00-01",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://radiovan.am:8000/32_stereo",
                "WebPage":  "http://radiovan.am"
                },
            {
                "Address":  "Maraash Street, Harboyan Building, 1203 Bourj Hammoud, Al-Metn, Lebanon",
                "Country":  "France",
                "Director": "",
                "Email":    "radioyan@imarmenian.com",
                "Icon":     "http://www.imarmenian.com/association2/wp-content/uploads/2011/11/radioyan-300x97.jpg",
                "Name":     "Radio YAN ARMENIAN",
                "Phone":    "+961-3-274-847",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://5.35.246.210:8000/stream",
                "WebPage":  "http://www.radioyan.com/"
                },
            {
                "Address":  "Maraash Street, Harboyan Building, 1203 Bourj Hammoud, Al-Metn, Lebanon",
                "Country":  "France",
                "Director": "",
                "Email":    "radioyan@imarmenian.com",
                "Icon":     "http://old.hooys.com/banasdeghzootyoon/55_P20_Dare_Zadooroghli_a.jpg",
                "Name":     "Radio YAN FOLK",
                "Phone":    "+961-3-274-847",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://5.35.246.210:8002/stream",
                "WebPage":  "http://www.radioyan.com/"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "radioyan@imarmenian.com",
                "Icon":     "http://radioyeraz.com/yeraz/wp-content/uploads/2013/12/radiologo.png",
                "Name":     "Radio Yeraz",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://50.7.173.162:8233/",
                "WebPage":  "http://radioyeraz.com/"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "",
                "Icon":     "http://triktrak.ca/wp-content/uploads/2011/09/triklogo31.jpg",
                "Name":     "Trik Trak",
                "Phone":    "",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://64.118.88.39:8010/",
                "WebPage":  "http://triktrak.ca/"
                },
            {
                "Address":  "19 Koriun Street,Yerevan 0009",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "",
                "Icon":     "http://www.vem.am/img/logo_pop.gifg",
                "Name":     "Vem Radio",
                "Phone":    "+374-10-54-15-95",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://vem.am//upload/February_Musical%20pearls_1361952495544.mp3",
                "WebPage":  "http://www.vem.am/"
                },
            {
                "Address":  "",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "",
                "Icon":     "http://www.voiceofvan.net/sites/all/themes/layout6/images/header-object.png",
                "Name":     "Voice of Van",
                "Phone":    "+961-1-241-199 ",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "http://www.voiceofvan.net/player/player.swf",
                "WebPage":  "http://www.voiceofvan.net/"
                },
            {
                "Address":  "3200 Wilshire Blvd. Ste 902NT, Los Angeles, CA, United States 90010",
                "Country":  "USA",
                "Director": "",
                "Email":    "info@yerevannights.com",
                "Icon":     "http://t2.gstatic.com/images?q=tbn:ANd9GcT_gI2q43Rgxs0Exa6JcZr9X3usmX5fGs2Do6_JDDmSrJ2sva3o",
                "Name":     "Yerevan Nights",
                "Phone":    "+1-877-220-8951",
                "Time":     "[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]]",
                "Url":      "mms://radio.yerevannights.com/YerevanNights",
                "WebPage":  "http://www.yerevannights.com/"
                }
            ]
    resp.sort(key=operator.itemgetter(sortingKey))
    return resp

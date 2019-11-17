
# returns the current sorted list of known stations
import operator

# TODO: verify stations
#{
#    "Name":"HayFM",
#    "Url":"http://hayfm.am:8000/",
#    "Icon":""
#},

#cityfm, http://www.cityfm.am/
#radio alpha
#Armenian radio of New Jersi, http://www.armenianradionj.net/
#radiomayak
#"Name":     "Lounge Radio Yerevan",
#"http://www.acabc.ca/radio-show"

# crontab TIME format: 
# MIN HOUR DOM MON DOW CMD - "* * * * *"

def getStations(sortingKey):
    resp = [
    	   {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "",
                "Icon":     "",
                "Name":     "",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "",
                "Verified": "",
                "Video":    "false",
                "WebPage":  ""
                },
    	   {
                "Address":  "Yerevan",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "support@armtv.com",
                "Icon":     "https://www.1tv.am/img/fb-share.png",
                "Name":     "H1",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "https://amtv1.livestreamingcdn.com/am1abr/index.m3u8",
                "Verified": "true",
                "Video":    "true",
                "WebPage":  "https://www.1tv.am/hy/"
                },
    	   {
                "Address":  "",
                "Country":  "Lebanon",
                "Director": "Kegham Depoyan",
                "Email":    "info@radioarev.com",
                "Icon":     "http://www.radioarev.com/images/logo/radioarev.png",
                "Name":     "Radio Arev",
                "Phone":    "+9613466270",
                "Schedule": "* * * * *",
                "Url":      "http://64.150.176.42:8013/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.radioarev.com"
                },
    	   {
                "Address":  "Beirut",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "info@yeridasartoutiantsayn.com",
                "Icon":     "http://yeridasartoutiantsayne.com/img/background/top_banner.png",
                "Name":     "Yeridasartoutyan Tsayny",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "http://199.189.111.28:8023/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://yeridasartoutiantsayne.com/"
                },
    	   {
                "Address":  "Yerevan, Nairi Zaryan 22, 7/9, 0051",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "radioaurora@radioaurora.am",
                "Icon":     "http://www.radioaurora.am/wp-content/themes/auroratwo/images/logo_1.png",
                "Name":     "Radio Aurora",
                "Phone":    "+37410 251007",
                "Schedule": "* * * * *",
                "Url":      "http://138.201.84.106:8050",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.radioaurora.am"
                },
            {
                "Address":  "",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "radioayk@gmail.com",
                "Icon":     "http://d1i6vahw24eb07.cloudfront.net/s160811q.png",
                "Name":     "Radio AYK",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "http://s3.streammonster.com:8117/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.radioayk.com"
                },
            {
                # verified
                "Address":  "0025 Yerevan, Alex Manoogian 5 str",
                "Country":  "Armenia",
                "Director": "Armen Amiryan",
                "Email":    "aa@arradio.am",
                "Icon":     "http://www.arradio.am/images/m_01.gif",
                "Name":     "Ar Radio Intercontinental",
                "Phone":    "+374-10-55-11-43",
                "Schedule": "* * * * *",
                "Url":      "http://199.195.194.92:8029",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.yerevanfm.am/"
                },
            {
                "Address":  "405 Waltham St. Lexington, MA 02421-7954",
                "Country":  "USA",
                "Director": "",
                "Email":    "info@bashde.org",
                "Icon":     "https://cdn.onlineradiobox.com/img/logo/5/43015.v2.png",
                "Name":     "Armenian Christian Radio",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "https://streams.radio.co/sa0bf8ec29/listen",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://bashde.org"
                },
            {
                "Address":  "Yerevan, Qochar 21",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "impulse@impulse.am",
                "Icon":     "http://www.lratvakan.am/img/logo.png",
                "Name":     "Lratvakan Radio",
                "Phone":    "+374 60 37 12 73",
                "Schedule": "* * * * *",
                "Url":      "http://212.34.233.78:8000/live",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.lratvakan.am/"
                },
            { # verified!
                "Address":  "",
                "Country":  "Armenia",
                "Director": "Aghabek Margaryan",
                "Email":    "info@lavradio.am",
                "Icon":     "http://www.lavradio.am/wp-content/uploads/2017/02/logo-1.png",
                "Name":     "Lav Radio Mix",
                "Phone":    "+37455830003",
                "Schedule": "* * * * *",
                "Url":      "http://163.172.7.220:8006/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.lavradio.am"
                },
            { # verified!
                "Address":  "",
                "Country":  "Armenia",
                "Director": "Aghabek Margaryan",
                "Email":    "info@lavradio.am",
                "Icon":     "http://www.lavradio.am/wp-content/uploads/2017/02/logo-1.png",
                "Name":     "Lav Radio",
                "Phone":    "+37455830003",
                "Schedule": "* * * * *",
                "Url":      "http://163.172.7.220:8000/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.lavradio.am"
                },
            {
                "Address":  "",
                "Country":  "Turkey",
                "Director": "",
                "Email":    "info@norradyo.com",
                "Icon":     "http://www.ermenikultur.org/wp-content/uploads/2013/10/Nor_Radyo__g_rsel.jpg",
                "Name":     "Nor Radyo",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "http://norradyo.com:8000/live",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.norradyo.com"
                },
            {
                # verified!
                "Address":  "Yerevan 25, Aleq Manukyan 5",
                "Country":  "Armenia",
                "Director": "Armen Amiryan",
                "Email":    "aa@arradio.am",
                "Icon":     "http://www.armradio.am/hy/wp-content/uploads/2014/10/logo_hy.png",
                "Name":     "Public Radio of Armenia",
                "Phone":    "+374-10-55-11-43",
                "Schedule": "* * * * *",
                "Url":      "http://37.252.79.131:8000/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.armradio.am"
                },
            {
                "Address":  "4 rue Marcellin Berthelot 69150 DECINES",
                "Country":  "France",
                "Director": "",
                "Email":    "",
                "Icon":     "http://www.radioarmenie.com/images/logo-long.png",
                "Name":     "Radio Armenie",
                "Phone":    "04-78-49-52-74",
                "Schedule": "* * * * *",
                "Url":      "http://direct.radioarmenie.com:9029/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.radioarmenie.com"
                },
            {
                "Address":  "",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "info@radioavol.org",
                "Icon":     "http://www.arm-radio.com/wp-content/uploads/2016/07/radio-avol.png",
                "Name":     "Radio AVOL",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "http://199.189.111.28:8209/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://radioavol.org"
                },
            {
                "Address":  "41 rue des ecolses, 94140 Alfortville",
                "Country":  "France",
                "Director": "",
                "Email":    "",
                "Icon":     "http://radio-aypfm.com/images/bientot_en_direct.jpg",
                "Name":     "Radio AYP",
                "Phone":    "01-43-53-19-90",
                "Schedule": "* * * * *",
                "Url":      "http://stric6.streamakaci.com/radioayp.mp3",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://radio-aypfm.com"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "",
                "Icon":     "http://radiohay.am/wp-content/uploads/2018/12/Logo-urish-chapi.png",
                "Name":     "Radio Hay (Yerevan)",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "http://51.158.21.33:8000/radiohay",
                "Verified": "false",
                "Video":    "false",
                "WebPage":  "http://radiohay.am"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "info@radiojan.am",
                "Icon":     "http://www.radiojan.am/images/logo2new.png",
                "Name":     "Radio Jan",
                "Phone":    "+374-96-01-08-55",
                "Schedule": "* * * * *",
                "Url":      "http://s7.voscast.com:10258/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.radiojan.am"
                },
            {
                "Address":  "Beirut, Khatchadurian Street, Khederlarian Building, Ground Floor",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "",
                "Icon":     "http://www.radiosevan.com/resources/radiosevan/css/images/logo.png",
                "Name":     "Radio Sevan",
                "Phone":    "+961-1-567161/2/3",
                "Schedule": "* * * * *",
                "Url":      "http://sevan.bitwize.me:8018",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.radiosevan.com"
                },
            {
                "Address":  "",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "",
                "Icon":     "http://static.wixstatic.com/media/9badce_2edb315888ac483287408d2d6d0d3d48.jpg_srz_p_171_87_75_22_0.50_1.20_0.00_jpg_srz",
                "Name":     "Radio Spyurq",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "http://manager1.creativradio.pro:2690/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.radiospurk.com"
                },
            {
                "Address":  "Yerevan, Xandjyan 13a",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "radiovan@radiovan.am",
                "Icon":     "https://www.radiovan.fm/css/images/radiovan.svg",
                "Name":     "Radio Van",
                "Phone":    "+374-10-54-00-01",
                "Schedule": "* * * * *",
                "Url":      "https://stream.radiovan.fm:8000/96_stereo",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://radiovan.am"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "radioyan@imarmenian.com",
                "Icon":     "http://www.haykakanmusic.com/images/radio-yeraz.jpg",
                "Name":     "Radio Yeraz",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "http://149.255.59.164:8008/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://radioyeraz.com"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "",
                "Icon":     "http://triktrak.ca/wp-content/uploads/2011/09/triklogo31.jpg",
                "Name":     "Trik Trak",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "http://64.118.87.22:8003",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://triktrak.ca"
                },
            {
                "Address":  "19 Koriun Street,Yerevan 0009",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "",
                "Icon":     "http://www.vem.am/img/logo_pop.gif",
                "Name":     "Vem Radio",
                "Phone":    "+374-10-54-15-95",
                "Schedule": "* * * * *",
                "Url":      "http://vem.am//upload/February_Musical%20pearls_1361952495544.mp3",
                "Verified": "false",
                "Video":    "false",
                "WebPage":  "http://www.vem.am/"
                },
            {
                "Address":  "",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "",
                "Icon":     "http://voiceofvan.net/wp-content/uploads/2017/09/LOGO-23-1.png",
                "Name":     "Voice of Van",
                "Phone":    "+961-1-241-199 ",
                "Schedule": "* * * * *",
                "Url":      "http://23.92.21.22/vovan.mp3",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.voiceofvan.net/"
                },
            {
                # verified!
                "Address":  "3200 Wilshire Blvd. Ste 902NT, Los Angeles, CA, United States 90010",
                "Country":  "USA",
                "Director": "Sarkis Chakarian",
                "Email":    "info@yerevannights.com",
                "Icon":     "http://www.armenische-kirche.ch/wp-content/uploads/2013/02/yerevannights.jpg",
                "Name":     "Yerevan Nights",
                "Phone":    "+1-877-220-8951",
                "Schedule":"* * * * *",
                "Url":      "http://icecast.yerevannights.com:80/YerevanNights",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.yerevannights.com"
                }
            ]
    resp.sort(key=operator.itemgetter(sortingKey))
    return resp

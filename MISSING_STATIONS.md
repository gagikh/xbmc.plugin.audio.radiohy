# Missing / Unresolved Stations

Stations found during research but not yet added to `stations.json`.

---

## Stream URL not found (dynamic player)

| Station | Country | Website | Notes |
|---|---|---|---|
| Sputnik Armenia | Armenia | https://armeniasputnik.am | Stream hidden behind radioplayer.ru — open DevTools > Network while playing |
| Nor Radyo | Turkey | https://norradyo.com | Armenian/Turkish community radio — stream not exposed on site or zeno.fm |
| Azatutyun (RFE/RL) | Armenia | https://www.azatutyun.am | Radio Free Europe Armenian service — site returns 403 |
| Im Radio | Armenia | https://imradio.armradio.am | Official youth channel of Public Radio of Armenia — behind armradio.am player |
| Radio Arevik | Armenia | https://en.armradio.am | Children's channel of Public Radio of Armenia — behind armradio.am player |
| Radio Culture | Armenia | https://mshakuyt.armradio.am | Culture/classical channel of Public Radio of Armenia — behind armradio.am player |
| Radio Nshkhar | Armenia | https://artsakhdiocese.am/en/station/radio-nshkhar | Christian/educational, FM 107.5 Stepanakert — no stream found |
| KHSH FM | Armenia | https://khsh.fm | Funk/House/Jazz — no stream found |
| IMusic.am | Armenia | https://imusic.am | Armenian music streaming — no stream found |
| Radio Muzofan | Armenia | https://radio.muzofan.net | Dance/Pop — no stream found |
| Armenian Pulse Radio | USA | http://www.armenianpulse.com | Glendale CA — no stream found |
| ARM Music Radio | USA | http://okteve.com/arm-music-channel-live/ | Hollywood CA — no stream found |
| Radio Menq | Armenia | https://www.facebook.com/radiomenq | Founded by visually impaired journalists — no stream found |
| Radio AYK | UAE | https://www.radioayk.com | Western Armenian diaspora radio — stream plays on their site, find URL via DevTools > Network |

## Appears offline

| Station | Country | Website |
|---|---|---|
| Radio Shant Gyumri | Armenia | https://azkitsayn.com |
| Armenian Voice | USA | http://www.armeniansvoice.com |
| Radio Spurk | France | http://www.radiospurk.com |
| ArmNews FM | Armenia | — |

## M3U8 streams (HLS — supported since July 2026)

| Station | Country | Stream URL | Website |
|---|---|---|---|
| Luys TV | Armenia | `http://luyse.mediatriple.net/luystv/luystv.smil/playlist.m3u8` | http://www.luys.tv |
| Radio Van | Armenia | `http://stream.radiovan.fm/stream/index.m3u8` | https://radiovan.fm | — stream was down at time of check |

## Time-slotted Armenian programs (not 24/7)

These are Armenian-language programs on mainstream stations — stream is the host station's feed, not always in Armenian.

### USA

| Program | Station | City | Schedule | Stream |
|---|---|---|---|---|
| Hye Oozh | KFSR 90.7 FM | Fresno, CA | Sat 9:00 AM–12:00 PM PT | https://kfsr.org |
| All Things Armenian | KFSR 90.7 FM | Fresno, CA | Sat 12:00–1:00 PM PT | https://kfsr.org |
| Armenian Radio Hour of NJ | WSOU 89.5 FM | South Orange, NJ | Sun 2:00–4:00 PM ET | https://www.iheart.com/live/wsou-895-fm-5252/ |
| Armenian Radio Hour | WARA 1320 AM | Attleboro, MA | Sun 9:00–10:00 AM ET | https://www.wararadio.com/listen.html |
| Armenian Radio | WJCU 88.7 FM | Cleveland, OH | Sun 5:00–7:00 PM ET | https://www.wjcu.org/player |
| Armenian Radio | RUSA FM 105.1 HD2 | New York, NY | Fri 3:30–5:00 PM ET | https://rusa.fm/en/watch-live |
| Armenian Radio Program | WNZK 690 AM | Detroit, MI | Sun 6:00–7:00 PM ET | https://onlineradiobox.com/us/wnzk690680am/ |

### Canada

| Program | Station | City | Schedule | Stream |
|---|---|---|---|---|
| Armenian Variety Show | CFRO 100.5 FM | Vancouver, BC | Tue 6:00–7:00 PM PT / Fri 8:00–9:00 AM PT | https://coopradio.radioapp.ca/ |

### Australia

| Program | Station | City | Schedule | Stream |
|---|---|---|---|---|
| SBS Armenian | SBS Radio 1 | Nationwide | Tue 6:00–7:00 PM AEST (live) / Sun 6:00–7:00 PM AEST (repeat) | https://www.sbs.com.au/audio/radio/sbs1 |

### Cyprus

| Program | Station | City | Schedule | Stream |
|---|---|---|---|---|
| Armenian Daily News | RIK Radio 2 | Nicosia (nationwide) | Daily 5:15 PM EET | https://radio.rik.cy/live-radio/rik-2/ |

### Uruguay

| Program | Station | City | Schedule | Stream |
|---|---|---|---|---|
| Audición Gomidas | CX4 Radio Rural 610 AM | Montevideo | Mon–Fri 8:00–9:00 PM / Sat–Sun 1:00–3:00 PM UYT | https://radiorural.uy |

> Oldest Armenian diaspora radio program in the world — on air since 1935 (90 years in 2025).

### France

| Program | Station | City | Schedule | Stream |
|---|---|---|---|---|
| Arménice | RCF Nice Côte d'Azur | Nice | Tue 1:30 PM / Sat 9:20 AM CET | https://rcf.fr |

---

## How to find a hidden stream URL

1. Open the station's website in Chrome
2. Open DevTools → **Network** tab → filter by **Media** or type `m3u8` / `mp3` / `aac`
3. Press play on their player
4. Copy the URL of the audio request that appears
5. Add it to `stations.json`

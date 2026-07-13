# Missing / Unresolved Stations

Stations found during research but not yet added to `stations.json`.

---

## Stream URL not found (dynamic player)

| Station | Country | Website | Notes |
|---|---|---|---|
| Sputnik Armenia | Armenia | https://armeniasputnik.am | Stream hidden behind radioplayer.ru — open DevTools > Network while playing |
| Nor Radyo | Turkey | https://norradyo.com | Armenian/Turkish community radio — stream not exposed on site or zeno.fm |
| Azatutyun (RFE/RL) | Armenia | https://www.azatutyun.am | Radio Free Europe Armenian service — site returns 403 |
| Radio MIR Armenia | Armenia | https://radiomir.fm/regions/armeniya | Old stream `http://46.162.206.108:8000/live.mp3` is dead — open DevTools > Network on their site to find new URL |
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

## How to find a hidden stream URL

1. Open the station's website in Chrome
2. Open DevTools → **Network** tab → filter by **Media** or type `m3u8` / `mp3` / `aac`
3. Press play on their player
4. Copy the URL of the audio request that appears
5. Add it to `stations.json`

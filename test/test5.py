from loguru import logger

from PicImageSearch import Google

google = Google()
res = google.search("https://media.discordapp.net/attachments/783138508038471701/813452582948306974/hl-18-1-900x1280.png?width=314&height=447")
#res = ascii2d.search(r'C:/kitUIN/img/tinted-good.jpg')  # Search Image URL or path
logger.info(res.origin)  # Original Data
logger.info(res.raw)  # Raw Data
# Should start from index 2, because from there is matching image
logger.info(res.raw[2])  # <NormGoogle(title=['ダメダメ皇子がじつは最強冒険者！？ 『最強出涸らし皇子の ...'], urls=['https://news.nicovideo.jp/watch/nw7477612'], thumbnail=['https://originalnews.nico/wp-content/uploads/2020/05/06113733/2020-05-06_10h37_00.jpg'])>
logger.info(res.raw[2].thumbnail[0])  # None
logger.info(res.raw[2].title[0])  # The Strongest Dull Prince's Secret Battle for the Throne ...
logger.info(res.raw[2].url[0])  # https://kiryuu.co/the-strongest-dull-princes-secret-battle-for-the-throne-chapter-3-bahasa-indonesia/
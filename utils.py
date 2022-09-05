tvg_ids_logos = {'DAZN 1': 'https://img.sport-tv-guide.live/images/tv-station-dazn-1-es-2510.png', 'DAZN 2': 'https://img.sport-tv-guide.live/images/tv-station-dazn-2-es-2511.png', 'DAZN 3': 'https://img.sport-tv-guide.live/images/tv-station-dazn-3-es-2524.png', 'DAZN 4': 'https://img.sport-tv-guide.live/images/tv-station-dazn-4-es-2525.png', 'DAZN F1 HD': 'https://img.sport-tv-guide.live/images/tv-station-dazn-formula-1-366.png', 'DAZN LaLigaHD': 'https://img.sport-tv-guide.live/images/stations/a2784.png', 'EUROSPORT1HD': 'https://img.sport-tv-guide.live/images/tv-station-es-eurosport-1-615.png', 'EUROSPORT2HD': 'https://img.sport-tv-guide.live/images/tv-station-es-eurosport-2-616.png', 'M+ #VAMOSHD': 'https://img.sport-tv-guide.live/images/tv-station-vamos-1601.png', 'M+DEPORTESHD': 'https://img.sport-tv-guide.live/images/tv-station-movistar-deportes-364.png', 'M+DEPORTES2HD': 'https://img.sport-tv-guide.live/images/tv-station-movistar-deportes-2-365.png', 'M+DEPORTES3': 'https://img.sport-tv-guide.live/images/tv-station-movistar-deportes-3-2502.png', 'M+ GOLF HD': 'https://img.sport-tv-guide.live/images/tv-station-movistar-golf-368.png', 'M+ LaLiga HD': 'https://img.sport-tv-guide.live/images/tv-station-movistar-laliga-1841.png', 'LaLiga SmartbankTV': 'https://i.postimg.cc/Njyrk4sJ/ligasmartbank.png', 'LaLiga SmartbankTV 2 HD': 'https://i.postimg.cc/Njyrk4sJ/ligasmartbank.png', 'LALIGATV BAR': 'https://img.sport-tv-guide.live/images/tv-station-laligatv-bar-2505.png', 'M+LCAMPEONES': 'https://img.sport-tv-guide.live/images/tv-station-moviestar-liga-de-campeones-1459.png', 'M+LCAMPEON2': 'https://img.sport-tv-guide.live/images/tv-station-moviestar-liga-de-campeones-2-1460.png', 'M+LCAMPEON3': 'https://img.sport-tv-guide.live/images/tv-station-movistar-liga-de-campeones-3-1548.png', 'M+LCAMPEON4': 'https://img.sport-tv-guide.live/images/tv-station-movistar-liga-de-campeones-4-1549.png', 'M+LCAMPEON5': 'https://img.sport-tv-guide.live/images/tv-station-movistar-liga-de-campeones-5-1550.png', 'M+ #0 HD': 'https://img.sport-tv-guide.live/images/stations/a371.png', 'BARCA TV': 'https://img.sport-tv-guide.live/images/tv-station-barca-tv-1456.png', 'BE MAD': 'https://img.sport-tv-guide.live/images/tv-station-be-mad-621.png', 'CUATRO HD': 'https://img.sport-tv-guide.live/images/tv-station-cuatro-619.png', 'GOL HD': 'https://img.sport-tv-guide.live/images/tv-station-gol-369.png', 'HISTORIA': 'https://i.postimg.cc/NGrXN3S1/historia.png', 'LA 1 HD': 'https://img.sport-tv-guide.live/images/tv-station-la-1-838.png', 'NAT GEO HD': 'https://i.postimg.cc/CMb7QnfM/natgeo.png', 'TELECINCO HD': 'https://img.sport-tv-guide.live/images/stations/a907.png', 'TELEDEPORTE': 'https://img.sport-tv-guide.live/images/tv-station-teledeporte-612.png', 'SPORT TV': 'https://i.imgur.com/YePx20b.png', 'BEIN SPORTS': 'https://i.imgur.com/XcjYBfj.png', 'ELLAS': 'https://i.imgur.com/OJaEosP.png', 'ESPN': 'https://i.imgur.com/vv9mfSp.png', 'NBA': 'https://i.imgur.com/4QrPlos.png'}
group_title_order = ["DAZN LaLiga", "DAZN F1", "DAZN", "M+ LaLiga", "M+ LaLiga Smartbank", "M+ LaLiga TV BAR", "M+ Liga de Campeones", "M+ Deportes", "EuroSport", "Otro contenido"]


def extract_group_title(channel_title):
	
	title = channel_title.upper()

	if "DAZN" in title:
		if "LIGA" in title:
			return "DAZN LaLiga"
		elif "F1" in title or "FORMULA 1" in title or "FÓRMULA 1" in title:
			return "DAZN F1"
		else:
			return "DAZN"
	elif "EUROSPORT" in title:
		return "EuroSport"
	elif "DEPORTES" in title or "VAMOS" in title or "GOLF" in title:
		return "M+ Deportes"
	elif "LIGA" in title and "BAR" not in title and "DAZN" not in title and "SMARTBANK" not in title and "CAMPEONES" not in title:
		return "M+ LaLiga"
	elif "SMARTBANK" in title:
		return "M+ LaLiga Smartbank"
	elif "BAR" in title and "BARÇA" not in title and "BARCA" not in title:
		return "M+ LaLiga TV BAR"
	elif "CAMPEONES" in title or "M.L." in title:
		return "M+ Liga de Campeones"
	else:
		return "Otro contenido"


def extract_tvg_id(channel_title):

	title = channel_title.upper().replace("1080", "").replace("720", "")

	if "BARÇA" in title or "BARCA" in title:
		return "BARCA TV"
	if "BE MAD" in title or "BEMAD" in title:
		return "BE MAD"
	if "CUATRO" in title:
		return "CUATRO HD"
	if "DAZN" in title:
		if "DAZN 2" in title:
			return "DAZN 2"
		elif "DAZN 3" in title:
			return "DAZN 3"
		elif "DAZN 4" in title:
			return "DAZN 4"
		elif "F1" in title or "FORMULA" in title or "FÓRMULA" in title:
			return 'DAZN F1 HD'
		elif "LIGA" in title:
			return 'DAZN LaLigaHD'
		else:
			return "DAZN 1"
	if "EUROSPORT 2" in title:
		return "EUROSPORT2HD"
	if "EUROSPORT" in title:
		return "EUROSPORT1HD"
	if "GOL" in title and "GOLF" not in title:
		return "GOL HD"
	if "HISTORIA" in title:
		return "HISTORIA"
	if "LA 1" in title or "LA1" in title:
		return "LA 1 HD"
	if "BAR" in title and "BARÇA":
		return 'LALIGATV BAR'
	if "SMARTBANK 2" in title or "SMARTBANK M2" in title:
		return 'LaLiga SmartbankTV 2 HD'
	if "SMARTBANK" in title:
		return 'LaLiga SmartbankTV'
	if "# 0" in title or "#0" in title:
		return 'M+ #0 HD'
	if "VAMOS" in title:
		return 'M+ #VAMOSHD'
	if "GOLF" in title:
		return 'M+ GOLF HD'
	if "LIGA" in title and "BAR" not in title and "DAZN" not in title and "SMARTBANK" not in title and "CAMPEONES" not in title:
		return "M+ LaLiga HD"
	if "DEPORTES" in title:
		if "2" in title:
			return "M+DEPORTES2HD"
		elif "3" in title:
			return "M+DEPORTES3"
		else:
			return "M+DEPORTESHD"
	if "CAMPEONES" in title:
		for i in ["2", "3", "4", "5"]:
			if i in title:
				return "M+LCAMPEON" + i
		return "M+LCAMPEONES"
	if "NATIONAL" in title or "GEOGRAPHIC" in title or "NAT" in title or "GEO" in title:
		return 'NAT GEO HD'
	if "CINCO" in title:
		return "TELECINCO HD"
	if "TELEDEPORTE" in title or "TDP" in title:
		return "TELEDEPORTE"
	if "SPORT TV" in title:
		return "SPORT TV"
	if "BEIN" in title:
		return "BEIN SPORTS"
	if "ELLAS #" in title:
		return "ELLAS"
	if "ESPN" in title:
		return "ESPN"
	return ""


def get_logo(tvg_id):
	if tvg_id in tvg_ids_logos:
		return tvg_ids_logos[tvg_id]
	else:
		return ""

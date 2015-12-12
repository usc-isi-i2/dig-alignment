# Scripts for modeling ATF data.

def atf_article_uri(url, post_id):
    return get_url_hash(url)+"/"+post_id

def atf_thread_uri(url):
    return get_url_hash(url)

test_date = "Wed Feb 11, 2015 10:31 am"

def atf_date_created(date, format="%a %b %d, %Y %I:%M %p"):
    """Put the date in ISO format"""
    return iso8601date(date, format)

def atf_joined_date(date, format="%a %b %d, %Y %I:%M %p"):
    """Put the date in ISO format"""
    return iso8601date(date, format)

test_date2 = "Wednesday, March 18, 2015 10:33 AM"
test_format2 = "%A, %B %d, %Y %I:%M %p"

test_date3 = "2014-01-14 02:52:44"

from HTMLParser import HTMLParser

class HTMLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def handle_starttag(self, tag, attrs):
        self.fed.append(" ")
    def handle_endtag(self, tag):
        self.fed.append(" ")
    def handle_startendtag(self, tag, attrs):
        self.fed.append(" ")
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = HTMLStripper()
    s.feed(html)
    return s.get_data()

test_signature = "<span style=\"font-style: italic\">Precision Combat Arms<br />1710 E Trent, Unit 1<br />Spokane, WA 99202<br />509-535-0655<br />M-F 9-5</span></div>"

def signature_clean(text):
    """Strip HTML"""
    return strip_tags(text).strip()


def atf_fc_uri(article_uri):
    """URI of feature collection"""
    return article_uri+"/featurecollection"

def atf_get_city(city_state):
    if "," in city_state:
        return city_state.split(",")[0]
    else:
        return city_state

def atf_get_state(city_state):
    if "," in city_state:
        return city_state.split(",")[1]
    else:
        return ""

def atf_address_uri(city, state, country):
    return address_uri(city, state, country)

def atf_clean_post_count(post_count):
    return numericOnly(post_count)

def atf_clean_from_user(user):
    user = user.strip()
    if user == "-" or user == "N/A":
        user = ''
    return user

import re

WEAPONS_PHRASES = ['gun',
                   'rifle',
                   'missile',
                   'mark',
                   'tank',
                   'mk',
                   'torpedo',
                   'naval',
                   'vehicle',
                   'remington',
                   'smith',
                   'pistol',
                   'wesson',
                   'grenade',
                   'howitzer',
                   'mine',
                   'mortar',
                   'colt',
                   'submachine',
                   'canon',
                   'cannon',
                   'mod\xe8le',
                   'ruger',
                   'koch',
                   'heckler',
                   'weapon',
                   'bomb',
                   'armoured',
                   'carbine',
                   'beretta',
                   'missile',
                   'armored',
                   'winchester',
                   'springfield',
                   'revolver',
                   'launcher',
                   'caliber',
                   'assault',
                   'sig',
                   '45',
                   'ordnance',
                   'zastava',
                   'rocket',
                   'anti-tank',
                   'walther',
                   'combat',
                   'benelli',
                   'sniper',
                   'series',
                   'mle',
                   'browning',
                   'schneider',
                   'm1',
                   'carrier',
                   'kanone',
                   'defense',
                   'artillery',
                   'tank',
                   'steyr',
                   'rml',
                   'mowag',
                   'wz.',
                   'mauser',
                   'm3',
                   'vehicle',
                   'vickers',
                   'taurus',
                   'tactical',
                   'sword',
                   'infantry',
                   'panzer',
                   'marlin',
                   'hotchkiss',
                   'fk',
                   'barrett',
                   'weapon',
                   'sauer',
                   'modello',
                   'explosive',
                   'aircraft',
                   'tractor',
                   'skoda',
                   'self-propelled',
                   'rheinmetall',
                   'reconnaissance',
                   'minenwerfer',
                   'm4',
                   'kel-tec',
                   'fighting',
                   'daewoo',
                   'bofors',
                   'rocket',
                   'sd.kfz.',
                   'scout',
                   'pindad',
                   'knife',
                   'carriage',
                   'bliss-leavitt',
                   'arms',
                   'advanced',
                   'storm',
                   'sdkfz',
                   'savage',
                   'saurer',
                   'renault',
                   'nuclear',
                   'missile',
                   'bayonet',
                   'arsenal',
                   'sword',
                   'armoured',
                   'weapons',
                   'weapon-stub',
                   'war',
                   'strike',
                   'spartan',
                   'oerlikon',
                   'obusier',
                   'nebelwerfer',
                   'm\xF6rser',
                   'munition',
                   'military',
                   'marksman',
                   'krupp',
                   'flamethrower',
                   'feldhaubitze',
                   'eagle',
                   'crosman',
                   'cobra',
                   'carrier',
                   'bushmaster',
                   'breda',
                   'army',
                   'amphibious',
                   'afv',
                   'wolf',
                   'vektor',
                   'vehicle',
                   'turret',
                   'tanks',
                   'stridsvagn',
                   'soltam',
                   'siege',
                   'shotgun',
                   'sg',
                   'schwerer',
                   'schwere',
                   'pdw',
                   'panhard',
                   'nambu',
                   'mortier',
                   'magnum',
                   'm8',
                   'm60',
                   'm1918',
                   'm1895',
                   'luftminenwerfer',
                   'leopard',
                   'kbk',
                   'kanon',
                   'imbel',
                   'humber',
                   'hi-point',
                   'guns',
                   'gryazev-shipunov',
                   'explosives',
                   'denel',
                   'battle',
                   'axe',
                   'automag',
                   'attack',
                   'armory',
                   'armalite',
                   'alfa',
                   'pistol',
                   'bomb',
                   'artillery']

def isInt(s):
    try:
        int(s)
        return True
    except:
        pass
    return False

WEAPONS_PHRASES = [w for w in WEAPONS_PHRASES if not isInt(w)]
# restore a few numbers
WEAPONS_PHRASES = WEAPONS_PHRASES + ["45", ".45", "38", "50", "3006", ".22", "22", "357"]
# add a few missing popular items
WEAPONS_PHRASES = WEAPONS_PHRASES + ['uzi', 'ammo', 'ammunition', 'stoner', 'scar17', 'taser', 'tazer', 
                                     'Tokarev', 'glock', 'AK-47', 'AK 47', 'luger', 'P38', 'spdmstr', 
                                     'AR15', 'AR-15', 'AMT', 'Trejo', 'Armatix', 'Astra', 'Bechowiec',
                                     'Bauer', 'Benelli', 'Versa', 'Browning', 'BUL', 'Caracal', 'Zamorana',
                                     'Wesson', 'Danuvia', 'Musgrave', 'Vektor', 'Enfield',
                                     'FEG', 'FN', 'Herstal', 'Gabilondo', 'Urresti', 'Makarov', 'Izhevsk',
                                     'Sauer', 'KBP', 'Kimber', 'MAB', 'Mauser', 'MAC-10', 'MAC-11',
                                     'MAC10', 'MAC11', 'Pindad',
                                     'RPC', 'Bonifacio', 'Steyr',
                                     'Tanfoglio', 'Tula', "CZ",
                                     "\x010CZ", 'RSAF', 'Webley',
                                     'Norinco', 'Akdal', 'Famars',
                                     'Marlin']

# FROM SPREADSHEET 28 May 2015

WMD_RELATED = [
"Abrin",
"Agent 15",
"Antrax",
"Arsines",
"Backpack nuke",
"Balancing Machines",
"Bambi",
"Beryllium",
"biohazard",
"biological",
"biological weapon",
"Bioreactors",
"bonus damage",
"bush",
"Capacitors",
"Chemical",
"chemical weapon",
"cheney",
"chlorine",
"Crucibles",
"cyanide",
"Cyanogen chloride",
"cyclosarin",
"Devices",
"Dirty Bomb",
"dirty bomber",
"Discharge",
"Electrical",
"face-shot",
"FAE",
"Fermenters",
"Filament",
"Flow Form Machines",
"Focal Plane Sensors",
"Frequency Changers",
"Generators",
"Gravity Gradiometers",
"Gravity Meters",
"Hafnium",
"Hafnium",
"Heat Exchanges",
"hydrogen chloride",
"hydrogen cyanide",
"IED",
"IID",
"incendiary",
"Inspection",
"Isostatic Presses",
"Lasers",
"Lathes",
"lewisite",
"Magnetic gradiometers",
"Maraging Steel",
"nerve gas",
"Niobium",
"nitrogen mustard",
"nitrogen oxide",
"Novichok",
"nuclear",
"nuclear weapon",
"Outlet pipes",
"phosgene",
"phosgene oxime",
"Pressure Transducers",
"Radioactive fallout device",
"radiological",
"radiological weapon",
"ricin",
"Sarin",
"soman",
"Spectrometers",
"spud gun",
"sulfur mustard",
"Switching Devices",
"tabun",
"Tantalum",
"tear gas",
"TOW",
"toxin",
"VR",
"VX",
"Weapons of Mass Destruction",
"weapons-grade",
"Winding",
"WMD",
"Wooden",
"Woompher",
"Zirconium"
]

EXPLOSIVES_RELATED = [
"Acetylides of heavy metals",
"aerial shell",
"aluminum",
"Aluminum containing polymeric propellant",
"Aluminum ophorite explosive",
"Amatex",
"Amatol",
"Ammonal",
"ammonia",
"ammonium nitrate",
# "Ammonium nitrate explosive mixtures (cap sensitive).",
"Ammonium nitrate explosive mixtures",
"cap sensitive",
# "Ammonium nitrate explosive mixtures (non-cap sensitive)",
"Ammonium nitrate explosive mixtures",
"non-cap sensitive",
#"Ammonium perchlorate explosive mixtures (excluding ammonium perchlorate composite propellant (APCP))",
"Ammonium perchlorate",
"explosive mixtures",
"APCP",
# "Ammonium perchlorate having particle size less than 15 microns",
"Ammonium perchlorate",
# "Ammonium picrate [picrate of ammonia, Explosive D].",
"Ammonium picrate",
"picrate of ammonia",
"Explosive D",
# "Ammonium salt lattice with isomorphously substituted inorganic salts",
"Ammonium salt lattice",
"isomorphously substituted inorganic salts",
# "ANFO [ammonium nitrate-fuel oil]",
"ANFO",
"ammonium nitrate-fuel oil",
"fuel oil",
"Aromatic nitro-compound explosive mixtures",
"articles pyrotechnic",
"ATF",
"ATFE",
"Azide explosives",
"bang",
"Baranol",
"Baratol",
"BATFE",
# "BEAF [1, 2-bis (2, 2-difluoro-2-nitroacetoxyethane)]",
"BEAF",
"1, 2-bis (2, 2-difluoro-2-nitroacetoxyethane)",
"binary",
"Black powder",
"black powder",
"Black powder based explosive mixtures",
"black powder bomb",
# "Blasting agents, nitro-carbo-nitrates, including non-cap sensitive slurry and water gel explosives",
"Blasting agents",
"nitro-carbo-nitrates", 
"non-cap sensitive slurry",
"water gel explosives",
"Blasting caps",
"Blasting gelatin",
"Blasting powder",
"blow up",
"bomb",
"boom",
"booster",
# "BTNEC [bis (trinitroethyl) carbonate]",
"BTNEC",
"bis (trinitroethyl) carbonate",
# "BTNEN [bis (trinitroethyl) nitramine]",
"BTNEN",
"bis (trinitroethyl) nitramine",
# "BTTN [1,2,4 butanetriol trinitrate]",
"BTTN",
"1,2,4 butanetriol trinitrate",
"Bulk salutes",
"Bureau of ATF",
"butane bomb",
"Butyl tetryl",
"c-4",
"cake",
# "Calcium nitrate explosive mixture",
"Calcium nitrate explosive mixture",
"Calcium nitrate",
"cap sensitive",
# "Cellulose hexanitrate explosive mixture",
"Cellulose hexanitrate explosive mixture",
"Cellulose hexanitrate",
"charge",
"Chlorate explosive mixtures",
"Class B",
"Class C",
# "Composition A and variations",
"Composition A and variations",
"Composition A",
# "Composition B and variations",
"Composition B and variations",
"Composition B",
# "Composition C and variations",
"Composition C and variations",
"Composition C",
"Copper acetylide",
"cord",
"Cyanuric triazide",
# "Cyclonite [RDX]",
"Cyclonite",
"RDX",
# "Cyclotetramethylenetetranitramine [HMX]",
"Cyclotetramethylenetetranitramine",
"HMX",
"Cyclotol",
# "Cyclotrimethylenetrinitramine",
"Cyclotrimethylenetrinitramine",
"RDX",
# "DATB [diaminotrinitrobenzene]",
"DATB",
"diaminotrinitrobenzene",
# "DATB [diaminotrinitrobenzene]",
"DATB",
"diaminotrinitrobenzene",
# "DDNP [diazodinitrophenol]",
"DDNP",
"diazodinitrophenol",
# "DEGDN [diethyleneglycol dinitrate]",
"DEGDN",
"diethyleneglycol dinitrate",
"depth charge",
"det cord",
"Detonating cord",
"detonator",
"detonator",
"Detonators",
"dets",
"diesel",
"diesel fuel",
"Dimethylol dimethyl methane dinitrate composition",
"Dinitroethyleneurea",
# "Dinitroglycerine [glycerol dinitrate]",
"Dinitroglycerine",
"glycerol dinitrate",
"Dinitrophenol",
"Dinitrophenolates",
"Dinitrophenyl hydrazine",
"Dinitroresorcinol",
"Dinitrotoluene-sodium nitrate explosive mixtures",
# "DIPAM [dipicramide; diaminohexanitrobiphenyl]",
"DIPAM",
"dipicramide; diaminohexanitrobiphenyl",
"Dipicryl sulfone",
"Dipicrylamine",
"Display fireworks",
# "DNPA [2,2-dinitropropyl acrylate]",
"DNPA",
"2,2-dinitropropyl acrylate",
# "DNPD [dinitropentano nitrile]",
"DNPD",
"dinitropentano nitrile",
"Dynamite",
# "EDDN [ethylene diamine dinitrate]",
"EDDN",
"ethylene diamine dinitrate",
# "EDNA [ethylenedinitramine]",
"EDNA",
"ethylenedinitramine",
"Ednatol",
# "EDNP [ethyl 4,4-dinitropentanoate]",
"EDNP",
"ethyl 4,4-dinitropentanoate",
# "EGDN [ethylene glycol dinitrate]",
"EGDN",
"ethylene glycol dinitrate",
"Emulsion",
"Erythritol tetranitrate explosives",
"Esters of nitro-substituted alcohols",
"Ethyl-tetryl",
"EX Number",
"explosive",
"Explosive conitrates",
"Explosive gelatins",
"Explosive liquids",
"Explosive mixtures containing oxygenreleasing inorganic salts and hydrocarbons",
"Explosive mixtures containing oxygenreleasing inorganic salts and nitro bodies",
"Explosive mixtures containing oxygenreleasing inorganic salts and water insoluble fuels",
"Explosive mixtures containing oxygenreleasing inorganic salts and water soluble fuels",
"Explosive mixtures containing sensitized nitromethane",
"Explosive mixtures containing tetranitromethane (nitroform)",
"Explosive nitro compounds of aromatic hydrocarbons",
"Explosive organic nitrate mixtures",
"Explosive powders",
"Federal Explosives Licensee",
"Federal Explosives Permit",
"FEL",
"FEP",
"fertilizer",
"firework",
"Flash powder",
"flash powder bomb",
"fuel",
"fuel air mixture bomb",
"Fulminate of mercury",
"Fulminate of silver",
"Fulminating gold",
"Fulminating mercury",
"Fulminating platinum",
"Fulminating silver",
"fuse",
"Gelatinized nitrocellulose",
"Gem-dinitro aliphatic explosive mixtures",
"grenade",
"Guanyl nitrosamino guanyl tetrazene",
"Guanyl nitrosamino guanylidene hydrazine",
"Guncotton",
"Heavy metal azides",
"helix",
"Hexanite",
"Hexanitrodiphenylamine",
"Hexanitrostilbene",
# "Hexogen [RDX]",
"Hexogen",
"RDX",
"Hexogene or octogene and a nitrated Nmethylaniline",
"Hexolites",
"high explosive",
"HME",
# "HMTD [hexamethylenetriperoxidediamine]",
"HMTD",
"hexamethylenetriperoxidediamine",
# "HMX [cyclo-1,3,5,7-tetramethylene 2,4,6,8-tetranitramine; Octogen]",
"HMX",
"cyclo-1,3,5,7-tetramethylene 2,4,6,8-tetranitramine",
"Octogen",
"homemade bomb",
"homemade explosive",
# "Hydrazinium nitrate/hydrazine/aluminum explosive system",
"Hydrazinium nitrate",
"hydrazine",
"aluminum explosive system",
"Hydrazoic acid",
"Hydrogen peroxide",
"igniter",
"Igniter cord",
"Igniters",
"incendiary",
"Initiating tube systems",
"instant mix",
# "KDNBF [potassium dinitrobenzo-furoxane]",
"KDNBF",
"potassium dinitrobenzo-furoxane",
"land mine",
"Lead azide",
"Lead mannite",
"Lead mononitroresorcinate",
"Lead picrate",
"Lead salts, explosive",
# "Lead styphnate [styphnate of lead, lead trinitroresorcinate]",
"Lead styphnate",
"styphnate of lead", 
"lead trinitroresorcinate",
"Liquid nitrated polyol and trimethylolethane",
"Liquid oxygen explosives",
"low explosive",
"M/S",
"M-80",
"Magnesium ophorite explosives",
"Mannitol hexanitrate",
"mass destruction",
"mass detonate",
"mass detonation",
"mass explosion",
"mass explosive",
# "MDNP [methyl 4,4-dinitropentanoate]",
"MDNP",
"methyl 4,4-dinitropentanoate",
# "MEAN [monoethanolamine nitrate]",
"MEAN",
"monoethanolamine nitrate",
"Mercuric fulminate",
"Mercury oxalate",
"Mercury tartrate",
"methane",
"Metriol trinitrate",
"millisecond",
# "Minol-2 [40% TNT, 40% ammonium nitrate, 20% aluminum]",
"Minol-2",
"40% TNT, 40% ammonium nitrate, 20% aluminum",
# "MMAN [monomethylamine nitrate]; methylamine nitrate",
"MMAN",
"monomethylamine nitrate",
"methylamine nitrate",
"molotov",
"molotov cocktail",
"Mononitrotoluene-nitroglycerin mixture",
"Monopropellants",
# "NIBTN [nitroisobutametriol trinitrate]",
"NIBTN",
"nitroisobutametriol trinitrate",
"Nitrate explosive mixtures",
"Nitrate sensitized with gelled nitroparaffin",
"Nitrated carbohydrate explosive",
"Nitrated glucoside explosive",
"Nitrated polyhydric alcohol explosives",
"Nitric acid and a nitro aromatic compound explosive",
"Nitric acid and carboxylic fuel explosive",
"Nitric acid explosive mixtures",
"nitro",
"Nitro aromatic explosive mixtures",
"Nitro compounds of furane explosive mixtures",
"Nitrocellulose explosive",
"Nitroderivative of urea explosive mixture",
"Nitrogelatin explosive",
"Nitrogen trichloride",
"Nitrogen tri-iodide",
# "Nitroglycerine [NG, RNG, nitro, glyceryl trinitrate, trinitroglycerine",
"Nitroglycerine",
"NG", 
"RNG", 
"nitro", 
"glyceryl trinitrate", 
"trinitroglycerine",
"Nitroglycide",
# "Nitroglycol [ethylene glycol dinitrate, EGDN",
"Nitroglycol",
"ethylene glycol dinitrate",
"EGDN",
"Nitroguanidine explosives",
"Nitronium perchlorate propellant mixtures",
# "Nitroparaffins Explosive Grade and ammonium nitrate mixtures",
"Nitroparaffins",
"Nitrostarch",
"Nitro-substituted carboxylic acids",
"Nitrourea",
# "Octogen [HMX",
"Octogen",
"HMX",
# "Octol [75 percent HMX, 25 percent TNT]",
"Octol",
"75 percent HMX, 25 percent TNT",
"oil perforator",
"Organic amine nitrates",
"Organic nitramines",
"oxidizer",
# "PBX [plastic bonded explosives]",
"PBX",
"plastic bonded explosives",
"Pellet powder",
"Penthrinite composition",
"Pentolite",
"Perchlorate explosive mixtures",
"Peroxide based explosive mixtures",
# "PETN [nitropentaerythrite, pentaerythrite tetranitrate, pentaerythritol tetranitrate]",
"PETN",
"nitropentaerythrite", 
"pentaerythrite tetranitrate", 
"pentaerythritol tetranitrate",
"Picramic acid and its salts",
"Picramide",
"Picrate explosives",
"Picrate of potassium explosive mixtures",
"Picratol",
# "Picric acid (manufactured as an explosive)",
"Picric acid",
"Picryl chloride",
"Picryl fluoride",
"pipe bomb",
"plastic explosive",
# "PLX [95% nitromethane, 5% ethylenediamine]",
"PLX",
"95% nitromethane, 5% ethylenediamine",
"Polynitro aliphatic compounds",
"Polyolpolynitrate-nitrocellulose explosive gels",
# "Potassium chlorate and lead sulfocyanate explosive",
"Potassium chlorate",
"lead sulfocyanate",
# "Potassium nitrate explosive mixtures",
"Potassium nitrate",
"Potassium nitroaminotetrazole",
"pounds",
"propane bomb",
"pyrotechnic",
"Pyrotechnic compositions",
# "PYX [2,6-bis(picrylamino)] 3,5-dinitropyridine",
"PYX",
"2,6-bis(picrylamino) 3,5-dinitropyridine",
"Quarter stick",
# "RDX [cyclonite, hexogen, T4, cyclo-1,3,5,-trimethylene-2,4,6,-trinitramine; hexahydro-1,3,5-trinitro-S-triazine]",
"RDX",
"cyclonite", 
"hexogen", 
"T4", 
"cyclo-1,3,5,-trimethylene-2,4,6,-trinitramine", 
"hexahydro-1,3,5-trinitro-S-triazine",
"Safety fuse",
"Salts of organic amino sulfonic acid explosive mixture",
"salute",
"Salutes (bulk)",
"bulk salutes",
"shape charge",
"shell",
"Silver acetylide",
"Silver azide",
"Silver fulminate",
# "Silver oxalate explosive mixtures",
"Silver oxalate explosive mixtures",
"Silver oxalate",
"Silver styphnate",
# "Silver tartrate explosive mixtures",
"Silver tartrate explosive mixtures",
"Silver tartrate",
"Silver tetrazene",
"Slurried explosive mixtures of water, inorganic oxidizing salt, gelling agent, fuel, and sensitizer (cap sensitive)",
"Smokeless powder",
"Sodatol",
"Sodium amatol",
"Sodium azide explosive mixture",
"Sodium dinitro-ortho-cresolate",
"Sodium nitrate explosive mixtures",
"Sodium nitrate-potassium nitrate explosive mixture",
"Sodium picramate",
"Special fireworks",
"Squibs",
"Styphnic acid explosives",
# "Tacot [tetranitro-2,3,5,6-dibenzo-1,3a,4,6a tetrazapentalene]",
"Tacot",
"tetranitro-2,3,5,6-dibenzo-1,3a,4,6a tetrazapentalene",
"tannerite",
# "TATB [triaminotrinitrobenzene]",
"TATB",
"triaminotrinitrobenzene",
# "TATP [triacetonetriperoxide]",
"TATP",
"triacetonetriperoxide",
# "TEGDN [triethylene glycol dinitrate]",
"TEGDN",
"triethylene glycol dinitrate",
"Tetranitrocarbazole",
# "Tetrazene [tetracene, tetrazine, 1(5-tetrazolyl)-4-guanyl tetrazene hydrate]",
"Tetrazene",
"tetracene", 
"tetrazine",
"1(5-tetrazolyl)-4-guanyl tetrazene hydrate",
# "Tetrazole explosives",
"Tetrazole explosives",
"Tetrazole",
# "Tetryl [2,4,6 tetranitro-N-methylaniline]",
"Tetrytol",
"thermobaric bomb",
"Thickened inorganic oxidizer salt slurried explosive mixture",
# "TMETN [trimethylolethane trinitrate]",
# "TNEF [trinitroethyl formal]",
# "TNEOC [trinitroethylorthocarbonate]",
# "TNEOF [trinitroethylorthoformate]",
# "TNT [trinitrotoluene, trotyl, trilite, triton]",
"Torpex",
"Tridite",
"Trimethylol ethyl methane trinitrate composition",
"Trimethylolthane trinitrate-nitrocellulose",
"Trimonite",
"Trinitroanisole",
"Trinitrobenzene",
"Trinitrobenzoic acid",
"Trinitrocresol",
"Trinitro-meta-cresol",
"Trinitronaphthalene",
"Trinitrophenetol",
"Trinitrophloroglucinol",
"Trinitroresorcinol",
"Tritonal",
"UN Number",
"Urea nitrate",
# "Water-bearing explosives having salts of oxidizing acids and nitrogen bases, sulfates, or sulfamates (cap sensitive)",
"Water-in-oil emulsion explosive compositions",
# "Xanthamonas hydrophilic colloid explosive mixture",
"Xanthamonas",
"hydrophilic colloid",
"Quarterstick",
"Halfstick"
]

NFA_RELATED = [
"11.5 inch",
'11.5"',
"14 inch",
'14"',
"any other weapon",
"AOW",
"ATF",
"ATFE",
"auto sear",
"automatic",
"autosear",
"AW-SIM",
"BATFE",
"Bureau of ATF",
"can",
"cane gun",
"class 3",
"class III",
"conversion",
"conversion kit",
"destructive device",
"DIAS",
"drop in auto sear",
"drop in autosear",
"FA",
"flash bang",
"flashbang",
"forward grip",
"full auto",
"grenade",
"homemade silencer",
"homemade suppressor",
"incendiary",
"land mine",
"Lightning Link",
"machine gun",
"machinegun",
"missile",
"molotov",
"molotov cocktail",
"muffler",
"nfa",
"pen gun",
"pistol grip",
"poison gas",
"RLL",
"rocket",
"rocket launcher",
"sawed off",
"sbr",
"sbs",
"sear",
"short barrel rifle",
"short barrel shotgun",
"short barreled rifle",
"short barreled shotgun",
"silencer",
"smooth bore",
"SOT",
"Special Occupational Tax",
"street sweeper",
"suppressor",
"umbrella gun",
"wallet gun",
"weapon made from",
"Zip gun",
"Zipgun"
]

GANG_RELATED = [
"boom stick",
"burner",
"cash",
"money", 
"heroin",
"chopper",
"clap-clap",
"dat fire",
"dat thang",
"davy crocket",
"deuce",
"deuce deuce",
"duece",
"fofo",
"four nickle",
"gat",
"gatt",
"gauge",
"ghost load",
"hammer",
"heater",
"hog leg",
"jammy",
"lead spitta",
"lil buddy",
"long pumps",
"mac",
"mack",
"mr. 9mm",
"narco",
"nina",
"nine",
"ol'betsy",
"ol' betsy",
"ooh wop",
"piece",
"pocket rocket",
"rod",
"roscoe",
"sawdy",
"shotty",
"smoke wagon",
"strap",
"throw down",
"thunder stick",
"toaster",
"tres",
"widow maker",
"yeezy"
]

NON_ENGLISH_RELATED = [
"arma larga",
"armas de fuego",
"bala",
"cahuetas",
"Cartucho",
"Cebolla",
"Cebollas",
"cortas",
"cuerno de chivo",
"cuerno de chivo",
"Cuerno de Chivo",
"Cuerno",
"cuete",
"El Subfusil ametralladora",
"escopete",
"escuadra",
"escuadra",
"explosivo",
"fusca",
"gat",
"la ametralladora",
"la escopeta",
"Lanza papas",
"largas",
"municion",
"Municiones",
"Papa",
"Papas",
"penas",
"Pertrechos",
"pistola",
"Polvora",
"proyectil",
"r quinze",
"Tolba",
"trick or treat",
"tricki-tricki",
"Vaina"
]

FIREARMS_RELATED = [
"5.56",
"7.62",
"1911",
".45 caliber",
".50 caliber",
"37 mm",
"37mm",
"3-D firearm",
"3-D print",
"3-D printed",
"80 percent receiver",
"80% receiver",
"9mm",
"AK",
"AK-47",
"AK-74",
"ammo",
"ammunition",
"APA",
"AR",
"AR-15",
"Armor piercing",
"Armor piercing ammuntion",
"assault rifle",
"ATF",
"ATFE",
"Barrett",
"BATFE",
"Build party",
"bullet proof vest",
"bump fire",
"bump stock",
"Bureau of ATF",
"caliber",
"carbine",
"cash only",
"centerfire",
"Chopper",
"clip",
"CNC",
"concealable",
"derringer",
"F2F",
"face to face",
"Federal Firearms License",
"FFL",
"fixed stock",
"flare gun",
"FMJ",
"folding stock",
"frame",
"full metal jacket",
"gas mask",
"ghost gun",
"glock",
"handgun",
"hi point",
"high capacity",
"homemade gun",
"jimenez",
"keltec",
"kevlar",
"long gun",
"lower",
"mag",
"magazine",
"MP4",
"MP5",
"no 4473",
"no background",
"no check",
"no paper work",
"no paperwork",
"no questions asked",
"oblit",
"obliterated",
"off book",
"pistol",
"receiver",
"revolver",
"rifle",
"rimfire",
"RPG",
"S&W",
"SA",
"scratched",
"semi-auto",
"semi-automatic",
"shotgun",
"shotty",
"shoty",
"sig brace",
"stripped lower",
"stun gun",
"Taurus",
"untraceable",
"uzi",
"vest"
]

FIREARMS_TECHNOLOGY_BRANCH = [
"Glock Switch",
"Glock Chip",
# "Chip (since this is so inclusive - I would only search in conjunction with other firearm words)",
"Chip",
"Baffle",
"Baffle Stack",
"Monocore",
"Anarchist",
"Solvent Trap",
"LDC",
"Belt Fed",
"Crew served",
"Hip Whip",
"Polymer",
"CNC machine",
"Green tip",
"Black tip",
"FAL",
"Outer tube",
"trigger"
]

WEAPONS_PHRASES.extend(FIREARMS_RELATED)
WEAPONS_PHRASES.extend(FIREARMS_TECHNOLOGY_BRANCH)
WEAPONS_PHRASES = list(set([w.lower() for w in WEAPONS_PHRASES]))

test_text = """New In Box Walther UZI .22LR RIFLE 20+1 $349.99"""

WEAPONS_PATTERNS = [re.compile(r"""\b%s\b""" % ph, re.IGNORECASE) for ph in WEAPONS_PHRASES]

def weapons_words(text, patterns=WEAPONS_PATTERNS, phrases=WEAPONS_PHRASES):
    matches = set()
    for (pattern, phrase) in zip(patterns, phrases):
        for match in re.finditer(pattern, text):
            matches.add(phrase)
    matches = list(matches)
    matches.sort()
    return matches

# print weapons_words(test_text)

def get_atf_weapons(*texts):
    all_text = " ".join([strip_tags(t) for t in texts])
    return "|".join(weapons_words(all_text))

##################################################################
KEYWORDS_PHRASES = WMD_RELATED + EXPLOSIVES_RELATED + NFA_RELATED + GANG_RELATED + NON_ENGLISH_RELATED
KEYWORDS_PHRASES = list(set([k.lower() for k in KEYWORDS_PHRASES]))

KEYWORDS_PATTERNS = [re.compile(r"""\b%s\b""" % ph, re.IGNORECASE) for ph in KEYWORDS_PHRASES]

def keywords_words(text, patterns=KEYWORDS_PATTERNS, phrases=KEYWORDS_PHRASES):
    matches = set()
    for (pattern, phrase) in zip(patterns, phrases):
        for match in re.finditer(pattern, text):
            matches.add(phrase)
    matches = list(matches)
    matches.sort()
    return matches

# print keywords_words(test_text)

def get_keywords(*texts):
    all_text = " ".join([strip_tags(t) for t in texts])
    return "|".join(keywords_words(all_text))

##################################################################

test_prices = ["I like to spend $50 for a sword, $75.00 for ammo, $ 100.00 for rifle, $ 1,000 for lunch, and BTC 2.468 to donate to Edward Snowden.", 
               "I make $60K a year on Herbalife.  Ask me how!",
               "JPY 500000 is more than CHF 200.5",
               "2.5 BTC or BTC 4.5"]

DOLLAR_PRICE_REGEXPS = [re.compile(r'''\$\s*(?:\d{1,3},\s?)*\d{1,3}(?:(?:\.\d+)|[KkMm])?''', re.IGNORECASE),
                        re.compile(r'''USD\s*\d{1,7}(?:\.\d+)?''', re.IGNORECASE),
                        re.compile(r'''\d{1,7}(?:\.\d+)?\s*USD''', re.IGNORECASE)
                        ]

BITCOIN_PRICE_REGEXPS = [re.compile(r'''(?:BTC|XBT|XBC)\s*\d{1,7}(?:\.\d+)?''', re.IGNORECASE),
                         re.compile(r'''\d{1,7}(?:\.\d+)?\s*(?:BTC|XBT|XBC)''', re.IGNORECASE)
                         ]

def get_dollar_prices(*texts):
    matches = []
    for t in texts:
        for r in DOLLAR_PRICE_REGEXPS:
            for m in r.findall(t):
                matches.append(m.replace('$ ','$').replace(',','').replace('$','').replace('K',"000").replace('k',"000").replace("M","000").replace('m',"000"))
    return "|".join(matches)

def get_prices(*texts):
    return get_dollar_prices(*texts)

def get_bitcoin_prices(*texts):
    matches = []
    for t in texts:
        for r in BITCOIN_PRICE_REGEXPS:
            for m in r.findall(t):
                matches.append(m.replace('BTC','').replace('XBT','').replace('XBC','').replace(' ',''))
    return "|".join(matches)


# print get_prices(*test_prices)

def atf_body_clean(text):
    """Strip HTML"""
    return strip_tags(text).strip()

def onion_name_to_provider_name(onion):
    if onion   in ["k5zq47j6wd3wdvjq.onion"]:
        return "evolution"
    elif onion in ["i25c62nvu4cgeqyz.onion"]:
        return "evolution-forums"
    else:
        return onion

def atf_provider_name(uri):
    domain = getWebsiteDomain(uri)
    if domain.endswith('backpage.com'):
        return "backpage.com"
    elif domain.endswith('.onion'):
        return onion_name_to_provider_name(domain)
    else:
        return domain

def person_userid_uri(cleaned):
    if cleaned:
        cleaned = cleaned.strip().replace(" ", "_").lower()
        return "person_userid/%s" % cleaned
    return ''

def person_postcount_uri(cleaned):
    if cleaned:
        cleaned = cleaned.strip().replace(" ", "_").lower()
        return "person_postcount/%s" % cleaned
    return ''

def enrollment_date_uri(cleaned):
    if cleaned:
        cleaned = cleaned.strip().replace(" ", "_").replace(":", "-").lower()
        return "enrollment_date/%s" % cleaned
    return ''

def fromUser_uri(cleaned):
    if cleaned:
        cleaned = cleaned.strip().replace(" ", "_").lower()
        return "fromUser/%s" % cleaned
    return ''

def weaponsMentioned_uri(cleaned):
    if cleaned:
        cleaned = cleaned.strip().replace(" ", "_").lower()
        return "weaponsMentioned/%s" % cleaned
    return ''

def keywordsMentioned_uri(cleaned):
    if cleaned:
        cleaned = cleaned.strip().replace(" ", "_").lower()
        return "keywordsMentioned/%s" % cleaned
    return ''

def place_postalAddress_uri(cleaned):
    if cleaned:
        cleaned = cleaned.strip().replace(" ", "_").lower()
        return "place_postalAddress/%s" % cleaned
    return ''

def ar15_user_uri(userid):
  return "person/ar15/" + userid

def calguns_user_uri(userid):
  return "person/calguns/" + userid

def glocktalk_user_uri(userid):
  return "person/glocktalk/" + userid

def ohioccw_user_uri(userid):
  return "person/ohioccwforums/" + userid

def postal_address_uri(location):
  return "address/" + location.replace(" ", "_").replace(".","_").replace(",", "_")

# print test_prices, get_dollar_prices(*test_prices)
# print test_prices, get_bitcoin_prices(*test_prices)

##################################################################

def get_weapons(*texts):
    atf_weapons = get_atf_weapons(*texts)
    keywords = get_keywords(*texts)
    return ("%s|%s" % (atf_weapons, keywords)).strip("|")

def floridaguntrader_availability_starts(date):
  """Return the date in iso format"""
  d = translate_date(date,"%m/%d","2015-%m-%d")
  if d == '':
    d = translate_date(date,"%b %d, %Y","%Y-%m-%d")
  return d

__author__ = 'amandeep'

import re

country_codes_2 = [
    "AF", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB",
    "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BA", "BA", "BW", "BV", "BV", "BR", "IO", "BN", "BG", "BF", "BI",
    "KH", "CM", "CA", "CV", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR", "CI", "HR",
    "HR", "CU", "CY", "CZ", "DK", "DJ", "DM", "DO", "TP", "EC", "EG", "SV", "GQ", "ER", "EE", "ET", "FK", "FK", "FO",
    "FJ", "FI", "FR", "FX", "GF", "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT",
    "GN", "GW", "GY", "HT", "HM", "VA", "VA", "HN", "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IL", "IT", "JM",
    "JP", "JO", "KZ", "KE", "KI", "KP", "KP", "KR", "KR", "KR", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI",
    "LT", "LU",
    "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "FM", "MD", "MD", "MC",
    "MN", "ME", "MS", "MA", "MZ", "MM", "MM", "NA", "NR", "NP", "NL", "AN", "NC", "NZ", "NI", "NE", "NG", "NU", "NF",
    "MP", "NO", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW",
    "KN", "LC", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SK", "SK", "SI", "SB", "SO", "ZA", "SS",
    "GS", "ES", "LK", "SH", "PM", "SD", "SR", "SJ", "SZ", "SE", "CH", "SY", "TW", "TJ", "TZ", "TZ", "TH", "TG", "TK",
    "TO", "TT", "TN", "TR", "TM", "TC", "TV", "UG", "UA", "AE", "GB", "US", "UM", "UY", "UZ", "VU", "VE", "VN", "VG",
    "VI", "WF", "EH", "YE", "ZM", "ZW"
]

country_codes_3 = [
    "AFG", "ALB", "DZA", "ASM", "AND", "AGO", "AIA", "ATA", "ATG", "ARG", "ARM", "ABW", "AUS", "AUT", "AZE", "BHS",
    "BHR", "BGD", "BRB", "BLR", "BEL", "BLZ", "BEN", "BMU", "BTN", "BOL", "BIH", "BIH", "BIH", "BWA", "BVT", "BVT",
    "BRA", "IOT", "BRN", "BGR", "BFA", "BDI", "KHM", "CMR", "CAN", "CPV", "CYM", "CAF", "TCD", "CHL", "CHN", "CXR",
    "CCK", "COL", "COM", "COG", "COD", "COK", "CRI", "CIV", "HRV", "HRV", "CUB", "CYP", "CZE", "DNK", "DJI", "DMA",
    "DOM", "TMP", "ECU", "EGY", "SLV", "GNQ", "ERI", "EST", "ETH", "FLK", "FLK", "FRO", "FJI", "FIN", "FRA", "FXX",
    "GUF", "PYF", "ATF", "GAB", "GMB", "GEO", "DEU", "GHA", "GIB", "GRC", "GRL", "GRD", "GLP", "GUM", "GTM", "GIN",
    "GNB", "GUY", "HTI", "HMD", "VAT", "VAT", "HND", "HKG", "HUN", "ISL", "IND", "IDN", "IRN", "IRQ", "IRL", "ISR",
    "ITA", "JAM", "JPN", "JOR", "KAZ", "KEN", "KIR", "PRK", "PRK", "KOR", "KOR", "KOR", "KWT", "KGZ", "LAO", "LVA",
    "LBN", "LSO",
    "LBR", "LBY", "LIE", "LTU", "LUX", "MAC", "MKD", "MDG", "MWI", "MYS", "MDV", "MLI", "MLT", "MHL", "MTQ", "MRT",
    "MUS", "MYT", "MEX", "FSM", "FSM", "MDA", "MDA", "MCO", "MNG", "MNE", "MSR", "MAR", "MOZ", "MMR", "MMR", "NAM",
    "NRU", "NPL", "NLD", "ANT", "NCL", "NZL", "NIC", "NER", "NGA", "NIU", "NFK", "MNP", "NOR", "OMN", "PAK", "PLW",
    "PAN", "PNG", "PRY", "PER", "PHL", "PCN", "POL", "PRT", "PRI", "QAT", "REU", "ROM", "RUS", "RWA", "KNA", "LCA",
    "VCT", "WSM", "SMR", "STP", "SAU", "SEN", "SRB", "SYC", "SLE", "SGP", "SVK", "SVK", "SVN", "SLB", "SOM", "ZAF",
    "SSD", "SGS", "ESP", "LKA", "SHN", "SPM", "SDN", "SUR", "SJM", "SWZ", "SWE", "CHE", "SYR", "TWN", "TJK", "TZA",
    "TZA", "THA", "TGO", "TKL", "TON", "TTO", "TUN", "TUR", "TKM", "TCA", "TUV", "UGA", "UKR", "ARE", "GBR", "USA",
    "UMI", "URY", "UZB", "VUT", "VEN", "VNM", "VGB", "VIR", "WLF", "ESH", "YEM", "ZMB", "ZWE"
]

country_names = [
    "AFGHANISTAN", "ALBANIA", "ALGERIA", "AMERICANSAMOA", "ANDORRA", "ANGOLA", "ANGUILLA", "ANTARCTICA",
    "ANTIGUAANDBARBUDA", "ARGENTINA", "ARMENIA", "ARUBA", "AUSTRALIA", "AUSTRIA", "AZERBAIJAN", "BAHAMAS", "BAHRAIN",
    "BANGLADESH", "BARBADOS", "BELARUS", "BELGIUM", "BELIZE", "BENIN", "BERMUDA", "BHUTAN", "BOLIVIA",
    "BOSNIAANDHERZEGOWINA", "BOSNIA", "HERZEGOWINA", "BOTSWANA", "BOUVETISLAND", "NORWAY", "BRAZIL",
    "BRITISHINDIANOCEANTERRITORY", "BRUNEIDARUSSALAM", "BULGARIA", "BURKINAFASO", "BURUNDI", "CAMBODIA",
    "CAMEROON", "CANADA", "CAPEVERDE", "CAYMANISLANDS", "CENTRALAFRICANREPUBLIC", "CHAD", "CHILE", "CHINA",
    "CHRISTMASISLAND", "COCOSISLANDS", "COLOMBIA", "COMOROS", "CONGO", "CONGOTHEDRC", "COOKISLANDS", "COSTARICA",
    "COTED'IVOIRE", "CROATIA", "HRVATSKA", "CUBA", "CYPRUS", "CZECHREPUBLIC", "DENMARK", "DJIBOUTI", "DOMINICA",
    "DOMINICANREPUBLIC", "EASTTIMOR", "ECUADOR", "EGYPT", "ELSALVADOR", "EQUATORIALGUINEA", "ERITREA", "ESTONIA",
    "ETHIOPIA", "FALKLANDISLANDS", "MALVINAS", "FAROEISLANDS", "FIJI", "FINLAND", "FRANCE", "FRANCEMETROPOLITAN",
    "FRENCHGUIANA", "FRENCHPOLYNESIA", "FRENCHSOUTHERNTERRITORIES", "GABON", "GAMBIA", "GEORGIA", "GERMANY",
    "GHANA", "GIBRALTAR", "GREECE", "GREENLAND", "GRENADA", "GUADELOUPE", "GUAM", "GUATEMALA", "GUINEA",
    "GUINEA-BISSAU", "GUYANA", "HAITI", "HEARDANDMCDONALDISLANDS", "HOLYSEE", "VATICANCITYSTATE", "HONDURAS",
    "HONGKONG", "HUNGARY", "ICELAND", "INDIA", "INDONESIA", "IRAN", "IRAQ", "IRELAND", "ISRAEL", "ITALY", "JAMAICA",
    "JAPAN", "JORDAN", "KAZAKHSTAN", "KENYA", "KIRIBATI", "KOREADPRO", "NORTHKOREA", "KOREAREPUBLICOF",
    "SOUTHKOREA", "REPUBLICOFKOREA",
    "KUWAIT", "KYRGYZSTAN", "LAOS", "LATVIA", "LEBANON", "LESOTHO", "LIBERIA", "LIBYANARABJAMAHIRIYA",
    "LIECHTENSTEIN", "LITHUANIA", "LUXEMBOURG", "MACAU", "MACEDONIA", "MADAGASCAR", "MALAWI", "MALAYSIA", "MALDIVES",
    "MALI", "MALTA", "MARSHALLISLANDS", "MARTINIQUE", "MAURITANIA", "MAURITIUS", "MAYOTTE", "MEXICO",
    "MICRONESIA,FEDERATEDSTATESOF", "FEDERATEDSTATESOFMICRONESIA", "MOLDOVAREPUBLICOF", "REPUBLICOFMOLDOVA",
    "MONACO", "MONGOLIA", "MONTENEGRO", "MONTSERRAT", "MOROCCO", "MOZAMBIQUE", "MYANMAR", "BURMA", "NAMIBIA", "NAURU",
    "NEPAL", "NETHERLANDS", "NETHERLANDSANTILLES", "NEWCALEDONIA", "NEWZEALAND", "NICARAGUA", "NIGER", "NIGERIA",
    "NIUE", "NORFOLKISLAND", "NORTHERNMARIANAISLANDS", "NORWAY", "OMAN", "PAKISTAN", "PALAU", "PANAMA",
    "PAPUANEWGUINEA", "PARAGUAY", "PERU", "PHILIPPINES", "PITCAIRN", "POLAND", "PORTUGAL", "PUERTORICO", "QATAR",
    "REUNION", "ROMANIA", "RUSSIANFEDERATION", "RWANDA", "SAINTKITTSANDNEVIS", "SAINTLUCIA",
    "SAINTVINCENTANDTHEGRENADINES", "SAMOA", "SANMARINO", "SAOTOMEANDPRINCIPE", "SAUDIARABIA", "SENEGAL",
    "SERBIA", "SEYCHELLES", "SIERRALEONE", "SINGAPORE", "SLOVAKIA", "SLOVAKREPUBLIC", "SLOVENIA", "SOLOMONISLANDS",
    "SOMALIA", "SOUTHAFRICA", "SOUTHSUDAN", "SOUTHGEORGIAANDSOUTHSS", "SPAIN", "SRILANKA", "STHELENA",
    "STPIERREANDMIQUELON", "SUDAN", "SURINAME", "SVALBARDANDJANMAYENISLANDS", "SWAZILAND", "SWEDEN",
    "SWITZERLAND", "SYRIANARABREPUBLIC", "TAIWAN", "TAJIKISTAN", "TANZANIA", "UNITEDREPUBLICOFTANZANIA",
    "THAILAND", "TOGO", "TOKELAU", "TONGA", "TRINIDADANDTOBAGO", "TUNISIA", "TURKEY", "TURKMENISTAN",
    "TURKSANDCAICOSISLANDS", "TUVALU", "UGANDA", "UKRAINE", "UNITEDARABEMIRATES", "UNITEDKINGDOM",
    "UNITEDSTATES", "USMINORISLANDS", "URUGUAY", "UZBEKISTAN", "VANUATU", "VENEZUELA", "VIETNAM",
    "VIRGINISLANDSBRITISH", "VIRGINISLANDSUS", "WALLISANDFUTUNAISLANDS", "WESTERNSAHARA", "YEMEN",
    "ZAMBIA", "ZIMBABWE"
]

country_names_readable = [
    "Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica",
    "Antigua And Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
    "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia",
    "Bosnia And Herzegowina", "Bosnia", "Herzegowina", "Botswana", "Bouvet Island", "Norway", "Brazil",
    "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia",
    "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China",
    "Christmas Island", "Cocos Islands", "Colombia", "Comoros", "Congo", "Congo, The Drc", "Cook Islands", "Costa Rica",
    "Cote D'ivoire", "Croatia", "Hrvatska", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica",
    "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
    "Ethiopia", "Falkland Islands", "Malvinas", "Faroe Islands", "Fiji", "Finland", "France", "France, Metropolitan",
    "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany",
    "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea",
    "Guinea-bissau", "Guyana", "Haiti", "Heard And Mc Donald Islands", "Holy See", "Vatican City State", "Honduras",
    "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica",
    "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, D.p.r.o.", "North Korea", "Korea, Republic Of",
    "South Korea", "Republic Of Korea",
    "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libyan Arab Jamahiriya",
    "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives",
    "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico",
    "Micronesia, Federated States Of", "Federated States Of Micronesia", "Moldova, Republic Of", "Republic Of Moldova",
    "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Burma", "Namibia", "Nauru",
    "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria",
    "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama",
    "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar",
    "Reunion", "Romania", "Russian Federation", "Rwanda", "Saint Kitts And Nevis", "Saint Lucia",
    "Saint Vincent And The Grenadines", "Samoa", "San Marino", "Sao Tome And Principe", "Saudi Arabia", "Senegal",
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovak Republic", "Slovenia", "Solomon Islands",
    "Somalia", "South Africa", "South Sudan", "South Georgia And South S.S.", "Spain", "Sri Lanka", "St. Helena",
    "St. Pierre And Miquelon", "Sudan", "Suriname", "Svalbard and Jan Mayen Islands", "Swaziland", "Sweden",
    "Switzerland", "Syrian Arab Republic", "Taiwan", "Tajikistan", "Tanzania", "United Republic Of Tanzania",
    "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad And Tobago", "Tunisia", "Turkey", "Turkmenistan",
    "Turks And Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
    "United States", "U.S. Minor Islands", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam",
    "Virgin Islands (British)", "Virgin Islands (U.S.)", "Wallis And Futuna Islands", "Western Sahara", "Yemen",
    "Zambia", "Zimbabwe"
]

us_states_names = [
    "ALABAMA", "ALASKA", "ARIZONA", "ARKANSAS", "CALIFORNIA", "COLORADO", "CONNECTICUT", "DELAWARE", "FLORIDA",
    "GEORGIA", "HAWAII", "IDAHO", "ILLINOIS", "INDIANA", "IOWA", "KANSAS", "KENTUCKY", "LOUISIANA", "MAINE", "MARYLAND",
    "MASSACHUSETTS", "MICHIGAN", "MINNESOTA", "MISSISSIPPI", "MISSOURI", "MONTANA", "NEBRASKA", "NEVADA",
    "NEWHAMPSHIRE", "NEWJERSEY", "NEWMEXICO", "NEWYORK", "NORTHCAROLINA", "NORTHDAKOTA", "OHIO", "OKLAHOMA", "OREGON",
    "PENNSYLVANIA", "RHODEISLAND", "SOUTHCAROLINA", "SOUTHDAKOTA", "TENNESSEE", "TEXAS", "UTAH", "VERMONT", "VIRGINIA",
    "WASHINGTON", "WESTVIRGINIA", "WISCONSIN", "WYOMING"
]

us_states_names_readable = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida",
    "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
    "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
    "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

us_states_codes = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME",
    "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA",
    "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

canada_states_names = [
    "ALBERTA", "BRITISHCOLUMBIA", "MANITOBA", "NEWBRUNSWICK", "NEWFOUNDLANDANDLABRADOR", "NOVASCOTIA",
    "NORTHWESTTERRITORIES", "NUNAVUT", "ONTARIO", "PRINCEEDWARDISLAND", "QUEBEC", "SASKATCHEWAN", "YUKON"
]

canada_states_names_readable = [
    "Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Nova Scotia",
    "Northwest Territories", "Nunavut", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon"
]

canada_states_codes = [
    "AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"
]


class LM(object):

    def __init__(self):
        self.name = "Location Manipulation"

    @staticmethod
    def clean_location(x):
        stripped = x.strip().lower()
        stripped = SM.alpha_numeric(stripped).strip()
        return SM.toTitleCaseCleaned(stripped)

    @staticmethod
    def get_only_city_name(x):
        values = x.split(" ")
        if len(values) > 1 and len(values[len(values) - 1]) == 2:
            return " ".join(values[0:len(values) - 1])
        return x

    @staticmethod
    def standard_country_code(country):
        if len(country) == 0:
            return ''

        country = country.upper()
        if len(country) == 2:
            try:
                idx = country_codes_2.index(country)
                return country
            except ValueError:
                idx = -1
        if len(country) == 3:
            try:
                idx = country_codes_3.index(country)
                code = country_codes_2[idx]
                return code
            except ValueError:
                idx = -1
        try:
            country = SM.alpha_only(country).upper()
            idx = country_names.index(country)
            code = country_codes_2[idx]
            return code
        except ValueError:
            return ''

    @staticmethod
    def standard_country_name(country):
        if len(country) == 0:
            return ''

        country = country.upper()
        if len(country) == 2:
            try:
                idx = country_codes_2.index(country)
                return country_names_readable[idx]
            except ValueError:
                idx = -1
        if len(country) == 3:
            try:
                idx = country_codes_3.index(country)
                return country_names_readable[idx]
            except ValueError:
                idx = -1
        try:
            country = SM.alpha_only(country).upper()
            idx = country_names.index(country)
            return country_names_readable[idx]
        except ValueError:
            return ''

    @staticmethod
    def clean_country(country):
        clean_country = LM.standard_country_name(country)
        if clean_country == '':
            return country
        return clean_country

    @staticmethod
    def standard_state_code(country, state):
        if len(state) == 0:
            return ''

        codes_arr = []
        names_arr = []

        if country == "US" or country == "United States":
            codes_arr = us_states_codes
            names_arr = us_states_names

        if country == "CA" or country == "Canada":
            codes_arr = canada_states_codes
            names_arr = canada_states_names

        if len(codes_arr) > 0:
            state = state.upper()
            if len(state) == 2:
                try:
                    idx = codes_arr.index(state)
                    return state
                except ValueError:
                    idx = -1

            try:
                state = SM.alpha_only(state).upper()
                idx = names_arr.index(state)
                code = codes_arr[idx]
                return code
            except ValueError:
                return ''

        return state

    @staticmethod
    def standardize_state_name(country, state):
        if len(state) == 0:
            return ''

        codes_arr = []
        names_arr = []
        names_readable_arr = []

        if country == "US" or country == "United States":
            codes_arr = us_states_codes
            names_arr = us_states_names
            names_readable_arr = us_states_names_readable

        if country == "CA" or country == "Canada":
            codes_arr = canada_states_codes
            names_arr = canada_states_names
            names_readable_arr = canada_states_names_readable

        if len(codes_arr) > 0:
            state = state.upper()
            if len(state) == 2:
                try:
                    idx = codes_arr.index(state)
                    return names_readable_arr[idx]
                except ValueError:
                    idx = -1

            try:
                state = SM.alpha_only(state).upper()
                idx = names_arr.index(state)
                return names_readable_arr[idx]
            except ValueError:
                return ''

        return state

    @staticmethod
    def get_decimal_coodinate(lat):
        result = 0
        x = SM.get_string(lat, 0, 1)
        if x:
            result += int(x)
        x = SM.get_string(lat, 2, 3)
        if x:
            result += int(x)/float("60")
        x = SM.get_string(lat, 4, 5)
        if x:
            result += int(x)/float("3600")
        return str(result)

    @staticmethod
    def get_decimal_coodinate(lat):
        result = 0
        x = SM.get_string(lat, 0, 1)
        if x:
            result += int(x)
        x = SM.get_string(lat, 2, 3)
        if x:
            result += int(x)/float("60")
        x = SM.get_string(lat, 4, 5)
        if x:
            result += int(x)/float("3600")
        return str(result)

    @staticmethod
    def parse_latitude_longitude(latlon):
        # Examples: LATMIN:2310N04350W
        # LATDEC:351025.3N0790125.7W
        idx = latlon.find(":")
        if idx != -1:
            ltype = latlon[0:idx]
            latlon = latlon[idx+1:]
            idx = latlon.find("-")
            if idx != -1:
                lat = latlon[0:idx-1]
                lon = latlon[idx+2:]
            else:
                latlon = re.sub('[^0-9\.]+', ',', latlon)
                latlons = latlon.split(",")
                lat = latlons[0]
                lon = latlons[1]
            if ltype == "LATMIN" or ltype == "LATDEC":
                return [LM.get_decimal_coodinate(lat), LM.get_decimal_coodinate(lon)]
            else:
                return [lat, lon]

        return [-1, -1]

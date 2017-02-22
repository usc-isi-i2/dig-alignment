__author__ = 'amandeep'

import re

us_area_codes = ["211", "242", "246", "264", "268", "284", "311", "345", "411", "441", "456", "473", "500", "511", "555", "600", "611", "649", "664", "684", "700", "710", "711", "758", "767", "784", "800", "809", "811", "822", "829", "833", "844", "849", "855", "866", "868", "869", "876", "877", "880", "881", "882", "888", "898", "900", "911", "976", "999", "52 55", "403", "587", "780", "825", "907", "205", "251", "256", "334", "479", "501", "870", "480", "520", "602", "623", "928", "236", "250", "604", "778", "209", "213", "310", "323", "341", "369", "408", "415", "424", "442", "510", "530", "559", "562", "619", "626", "627", "628", "650", "657", "661", "669", "707", "714", "747", "760", "764", "805", "818", "831", "858", "909", "916", "925", "935", "949", "951", "303", "719", "720", "970", "203", "475", "860", "959", "202", "302", "239", "305", "321", "352", "386", "407", "561", "689", "727", "754", "772", "786", "813", "850", "863", "904", "927", "941", "954", "229", "404", "470", "478", "678", "706", "762", "770", "912", "671", "808", "319", "515", "563", "641", "712", "208", "217", "224", "309", "312", "331", "464", "618", "630", "708", "773", "779", "815", "847", "872", "219", "260", "317", "574", "765", "812", "316", "620", "785", "913", "270", "502", "606", "859", "225", "318", "337", "504", "985", "339", "351", "413", "508", "617", "774", "781", "857", "978", "204", "431", "240", "301", "410", "443", "207", "231", "248", "269", "278", "313", "517", "586", "616", "679", "734", "810", "906", "947", "989", "218", "320", "507", "612", "651", "763", "952", "314", "417", "557", "573", "636", "660", "816", "975", "670", "228", "601", "662", "769", "406", "506", "252", "336", "704", "828", "910", "919", "980", "984", "701", "308", "402", "603", "201", "551", "609", "732", "848", "856", "862", "908", "973", "709", "505", "575", "957", "782", "902", "702", "775", "212", "315", "347", "516", "518", "585", "607", "631", "646", "716", "718", "845", "914", "917", "216", "234", "283", "330", "380", "419", "440", "513", "567", "614", "740", "937", "405", "539", "580", "918", "226", "289", "343", "365", "416", "437", "519", "548", "613", "647", "705", "807", "905", "503", "541", "971", "215", "267", "412", "484", "570", "610", "717", "724", "814", "835", "878", "787", "939", "418", "438", "450", "481", "514", "579", "819", "873", "401", "803", "843", "864", "605", "306", "639", "423", "615", "731", "865", "901", "931", "210", "214", "254", "281", "325", "361", "409", "430", "432", "469", "512", "682", "713", "737", "806", "817", "830", "832", "903", "915", "936", "940", "956", "972", "979", "385", "435", "801", "276", "434", "540", "571", "703", "757", "804", "340", "802", "206", "253", "360", "425", "509", "564", "262", "414", "608", "715", "920", "304", "681", "307", "867"]
country_dialing_codes = [
    "93", "355", "213", "1 684", "376", "244", "1 264", "672", "1 268", "54", "374", "297", "61", "43", "994", "1 242",
    "973", "880", "1 246", "375", "32", "501", "229", "1 441", "975", "591", "387", "387", "387", "387", "61", "61",
    "55", "246", "672", "359", "226", "257", "855", "237", "1", "238", "1 345", "236", "235", "56", "86", "61", "891",
    "57", "269", "242", "243", "682", "506", "225", "385", "385", "53", "357", "420", "45", "253", "1 767", "1 809",
    "670", "593", "20", "503", "240", "291", "372", "251", "500", "500", "298", "679", "358", "33", "33", "594", "689",
    "262", "241", "220", "995", "49", "233", "350", "30", "299", "1 473", "590", "1 671", "502", "224", "245", "592",
    "509", "672", "379", "379", "504", "852", "36", "354", "91", "62", "98", "964", "353", "972", "39", "1 876", "81",
    "962", "7", "254", "686", "850", "850", "82", "82", "82", "965", "996", "856", "371", "961", "266", "231", "218",
    "423", "370",
    "352", "853", "389", "261", "265", "60", "960", "223", "356", "692", "596", "222", "230", "262", "52", "691", "691",
    "373", "373", "377", "976", "382", "1 664", "212", "258", "95", "95", "264", "674", "977", "31", "599", "687", "64",
    "505", "227", "234", "683", "672", "1 670", "47", "968", "92", "680", "507", "675", "595", "51", "63", "870", "48",
    "351", "1", "974", "262", "40", "7", "250", "1 869", "1 758", "1 784", "685", "378", "239", "966", "221", "381",
    "248", "232", "65", "421", "421", "386", "677", "252", "27", "211", "500", "34", "94", "290", "508", "249", "597",
    "47", "268", "46", "41", "963", "886", "992", "255", "255", "66", "228", "690", "676", "1 868", "216", "90", "993",
    "1 649", "688", "256", "380", "971", "44", "1", "1", "598", "998", "678", "58", "84", "1 284", "1 430", "681",
    "212", "967", "260", "263"
]
USPhonePattern = re.compile(r"^\([0-9]{3}\) [0-9]{3}\-[0-9]{4}$")

country_phone_dial_codes = [{"dialing_code": "93", "code_2": "AF", "code_3": "AFG", "name": "Afghanistan"},
                            {"dialing_code": "355", "code_2": "AL", "code_3": "ALB", "name": "Albania"},
                            {"dialing_code": "213", "code_2": "DZ", "code_3": "DZA", "name": "Algeria"},
                            {"dialing_code": "1-684", "code_2": "AS", "code_3": "ASM", "name": "American Samoa"},
                            {"dialing_code": "376", "code_2": "AD", "code_3": "AND", "name": "Andorra"},
                            {"dialing_code": "244", "code_2": "AO", "code_3": "AGO", "name": "Angola"},
                            {"dialing_code": "1-264", "code_2": "AI", "code_3": "AIA", "name": "Anguilla"},
                            {"dialing_code": "672", "code_2": "AQ", "code_3": "ATA", "name": "Antarctica"},
                            {"dialing_code": "1-268", "code_2": "AG", "code_3": "ATG", "name": "Antigua and Barbuda"},
                            {"dialing_code": "54", "code_2": "AR", "code_3": "ARG", "name": "Argentina"},
                            {"dialing_code": "374", "code_2": "AM", "code_3": "ARM", "name": "Armenia"},
                            {"dialing_code": "297", "code_2": "AW", "code_3": "ABW", "name": "Aruba"},
                            {"dialing_code": "61", "code_2": "AU", "code_3": "AUS", "name": "Australia"},
                            {"dialing_code": "43", "code_2": "AT", "code_3": "AUT", "name": "Austria"},
                            {"dialing_code": "994", "code_2": "AZ", "code_3": "AZE", "name": "Azerbaijan"},
                            {"dialing_code": "1-242", "code_2": "BS", "code_3": "BHS", "name": "Bahamas"},
                            {"dialing_code": "973", "code_2": "BH", "code_3": "BHR", "name": "Bahrain"},
                            {"dialing_code": "880", "code_2": "BD", "code_3": "BGD", "name": "Bangladesh"},
                            {"dialing_code": "1-246", "code_2": "BB", "code_3": "BRB", "name": "Barbados"},
                            {"dialing_code": "375", "code_2": "BY", "code_3": "BLR", "name": "Belarus"},
                            {"dialing_code": "32", "code_2": "BE", "code_3": "BEL", "name": "Belgium"},
                            {"dialing_code": "501", "code_2": "BZ", "code_3": "BLZ", "name": "Belize"},
                            {"dialing_code": "229", "code_2": "BJ", "code_3": "BEN", "name": "Benin"},
                            {"dialing_code": "1-441", "code_2": "BM", "code_3": "BMU", "name": "Bermuda"},
                            {"dialing_code": "975", "code_2": "BT", "code_3": "BTN", "name": "Bhutan"},
                            {"dialing_code": "591", "code_2": "BO", "code_3": "BOL", "name": "Bolivia"},
                            {"dialing_code": "599", "code_2": "BQ", "code_3": "BES", "name": "Bonaire"},
                            {"dialing_code": "387", "code_2": "BA", "code_3": "BIH", "name": "Bosnia and Herzegovina"},
                            {"dialing_code": "267", "code_2": "BW", "code_3": "BWA", "name": "Botswana"},
                            {"dialing_code": "47", "code_2": "BV", "code_3": "BVT", "name": "Bouvet Island"},
                            {"dialing_code": "55", "code_2": "BR", "code_3": "BRA", "name": "Brazil"},
                            {"dialing_code": "246", "code_2": "IO", "code_3": "IOT", "name": "British Indian Ocean "
                                                                                             "Territory"},
                            {"dialing_code": "673", "code_2": "BN", "code_3": "BRN", "name": "Brunei Darussalam"},
                            {"dialing_code": "359", "code_2": "BG", "code_3": "BGR", "name": "Bulgaria"},
                            {"dialing_code": "226", "code_2": "BF", "code_3": "BFA", "name": "Burkina Faso"},
                            {"dialing_code": "257", "code_2": "BI", "code_3": "BDI", "name": "Burundi"},
                            {"dialing_code": "855", "code_2": "KH", "code_3": "KHM", "name": "Cambodia"},
                            {"dialing_code": "237", "code_2": "CM", "code_3": "CMR", "name": "Cameroon"},
                            {"dialing_code": "1", "code_2": "CA", "code_3": "CAN", "name": "Canada"},
                            {"dialing_code": "238", "code_2": "CV", "code_3": "CPV", "name": "Cape Verde"},
                            {"dialing_code": "1-345", "code_2": "KY", "code_3": "CYM", "name": "Cayman Islands"},
                            {"dialing_code": "236", "code_2": "CF", "code_3": "CAF", "name": "Central African "
                                                                                             "Republic"},
                            {"dialing_code": "235", "code_2": "TD", "code_3": "TCD", "name": "Chad"},
                            {"dialing_code": "56", "code_2": "CL", "code_3": "CHL", "name": "Chile"},
                            {"dialing_code": "86", "code_2": "CN", "code_3": "CHN", "name": "China"},
                            {"dialing_code": "61", "code_2": "CX", "code_3": "CXR", "name": "Christmas Island"},
                            {"dialing_code": "61", "code_2": "CC", "code_3": "CCK", "name": "Cocos (Keeling) Islands"},
                            {"dialing_code": "57", "code_2": "CO", "code_3": "COL", "name": "Colombia"},
                            {"dialing_code": "269", "code_2": "KM", "code_3": "COM", "name": "Comoros"},
                            {"dialing_code": "242", "code_2": "CG", "code_3": "COG", "name": "Congo"},
                            {"dialing_code": "243", "code_2": "CD", "code_3": "COD", "name": "Democratic "
                                                                                             "Republic of the Congo"},
                            {"dialing_code": "682", "code_2": "CK", "code_3": "COK", "name": "Cook Islands"},
                            {"dialing_code": "506", "code_2": "CR", "code_3": "CRI", "name": "Costa Rica"},
                            {"dialing_code": "385", "code_2": "HR", "code_3": "HRV", "name": "Croatia"},
                            {"dialing_code": "53", "code_2": "CU", "code_3": "CUB", "name": "Cuba"},
                            {"dialing_code": "599", "code_2": "CW", "code_3": "CUW", "name": "Cura\u00c3\u00a7ao"},
                            {"dialing_code": "357", "code_2": "CY", "code_3": "CYP", "name": "Cyprus"},
                            {"dialing_code": "420", "code_2": "CZ", "code_3": "CZE", "name": "Czech Republic"},
                            {"dialing_code": "225", "code_2": "CI", "code_3": "CIV", "name": "C\u00c3\u00b4te "
                                                                                             "d'Ivoire"},
                            {"dialing_code": "45", "code_2": "DK", "code_3": "DNK", "name": "Denmark"},
                            {"dialing_code": "253", "code_2": "DJ", "code_3": "DJI", "name": "Djibouti"},
                            {"dialing_code": "1-767", "code_2": "DM", "code_3": "DMA", "name": "Dominica"},
                            {"dialing_code": "1-809,1-829,1-849", "code_2": "DO", "code_3": "DOM", "name": "Dominican "
                                                                                                           "Republic"},
                            {"dialing_code": "593", "code_2": "EC", "code_3": "ECU", "name": "Ecuador"},
                            {"dialing_code": "20", "code_2": "EG", "code_3": "EGY", "name": "Egypt"},
                            {"dialing_code": "503", "code_2": "SV", "code_3": "SLV", "name": "El Salvador"},
                            {"dialing_code": "240", "code_2": "GQ", "code_3": "GNQ", "name": "Equatorial Guinea"},
                            {"dialing_code": "291", "code_2": "ER", "code_3": "ERI", "name": "Eritrea"},
                            {"dialing_code": "372", "code_2": "EE", "code_3": "EST", "name": "Estonia"},
                            {"dialing_code": "251", "code_2": "ET", "code_3": "ETH", "name": "Ethiopia"},
                            {"dialing_code": "500", "code_2": "FK", "code_3": "FLK", "name": "Falkland Islands "
                                                                                             "(Malvinas)"},
                            {"dialing_code": "298", "code_2": "FO", "code_3": "FRO", "name": "Faroe Islands"},
                            {"dialing_code": "679", "code_2": "FJ", "code_3": "FJI", "name": "Fiji"},
                            {"dialing_code": "358", "code_2": "FI", "code_3": "FIN", "name": "Finland"},
                            {"dialing_code": "33", "code_2": "FR", "code_3": "FRA", "name": "France"},
                            {"dialing_code": "594", "code_2": "GF", "code_3": "GUF", "name": "French Guiana"},
                            {"dialing_code": "689", "code_2": "PF", "code_3": "PYF", "name": "French Polynesia"},
                            {"dialing_code": "262", "code_2": "TF", "code_3": "ATF", "name": "French Southern "
                                                                                             "Territories"},
                            {"dialing_code": "241", "code_2": "GA", "code_3": "GAB", "name": "Gabon"},
                            {"dialing_code": "220", "code_2": "GM", "code_3": "GMB", "name": "Gambia"},
                            {"dialing_code": "995", "code_2": "GE", "code_3": "GEO", "name": "Georgia"},
                            {"dialing_code": "49", "code_2": "DE", "code_3": "DEU", "name": "Germany"},
                            {"dialing_code": "233", "code_2": "GH", "code_3": "GHA", "name": "Ghana"},
                            {"dialing_code": "350", "code_2": "GI", "code_3": "GIB", "name": "Gibraltar"},
                            {"dialing_code": "30", "code_2": "GR", "code_3": "GRC", "name": "Greece"},
                            {"dialing_code": "299", "code_2": "GL", "code_3": "GRL", "name": "Greenland"},
                            {"dialing_code": "1-473", "code_2": "GD", "code_3": "GRD", "name": "Grenada"},
                            {"dialing_code": "590", "code_2": "GP", "code_3": "GLP", "name": "Guadeloupe"},
                            {"dialing_code": "1-671", "code_2": "GU", "code_3": "GUM", "name": "Guam"},
                            {"dialing_code": "502", "code_2": "GT", "code_3": "GTM", "name": "Guatemala"},
                            {"dialing_code": "44", "code_2": "GG", "code_3": "GGY", "name": "Guernsey"},
                            {"dialing_code": "224", "code_2": "GN", "code_3": "GIN", "name": "Guinea"},
                            {"dialing_code": "245", "code_2": "GW", "code_3": "GNB", "name": "Guinea-Bissau"},
                            {"dialing_code": "592", "code_2": "GY", "code_3": "GUY", "name": "Guyana"},
                            {"dialing_code": "509", "code_2": "HT", "code_3": "HTI", "name": "Haiti"},
                            {"dialing_code": "672", "code_2": "HM", "code_3": "HMD", "name": "Heard Island and "
                                                                                             "McDonald Mcdonald Islands"},
                            {"dialing_code": "379", "code_2": "VA", "code_3": "VAT", "name": "Holy See (Vatican "
                                                                                             "City State)"},
                            {"dialing_code": "504", "code_2": "HN", "code_3": "HND", "name": "Honduras"},
                            {"dialing_code": "852", "code_2": "HK", "code_3": "HKG", "name": "Hong Kong"},
                            {"dialing_code": "36", "code_2": "HU", "code_3": "HUN", "name": "Hungary"},
                            {"dialing_code": "354", "code_2": "IS", "code_3": "ISL", "name": "Iceland"},
                            {"dialing_code": "91", "code_2": "IN", "code_3": "IND", "name": "India"},
                            {"dialing_code": "62", "code_2": "ID", "code_3": "IDN", "name": "Indonesia"},
                            {"dialing_code": "98", "code_2": "IR", "code_3": "IRN", "name": "Iran, Islamic "
                                                                                            "Republic of"},
                            {"dialing_code": "964", "code_2": "IQ", "code_3": "IRQ", "name": "Iraq"},
                            {"dialing_code": "353", "code_2": "IE", "code_3": "IRL", "name": "Ireland"},
                            {"dialing_code": "44", "code_2": "IM", "code_3": "IMN", "name": "Isle of Man"},
                            {"dialing_code": "972", "code_2": "IL", "code_3": "ISR", "name": "Israel"},
                            {"dialing_code": "39", "code_2": "IT", "code_3": "ITA", "name": "Italy"},
                            {"dialing_code": "1-876", "code_2": "JM", "code_3": "JAM", "name": "Jamaica"},
                            {"dialing_code": "81", "code_2": "JP", "code_3": "JPN", "name": "Japan"},
                            {"dialing_code": "44", "code_2": "JE", "code_3": "JEY", "name": "Jersey"},
                            {"dialing_code": "962", "code_2": "JO", "code_3": "JOR", "name": "Jordan"},
                            {"dialing_code": "7", "code_2": "KZ", "code_3": "KAZ", "name": "Kazakhstan"},
                            {"dialing_code": "254", "code_2": "KE", "code_3": "KEN", "name": "Kenya"},
                            {"dialing_code": "686", "code_2": "KI", "code_3": "KIR", "name": "Kiribati"},
                            {"dialing_code": "850", "code_2": "KP", "code_3": "PRK", "name": "Korea, Democratic "
                                                                                             "People's Republic of"},
                            {"dialing_code": "82", "code_2": "KR", "code_3": "KOR", "name": "Korea, Republic of"},
                            {"dialing_code": "965", "code_2": "KW", "code_3": "KWT", "name": "Kuwait"},
                            {"dialing_code": "996", "code_2": "KG", "code_3": "KGZ", "name": "Kyrgyzstan"},
                            {"dialing_code": "856", "code_2": "LA", "code_3": "LAO", "name": "Lao People's "
                                                                                             "Democratic Republic"},
                            {"dialing_code": "371", "code_2": "LV", "code_3": "LVA", "name": "Latvia"},
                            {"dialing_code": "961", "code_2": "LB", "code_3": "LBN", "name": "Lebanon"},
                            {"dialing_code": "266", "code_2": "LS", "code_3": "LSO", "name": "Lesotho"},
                            {"dialing_code": "231", "code_2": "LR", "code_3": "LBR", "name": "Liberia"},
                            {"dialing_code": "218", "code_2": "LY", "code_3": "LBY", "name": "Libya"},
                            {"dialing_code": "423", "code_2": "LI", "code_3": "LIE", "name": "Liechtenstein"},
                            {"dialing_code": "370", "code_2": "LT", "code_3": "LTU", "name": "Lithuania"},
                            {"dialing_code": "352", "code_2": "LU", "code_3": "LUX", "name": "Luxembourg"},
                            {"dialing_code": "853", "code_2": "MO", "code_3": "MAC", "name": "Macao"},
                            {"dialing_code": "389", "code_2": "MK", "code_3": "MKD", "name": "Macedonia, the Former "
                                                                                             "Yugoslav Republic of"},
                            {"dialing_code": "261", "code_2": "MG", "code_3": "MDG", "name": "Madagascar"},
                            {"dialing_code": "265", "code_2": "MW", "code_3": "MWI", "name": "Malawi"},
                            {"dialing_code": "60", "code_2": "MY", "code_3": "MYS", "name": "Malaysia"},
                            {"dialing_code": "960", "code_2": "MV", "code_3": "MDV", "name": "Maldives"},
                            {"dialing_code": "223", "code_2": "ML", "code_3": "MLI", "name": "Mali"},
                            {"dialing_code": "356", "code_2": "MT", "code_3": "MLT", "name": "Malta"},
                            {"dialing_code": "692", "code_2": "MH", "code_3": "MHL", "name": "Marshall Islands"},
                            {"dialing_code": "596", "code_2": "MQ", "code_3": "MTQ", "name": "Martinique"},
                            {"dialing_code": "222", "code_2": "MR", "code_3": "MRT", "name": "Mauritania"},
                            {"dialing_code": "230", "code_2": "MU", "code_3": "MUS", "name": "Mauritius"},
                            {"dialing_code": "262", "code_2": "YT", "code_3": "MYT", "name": "Mayotte"},
                            {"dialing_code": "52", "code_2": "MX", "code_3": "MEX", "name": "Mexico"},
                            {"dialing_code": "691", "code_2": "FM", "code_3": "FSM", "name": "Micronesia, Federated "
                                                                                             "States of"},
                            {"dialing_code": "373", "code_2": "MD", "code_3": "MDA", "name": "Moldova, Republic of"},
                            {"dialing_code": "377", "code_2": "MC", "code_3": "MCO", "name": "Monaco"},
                            {"dialing_code": "976", "code_2": "MN", "code_3": "MNG", "name": "Mongolia"},
                            {"dialing_code": "382", "code_2": "ME", "code_3": "MNE", "name": "Montenegro"},
                            {"dialing_code": "1-664", "code_2": "MS", "code_3": "MSR", "name": "Montserrat"},
                            {"dialing_code": "212", "code_2": "MA", "code_3": "MAR", "name": "Morocco"},
                            {"dialing_code": "258", "code_2": "MZ", "code_3": "MOZ", "name": "Mozambique"},
                            {"dialing_code": "95", "code_2": "MM", "code_3": "MMR", "name": "Myanmar"},
                            {"dialing_code": "264", "code_2": "NA", "code_3": "NAM", "name": "Namibia"},
                            {"dialing_code": "674", "code_2": "NR", "code_3": "NRU", "name": "Nauru"},
                            {"dialing_code": "977", "code_2": "NP", "code_3": "NPL", "name": "Nepal"},
                            {"dialing_code": "31", "code_2": "NL", "code_3": "NLD", "name": "Netherlands"},
                            {"dialing_code": "687", "code_2": "NC", "code_3": "NCL", "name": "New Caledonia"},
                            {"dialing_code": "64", "code_2": "NZ", "code_3": "NZL", "name": "New Zealand"},
                            {"dialing_code": "505", "code_2": "NI", "code_3": "NIC", "name": "Nicaragua"},
                            {"dialing_code": "227", "code_2": "NE", "code_3": "NER", "name": "Niger"},
                            {"dialing_code": "234", "code_2": "NG", "code_3": "NGA", "name": "Nigeria"},
                            {"dialing_code": "683", "code_2": "NU", "code_3": "NIU", "name": "Niue"},
                            {"dialing_code": "672", "code_2": "NF", "code_3": "NFK", "name": "Norfolk Island"},
                            {"dialing_code": "1-670", "code_2": "MP", "code_3": "MNP", "name": "Northern Mariana "
                                                                                               "Islands"},
                            {"dialing_code": "47", "code_2": "NO", "code_3": "NOR", "name": "Norway"},
                            {"dialing_code": "968", "code_2": "OM", "code_3": "OMN", "name": "Oman"},
                            {"dialing_code": "92", "code_2": "PK", "code_3": "PAK", "name": "Pakistan"},
                            {"dialing_code": "680", "code_2": "PW", "code_3": "PLW", "name": "Palau"},
                            {"dialing_code": "970", "code_2": "PS", "code_3": "PSE", "name": "Palestine, State of"},
                            {"dialing_code": "507", "code_2": "PA", "code_3": "PAN", "name": "Panama"},
                            {"dialing_code": "675", "code_2": "PG", "code_3": "PNG", "name": "Papua New Guinea"},
                            {"dialing_code": "595", "code_2": "PY", "code_3": "PRY", "name": "Paraguay"},
                            {"dialing_code": "51", "code_2": "PE", "code_3": "PER", "name": "Peru"},
                            {"dialing_code": "63", "code_2": "PH", "code_3": "PHL", "name": "Philippines"},
                            {"dialing_code": "870", "code_2": "PN", "code_3": "PCN", "name": "Pitcairn"},
                            {"dialing_code": "48", "code_2": "PL", "code_3": "POL", "name": "Poland"},
                            {"dialing_code": "351", "code_2": "PT", "code_3": "PRT", "name": "Portugal"},
                            {"dialing_code": "1", "code_2": "PR", "code_3": "PRI", "name": "Puerto Rico"},
                            {"dialing_code": "974", "code_2": "QA", "code_3": "QAT", "name": "Qatar"},
                            {"dialing_code": "40", "code_2": "RO", "code_3": "ROU", "name": "Romania"},
                            {"dialing_code": "7", "code_2": "RU", "code_3": "RUS", "name": "Russian Federation"},
                            {"dialing_code": "250", "code_2": "RW", "code_3": "RWA", "name": "Rwanda"},
                            {"dialing_code": "262", "code_2": "RE", "code_3": "REU", "name": "Reunion"},
                            {"dialing_code": "590", "code_2": "BL", "code_3": "BLM", "name": "Saint Barthalemy"},
                            {"dialing_code": "290", "code_2": "SH", "code_3": "SHN", "name": "Saint Helena"},
                            {"dialing_code": "1-869", "code_2": "KN", "code_3": "KNA", "name": "Saint Kitts and Nevis"},
                            {"dialing_code": "1-758", "code_2": "LC", "code_3": "LCA", "name": "Saint Lucia"},
                            {"dialing_code": "590", "code_2": "MF", "code_3": "MAF", "name": "Saint Martin "
                                                                                             "(French part)"},
                            {"dialing_code": "508", "code_2": "PM", "code_3": "SPM", "name": "Saint Pierre and "
                                                                                             "Miquelon"},
                            {"dialing_code": "1-784", "code_2": "VC", "code_3": "VCT", "name": "Saint Vincent "
                                                                                               "and the Grenadines"},
                            {"dialing_code": "685", "code_2": "WS", "code_3": "WSM", "name": "Samoa"},
                            {"dialing_code": "378", "code_2": "SM", "code_3": "SMR", "name": "San Marino"},
                            {"dialing_code": "239", "code_2": "ST", "code_3": "STP", "name": "Sao Tome and Principe"},
                            {"dialing_code": "966", "code_2": "SA", "code_3": "SAU", "name": "Saudi Arabia"},
                            {"dialing_code": "221", "code_2": "SN", "code_3": "SEN", "name": "Senegal"},
                            {"dialing_code": "381", "code_2": "RS", "code_3": "SRB", "name": "Serbia"},
                            {"dialing_code": "248", "code_2": "SC", "code_3": "SYC", "name": "Seychelles"},
                            {"dialing_code": "232", "code_2": "SL", "code_3": "SLE", "name": "Sierra Leone"},
                            {"dialing_code": "65", "code_2": "SG", "code_3": "SGP", "name": "Singapore"},
                            {"dialing_code": "1-721", "code_2": "SX", "code_3": "SXM", "name": "Sint Maarten "
                                                                                               "(Dutch part)"},
                            {"dialing_code": "421", "code_2": "SK", "code_3": "SVK", "name": "Slovakia"},
                            {"dialing_code": "386", "code_2": "SI", "code_3": "SVN", "name": "Slovenia"},
                            {"dialing_code": "677", "code_2": "SB", "code_3": "SLB", "name": "Solomon Islands"},
                            {"dialing_code": "252", "code_2": "SO", "code_3": "SOM", "name": "Somalia"},
                            {"dialing_code": "27", "code_2": "ZA", "code_3": "ZAF", "name": "South Africa"},
                            {"dialing_code": "500", "code_2": "GS", "code_3": "SGS", "name": "South Georgia and the "
                                                                                             "South Sandwich Islands"},
                            {"dialing_code": "211", "code_2": "SS", "code_3": "SSD", "name": "South Sudan"},
                            {"dialing_code": "34", "code_2": "ES", "code_3": "ESP", "name": "Spain"},
                            {"dialing_code": "94", "code_2": "LK", "code_3": "LKA", "name": "Sri Lanka"},
                            {"dialing_code": "249", "code_2": "SD", "code_3": "SDN", "name": "Sudan"},
                            {"dialing_code": "597", "code_2": "SR", "code_3": "SUR", "name": "Suriname"},
                            {"dialing_code": "47", "code_2": "SJ", "code_3": "SJM", "name": "Svalbard and Jan Mayen"},
                            {"dialing_code": "268", "code_2": "SZ", "code_3": "SWZ", "name": "Swaziland"},
                            {"dialing_code": "46", "code_2": "SE", "code_3": "SWE", "name": "Sweden"},
                            {"dialing_code": "41", "code_2": "CH", "code_3": "CHE", "name": "Switzerland"},
                            {"dialing_code": "963", "code_2": "SY", "code_3": "SYR", "name": "Syrian Arab Republic"},
                            {"dialing_code": "886", "code_2": "TW", "code_3": "TWN", "name": "Taiwan, Province "
                                                                                             "of China"},
                            {"dialing_code": "992", "code_2": "TJ", "code_3": "TJK", "name": "Tajikistan"},
                            {"dialing_code": "255", "code_2": "TZ", "code_3": "TZA", "name": "United Republic "
                                                                                             "of Tanzania"},
                            {"dialing_code": "66", "code_2": "TH", "code_3": "THA", "name": "Thailand"},
                            {"dialing_code": "670", "code_2": "TL", "code_3": "TLS", "name": "Timor-Leste"},
                            {"dialing_code": "228", "code_2": "TG", "code_3": "TGO", "name": "Togo"},
                            {"dialing_code": "690", "code_2": "TK", "code_3": "TKL", "name": "Tokelau"},
                            {"dialing_code": "676", "code_2": "TO", "code_3": "TON", "name": "Tonga"},
                            {"dialing_code": "1-868", "code_2": "TT", "code_3": "TTO", "name": "Trinidad and Tobago"},
                            {"dialing_code": "216", "code_2": "TN", "code_3": "TUN", "name": "Tunisia"},
                            {"dialing_code": "90", "code_2": "TR", "code_3": "TUR", "name": "Turkey"},
                            {"dialing_code": "993", "code_2": "TM", "code_3": "TKM", "name": "Turkmenistan"},
                            {"dialing_code": "1-649", "code_2": "TC", "code_3": "TCA", "name": "Turks and "
                                                                                               "Caicos Islands"},
                            {"dialing_code": "688", "code_2": "TV", "code_3": "TUV", "name": "Tuvalu"},
                            {"dialing_code": "256", "code_2": "UG", "code_3": "UGA", "name": "Uganda"},
                            {"dialing_code": "380", "code_2": "UA", "code_3": "UKR", "name": "Ukraine"},
                            {"dialing_code": "971", "code_2": "AE", "code_3": "ARE", "name": "United Arab Emirates"},
                            {"dialing_code": "44", "code_2": "GB", "code_3": "GBR", "name": "United Kingdom"},
                            {"dialing_code": "1", "code_2": "US", "code_3": "USA", "name": "United States"},
                            {"dialing_code": "1", "code_2": "UM", "code_3": "UMI", "name": "United States Minor "
                                                                                           "Outlying Islands"},
                            {"dialing_code": "598", "code_2": "UY", "code_3": "URY", "name": "Uruguay"},
                            {"dialing_code": "998", "code_2": "UZ", "code_3": "UZB", "name": "Uzbekistan"},
                            {"dialing_code": "678", "code_2": "VU", "code_3": "VUT", "name": "Vanuatu"},
                            {"dialing_code": "58", "code_2": "VE", "code_3": "VEN", "name": "Venezuela"},
                            {"dialing_code": "84", "code_2": "VN", "code_3": "VNM", "name": "Viet Nam"},
                            {"dialing_code": "1-284", "code_2": "VG", "code_3": "VGB", "name": "British Virgin "
                                                                                               "Islands"},
                            {"dialing_code": "1-340", "code_2": "VI", "code_3": "VIR", "name": "US Virgin Islands"},
                            {"dialing_code": "681", "code_2": "WF", "code_3": "WLF", "name": "Wallis and Futuna"},
                            {"dialing_code": "212", "code_2": "EH", "code_3": "ESH", "name": "Western Sahara"},
                            {"dialing_code": "967", "code_2": "YE", "code_3": "YEM", "name": "Yemen"},
                            {"dialing_code": "260", "code_2": "ZM", "code_3": "ZMB", "name": "Zambia"},
                            {"dialing_code": "263", "code_2": "ZW", "code_3": "ZWE", "name": "Zimbabwe"},
                            {"dialing_code": "358", "code_2": "AX", "code_3": "ALA", "name": "Aland Islands"}]


class PM(object):

    def __init__(self):
        self.name = "Phone Manipulation"

    @staticmethod
    def get_country_code(phone, country):
        phone = phone.strip()
        phone = SM.numeric_only(phone)
        country = country.strip()

        if '+' not in phone and '-' not in phone:
            if len(phone) == 10:
                return "1"  # Assumed US country code
            if len(phone) == 11 and phone[0] == '1':
                return "1"

        if phone.startswith("+"):
            if country != '':
                for entry in country_phone_dial_codes:
                    if entry['name'].lower() == country.strip().lower():
                        return entry['dialing_code']
            else:
                if '-' in phone:
                    idx = phone.find('-')
                    return phone[1:idx]

                else:  # this block of code shamelessly copied from get_phone_country_code()
                    for i in range(1, 5):
                        cc = phone[0:i]
                        try:
                            idx = country_dialing_codes.index(cc)
                            return cc
                        except ValueError:
                            idx = -1
                            return ''
        return ''

    @staticmethod
    def is_us_area_code(phonenumber):
        areacode = phonenumber[0:3]
        if areacode in us_area_codes:
            return True
        return False

    @staticmethod
    def phone_exchange(phonenumber):
        """Return the first six digits of a phone if it is a 10-digit USA phone, ie, starts with 1-."""
        result = ''
        if phonenumber.startswith("+1-"):
            tendigitphone = phonenumber[3:]
            if tendigitphone.isdigit() and len(tendigitphone.decode("utf-8")) == 10:
                result = tendigitphone[0:6]
        else:
            if phonenumber.isdigit() and len(phonenumber.decode("utf-8")) == 10:
                if PM.is_us_area_code(phonenumber):
                    result = phonenumber[0:6]
        return result

    @staticmethod
    def get_phone_country_code(phone_clean):
        idx = phone_clean.find("-")
        if idx != -1:
            cc = phone_clean[0:idx]
            if cc.startswith("+"):
                cc = cc[1:]
            return cc
        return ''

    @staticmethod
    def detect_country_code(phonenumber):
        if phonenumber.find("+") == 0:
            ph = phonenumber[1:]
            for i in range(1, 5):
                cc = ph[0:i]
                try:
                    idx = country_dialing_codes.index(cc)
                    return cc
                except ValueError:
                    idx = -1
        return None

    @staticmethod
    def get_local_phone_number(phone_clean):
        idx = phone_clean.find("-")
        if idx != -1:
            return phone_clean[idx+1:]
        return phone_clean

    @staticmethod
    def clean_phone(x):
        """Return the phone as a 10 digit number,
         or as close to that as we can make it.
         Prefix with country code '+1' at the end.
        """
        if len(x) > 0:
            x = x.strip().lower()
            cc = ''
            if x.find("+") == 0:
                end1 = x.find(" ")
                end2 = x.find("-")
                if end1 == -1:
                    end1 = 10000
                if end2 == -1:
                    end2 = 10000
                if end1 != 10000 or end2 != 10000:
                    end = min(end1, end2)
                    cc = x[1:end]
                    ph = SM.numeric_only(x[end+1:])
                else:
                    test_cc = PM.detect_country_code(x)
                    if test_cc:
                        cc = test_cc
                        cc_len = len(cc)
                        ph = x[cc_len+1:]
                        ph = SM.numeric_only(ph)
                    else:
                        ph = SM.numeric_only(x)
            else:
                valid = USPhonePattern.match(x)
                if valid:
                    ph = valid.group()
                    cc = "1"
                    ph = SM.numeric_only(ph)
                else:
                    ph = SM.numeric_only(x)

            # If there are 11 numbers
            if len(ph) == 11 and ph[0] == "1":
                ph = ph[1:]
                cc = "1"

            """
            MAKE THIS BETTER
             if len(cc) > 0:
                ph = "+" + cc + "-" + ph
            """
            return ph
        return ''

    @staticmethod
    def ten_digit_phone_number(x):
        """Return the 10-digit phone number of a phone, as 10 consecutive digits"""
        return re.sub('[^0-9]+', '', x)

    @staticmethod
    def phone_uri(number, country_code):
        """Create a URI for a phone from the number and optional country_code
        If country_code is empty use "x" as the country code, which unfortunately
        makes same number in different countries have the same URI.
        """
        phone = number.strip()
        cc = country_code.strip()
        if phone == '' and cc == '':
            return ''
        if cc == '':
            cc = "x"
        return 'phone/' + cc + '-' + phone

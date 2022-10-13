# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
from obps_dashboard.apps.models import Ganalytics_obpsorg, Ganalytics_obpsorg_countries, Ganalytics_obpsorg_docs
from obps_dashboard.apps.models import Ganalytics_obpsorg_lastmonth, Ganalytics_obpsorg_lastmonth_countries, Ganalytics_obpsorg_lastmonth_docs
from obps_dashboard.apps.models import Ganalytics_obpsystem, Ganalytics_obpsystem_countries
from obps_dashboard.apps.models import Conferences, Newsletter, Newsletter_subscribers_grouth, Newsletter_locations, Communities_engagement
from obps_dashboard.apps.models import Dspace_records, Dspace_collections, Dspace_communities, Dspace_record_disciplines, Dspace_record_bptypes, Dspace_record_adoptiontypes, Dspace_record_eovs, Dspace_record_sdgs
from obps_dashboard.apps.models import Obps_workshops

from django.db.models import Count
from django.db.models import Sum
from django.db import connection

import pandas as pd
import numpy as np
import json


def start(request):

    return render(request, 'index.html')

def get_countries_names_map():
    countries_dict = {
    	'AD': 'Andorra',
    	'AE': 'United Arab Emirates',
    	'AF': 'Afghanistan',
    	'AG': 'Antigua & Barbuda',
    	'AI': 'Anguilla',
    	'AL': 'Albania',
    	'AM': 'Armenia',
    	'AN': 'Netherlands Antilles',
    	'AO': 'Angola',
    	'AQ': 'Antarctica',
    	'AR': 'Argentina',
    	'AS': 'American Samoa',
    	'AT': 'Austria',
    	'AU': 'Australia',
    	'AW': 'Aruba',
    	'AZ': 'Azerbaijan',
    	'BA': 'Bosnia and Herzegovina',
    	'BB': 'Barbados',
    	'BD': 'Bangladesh',
    	'BE': 'Belgium',
    	'BF': 'Burkina Faso',
    	'BG': 'Bulgaria',
    	'BH': 'Bahrain',
    	'BI': 'Burundi',
    	'BJ': 'Benin',
        'BL': 'Saint Barthélemy',
    	'BM': 'Bermuda',
    	'BN': 'Brunei Darussalam',
    	'BO': 'Bolivia',
    	'BR': 'Brazil',
    	'BS': 'Bahama',
    	'BT': 'Bhutan',
    	'BU': 'Burma (no longer exists)',
    	'BV': 'Bouvet Island',
    	'BW': 'Botswana',
    	'BY': 'Belarus',
    	'BZ': 'Belize',
    	'CA': 'Canada',
    	'CC': 'Cocos (Keeling) Islands',
        'CD': 'Democratic Republic of the Congo',
    	'CF': 'Central African Republic',
    	'CG': 'Congo',
    	'CH': 'Switzerland',
    	'CI': 'Côte D\'ivoire (Ivory Coast)',
    	'CK': 'Cook Islands',
    	'CL': 'Chile',
    	'CM': 'Cameroon',
    	'CN': 'China',
    	'CO': 'Colombia',
    	'CR': 'Costa Rica',
    	'CS': 'Czechoslovakia (no longer exists)',
    	'CU': 'Cuba',
    	'CV': 'Cape Verde',
    	'CX': 'Christmas Island',
    	'CY': 'Cyprus',
        'CW': 'Curaçao',
    	'CZ': 'Czech Republic',
    	'DD': 'German Democratic Republic (no longer exists)',
    	'DE': 'Germany',
    	'DJ': 'Djibouti',
    	'DK': 'Denmark',
    	'DM': 'The Commonwealth of Dominica',
    	'DO': 'Dominican Republic',
    	'DZ': 'Algeria',
    	'EC': 'Ecuador',
    	'EE': 'Estonia',
    	'EG': 'Egypt',
    	'EH': 'Western Sahara',
    	'ER': 'Eritrea',
    	'ES': 'Spain',
    	'ET': 'Ethiopia',
    	'FI': 'Finland',
    	'FJ': 'Fiji',
    	'FK': 'Falkland Islands',
    	'FM': 'Micronesia',
    	'FO': 'Faroe Islands',
    	'FR': 'France',
    	'FX': 'France, Metropolitan',
    	'GA': 'Gabon',
    	'GB': 'United Kingdom',
    	'GD': 'Grenada',
    	'GE': 'Georgia',
    	'GF': 'French Guiana',
        'GG': 'Guernsey',
    	'GH': 'Ghana',
    	'GI': 'Gibraltar',
    	'GL': 'Greenland',
    	'GM': 'Gambia',
    	'GN': 'Guinea',
    	'GP': 'Guadeloupe',
    	'GQ': 'The Republic of Equatorial Guinea',
    	'GR': 'Greece',
    	'GS': 'South Georgia and the South Sandwich Islands',
    	'GT': 'Guatemala',
    	'GU': 'Guam',
    	'GW': 'The Republic of Guinea-Bissau',
    	'GY': 'Guyana',
    	'HK': 'Hong Kong',
    	'HM': 'Heard & McDonald Islands',
    	'HN': 'Honduras',
    	'HR': 'Croatia',
    	'HT': 'Haiti',
    	'HU': 'Hungary',
    	'ID': 'Indonesia',
    	'IE': 'Ireland',
    	'IL': 'Israel',
    	'IN': 'India',
    	'IO': 'British Indian Ocean Territory',
    	'IQ': 'Iraq',
    	'IR': 'Islamic Republic of Iran',
    	'IS': 'Iceland',
    	'IT': 'Italy',
        'JE': 'Jersey',
    	'JM': 'Jamaica',
    	'JO': 'Jordan',
    	'JP': 'Japan',
    	'KE': 'Kenya',
    	'KG': 'Kyrgyzstan',
    	'KH': 'Cambodia',
    	'KI': 'Kiribati',
    	'KM': 'Comoros',
    	'KN': 'Saint Kitts and Nevis',
    	'KP': 'Democratic People\'s Republic of Korea',
    	'KR': 'Republic of Korea',
    	'KW': 'Kuwait',
    	'KY': 'Cayman Islands',
    	'KZ': 'Kazakhstan',
    	'LA': 'Lao People\'s Democratic Republic',
    	'LB': 'Lebanon',
    	'LC': 'Saint Lucia',
    	'LI': 'Liechtenstein',
    	'LK': 'Sri Lanka',
    	'LR': 'Liberia',
    	'LS': 'Lesotho',
    	'LT': 'Lithuania',
    	'LU': 'Luxembourg',
    	'LV': 'Latvia',
    	'LY': 'Libya',
    	'MA': 'Morocco',
    	'MC': 'Monaco',
    	'MD': 'Republic of Moldova',
        'ME': 'Montenegro',
        'MF': 'Saint Martin',
    	'MG': 'Madagascar',
    	'MH': 'Marshall Islands',
        'MK': 'North Macedonia',
    	'ML': 'Mali',
    	'MN': 'Mongolia',
    	'MM': 'Myanmar',
    	'MO': 'Macao',
    	'MP': 'Northern Mariana Islands',
    	'MQ': 'Martinique',
    	'MR': 'Mauritania',
    	'MS': 'Montserrat',
    	'MT': 'Malta',
    	'MU': 'Mauritius',
    	'MV': 'Maldives',
    	'MW': 'Malawi',
    	'MX': 'Mexico',
    	'MY': 'Malaysia',
    	'MZ': 'Mozambique',
    	'NA': 'Namibia',
    	'NC': 'New Caledonia',
    	'NE': 'Niger',
    	'NF': 'Norfolk Island',
    	'NG': 'Federal Republic of Nigeria',
    	'NI': 'Nicaragua',
    	'NL': 'Netherlands',
    	'NO': 'Norway',
    	'NP': 'Nepal',
    	'NR': 'Nauru',
    	'NT': 'Neutral Zone (no longer exists)',
    	'NU': 'Niue',
    	'NZ': 'New Zealand',
    	'OM': 'Oman',
    	'PA': 'Panama',
    	'PE': 'Peru',
    	'PF': 'French Polynesia',
    	'PG': 'Independent State of Papua New Guinea',
    	'PH': 'Philippines',
    	'PK': 'Pakistan',
    	'PL': 'Poland',
    	'PM': 'St. Pierre & Miquelon',
    	'PN': 'Pitcairn',
    	'PR': 'Puerto Rico',
        'PS': 'Palestine',
    	'PT': 'Portugal',
    	'PW': 'Palau',
    	'PY': 'Paraguay',
    	'QA': 'Qatar',
    	'RE': 'Réunion',
        'RS': 'Serbia',
    	'RO': 'Romania',
    	'RU': 'Russian Federation',
    	'RW': 'Rwanda',
    	'SA': 'Saudi Arabia',
    	'SB': 'Solomon Islands',
    	'SC': 'Seychelles',
    	'SD': 'Sudan',
    	'SE': 'Sweden',
    	'SG': 'Singapore',
    	'SH': 'St. Helena',
    	'SI': 'Slovenia',
    	'SJ': 'Svalbard and Jan Mayen',
    	'SK': 'Slovakia',
    	'SL': 'Sierra Leone',
    	'SM': 'San Marino',
    	'SN': 'Senegal',
    	'SO': 'Somalia',
    	'SR': 'Suriname',
    	'ST': 'Sao Tome and Principe',
    	'SU': 'Union of Soviet Socialist Republics (no longer exists)',
    	'SV': 'El Salvador',
        'SX': 'Sint Maarten',
    	'SY': 'Syrian Arab Republic',
    	'SZ': 'Eswatini',
    	'TC': 'Turks & Caicos Islands',
    	'TD': 'Chad',
    	'TF': 'French Southern Territories',
    	'TG': 'Togo',
    	'TH': 'Thailand',
    	'TJ': 'Tajikistan',
    	'TK': 'Tokelau',
    	'TM': 'Turkmenistan',
        'TL': 'Timor-Leste',
    	'TN': 'Tunisia',
    	'TO': 'Tonga',
    	'TP': 'East Timor',
    	'TR': 'Turkey',
    	'TT': 'Trinidad & Tobago',
    	'TV': 'Tuvalu',
    	'TW': 'Taiwan, Province of China',
    	'TZ': 'United Republic of Tanzania',
    	'UA': 'Ukraine',
    	'UG': 'Uganda',
    	'UM': 'United States Minor Outlying Islands',
    	'US': 'United States of America',
    	'UY': 'Uruguay',
    	'UZ': 'Uzbekistan',
    	'VA': 'Vatican City State (Holy See)',
    	'VC': 'Saint Vincent and the Grenadines',
    	'VE': 'Venezuela',
    	'VG': 'British Virgin Islands',
    	'VI': 'United States Virgin Islands',
    	'VN': 'Viet Nam',
    	'VU': 'Vanuatu',
    	'WF': 'Wallis & Futuna Islands',
    	'WS': 'Samoa',
    	'YD': 'Democratic Yemen (no longer exists)',
    	'YE': 'Yemen',
    	'YT': 'Mayotte',
    	'YU': 'Yugoslavia',
    	'ZA': 'South Africa',
    	'ZM': 'Zambia',
    	'ZR': 'Zaire',
    	'ZW': 'Zimbabwe',
    	'ZZ': 'Unknown or unspecified country',
    }
    countries_names_map = dict((k.lower(), v) for k, v in countries_dict.items())
    countries_names_map = dict([(value, key) for key, value in countries_names_map.items()])
    return countries_names_map

def dspace_metrics(request):
    count_records = str(Dspace_records.objects.all().count()) # available documents in OBPS
    count_collections = str(Dspace_collections.objects.all().count()) # available collections in OBPS
    count_communities = str(Dspace_communities.objects.all().count()) # available communities in OBPS

    df = pd.DataFrame(list(Dspace_records.objects.all().values('handle', 'title', 'abstract', 'date_submitted', 'maturity_level', 'doi', 'doi_obp', 'submitter_id', 'publisher_place', 'country', 'last_modified', 'year_created')))
    count_submitters = len(df.groupby(df['submitter_id']).count())
    count_dois_obp = len(df.groupby(df['doi_obp']).count())
    print df
    # date submition
    df_group = df.groupby(df['date_submitted'].dt.to_period('M')).count().cumsum()
    dates_list = df_group.index.tolist()
    records_count = df_group['title'].tolist()
    dates_counts = list(zip(dates_list, records_count))

    df['not_dup'] = 1 - df.submitter_id.duplicated()  #Indicator that 'sn' is not duplicated
    series_group_submitters = df.groupby(df['date_submitted'].dt.to_period('M')).not_dup.sum().cumsum()
    df_group_submitters = series_group_submitters.to_frame()
    dates_list = df_group_submitters.index.tolist()
    submitters_count = df_group_submitters['not_dup'].tolist()
    submitters_counts = list(zip(dates_list, submitters_count))

    # date modified
    df_group_last_modified = df.groupby(df['last_modified'].dt.to_period('M')).count().cumsum()
    dates_list_last_modified = df_group_last_modified.index.tolist()
    records_count = df_group_last_modified['title'].tolist()
    dates_counts_last_modified = list(zip(dates_list_last_modified, records_count))

    #year of creation
    df_group_created = df.groupby(df['year_created']).count()
    dates_list_created = df_group_created.index.tolist()
    record_count = df_group_created['title'].tolist()
    dates_created_counts = list(zip(dates_list_created, record_count))

    countries_names_map = get_countries_names_map()
    for i in range(len(df)) :
        if ('United States' in df.loc[i, 'country']) and (df.loc[i, 'country'] != 'United States Virgin Islands') and (df.loc[i, 'country'] != 'United States Minor Outlying Islands'):
            df.loc[i, 'country'] = 'United States of America'

    df_group_countries = df.groupby(df['country']).count()
    df_group_countries_top10 = df_group_countries.sort_values(by='title', ascending=False).head(10)
    countries_list = df_group_countries.index.tolist()

    for i in range(0, len(countries_list)):
        for key in countries_names_map:
            if key in countries_list[i]:
                countries_list[i] = countries_names_map[key]

    records_country_count_list = df_group_countries.title.tolist()
    group_countries_list = list(zip(countries_list, records_country_count_list))
    group_countries_dict = dict(zip(countries_list, records_country_count_list))
    countries = json.dumps(group_countries_dict)

    # Dspace_record_disciplines
    df_disciplines = pd.DataFrame(list(Dspace_record_disciplines.objects.all().values('dspace_object_id','discipline_name')))
    df_group_disciplines = df_disciplines.groupby(df_disciplines['discipline_name']).count()

    total_record_disciplines = len(df_disciplines.drop_duplicates(subset = ['dspace_object_id'],keep = 'first').reset_index(drop = True))
    df_group_disciplines['percent'] = df_group_disciplines['dspace_object_id'] * 100 / total_record_disciplines
    df_group_disciplines['percent'] = df_group_disciplines['percent'].round(decimals=2)
    total_disciplines_percent = df_group_disciplines['percent'].sum()
    disciplines_list = df_group_disciplines.index.tolist()
    percent_list = df_group_disciplines['percent'].tolist()
    disciplines_percent = list(zip(disciplines_list, percent_list))

    # Dspace record maturity levels
    trl_cat_list = ['TRL 1 ', 'TRL 2 ', 'TRL 3 ', 'TRL 4 ', 'TRL 5 ', 'TRL 6 ', 'TRL 7 ', 'TRL 8 ', 'TRL 9 ']
    df_group_trl = df_disciplines.groupby(df['maturity_level']).count()
    df_group_trl = df_group_trl[df_group_trl.index.str.contains('|'.join(trl_cat_list))==True]
    df_group_trl['trl_short'] = df_group_trl.index.str[:5]
    total_trl_count = df_group_trl['dspace_object_id'].sum()
    df_group_trl['percent'] = df_group_trl['dspace_object_id'] * 100 / total_trl_count
    df_group_trl['percent'] = df_group_trl['percent'].round(decimals=2)
    total_trl_percent = df_group_trl['percent'].sum()
    trl_list = df_group_trl.trl_short.tolist()
    percent_list = df_group_trl['percent'].tolist()
    trl_percent = list(zip(trl_list, percent_list))

    # Dspace_record_bptypes
    df_bptypes = pd.DataFrame(list(Dspace_record_bptypes.objects.all().values('dspace_object_id','bp_type')))
    for i in range(len(df_bptypes)):
        if 'Manual' in df_bptypes.loc[i, 'bp_type']:
            df_bptypes.loc[i, 'bp_type'] = 'Manual'
        elif 'Best' in df_bptypes.loc[i, 'bp_type']:
            df_bptypes.loc[i, 'bp_type'] = 'Best Practice'
    df_group_bptypes = df_bptypes.groupby(df_bptypes['bp_type']).count()
    total_record_bptypes = len(df_bptypes.drop_duplicates(subset = ['dspace_object_id'],keep = 'first').reset_index(drop = True))
    df_group_bptypes['percent'] = df_group_bptypes['dspace_object_id'] * 100 / total_record_bptypes
    df_group_bptypes['percent'] = df_group_bptypes['percent'].round(decimals=2)
    total_bptypes_percent = df_group_bptypes['percent'].sum()
    bptypes_list = df_group_bptypes.index.tolist()
    percent_list = df_group_bptypes['percent'].tolist()
    bptypes_percent = list(zip(bptypes_list, percent_list))

    # Dspace_record_bptypes
    df_adoptiontypes = pd.DataFrame(list(Dspace_record_adoptiontypes.objects.all().values('dspace_object_id','adoption_type')))
    df_group_adoptiontypes = df_adoptiontypes.groupby(df_adoptiontypes['adoption_type']).count()
    total_record_adoptiontypes = len(df_adoptiontypes.drop_duplicates(subset = ['dspace_object_id'],keep = 'first').reset_index(drop = True))
    df_group_adoptiontypes['percent'] = df_group_adoptiontypes['dspace_object_id'] * 100 / total_record_adoptiontypes
    df_group_adoptiontypes['percent'] = df_group_adoptiontypes['percent'].round(decimals=2)
    total_adoptiontypes_percent = df_group_adoptiontypes['percent'].sum()
    adoptiontypes_list = df_group_adoptiontypes.index.tolist()
    percent_list = df_group_adoptiontypes['percent'].tolist()
    adoptiontypes_percent = list(zip(adoptiontypes_list, percent_list))

    # Dspace_record_eovs
    df_eovs = pd.DataFrame(list(Dspace_record_eovs.objects.all().values('dspace_object_id','eov')))
    for i in range(len(df_eovs)):
        if df_eovs.loc[i, 'eov'].lower() == 'sea surface temperature':
            df_eovs.loc[i, 'eov'] = 'sea surface temperature'
        elif df_eovs.loc[i, 'eov'].lower() == 'sea surface salinity':
            df_eovs.loc[i, 'eov'] = 'sea surface salinity'
        elif df_eovs.loc[i, 'eov'].lower() == 'surface currents':
            df_eovs.loc[i, 'eov'] = 'surface currents'
        elif 'oxygen' in df_eovs.loc[i, 'eov'].lower():
            df_eovs.loc[i, 'eov'] = 'oxygen'
        elif df_eovs.loc[i, 'eov'].lower() == 'n/a':
            df_eovs.loc[i, 'eov'] = 'N/A'
    df_group_eovs = df_eovs.groupby(df_eovs['eov']).count()
    total_record_eovs = len(df_eovs.drop_duplicates(subset = ['dspace_object_id'],keep = 'first').reset_index(drop = True))
    df_group_eovs['percent'] = df_group_eovs['dspace_object_id'] * 100 / total_record_eovs
    df_group_eovs['percent'] = df_group_eovs['percent'].round(decimals=2)
    total_eovs_percent = df_group_eovs['percent'].sum()
    eovs_list = df_group_eovs.index.tolist()
    percent_list = df_group_eovs['percent'].tolist()
    eovs_percent = list(zip(eovs_list, percent_list))

    # Dspace_record_sdgs
    df_sdgs = pd.DataFrame(list(Dspace_record_sdgs.objects.all().values('dspace_object_id','sdg')))
    for i in range(len(df_sdgs)):
        if '17' in df_sdgs.loc[i, 'sdg']:
            df_sdgs.loc[i, 'sdg'] = 'SDG17'
        elif '16' in df_sdgs.loc[i, 'sdg']:
            df_sdgs.loc[i, 'sdg'] = 'SDG16'
        elif '15' in df_sdgs.loc[i, 'sdg']:
            df_sdgs.loc[i, 'sdg'] = 'SDG15'
        elif '14' in df_sdgs.loc[i, 'sdg']:
            df_sdgs.loc[i, 'sdg'] = 'SDG14'
        elif '13' in df_sdgs.loc[i, 'sdg']:
            df_sdgs.loc[i, 'sdg'] = 'SDG13'
        elif '12' in df_sdgs.loc[i, 'sdg']:
            df_sdgs.loc[i, 'sdg'] = 'SDG12'
        elif '11' in df_sdgs.loc[i, 'sdg']:
            df_sdgs.loc[i, 'sdg'] = 'SDG11'
        elif '10' in df_sdgs.loc[i, 'sdg']:
            df_sdgs.loc[i, 'sdg'] = 'SDG10'
        elif '9' in df_sdgs.loc[i, 'sdg']:
            df_sdgs.loc[i, 'sdg'] = 'SDG9'
        elif '8' in df_sdgs.loc[i, 'sdg']:
            df_sdgs.loc[i, 'sdg'] = 'SDG8'
        elif (df_sdgs.loc[i, 'sdg'] == '7') or ('7.' in df_sdgs.loc[i, 'sdg']):
            df_sdgs.loc[i, 'sdg'] = 'SDG7'
        elif (df_sdgs.loc[i, 'sdg'] == '6') or ('6.' in df_sdgs.loc[i, 'sdg']):
            df_sdgs.loc[i, 'sdg'] = 'SDG6'
        elif (df_sdgs.loc[i, 'sdg'] == '5') or ('5.' in df_sdgs.loc[i, 'sdg']) or ('SDG - 5' in df_sdgs.loc[i, 'sdg']):
            df_sdgs.loc[i, 'sdg'] = 'SDG5'
        elif (df_sdgs.loc[i, 'sdg'] == '4') or ('4.' in df_sdgs.loc[i, 'sdg']):
            df_sdgs.loc[i, 'sdg'] = 'SDG4'
        elif (df_sdgs.loc[i, 'sdg'] == '3') or ('3.' in df_sdgs.loc[i, 'sdg']):
            df_sdgs.loc[i, 'sdg'] = 'SDG3'
        elif (df_sdgs.loc[i, 'sdg'] == '2') or ('2.' in df_sdgs.loc[i, 'sdg']):
            df_sdgs.loc[i, 'sdg'] = 'SDG2'
        elif (df_sdgs.loc[i, 'sdg'] == '1') or ('1.' in df_sdgs.loc[i, 'sdg']):
            df_sdgs.loc[i, 'sdg'] = 'SDG1'

    df_group_sdgs = df_sdgs.groupby(df_sdgs['sdg']).count()
    total_record_sdgs = len(df_sdgs.drop_duplicates(subset = ['dspace_object_id'],keep = 'first').reset_index(drop = True))
    df_group_sdgs['percent'] = df_group_sdgs['dspace_object_id'] * 100 / total_record_sdgs
    df_group_sdgs['percent'] = df_group_sdgs['percent'].round(decimals=2)
    total_sdgs_percent = df_group_sdgs['percent'].sum()
    sdgs_list = df_group_sdgs.index.tolist()
    percent_list_sdgs = df_group_sdgs['percent'].tolist()
    sdgs_percent = list(zip(sdgs_list, percent_list_sdgs))

    context= {'doc_count': count_records,
              'submitters_count': count_submitters,
              'count_dois_obp': count_dois_obp,
              'dates_counts': dates_counts,
              'submitters_counts': submitters_counts,
              'dates_counts_last_modified': dates_counts_last_modified,
              'dates_created_counts': dates_created_counts,
              'count_collections': count_collections,
              'count_communities': count_communities,
              'countries': json.loads(countries),
              'df_countries_top10': df_group_countries_top10,
              'disciplines_percent': disciplines_percent,
              'total_disciplines_count': total_record_disciplines,
              'count_records': count_records,
              'trl_percent': trl_percent,
              'total_trl_count': total_trl_count,
              'bptypes_percent': bptypes_percent,
              'total_bptypes_count': total_record_bptypes,
              'adoptiontypes_percent': adoptiontypes_percent,
              'total_adoptiontypes_count': total_record_adoptiontypes,
              'eovs_percent': eovs_percent,
              'total_eovs_count': total_record_eovs,
              'sdgs_percent': sdgs_percent,
              'total_sdgs_count': total_record_sdgs,
            }
    return render(request, 'dspace_metrics.html', context)


def obps_realtime(request):
    users_total_sum = Ganalytics_obpsorg_lastmonth.objects.aggregate(sum=Sum('users_num_total')).get('sum')
    users_new_sum = Ganalytics_obpsorg_lastmonth.objects.aggregate(sum=Sum('users_num_new')).get('sum')
    #docs_access_num_sum = Ganalytics_obpsorg.objects.aggregate(sum=Sum('docs_access_num')).get('sum')
    docs_access_num_sum = Ganalytics_obpsorg_lastmonth_docs.objects.aggregate(sum=Sum('sessions')).get('sum')
    visits_num_sum = Ganalytics_obpsorg_lastmonth.objects.aggregate(sum=Sum('visits_num')).get('sum')
    dates_list = Ganalytics_obpsorg_lastmonth.objects.values('date_start')
    users_new_list = Ganalytics_obpsorg_lastmonth.objects.values('users_num_new')
    ganalytics_obpsorg_data = Ganalytics_obpsorg_lastmonth.objects.order_by('date_start')

    count_countries = str(Ganalytics_obpsorg_lastmonth_countries.objects.all().count())

    countries_df = pd.DataFrame(list(Ganalytics_obpsorg_lastmonth_countries.objects.all().values('country', 'users', 'sessions')))
    for i in range(len(countries_df)) :
        if ('United States' in countries_df.loc[i, 'country']) and (countries_df.loc[i, 'country'] != 'United States Virgin Islands') and (countries_df.loc[i, 'country'] != 'United States Minor Outlying Islands'):
            countries_df.loc[i, 'country'] = 'United States of America'
        elif 'United Kingdom' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'United Kingdom'
        elif 'Côte' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Côte D\'ivoire (Ivory Coast)'
        elif 'Czechia' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Czech Republic'
        elif 'Eswatini' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Eswatini'
        elif 'Moldova' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Republic of Moldova'
        elif 'Tanzania' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'United Republic of Tanzania'
        elif 'U.S. Virgin Islands' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'United States Virgin Islands'
        elif 'Russia' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Russian Federation'
        elif 'Vietnam' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Viet Nam'
        elif 'Taiwan' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Taiwan, Province of China'
        elif 'Iran' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Islamic Republic of Iran'
        elif 'South Korea' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Republic of Korea'
        elif 'Bosnia & Herzegovina' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Bosnia and Herzegovina'
        elif 'St. Vincent & Grenadines' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Saint Vincent and the Grenadines'
        elif 'Brunei' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Brunei Darussalam'
        elif '(not set)' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Unknown or unspecified country'
        elif 'Syria' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Syrian Arab Republic'
        elif 'St. Martin' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Saint Martin'
        elif 'Laos' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Lao People\'s Democratic Republic'
        elif countries_df.loc[i, 'country'] == 'Nigeria                                 ':
            countries_df.loc[i, 'country'] = 'Federal Republic of Nigeria'
        elif countries_df.loc[i, 'country'] == 'Niger                                   ':
            countries_df.loc[i, 'country'] = 'Niger'
        elif countries_df.loc[i, 'country'] == 'St. Barthélemy                          ':
            countries_df.loc[i, 'country'] = 'Saint Barthélemy'
        elif countries_df.loc[i, 'country'] == 'Svalbard & Jan Mayen                    ':
            countries_df.loc[i, 'country'] = 'Svalbard and Jan Mayeny'
        elif countries_df.loc[i, 'country'] == 'St. Kitts & Nevis                       ':
            countries_df.loc[i, 'country'] = 'Saint Kitts and Nevis'
        elif countries_df.loc[i, 'country'] == 'St. Lucia                               ':
            countries_df.loc[i, 'country'] = 'Saint Lucia'
        elif countries_df.loc[i, 'country'] == 'São Tomé & Príncipe                     ':
            countries_df.loc[i, 'country'] = 'Sao Tome and Principe'
        elif countries_df.loc[i, 'country'] == 'Congo - Kinshasa                        ':
            countries_df.loc[i, 'country'] = 'Democratic Republic of the Congo'
        elif countries_df.loc[i, 'country'] == 'Congo - Brazzaville                     ':
            countries_df.loc[i, 'country'] = 'Congo'
        elif countries_df.loc[i, 'country'] == 'Dominican Republic                      ':
            countries_df.loc[i, 'country'] = 'Dominican Republic'
        elif countries_df.loc[i, 'country'] == 'Dominica                                ':
            countries_df.loc[i, 'country'] = 'The Commonwealth of Dominica'
        elif countries_df.loc[i, 'country'] == 'Papua New Guinea                        ':
            countries_df.loc[i, 'country'] = 'Independent State of Papua New Guinea'
        elif countries_df.loc[i, 'country'] == 'Guinea-Bissau                           ':
            countries_df.loc[i, 'country'] = 'The Republic of Guinea-Bissau'
        elif 'Equatorial Guinea' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'The Republic of Equatorial Guinea'

    countries_df_top20 = countries_df.sort_values(by='users', ascending=False).head(20)

    pagepaths_df = pd.DataFrame(list(Ganalytics_obpsorg_lastmonth_docs.objects.all().values('doc_path', 'users', 'sessions')))
    pagepaths_df = pagepaths_df.sort_values(by='users', ascending=False).head(20).reset_index(drop=True)

    # Add title besides URLs to ba accessed from frontend
    records_df = pd.DataFrame(list(Dspace_records.objects.all().values('handle', 'title'))) # available documents in OBPS
    pagepaths_df['title'] = ''

    # convert doc_path into URLs to ba accessed from frontend
    for i in range(0,len(pagepaths_df)):
        doc_path = pagepaths_df['doc_path'].iloc[i]
        doc_path = doc_path.rsplit('/',1)[0]
        pagepaths_df['doc_path'].iloc[i] = doc_path
    pagepaths_df['doc_path'] = pagepaths_df['doc_path'].str.replace(r'/bitstream', 'https://www.oceanbestpractices.net')

    for i in range(0,len(pagepaths_df)):
        for j in range(0,len(records_df)):
            doc_path = pagepaths_df.loc[i, 'doc_path']
            doc_path_split = doc_path.split('/')
            doc_path_handle = doc_path_split[-2] + '/' + doc_path_split[-1]
            handle = str(records_df.loc[j, 'handle'])
            if handle == doc_path_handle:
                pagepaths_df.loc[i, 'title'] = records_df.loc[j, 'title']


    #print records_df
    countries_names_map = get_countries_names_map()
    df_group_countries_top10 = countries_df.sort_values(by='users', ascending=False).head(10)
    countries_list = countries_df.country.tolist()
    for i in range(0, len(countries_list)):
        for key in countries_names_map:
            if key in countries_list[i]:
                countries_list[i] = countries_names_map[key]

    records_country_count_list = countries_df.users.tolist()
    group_countries_list = list(zip(countries_list, records_country_count_list))
    group_countries_dict = dict(zip(countries_list, records_country_count_list))
    countries = json.dumps(group_countries_dict)

    context= {'total_users_sum': users_total_sum, 'total_new_users_sum': users_new_sum,
            'total_docs_access_sum': docs_access_num_sum, 'visits_num_sum': visits_num_sum,
            'dates': dates_list, 'new_users': users_new_list, 'ganalytics_obpsorg_data': ganalytics_obpsorg_data,
            'countries_count': count_countries, 'countries_df': countries_df_top20, 'pagepaths_df': pagepaths_df,
            'countries': json.loads(countries),}
    # context= {'total_users_sum': users_total_sum, 'total_new_users_sum': users_new_sum,
    #         'total_docs_access_sum': docs_access_num_sum, 'visits_num_sum': visits_num_sum,
    #         'dates': dates_list, 'new_users': users_new_list, 'ganalytics_obpsorg_data': ganalytics_obpsorg_data,
    #         'countries_count': count_countries, 'countries_df': countries_df, 'pagepaths_df': pagepaths_df}

    return render(request, 'obps_realtime.html', context)


def obps_history(request):
    users_total_sum = Ganalytics_obpsorg.objects.aggregate(sum=Sum('users_num_total')).get('sum')
    users_new_sum = Ganalytics_obpsorg.objects.aggregate(sum=Sum('users_num_new')).get('sum')
    #docs_access_num_sum = Ganalytics_obpsorg.objects.aggregate(sum=Sum('docs_access_num')).get('sum')
    docs_access_num_sum = Ganalytics_obpsorg_docs.objects.aggregate(sum=Sum('sessions')).get('sum')
    visits_num_sum = Ganalytics_obpsorg.objects.aggregate(sum=Sum('visits_num')).get('sum')
    dates_list = Ganalytics_obpsorg.objects.values('date_start')
    users_new_list = Ganalytics_obpsorg.objects.values('users_num_new')
    ganalytics_obpsorg_data = Ganalytics_obpsorg.objects.order_by('date_start')

    count_countries = str(Ganalytics_obpsorg_countries.objects.all().count())

    countries_df = pd.DataFrame(list(Ganalytics_obpsorg_countries.objects.all().values('country', 'users', 'sessions')))
    for i in range(len(countries_df)) :
        if ('United States' in countries_df.loc[i, 'country']) and (countries_df.loc[i, 'country'] != 'United States Virgin Islands') and (countries_df.loc[i, 'country'] != 'United States Minor Outlying Islands'):
            countries_df.loc[i, 'country'] = 'United States of America'
        elif 'United Kingdom' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'United Kingdom'
        elif 'Côte' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Côte D\'ivoire (Ivory Coast)'
        elif 'Czechia' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Czech Republic'
        elif 'Eswatini' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Eswatini'
        elif 'Moldova' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Republic of Moldova'
        elif 'Tanzania' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'United Republic of Tanzania'
        elif 'U.S. Virgin Islands' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'United States Virgin Islands'
        elif 'Russia' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Russian Federation'
        elif 'Vietnam' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Viet Nam'
        elif 'Taiwan' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Taiwan, Province of China'
        elif 'Iran' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Islamic Republic of Iran'
        elif 'South Korea' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Republic of Korea'
        elif 'Bosnia & Herzegovina' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Bosnia and Herzegovina'
        elif 'St. Vincent & Grenadines' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Saint Vincent and the Grenadines'
        elif 'Brunei' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Brunei Darussalam'
        elif '(not set)' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Unknown or unspecified country'
        elif 'Syria' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Syrian Arab Republic'
        elif 'St. Martin' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Saint Martin'
        elif 'Laos' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'Lao People\'s Democratic Republic'
        elif countries_df.loc[i, 'country'] == 'Nigeria                                 ':
            countries_df.loc[i, 'country'] = 'Federal Republic of Nigeria'
        elif countries_df.loc[i, 'country'] == 'Niger                                   ':
            countries_df.loc[i, 'country'] = 'Niger'
        elif countries_df.loc[i, 'country'] == 'St. Barthélemy                          ':
            countries_df.loc[i, 'country'] = 'Saint Barthélemy'
        elif countries_df.loc[i, 'country'] == 'Svalbard & Jan Mayen                    ':
            countries_df.loc[i, 'country'] = 'Svalbard and Jan Mayeny'
        elif countries_df.loc[i, 'country'] == 'St. Kitts & Nevis                       ':
            countries_df.loc[i, 'country'] = 'Saint Kitts and Nevis'
        elif countries_df.loc[i, 'country'] == 'St. Lucia                               ':
            countries_df.loc[i, 'country'] = 'Saint Lucia'
        elif countries_df.loc[i, 'country'] == 'São Tomé & Príncipe                     ':
            countries_df.loc[i, 'country'] = 'Sao Tome and Principe'
        elif countries_df.loc[i, 'country'] == 'Congo - Kinshasa                        ':
            countries_df.loc[i, 'country'] = 'Democratic Republic of the Congo'
        elif countries_df.loc[i, 'country'] == 'Congo - Brazzaville                     ':
            countries_df.loc[i, 'country'] = 'Congo'
        elif countries_df.loc[i, 'country'] == 'Dominican Republic                      ':
            countries_df.loc[i, 'country'] = 'Dominican Republic'
        elif countries_df.loc[i, 'country'] == 'Dominica                                ':
            countries_df.loc[i, 'country'] = 'The Commonwealth of Dominica'
        elif countries_df.loc[i, 'country'] == 'Papua New Guinea                        ':
            countries_df.loc[i, 'country'] = 'Independent State of Papua New Guinea'
        elif countries_df.loc[i, 'country'] == 'Guinea-Bissau                           ':
            countries_df.loc[i, 'country'] = 'The Republic of Guinea-Bissau'
        elif 'Equatorial Guinea' in countries_df.loc[i, 'country']:
            countries_df.loc[i, 'country'] = 'The Republic of Equatorial Guinea'

    countries_df_top20 = countries_df.sort_values(by='users', ascending=False).head(20)

    pagepaths_df = pd.DataFrame(list(Ganalytics_obpsorg_docs.objects.all().values('doc_path', 'users', 'sessions')))
    pagepaths_df = pagepaths_df.sort_values(by='users', ascending=False).head(20).reset_index(drop=True)

    # Add title besides URLs to ba accessed from frontend
    records_df = pd.DataFrame(list(Dspace_records.objects.all().values('handle', 'title'))) # available documents in OBPS
    pagepaths_df['title'] = ''

    # convert doc_path into URLs to ba accessed from frontend
    for i in range(0,len(pagepaths_df)):
        doc_path = pagepaths_df['doc_path'].iloc[i]
        doc_path = doc_path.rsplit('/',1)[0]
        pagepaths_df['doc_path'].iloc[i] = doc_path
    pagepaths_df['doc_path'] = pagepaths_df['doc_path'].str.replace(r'/bitstream', 'https://www.oceanbestpractices.net')


    for i in range(0,len(pagepaths_df)):
        for j in range(0,len(records_df)):
            doc_path = pagepaths_df.loc[i, 'doc_path']
            doc_path_split = doc_path.split('/')
            doc_path_handle = doc_path_split[-2] + '/' + doc_path_split[-1]
            handle = str(records_df.loc[j, 'handle'])
            if handle == doc_path_handle:
                pagepaths_df.loc[i, 'title'] = records_df.loc[j, 'title']
                print pagepaths_df.loc[i, 'title']
                print records_df.loc[j, 'title']




    #print records_df
    countries_names_map = get_countries_names_map()
    df_group_countries_top10 = countries_df.sort_values(by='users', ascending=False).head(10)
    countries_list = countries_df.country.tolist()
    for i in range(0, len(countries_list)):
        for key in countries_names_map:
            if key in countries_list[i]:
                countries_list[i] = countries_names_map[key]

    records_country_count_list = countries_df.users.tolist()
    group_countries_list = list(zip(countries_list, records_country_count_list))
    group_countries_dict = dict(zip(countries_list, records_country_count_list))
    countries = json.dumps(group_countries_dict)


    context= {'total_users_sum': users_total_sum, 'total_new_users_sum': users_new_sum,
            'total_docs_access_sum': docs_access_num_sum, 'visits_num_sum': visits_num_sum,
            'dates': dates_list, 'new_users': users_new_list, 'ganalytics_obpsorg_data': ganalytics_obpsorg_data,
            'countries_count': count_countries, 'countries_df': countries_df_top20, 'pagepaths_df': pagepaths_df,
            'countries': json.loads(countries),}

    return render(request, 'obps_history.html', context)


def obps_history_mainlanding(request):
    users_total_sum = Ganalytics_obpsystem.objects.aggregate(sum=Sum('users_num_total')).get('sum')
    users_new_sum = Ganalytics_obpsystem.objects.aggregate(sum=Sum('users_num_new')).get('sum')
    visits_num_sum = Ganalytics_obpsystem.objects.aggregate(sum=Sum('visits_num')).get('sum')
    dates_list = Ganalytics_obpsystem.objects.values('date_start')
    users_new_list = Ganalytics_obpsystem.objects.values('users_num_new')
    ganalytics_obpsystem_data = Ganalytics_obpsystem.objects.order_by('date_start')

    count_countries = str(Ganalytics_obpsystem_countries.objects.all().count())

    countries_df = pd.DataFrame(list(Ganalytics_obpsystem_countries.objects.all().values('country', 'users', 'sessions')))
    countries_df = countries_df.sort_values(by='users', ascending=False).head(20)

    # context= {'total_users_sum': users_total_sum, 'total_new_users_sum': users_new_sum,
    #          'visits_num_sum': visits_num_sum,
    #         'dates': dates_list, 'new_users': users_new_list, 'ganalytics_obpsystem_data': ganalytics_obpsystem_data,
    #         'countries_count': count_countries, 'countries_df': countries_df}
    context= {'total_users_sum': users_total_sum, 'total_new_users_sum': users_new_sum,
              'visits_num_sum': visits_num_sum,
              'dates': dates_list, 'new_users': users_new_list, 'ganalytics_obpsystem_data': ganalytics_obpsystem_data,
              'countries_count': count_countries, 'countries_df': countries_df
             }
    return render(request, 'obps_history_mainlanding.html', context)



def conferences(request):
    df_total = pd.DataFrame(list(Conferences.objects.all().values('activity_name', 'event', 'country', 'date', 'type')))
    drop_values = ['peer-reviewed publication','non-peer-reviewed publication','book','report','poster','external newsletter', 'OBPS newsletter']
    df = df_total.copy()
    df = df[df['type'].str.contains('|'.join(drop_values))==False]
    df_latest = df.sort_values(by='date', ascending=False).head(20)
    conferences_total = len(df)
    df_group = df.groupby(df['date'].dt.year).count()
    dates_list = df_group.index.tolist()
    activities_count = df_group['activity_name'].tolist()
    dates_counts = list(zip(dates_list, activities_count))
    total_countries_events = len(df.groupby(df['country']).count())
    events_count = len(df.groupby(df['event']).count())
    df_event_type = df.groupby(df['type']).count()

    type_count = df_event_type['activity_name'].tolist()
    event_type_list = df_event_type.index.tolist()
    events_types_counts = list(zip(event_type_list, type_count))

    countries_names_map = get_countries_names_map()

    df_group_countries = df.groupby(df['country']).count()
    df_group_countries_top10 = df_group_countries.sort_values(by='activity_name', ascending=False).head(10)
    countries_list = df_group_countries.index.tolist()
    for i in range(0, len(countries_list)):
        for key in countries_names_map:
            if key in countries_list[i]:
                countries_list[i] = countries_names_map[key]

    activities_country_count_list = df_group_countries.activity_name.tolist()
    group_countries_list = list(zip(countries_list, activities_country_count_list))
    group_countries_dict = dict(zip(countries_list, activities_country_count_list))
    countries = json.dumps(group_countries_dict)

    context= {
              'conferences_total': conferences_total,
              'conferences_df': df,
              'conferences_df_latest': df_latest,
              'dates_counts': dates_counts,
              'total_countries_events': total_countries_events,
              'events_count': events_count,
              'events_types_counts': events_types_counts,
              'total_events_types_counts': len(event_type_list),
              'countries': json.loads(countries),
              'df_group_countries_top10': df_group_countries_top10,
             }
    return render(request, 'conferences.html', context)


def publications(request):
    df_total = pd.DataFrame(list(Conferences.objects.all().values('activity_name', 'event', 'country', 'date', 'type','publisher')))
    df_publications = df_total.copy()
    drop_values = ['workshop presentation', 'webinar','project meeting','conference townhall','conference presentation','conference poster']
    df_publications = df_publications[df_publications['type'].str.contains('|'.join(drop_values))==False]
    publications_total = len(df_publications)
    df_latest = df_publications.sort_values(by='date', ascending=False).head(20)
    total_countries_publications = len(df_publications.groupby(df_publications['country']).count())
    publishers_count = len(df_publications.groupby(df_publications['publisher']).count())
    events_count = len(df_publications.groupby(df_publications['event']).count())
    df_event_type = df_publications.groupby(df_publications['type']).count()
    type_count = df_event_type['activity_name'].tolist()
    event_type_list = df_event_type.index.tolist()
    events_types_counts = list(zip(event_type_list, type_count))

    df_group = df_publications.groupby(df_publications['date'].dt.year).count()
    dates_list = df_group.index.tolist()
    activities_count = df_group['activity_name'].tolist()
    dates_counts = list(zip(dates_list, activities_count))


    countries_names_map = get_countries_names_map()
    df_group_countries = df_publications.groupby(df_publications['country']).count()
    df_group_countries_top10 = df_group_countries.sort_values(by='activity_name', ascending=False).head(10)
    countries_list = df_group_countries.index.tolist()
    print countries_list
    for i in range(0, len(countries_list)):
        for key in countries_names_map:
            if key in countries_list[i]:
                countries_list[i] = countries_names_map[key]
    activities_country_count_list = df_group_countries.activity_name.tolist()
    group_countries_list = list(zip(countries_list, activities_country_count_list))
    group_countries_dict = dict(zip(countries_list, activities_country_count_list))
    countries = json.dumps(group_countries_dict)

    context= {

              'publications_total': publications_total,
              'publications_latest': df_latest,
              'total_countries_publications': total_countries_publications,
              'total_events_types_counts': len(event_type_list),
              'dates_counts': dates_counts,
              'events_types_counts': events_types_counts,
              'publishers_count': publishers_count,
              'countries': json.loads(countries),
              'df_group_countries_top10': df_group_countries_top10,
             }
    return render(request, 'publications.html', context)



def newsletter(request):
    df_publications = pd.DataFrame(list(Conferences.objects.all().values('activity_name', 'event', 'country', 'date', 'type','publisher')))
    df_publications = df_publications[df_publications['type'] == 'OBPS newsletter']
    df_publications_latest = df_publications.sort_values(by='date', ascending=False).head(20)


    df_newsletter = pd.DataFrame(list(Newsletter.objects.all().values('date', 'subject_line', 'emails_sent', 'unsubscribed',
    'hard_bounces', 'soft_bounces', 'opens_total', 'unique_opens', 'clicks_total', 'unique_clicks', 'unique_subscriber_clicks')))
    df_newsletter_locations = pd.DataFrame(list(Newsletter_locations.objects.all().values('country', 'cc', 'total')))
    print (df_newsletter_locations)
    df_newsletter_locations_top10 = df_newsletter_locations.sort_values(by='total', ascending=False).head(10)

    # Newsletter locations
    for i in range(len(df_newsletter_locations)) :
        if 'USA' in df_newsletter_locations.loc[i, 'country']:
            df_newsletter_locations.loc[i, 'country'] = 'United States of America'
            df_newsletter_locations_top10.loc[i, 'country'] = 'United States of America'
        elif ('United Kingdom' in df_newsletter_locations.loc[i, 'country']) and ('UK' in df_newsletter_locations.loc[i, 'cc']):
            df_newsletter_locations.loc[i, 'cc'] = 'GB'
    locations_count_list = df_newsletter_locations.total.tolist()
    cc_list = df_newsletter_locations['cc'].str.lower().tolist()
    locations_list = list(zip(cc_list, locations_count_list))
    locations_dict = dict(zip(cc_list, locations_count_list))
    countries = json.dumps(locations_dict)

    # Newsletter subscribers grouth
    df_newsletter_grouth = pd.DataFrame(list(Newsletter_subscribers_grouth.objects.all().values('date', 'subscribed')))
    df_newsletter_grouth = df_newsletter_grouth.sort_values(by=['date'])
    dates_list = df_newsletter_grouth['date'].dt.to_period('M').tolist()
    subscribed_count = df_newsletter_grouth['subscribed'].tolist()
    subscribed_counts = list(zip(dates_list, subscribed_count))

    # Newsletter total sent, bounces, unsubscribed
    dates_list = df_newsletter['date'].dt.to_period('M').tolist()
    emails_sent_list = df_newsletter['emails_sent'].tolist()
    unsubscribed_list = df_newsletter['unsubscribed'].tolist()
    hard_bounces_list = df_newsletter['hard_bounces'].tolist()
    soft_bounces_list = df_newsletter['soft_bounces'].tolist()
    opens_list = df_newsletter['opens_total'].tolist()
    unique_opens_list = df_newsletter['unique_opens'].tolist()
    clicks_list = df_newsletter['clicks_total'].tolist()
    unique_clicks_list = df_newsletter['unique_clicks'].tolist()
    unique_subscriber_clicks_list = df_newsletter['unique_subscriber_clicks'].tolist()
    emails_sent_timeseries = list(zip(dates_list, emails_sent_list))
    bounces_timeseries = list(zip(dates_list, unsubscribed_list, hard_bounces_list, soft_bounces_list))
    opens_timeseries = list(zip(dates_list, opens_list, unique_opens_list))
    clicks_timeseries = list(zip(dates_list, clicks_list, unique_clicks_list, unique_subscriber_clicks_list))

    # Newsletter totasl counts
    count_countries = str(Newsletter_locations.objects.all().count())
    total_subscribers = str(df_newsletter_grouth['subscribed'].values[-1])
    count_newsletter = str(df_publications['type'].count())

    print bounces_timeseries


    context= {
              'subscribed_counts': subscribed_counts,
              'countries': json.loads(countries),
              'df_group_countries_top10': df_newsletter_locations_top10,
              'count_countries': count_countries,
              'total_subscribers': total_subscribers,
              'count_newsletter': count_newsletter,
              'emails_sent_timeseries': emails_sent_timeseries,
              'bounces_timeseries': bounces_timeseries,
              'opens_timeseries': opens_timeseries,
              'clicks_timeseries':clicks_timeseries,
              'publications_latest': df_publications_latest,

             }
    return render(request, 'newsletter.html', context)

def community_engagement(request):
    df = pd.DataFrame(list(Communities_engagement.objects.all().values('date', 'user_community', 'description', 'country')))
    df_latest = df.sort_values(by='date', ascending=False).head(20)
    df_group = df.groupby(df['date'].dt.to_period('M')).count().cumsum()

    total_engagements = len(df)
    user_community_count = df_group['user_community'].tolist()
    dates_list = df_group.index.tolist()
    user_communities_timeseries = list(zip(dates_list, user_community_count))

    df_group = df.groupby(df['date'].dt.year).count()
    dates_list = df_group.index.tolist()
    user_communities_count = df_group['user_community'].tolist()
    user_communities_counts = list(zip(dates_list, user_communities_count))

    countries_names_map = get_countries_names_map()
    df_group_countries = df.groupby(df['country']).count()
    df_group_countries_top10 = df_group_countries.sort_values(by='user_community', ascending=False).head(10)
    countries_list = df_group_countries.index.tolist()

    for i in range(0, len(countries_list)):
        for key in countries_names_map:
            if key in countries_list[i]:
                countries_list[i] = countries_names_map[key]
    engagement_country_count_list = df_group_countries.user_community.tolist()
    group_countries_list = list(zip(countries_list, engagement_country_count_list))
    group_countries_dict = dict(zip(countries_list, engagement_country_count_list))
    countries = json.dumps(group_countries_dict)

    context= {
              'total_engagements': total_engagements,
              'user_communities_latest': df_latest,
              'user_communities_timeseries': user_communities_timeseries,
              'user_communities_counts': user_communities_counts,
              'countries': json.loads(countries),
              'df_group_countries_top10': df_group_countries_top10,
              'count_countries': len(df_group_countries),
             }
    return render(request, 'community_engagement.html', context)

def obps_workshops(request):
    df = pd.DataFrame(list(Obps_workshops.objects.all().values('name', 'date', 'country_celebration', 'num_participants', 'num_participants_countries_origin', 'num_support_organizations')))
    df_latest = df.sort_values(by='date', ascending=False).head(20)
    df_group = df.groupby(df['date'].dt.to_period('M')).count().cumsum()

    total_workshops = len(df)
    num_participants = df['num_participants'].tolist()
    num_participants_countries = df['num_participants_countries_origin'].tolist()
    dates_list = df_group.index.tolist()
    workshops_info_timeseries = list(zip(dates_list, num_participants, num_participants_countries))
    print workshops_info_timeseries
    df_group = df.groupby(df['date'].dt.year).count()
    dates_list = df_group.index.tolist()
    workshops_count = df_group['name'].tolist()
    workshops_counts = list(zip(dates_list, workshops_count))
    #
    # countries_names_map = get_countries_names_map()
    # df_group_countries = df.groupby(df['country']).count()
    # df_group_countries_top10 = df_group_countries.sort_values(by='user_community', ascending=False).head(10)
    # countries_list = df_group_countries.index.tolist()
    #
    # for i in range(0, len(countries_list)):
    #     for key in countries_names_map:
    #         if key in countries_list[i]:
    #             countries_list[i] = countries_names_map[key]
    # engagement_country_count_list = df_group_countries.user_community.tolist()
    # group_countries_list = list(zip(countries_list, engagement_country_count_list))
    # group_countries_dict = dict(zip(countries_list, engagement_country_count_list))
    # countries = json.dumps(group_countries_dict)

    context= {
              'total_workshops': total_workshops,
              'workshops_latest': df_latest,
              'workshops_info_timeseries': workshops_info_timeseries,
              'workshops_counts': workshops_counts,
              # 'countries': json.loads(countries),
              # 'df_group_countries_top10': df_group_countries_top10,
              # 'count_countries': len(df_group_countries),
             }
    return render(request, 'obps_workshops.html', context)

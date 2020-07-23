# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from obps_dashboard.apps.models import Ganalytics_obpsorg, Ganalytics_obpsorg_countries, Ganalytics_obpsorg_docs
from obps_dashboard.apps.models import Ganalytics_obpsorg_lastmonth, Ganalytics_obpsorg_lastmonth_countries, Ganalytics_obpsorg_lastmonth_docs
from obps_dashboard.apps.models import Ganalytics_obpsystem, Ganalytics_obpsystem_countries
from django.db.models import Count
from django.db.models import Sum
from django.db import connection

import pandas as pd


def start(request):

    return render(request, 'index.html')

def dspace_metrics(request):
    count_communities = str(Community.objects.all().count()) # communities available in obps_dashboard
    count_epersons = str(Eperson.objects.all().count())
    count_dois = str(Doi.objects.all().count()) # number of DOIs assigned
    count_collections = str(Collection.objects.all().count()) # collections available in OBPS
    count_docs = str(len(Item.objects.filter(withdrawn=False, discoverable=True, in_archive=True))) # available documents in OBPS

    context= {'community_count': count_communities, 'doi_count': count_dois,
              'collection_count': count_collections, 'eperson_count': count_epersons,
              'doc_count': count_docs}
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
    countries_df = countries_df.sort_values(by='users', ascending=False).head(20)

    pagepaths_df = pd.DataFrame(list(Ganalytics_obpsorg_lastmonth_docs.objects.all().values('doc_path', 'users', 'sessions')))
    pagepaths_df = pagepaths_df.sort_values(by='users', ascending=False).head(20)

    # convert doc_path into URLs to ba accessed from frontend
    for i in range(0,len(pagepaths_df)):
        doc_path = pagepaths_df['doc_path'].iloc[i]
        doc_path = doc_path.rsplit('/',1)[0]
        pagepaths_df['doc_path'].iloc[i] = doc_path
    pagepaths_df['doc_path'] = pagepaths_df['doc_path'].str.replace(r'/bitstream', 'https://www.oceanbestpractices.net')

    #print countries_df
    #print pagepaths_df
    # print dates_list
    # print users_new_list
    #print users_new_list[0].values()
    #users_total_sum = Ganalytics_obpsorg.objects.all().count()
    #print users_total_sum
    context= {'total_users_sum': users_total_sum, 'total_new_users_sum': users_new_sum,
            'total_docs_access_sum': docs_access_num_sum, 'visits_num_sum': visits_num_sum,
            'dates': dates_list, 'new_users': users_new_list, 'ganalytics_obpsorg_data': ganalytics_obpsorg_data,
            'countries_count': count_countries, 'countries_df': countries_df, 'pagepaths_df': pagepaths_df}

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
    countries_df = countries_df.sort_values(by='users', ascending=False).head(20)

    pagepaths_df = pd.DataFrame(list(Ganalytics_obpsorg_docs.objects.all().values('doc_path', 'users', 'sessions')))
    pagepaths_df = pagepaths_df.sort_values(by='users', ascending=False).head(20)

    # convert doc_path into URLs to ba accessed from frontend
    for i in range(0,len(pagepaths_df)):
        doc_path = pagepaths_df['doc_path'].iloc[i]
        doc_path = doc_path.rsplit('/',1)[0]
        pagepaths_df['doc_path'].iloc[i] = doc_path
    pagepaths_df['doc_path'] = pagepaths_df['doc_path'].str.replace(r'/bitstream', 'https://www.oceanbestpractices.net')

    context= {'total_users_sum': users_total_sum, 'total_new_users_sum': users_new_sum,
            'total_docs_access_sum': docs_access_num_sum, 'visits_num_sum': visits_num_sum,
            'dates': dates_list, 'new_users': users_new_list, 'ganalytics_obpsorg_data': ganalytics_obpsorg_data,
            'countries_count': count_countries, 'countries_df': countries_df, 'pagepaths_df': pagepaths_df}

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

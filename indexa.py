#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:26:28 2023

@author: dakid
"""

import requests
import csv

def submit_to_search_engines(url):
    search_engines = [
        'https://www.google.com/ping?sitemap=',
        'https://www.bing.com/ping?sitemap=',
        'https://rpc.weblogs.com/pingSiteForm?name=',
        'https://www.yahoo.com/ping?sitemap=',
        'https://api.moreover.com/ping?u=',
        'https://www.blogsnow.com/ping',
        'https://www.blogshares.com/rpc.php',
        'https://www.blogdigger.com/RPC2',
        'https://www.blogpeople.net/servlet/weblogUpdates',
        'https://www.blogoon.net/ping/',
        'https://www.blogroots.com/tb_populi.blog?id=1',
        'https://www.blogoon.net/ping/',
        'https://www.blogstreet.com/xrbin/xmlrpc.cgi',
        'https://bulkfeeds.net/rpc',
        'https://www.newsisfree.com/xmlrpctest.php',
        'https://ping.blo.gs/',
        'https://ping.feedburner.com',
        'https://ping.syndic8.com/xmlrpc.php',
        'https://ping.weblogalot.com/rpc.php',
        'https://rpc.blogbuzzmachine.com/RPC2',
        'https://rpc.blogrolling.com/pinger/',
        'https://rpc.icerocket.com:10080/',
        'https://rpc.pingomatic.com/',
        'https://rpc.technorati.com/rpc/ping',
        'https://rpc.weblogs.com/RPC2',
        'https://topicexchange.com/RPC2',
        'https://trackback.bakeinu.jp/bakeping.php',
        'https://www.bitacoles.net/ping.php',
        'https://www.blogoole.com/ping/',
        'https://www.blogpeople.net/servlet/weblogUpdates',
        'https://www.blogroots.com/tb_populi.blog?id=1',
        'https://www.blogshares.com/rpc.php',
        'https://www.blogsnow.com/ping',
        'https://www.blogstreet.com/xrbin/xmlrpc.cgi',
        'https://www.newsisfree.com/xmlrpctest.php',
        'https://ping.blo.gs/',
        'https://ping.feedburner.com',
        'https://ping.syndic8.com/xmlrpc.php',
        'https://ping.weblogalot.com/rpc.php',
        'https://rpc.blogbuzzmachine.com/RPC2',
        'https://rpc.blogrolling.com/pinger/',
        'https://rpc.icerocket.com:10080/',
        'https://rpc.pingomatic.com/',
        'https://rpc.technorati.com/rpc/ping',
        'https://rpc.weblogs.com/RPC2',
        'https://topicexchange.com/RPC2',
        'https://trackback.bakeinu.jp/bakeping.php',
        'https://www.bitacoles.net/ping.php',
        'https://www.blogdigger.com/RPC2',
        'https://www.blogoole.com/ping/',
        'https://www.blogpeople.net/servlet/weblogUpdates',
        'https://www.blogroots.com/tb_populi.blog?id=1',
        'https://www.blogshares.com/rpc.php',
        'https://www.blogsnow.com/ping',
        'https://www.blogstreet.com/xrbin/xmlrpc.cgi',
        'https://www.newsisfree.com/xmlrpctest.php',
        'https://ping.blo.gs/',
        'https://ping.feedburner.com',
        'https://ping.syndic8.com/xmlrpc.php',
        'https://ping.weblogalot.com/rpc.php',
        'https://rpc.blogbuzzmachine.com/RPC2',
        'https://rpc.blogrolling.com/pinger/',
        'https://rpc.icerocket.com:10080/',
        'https://rpc.pingomatic.com/',
        'https://rpc.technorati.com/rpc/ping',
        'https://rpc.weblogs.com/RPC2',
        'https://topicexchange.com/RPC2',
        'https://trackback.bakeinu.jp/bakeping.php',
        'https://www.bitacoles.net/ping.php',
        'https://www.blogdigger.com/RPC2',
        'https://www.blogoole.com/ping/',
        'https://www.blogpeople.net/servlet/weblogUpdates',
        'https://www.blogroots.com/tb_populi.blog?id=1',
        'https://www.blogshares.com/rpc.php',
        'https://www.blogsnow.com/ping',
        'https://www.blogstreet.com/xrbin/xmlrpc.cgi',
        'https://www.newsisfree.com/xmlrpctest.php',
        'https://ping.blo.gs/',
        'https://ping.feedburner.com',
        'https://ping.syndic8.com/xmlrpc.php',
        'https://ping.weblogalot.com/rpc.php',
        'https://rpc.blogbuzzmachine.com/RPC2',
        'https://rpc.blogrolling.com/pinger/',
        'https://rpc.icerocket.com:10080/',
        'https://rpc.pingomatic.com/',
        'https://rpc.technorati.com/rpc/ping',
        'https://rpc.weblogs.com/RPC2',
        'https://topicexchange.com/RPC2',
        'https://trackback.bakeinu.jp/bakeping.php',
        'https://www.bitacoles.net/ping.php',
    ]
    
    results = []
    
    for engine in search_engines:
        ping_url = engine + url
        try:
            response = requests.get(ping_url)
            if response.status_code == 200:
                results.append({'Search Engine': engine, 'URL': url, 'Status': 'Success'})
            else:
                results.append({'Search Engine': engine, 'URL': url, 'Status': f'Error ({response.status_code})'})
        except requests.exceptions.RequestException as e:
            results.append({'Search Engine': engine, 'URL': url, 'Status': f'Error ({e})'})

    return results

# Read URLs from a text file
file_path = 'urls.txt'
with open(file_path, 'r') as file:
    urls = file.read().splitlines()

# Submit each URL to search engines and collect results
all_results = []
for url in urls:
    results = submit_to_search_engines(url)
    all_results.extend(results)

# Generate and save reports in a CSV file
report_file = 'submission_report.csv'
fieldnames = ['Search Engine', 'URL', 'Status']

with open(report_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_results)

print(f"Submission report saved in '{report_file}'")

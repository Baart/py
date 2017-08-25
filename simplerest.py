#!/usr/bin/env python

import requests



def post(url, data, headers=None, params=None):
    if headers is None:
        headers = {}
    if params is None:
        params = {}
    response = requests.post(url, data, headers=headers, params=params)
    response.raise_for_status()
    return response


def put(url, data, headers=None, params=None):
    if headers is None:
        headers = {}
    if params is None:
        params = {}
    headers['Content-type'] = 'application/json'
    response = requests.put(url, data, headers=headers, params=params)
    response.raise_for_status()
    return response


def get(url, params=None, headers=None):
    if headers is None:
        headers = {}
    if params is None:
        params = {}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response

'''
url = 'https://eddb.io/system/search?system%5Bname%5D=har+pahary&expand=stations&system%5Bhas_commodities%5D=1&system%5Bversion%5D=2&_=1499332382133'

r = get(url).json()

for a in r:
    print a
    print ' - '
'''

'''
url = 'http://www.miggy.org/games/elite-dangerous/routes/suggest-system-names.pl?prefix=har%20pahary'
r = get(url).json()

print r
'''

'''
url = 'http://www.miggy.org/games/elite-dangerous/routes/find-route.pl?max_jump=50&origin_system=har+pahary&destination_system=LTT+10311&allow_permit_required=true'
print 'computing...'
r = get(url).json()
print r
'''

def compute_system(src, dst):
    url = 'https://www.spansh.co.uk/api/route'
    data = {
        "from": src,
        "to": dst,
        "range": "15",
        "efficiency": "25"
    }
    r = post(url, data)
    job_id = r.json()['job']
    #print job_id
    while True:

        try:
            job_poll = 'https://www.spansh.co.uk/api/results/' + job_id # DFF7EAE2-622D-11E7-8F8F-CD3724079CAE
            r = get(job_poll)
            job = r.json()
            #print job
            if 'result' in job:
                #print data['from'], data['to'], ' -> ', '{:f}'.format(job['result']['distance'])
                return job['result']['distance']
        except Exception as e:
            print e
            return -1


def compute_list(src, input_filename, output_filename):
    results = []
    with open('systems.txt') as f:
        for line in f.readlines():
            system = line.strip()

            distance = compute_system(src, system)
            print src, system, distance
            result = {
                'src': src,
                'destination': system,
                'distance': distance
            }

            results.append(result)

    print results

    with open('systems_output.txt', 'w') as f:

        for result in sorted(results, key=lambda x : x['distance']):
            f.write( str(int(result['distance'])) + ' ; ' + result['destination'] + ' ; ' + result['src'] + ' \n')


# compute_list('Har Pahary', 'systems.txt', 'systems_output2.txt')

r = compute_system('Har Pahary', 'HIP 17692')

print r





import requests
import pandas as pd
import numpy as np
import richdem as rd

def get_mdt(mdt_response):
    mdt_splitted=mdt_response.split('\n')
    altitudes=mdt_splitted[5:]
    mdt=[]
    df=list(altitudes)
    for row in df:
        cotas=row.split(' ')
        cotas=[float(x) for x in cotas if x]
        mdt.append(cotas)
    return rd.rdarray(pd.DataFrame(mdt).to_numpy(),no_data=-9999)

def get_cotas(mdt_response):
    mdt_splitted=mdt_response.split('\n')
    altitudes=mdt_splitted[5:]
    merge_altitudes=[]
    df=list(altitudes)
    for row in df:
        for cota in row.split(' '):
            try:
                merge_altitudes.append(float(cota))
            except:
                pass


    return merge_altitudes

def get_bounding_box(lat,lon):
    if lon<0:
        lon_si=lon-0.2
        lon_id=lon+0.2
    else:
        lon_si=lon-0.2
        lon_id = lon + 0.2
    lat_si = lat - 0.2
    lat_id = lat + 0.2

    s = ","
    seq = (str(lon_si), str(lat_si), str(lon_id),str(lat_id))

    bbox=s.join(seq)

    return bbox

def get_pendiente_media(cotas):
    max_c=max(cotas)
    min_c=min(cotas)
    delta=(max_c-min_c)/len(cotas)
    return delta


def get_slope(lat,lng):
    bbox = get_bounding_box(lat, lng)
    url="http://servicios.idee.es/wcs-inspire/mdt?SERVICE=WCS&REQUEST=GetCoverage&VERSION=1.0.0&CRS=EPSG:4326&" \
        "BBOX=" + \
        bbox + \
        "&COVERAGE=Elevacion4258_200&RESX=0.026699999999999998&RESY=0.026699999999999998&FORMAT=application/asc&EXCEPTIONS=XML"
    response=requests.get(url)
    cotas=get_cotas(response.text)
    mdt=get_mdt(response.text)
    slope = rd.TerrainAttribute(mdt, attrib='slope_riserun')
    return np.nanmean(slope)


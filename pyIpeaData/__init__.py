""" Module to get data from ipeadata.com.br """
import requests as req
import pandas as pd

link = "http://www.ipeadata.gov.br/api/odata4/"
link2 = "http://ipeadata2-homologa.ipea.gov.br/api/v1/"

def basic_api_call(consulta):
    """
    Function to make a call on ipedata api
    :param api: url on api
    :return: a dataFrame with data
    """
    response = req.get(consulta)
    if response.status_code == req.codes.ok: # pylint: disable=no-member
        json_response = response.json()
        if 'value' in json_response:
            try:
                data_frame = pd.DataFrame(json_response['value'])
                return data_frame
            except Exception: # pylint: disable=broad-except
                return None
    return None

def get_metadados(serie = None):
    """
    Return metadata of a serie
    :param serie: serie to search for otherwise return metadata for all series
    :return: a data frame
    """
    consulta = link + "Metadados"
    if(serie is not None):
        consulta = consulta + "('%s')" %serie
    return basic_api_call(consulta)

def get_temas(tema = None):
    """
    Return a list of subjects
    :param pais: subject to search for
    :return: a data frame
    """
    consulta = link + 'Temas'
    if(tema is not None):
        consulta = consulta + "(%s)" %tema
    return basic_api_call(consulta)

def get_paises(pais = None):
    """
    Return a list of countries
    :param pais: country to search for
    :return: a data frame
    """
    consulta = link + 'Paises'
    if(pais is not None):
        consulta = consulta + "('%s')" %pais
    return basic_api_call(consulta)

def get_territorios(territorio = None, nivel = None):
    """
    Return a list of territories
    :param pais: territory to search for
    :return: a data frame
    """
    consulta = link + 'Territorios'
    if(territorio is not None and nivel is not None):
        consulta = consulta + "(TERCODIGO='%s',NIVNOME='%s')" %(territorio, nivel)
        return basic_api_call(consulta)
    elif(territorio is None and nivel is None):
        return basic_api_call(consulta)
    else:
        raise Exception('Uso: get_territorios() ou get_territorios(territorio, nivel).')

def get_fontes():
    """
    Get sources from ipea web site
    :return: a data frame with the information
    """
    consulta = link2 + "Fontes"
    return basic_api_call(consulta)

def get_nivel_regiao(serie):
    """
    Return region level of a serie
    :param serie: serie to search for
    :return: a data frame
    """
    consulta = (link + "Metadados('{}')"
           "/Valores?$apply=groupby((NIVNOME))&$orderby=NIVNOME").format(serie)
    return basic_api_call(consulta)

# pylint: disable=invalid-name
def get_serie(serie, groupby=None):
    """
    Return the values from a given serie
    :param serie: a serie to search for
    :return: a data frame with the values
    """
    serie_numerica = get_metadados(serie)['SERNUMERICA'].iloc[0]
    if(serie_numerica):
        consulta = link + "ValoresSerie" #séries numéricas
    else:
        consulta = link + "ValoresStrSerie" #séries alfanuméricas

    if groupby is not None:
        df = get_nivel_regiao(serie)
        if df['NIVNOME'].isin([groupby]).any():
            consulta = (link2 + "AnoValors"
                   "(SERCODIGO='{}',NIVNOME='{}')?$top=100&$skip=0&$orderby"
                   "=SERATUALIZACAO&$count=true").format(serie, groupby)
            return basic_api_call(consulta)
        return None

    consulta = consulta + "(SERCODIGO='%s')" % serie
    return basic_api_call(consulta)

if __name__ == "__main__":
    print(get_serie('ADMIS'))

from newsapi.newsapi_client import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException
import click
from sqlclient import SqlClient
import const


@click.command()
@click.option(
        '--query','-q', default=None, 
        help='headlines w/ specific keyword. Example: \'bitcoin\', \'trump\' ')
@click.option(
        '--sources','-s', default=None,
        help='headlines of news sources. Example: \'bbc-news\', \'abc-news\' \nNote: You cannot mix this parameter with country or category ')
@click.option(
        '--language','-l', default='en',
        help='The 2-letter ISO-639-1 code of the language you want to get headlines for. Valid values are:\
        \'ar\',\'de\',\'en\',\'es\',\'fr\',\'he\',\'it\',\'nl\',\'no\',\'pt\',\'ru\',\'se\',\'ud\',\'zh\'')
@click.option(
        '--country','-c', default=None,
        help='The 2-letter ISO 3166-1 code of the country you want to get headlines. Valid values are:\
            \'ae\',\'ar\',\'at\',\'au\',\'be\',\'bg\',\'br\',\'ca\',\'ch\',\'cn\',\'co\',\'cu\',\'cz\',\'de\',\'eg\',\'fr\',\'gb\',\'gr\',\
            \'hk\',\'hu\',\'id\',\'ie\',\'il\',\'in\',\'it\',\'jp\',\'kr\',\'lt\',\'lv\',\'ma\',\'mx\',\'my\',\'ng\',\'nl\',\'no\',\'nz\',\
            \'ph\',\'pl\',\'pt\',\'ro\',\'rs\',\'ru\',\'sa\',\'se\',\'sg\',\'si\',\'sk\',\'th\',\'tr\',\'tw\',\'ua\',\'us\'\
            Note: you can\'t mix this param with the sources param.')
@click.option('--category','-g', default=None,
              help='The category you want to get headlines for! Valid values are:\
			\'business\',\'entertainment\',\'general\',\'health\',\'science\',\'sports\',\'technology\'\
            Note: you can\'t mix this param with the sources param.')
@click.argument('outputfile', type=click.Path(exists=False))
def top_headlines(outputfile, query, sources, language, country, category):

    api_key = const.SAMPLE_API_KEY  
    newsapi = NewsApiClient(api_key)
    try:
            headlines = newsapi.get_top_headlines(
                    query, sources, language, country, 
                    category, page_size=100
                    )
            if headlines['status'] == "ok" :
               #print (headlines['totalResults'])
               
               sqlclient = SqlClient(const.DB_NAME) 
               connection = sqlclient.create_connection()
               sqlclient.create_table(connection,const.TABLE)
               sqlclient.add_newsitem(connection,const.TABLE,headlines)
               
               #Export news to csv file
               sqlclient.export_to_csv(connection,const.TABLE,outputfile)
            else :
                print (headlines['message'])                
    except NewsAPIException as inst:
            print ("Error: "+inst.get_message())
    except Exception as inst:
            print (inst)


if __name__ == '__main__':
    top_headlines()
 
#Usage: python news.py news04252019.csv 
#Usage: python news.py newstrump.csv --query=Trump

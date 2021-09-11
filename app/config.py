

class Config:
    '''
    General configuration parent class
    '''

NEWS_API_BASE_URL =' https://newsapi.org/v2/everything?q=tesla&from=2021-08-10&sortBy=publishedAt&apiKey={}'
# NEWS_API_BASE_URL ='https://api.thnewsapi.org/3/news/{}?api_key={}'    

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
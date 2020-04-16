
import os
from dotenv import find_dotenv, load_dotenv
from requests import session
import logging

payload = {
    'action': 'login',
    'username': os.environ.get("KAGGLE_USERNAME"),
    'password': os.environ.get("KAGGLE_PASSWORD")
     
}

def extract_data(url, file_path):
    """
        method to extract data
    """
    with session() as c:
        c.post("https://www.kaggle.com/account/login",data=payload)
        with open(filepath, 'w') as handle:
           response = c.get(url, stream=True)
           for block in response.iter_content(1024): 
             handle.write(block)
              
            
def main(project_dir):
    """
    main method
    """
    #get logger
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')
    
    #urls$
    test_url = "https://www.kaggle.com/c/titanic/download/test.csv"
    train_url = "https://www.kaggle.com/c/titanic/download/train.csv"
    
    #file_paths
    raw_data_path = os.path.join(project_dir, 'data', 'raw')
    train_data_path = os.path.join(raw_data_path, 'train_1.csv')
    test_data_path = os.path.join(raw_data_path, 'test_1.csv')
    
    #extract data
    extract_data(train_url, train_data_path)
    extract_data(test_url, test_data_path)
    logger("downloaded test and train data")
    
    if __name__ == '__main__':
        #getting root directory
        #print os.path.dirname(__file__)
        print os.path.dirname(__file__)
        project_dir = os.path.join(os.path.dirname(__file__), 'raw')
        
        #setup logger
        log_fmt = '%(asc_time)s-%(name)s-%(levelname)s-%(message)s'
        logging.basicConfig(level=logging.INFO, format= log_fmt)
        
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        
        main(project_dir)
            
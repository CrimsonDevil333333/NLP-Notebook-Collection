import configparser
import os
config = configparser.ConfigParser()
config.read('config.ini')

def get_key(key_name):
    return config.get('Settings',key_name)

def set_openai_env_key():
    os.environ["OPENAI_API_KEY"] = get_key("OPENAI_API_KEY")
    
if __name__ == "__main__":
    set_openai_env_key()
    print(os.getenv("OPENAI_API_KEY"))
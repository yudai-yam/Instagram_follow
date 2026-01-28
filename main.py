from bs4 import BeautifulSoup

import argparse

import logging


logger = logging.getLogger(__name__)

def main(following_file, followers_file):

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    followers = parsing(followers_file)

    follows = parsing(following_file)

    black_list = []
    for follow in follows:
        if follow not in followers:
            black_list.append(follow)

    print(f'black list: {black_list}')

# returns a list of accounts
def parsing(file_path):
    accounts = []
    with open(file_path,'r') as f: 

        soup = BeautifulSoup(f, 'html.parser')

        # logger.debug(f'the soup is: {soup}')

        result = soup.find_all('a')

        for account in result:
            
            accounts.append(account.text)

    # logger.debug(f'the list is {accounts}')
    return accounts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is a program that identifies who does not follow you back on Instagram") 
    parser.add_argument('following_file', help='Path to the following HTML file. Download available from offical instagram')
    parser.add_argument('followers_file', help='Path to the followers HTML file. Download available from offical instagram')
    args = parser.parse_args()
    main(args.following_file, args.followers_file)

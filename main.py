from MENU import *

if __name__ == "__main__":

    url = 'https://raw.githubusercontent.com/whis-19/Prob-Dataset/main/songs_normalize.csv'
    df = pd.read_csv(url)

    menu(df)


 
    




from func import *
import time
import os
def menu(df):
    while True:
        print("\nMenu:")
        print("0. Data Info")
        print("1. Scatter Energy-Loudness") 
        print("2. Scatter Speechiness-Popularity")
        print("3. Heatmap Correlation")
        print("4. Plot Feature Distribution")
        print("5. Plot Yearly Distribution")
        print("6. Plot Genre Songs")
        print("7. Plot Genre Popularity")
        print("8. Plot Songs by Each Singer")
        print("9. Plot Top Popular Singers")
        print("10. Plot Top Songs")
        print("11. Plot Tree Map")
        print("12. Plot Explicit Content")
        print("13. Plot Explicit Yearwise")
        print("14. Plot Popularity Explicit")
        print("15. Plot Tempo Popularity")
        print("16. Plot Energy Danceability")
        print("17. Prediction Results")
        print("18. Print Descriptive Statistics")
        print("19. Exit")

        choice = input("Enter your choice (0-19): ")
        if choice == '0':
            df.info()
        elif choice == '1':
            plot_energy_loudness(df)
        elif choice == '2':
            plot_speechiness_popularity(df)
        elif choice == '3':
            heatmap_correlation(df)
        elif choice == '4':
            plot_feature_distribution(df)
        elif choice == '5':
            plot_yearly_distribution(df)
        elif choice == '6':
            plot_genre_songs(df)
        elif choice == '7':
            plot_genre_popularity(df)
        elif choice == '8':
            plot_songs_by_each_singer(df)
        elif choice == '9':
            plot_top_popular_singers(df)
        elif choice == '10':
            n = int(input("Enter no. of top songs you want to check: "))
            plot_top_songs(df,n)
        elif choice == '11':
            plot_tree_map(df)
        elif choice == '12':
            plot_explicit_content(df)
        elif choice == '13':
            plot_explicit_yearwise(df)
        elif choice == '14':
            plot_popularity_explicit(df)
        elif choice == '15':
            plot_tempo_popularity(df)
        elif choice == '16':
            plot_energy_danceability(df)
        elif choice == '17':
            con = int(input("Enter confidance%: "))
            prediction_results(df,con)
        elif choice == '18':
            descriptive_statistics(df)
        elif choice == '19':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 18.")

        
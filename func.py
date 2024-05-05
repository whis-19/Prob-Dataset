from dataProcessing import *

def plot_energy_loudness(df):
    plt.figure(figsize=(10, 10))
    plt.scatter(df['energy'], df['loudness'], c=df['energy'],cmap='plasma')
    plt.colorbar(label='Energy')
    plt.title('Energy versus Loudness correlation')
    plt.xlabel('Energy')
    plt.ylabel('Loudness')
    plt.grid(True)
    plt.show()

def plot_speechiness_popularity(df):
    plt.figure(figsize=(10, 10))
    plt.scatter(df['speechiness'], df['popularity'], c=df['speechiness'], cmap='plasma')
    plt.colorbar(label='Speechiness')
    plt.title('Speechiness Versus Popularity')
    plt.xlabel('Speechiness')
    plt.ylabel('Popularity')
    plt.grid(True)
    plt.show()

def heatmap_correlation(df):
    plt.figure(figsize=(10, 10))
    numeric_df = df._get_numeric_data()
    sns.heatmap(numeric_df.corr(), annot=True, cmap='rocket', fmt=".2f")
    plt.title('Pairwise correlation of columns', fontsize=16)
    plt.title('Pairwise correlation of columns', loc='center')
    plt.show()

def plot_feature_distribution(df):
    fig, axs = plt.subplots(3, 3, figsize=(12, 10))
    features = ['popularity', 'danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'liveness', 'valence', 'tempo']
    data = [df[feature] for feature in features]
    for i, ax in enumerate(axs.flat):
        ax.hist(data[i], bins=20, color='skyblue', edgecolor='black')
        ax.set_title(features[i], fontstyle='italic')
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
    plt.tight_layout()
    plt.suptitle('Feature Distribution', fontsize=16, fontweight='bold', y=1.02)
    plt.show()

def plot_yearly_distribution(df):
    grouped_df = df.groupby('year').count().sort_values(by='year').reset_index()
    years = grouped_df['year']
    total_songs = grouped_df['song']
    plt.figure(figsize=(10, 6))

    plt.plot(years, total_songs, marker='o', color='green')
    plt.title('Year by Year Songs Collection', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Total songs', fontsize=14)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_tree_map(df):
    fig = px.treemap(df, path=[px.Constant('Singer'), 'artist', 'genre', 'song'], values='popularity', title='<b>TreeMap of Singers Playlist')
    fig.update_traces(root_color='lightgreen')
    fig.update_layout(title_x=0.5)
    pio.show(fig, renderer="browser", encoding="utf-8")

def plot_genre_songs(df):
    grouped_df = df.groupby('genre').count().sort_values(by='song', ascending=False).reset_index()
    genres = grouped_df['genre']
    total_songs = grouped_df['song']
    plt.figure(figsize=(10, 6))
    plt.bar(genres, total_songs, color='blue')
    plt.title('Total songs based on genres', fontsize=16)
    plt.xlabel('Genre', fontsize=14)
    plt.ylabel('Total songs', fontsize=14)
    plt.xticks(rotation=90, ha='right')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def plot_top_popular_singers(df):
    top_popular_artists_df = df.groupby('artist').sum().reset_index().sort_values(by='popularity', ascending=False).head(30)
    artists = top_popular_artists_df['artist']
    popularity = top_popular_artists_df['popularity']
    plt.figure(figsize=(12, 10))
    bars = plt.bar(artists, popularity, color='grey')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval), va='bottom', ha='center', fontsize=8)
    plt.xlabel('Artist', fontsize=14)
    plt.ylabel('Popularity', fontsize=14)
    plt.title('Top 30 Popular Singers', fontsize=16)
    plt.xticks(rotation=90)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_songs_by_each_singer(df):
    top_artists_df = df.groupby('artist').size().reset_index(name='total_songs').sort_values(by='total_songs', ascending=False).head(50)
    artists = top_artists_df['artist']
    total_songs = top_artists_df['total_songs']
    plt.figure(figsize=(12, 10))
    bars = plt.bar(artists, total_songs, color='green')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom', ha='center', fontsize=8)
    plt.xlabel('Artist', fontsize=14)
    plt.ylabel('Total Songs', fontsize=14)
    plt.title('List of Songs Recorded by Each Singer', fontsize=16)
    plt.xticks(rotation=90)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_genre_popularity(df):
    grouped_df = df.groupby('genre', as_index=False).sum().sort_values(by='popularity', ascending=False)
    genres = grouped_df['genre']
    popularity = grouped_df['popularity']
    plt.figure(figsize=(10, 6))
    plt.bar(genres, popularity, color='pink')
    plt.title('Popular genres based on popularity', fontsize=16)
    plt.xlabel('Genre', fontsize=14)
    plt.ylabel('Popularity', fontsize=14)
    plt.xticks(rotation=90, ha='right')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def plot_top_songs(df,n): 
    top_songs_df = df.sort_values(by='popularity', ascending=False).head(n)
    songs = top_songs_df['song']
    popularity = top_songs_df['popularity']
    plt.figure(figsize=(12, 6))
    plt.plot(songs, popularity, marker='o', color='green', linestyle='-', linewidth=2)
    for i, txt in enumerate(top_songs_df['artist']):
        plt.annotate(txt, (songs.iloc[i], popularity.iloc[i]), xytext=(10, -5), textcoords='offset points', fontsize=8, ha='center')
    plt.title(f'Top {n} songs in Spotify', fontsize=16)
    plt.xlabel('Song', fontsize=14)
    plt.ylabel('Popularity', fontsize=14)
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_explicit_content(df):

    grouped_df = df.groupby('explicit', as_index=False).count().sort_values(by='song', ascending=False)
    labels = grouped_df['explicit']
    sizes = grouped_df['song']
    colors = ['blue', 'red']
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.axis('equal')
    plt.title('Songs having explicit content', fontsize=16)
    plt.tight_layout()
    plt.show()

def plot_explicit_yearwise(df):
    explicit_df = df[df['explicit'] == True]
    grouped_df = explicit_df.groupby('year', as_index=False).count().sort_values(by='year')
    years = grouped_df['year']
    total_songs = grouped_df['song']
    plt.figure(figsize=(10, 6))
    plt.fill_between(years, total_songs, color='red', alpha=0.5, label='Explicit content songs')
    plt.plot(years, total_songs, marker='o', color='red')
    plt.title('Yearwise explicit content songs', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Total songs', fontsize=14)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_popularity_explicit(df):  
    plt.figure(figsize=(10, 6))
    plt.boxplot([df[df['explicit'] == True]['popularity'], df[df['explicit'] == False]['popularity']],
                labels=['Explicit', 'Non-Explicit'],
                patch_artist=True,
                boxprops=dict(facecolor='pink', color='black'),
                whiskerprops=dict(color='black'),
                capprops=dict(color='black'),
                medianprops=dict(color='blue'),
                flierprops=dict(marker='o', markersize=6, linestyle='none', markerfacecolor='red'))    
    explicit_outliers = df[(df['explicit'] == True) & (df['popularity'] > df['popularity'].quantile(0.75) + 1.5*(df['popularity'].quantile(0.75) - df['popularity'].quantile(0.25)))]
    non_explicit_outliers = df[(df['explicit'] == False) & (df['popularity'] > df['popularity'].quantile(0.75) + 1.5*(df['popularity'].quantile(0.75) - df['popularity'].quantile(0.25)))]
    plt.scatter([1] * len(explicit_outliers), explicit_outliers['popularity'], color='red', label='Explicit outliers')
    plt.scatter([2] * len(non_explicit_outliers), non_explicit_outliers['popularity'], color='red', label='Non-Explicit outliers')
    plt.title('Popularity based on explicit content', fontsize=16)
    plt.xlabel('Explicit', fontsize=14)
    plt.ylabel('Popularity', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()



def plot_tempo_popularity(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['tempo'], df['popularity'], c=df['tempo'], cmap='plasma')
    cbar = plt.colorbar()
    cbar.set_label('Tempo', fontsize=14)
    plt.title('Tempo Versus Popularity', fontsize=16)
    plt.xlabel('Tempo', fontsize=14)
    plt.ylabel('Popularity', fontsize=14)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_energy_danceability(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['energy'], df['danceability'], c=df['danceability'], cmap='plasma')
    cbar = plt.colorbar()
    cbar.set_label('Danceability', fontsize=14)
    plt.title('Energy Versus Danceability', fontsize=16)
    plt.xlabel('Energy', fontsize=14)
    plt.ylabel('Danceability', fontsize=14)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_confidence_interval(lower_bound, upper_bound, confidence):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    counts, bins, _ = ax1.hist(lower_bound, bins=20, density=True, alpha=0.7, color='b')
    ax1.set_title('Lower Bound Confidence Interval')
    ax1.set_xlabel('Value')
    ax1.set_ylabel('Density')

    mu_lower = np.mean(lower_bound)
    poisson_dist_lower = poisson(mu_lower)
    x_lower = np.arange(0, max(bins), 1)
    ax1.plot(x_lower, poisson_dist_lower.pmf(x_lower), color='r', label='Poisson Distribution')
    ax1.legend()

    counts, bins, _ = ax2.hist(upper_bound, bins=20, density=True, alpha=0.7, color='g')
    ax2.set_title('Upper Bound Confidence Interval')
    ax2.set_xlabel('Value')
    ax2.set_ylabel('Density')

    mu_upper = np.mean(upper_bound)
    poisson_dist_upper = poisson(mu_upper)
    x_upper = np.arange(0, max(bins), 1)
    ax2.plot(x_upper, poisson_dist_upper.pmf(x_upper), color='r', label='Poisson Distribution')
    ax2.legend()

    plt.tight_layout()
    plt.show()

def prediction_results(df,confidance):
    models, evaluation_results = train_predict_regression_model(df,confidance)
    for name, metrics in evaluation_results.items():
        print(f"Model: {name}")
        print(f"Train Score: {metrics['Train Score']:.2f}")
        print(f"Test Score: {metrics['Test Score']:.2f}")
        print(f"Prediction Score: {metrics['Prediction Score']:.2f}")
        print(f"Original Score: {metrics['Original Score']:.2f}")  
        #print(f"Confidence Interval : [{metrics['Lower Bound']}, {metrics['Upper Bound']}]")
        print()
    plot_confidence_interval(metrics['Lower Bound'],metrics['Upper Bound'],confidance)

def descriptive_statistics(df):
    print("Descriptive Statistics:")
    print(df.describe())
    print("\nMode Statistics:")
    print(df.mode())

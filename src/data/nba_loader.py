import os
import pandas as pd
from nba_api.stats.endpoints import leaguegamelog
from nba_api.stats.library.parameters import SeasonAll

def fetch_nba_season_data(season_year: str, save_path: str = "data/raw"):
    """
    Fetches the entire season's game logs for all teams.
    
    Args:
        season_year (str): Format '2023-24'
        save_path (str): Relative path to save the CSV
    """

    print(f"--- Fetching NBA data for season: {season_year} ---")
    log = leaguegamelog.LeagueGameLog(season=season_year, player_or_team_abbreviation='T')

    df = log.get_data_frames()[0]

    if df.empty:
        print("Error: No data found. Check your season string format (e.g., '2023-24').")
        return None

    os.makedirs(save_path, exist_ok=True)
    
    filename = f"nba_gamelogs_{season_year.replace('-', '_')}.csv"
    full_path = os.path.join(save_path, filename)
    
    df.to_csv(full_path, index=False)
    print(f"Success! Data saved to: {full_path}")
    print(f"Total Games Fetched: {len(df)}")
    
    return full_path

if __name__ == "__main__":
    # Quick test to run this file directly
    fetch_nba_season_data("2023-24")

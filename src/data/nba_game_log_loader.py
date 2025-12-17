import os
import pandas as pd
from nba_api.stats.endpoints import leaguegamelog

def fetch_nba_team_data(season_year: str, save_path: str = "data/raw"):
    """
    Fetches the entire season's game logs for TEAMS.
    """
    print(f"--- Fetching NBA TEAM data for season: {season_year} ---")
    
    log = leaguegamelog.LeagueGameLog(season=season_year, player_or_team_abbreviation='T')
    df = log.get_data_frames()[0]
    
    if df.empty:
        print("Error: No team data found.")
        return None

    os.makedirs(save_path, exist_ok=True)
    filename = f"nba_team_gamelogs_{season_year.replace('-', '_')}.csv"
    full_path = os.path.join(save_path, filename)
    
    df.to_csv(full_path, index=False)
    print(f"Success! Team data saved to: {full_path}")
    return full_path

def fetch_nba_player_data(season_year: str, save_path: str = "data/raw"):
    """
    Fetches the entire season's game logs for PLAYERS.
    """
    print(f"--- Fetching NBA PLAYER data for season: {season_year} ---")
    
    # Switch 'T' to 'P' to get player stats
    log = leaguegamelog.LeagueGameLog(season=season_year, player_or_team_abbreviation='P')
    df = log.get_data_frames()[0]
    
    if df.empty:
        print("Error: No player data found.")
        return None

    os.makedirs(save_path, exist_ok=True)
    filename = f"nba_player_gamelogs_{season_year.replace('-', '_')}.csv"
    full_path = os.path.join(save_path, filename)
    
    df.to_csv(full_path, index=False)
    print(f"Success! Player data saved to: {full_path}")
    return full_path

if __name__ == "__main__":
    # Test both functions
    fetch_nba_season_data("2023-24")
    fetch_nba_player_data("2023-24")
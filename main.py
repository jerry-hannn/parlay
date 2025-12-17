from src.data.nba_game_log_loader import fetch_nba_team_data, fetch_nba_player_data

def main():
    # In the future, this year will be pulled from config/config.yaml
    target_season = "2024-25"
    
    team_raw_path = fetch_nba_team_data(target_season)

    player_raw_path = fetch_nba_player_data(target_season)


if __name__ == "__main__":
    main()

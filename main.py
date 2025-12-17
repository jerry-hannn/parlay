from src.data.nba_loader import fetch_nba_season_data

def main():
    # In the future, this year will be pulled from config/config.yaml
    target_season = "2024-25"
    
    # 1. Ingestion
    raw_file_path = fetch_nba_season_data(target_season)
    
    if raw_file_path:
        print(f"Pipeline finished. Raw data ready at {raw_file_path}")

if __name__ == "__main__":
    main()

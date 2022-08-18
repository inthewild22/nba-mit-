import pandas as pd

if __name__ == "__main__":
    print("this file is not meant to be run directly")
    # generating the schedule for the regular season
    with open("games.csv", 'r') as f:
        #     create a dataframe from the csv file
        df = pd.read_csv(f)
    # filter the dataframe to only include the 2021 season
    df2021 = df.query("SEASON == 2021")
    # filter dataframe to only include dates between 2021-10-19 and 2022-04-29 (regular season)
    df_reg_season = df2021.query('GAME_DATE_EST>= "2021-10-19" and GAME_DATE_EST <= "2022-04-29"')
#     save dataframe to csv file
    df_reg_season.to_csv("2021_regular_season.csv", index=False)


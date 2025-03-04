# Programmer: Mason Colacicco
# Date: March
# Program: Caitlyn Clark

def main():
    # Initialize first 3 seasons
    seasons = [799, 863, 1055]
    ppgs = [26.6, 27.0, 27.8]
    # ppg doubled its increase from season 2 to 3 compared to season 1 to 2
    # So I will double the difference every season
    ppg_rate = 0.8
    # season point difference tripled from season to season 64 between first two and 192 between second 2
    season_rate = 192

    # While the total begins to become unrealistic, based off of the data it will exponentially increase
    for i in range(2):
        ppg_rate *= 2
        season_rate *= 3
        ppgs.append(max(ppgs)+ppg_rate)
        seasons.append(max(seasons)+season_rate)

    # loop to display data
    for i in range(len(seasons)):
        print(f"Season {i+1} Total: {seasons[i]} \nSeason {i+1} ppg: {ppgs[i]:.1f}")


# Call main function
if __name__ == '__main__':
    main()
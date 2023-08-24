class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

    def display(self):
        print(f"Location: {self.location}, Team 1: {self.team1}, Team 2: {self.team2}, Timing: {self.timing}")


class MatchData:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def search_by_team(self, team):
        print(f"Matches involving {team}:")
        for match in self.matches:
            if team in [match.team1, match.team2]:
                match.display()

    def search_by_location(self, location):
        print(f"Matches at {location}:")
        for match in self.matches:
            if match.location == location:
                match.display()

    def search_by_timing(self, timing):
        print(f"Matches with timing {timing}:")
        for match in self.matches:
            if match.timing == timing:
                match.display()


def main():
    match_data = MatchData()

    match_data.add_match(Match("Mumbai", "India", "Sri Lanka", "DAY"))
    match_data.add_match(Match("Delhi", "England", "Australia", "DAY-NIGHT"))
    match_data.add_match(Match("Chennai", "India", "South Africa", "DAY"))
    match_data.add_match(Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
    match_data.add_match(Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
    match_data.add_match(Match("Delhi", "India", "Australia", "DAY"))

    while True:
        print("\nSearch Options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            team = input("Enter team name: ")
            match_data.search_by_team(team)
        elif choice == 2:
            location = input("Enter location: ")
            match_data.search_by_location(location)
        elif choice == 3:
            timing = input("Enter timing: ")
            match_data.search_by_timing(timing)
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()

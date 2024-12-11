#define the  member class to represent team members 
class Member:
#initialize a member with a name 
    def init(self, name):
        self.name = name  

#provide a readable string representation of the member  
def __repr__(self):  
    return self.name  


# Define the Team class to manage teams
class Team:
# Initialize a team with a name    
    def init(self, name):
        self.name = name
# Using a set to avoid duplicate members  
        
        self.team_members = set()   
 
 # Adding a member to the team
    def add_member(self, member): 
         # Check if the member is already in the team
        if member in self.team_members: 
            print(f"{member.name} is already a member of team {self.name}.")  
        else:  
            # Adding the member to the team
            self.team_members.add(member)  
            print(f"Added {member.name} to team {self.name}.")  

    def __repr__(self):  # Provide a readable string representation of the team
        return self.name  

# Define the Project class to manage projects and associated teams
class Project:
     # Initialize a project with a name
    def __init__(self, name): 
        self.name = name
        self.teams = []  # Store teams in a list  


 # Assign a team to the project
    def assign_team(self, team): 
        if team not in self.teams:  # Check if the team is already assigned
            # Assigned the team to the project
            self.teams.append(team)  
            print(f"Assigned team {team.name} to project {self.name}.")  
        else:  
            print(f"Team {team.name} is already assigned to project {self.name}.")  

    def display_members(self):  # Display all unique members in the project
        unique_members = set()  # Store unique members
        for team in self.teams:  
            unique_members.update(team.team_members)  # Add team members
        print(f"Members in project {self.name}: {', '.join(str(member) for member in unique_members)}")  

    def total_unique_members(self):  # Calculate total unique members in the project
        unique_members = set()  # Store unique members
        for team in self.teams:  
            unique_members.update(team.team_members)  
        return len(unique_members)  # Return the count
#Creating members
maxwell = Member("maxwell")# Create a member named maxwell
peter = Member("iris") # Create a member named peter
iris = Member("peter")   # Create a member named iris

#create teams
team_a = Team("Team A") # Create a team named Team A
  # Create a team named Team B
team_b = Team("Team B")  
#add members to team A
 # Add iris to Team A
team_a.add_member(iris)
team_a.add_member(peter)
#add 
team_b.add_member(peter)  
team_b.add_member(iris)  

#add maxwell to team A
team_a.add_member(maxwell)  
 

project_1 = Project("Project 1")
project_2 = Project("Project 2")  

project_1.assign_team(team_a)
project_2.assign_team(team_b)  

project_1.display_members()
 
project_2.display_members()  
# Calculate total unique members across both projects
total_unique = project_1.total_unique_members() + project_2.total_unique_members()
print(f"Total unique members across all projects: {total_unique}")
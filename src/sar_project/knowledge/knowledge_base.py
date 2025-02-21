class KnowledgeBase:
    def __init__(self):
        """
        Initializes the knowledge base with empty datasets for terrain, weather,
        resources, and mission history.
        """
        self.volunteers = {}  # Stores volunteer data
    
    def add_volunteer(self, volunteer_id, name, contact_info, skills, availability, location, health_status, task_preferences, satisfaction_scores):
        """
        Adds a volunteer to the knowledge base with detailed information.

        Args:
            volunteer_id (str): Unique identifier for the volunteer.
            name (str): Full name of the volunteer.
            contact_info (dict): Contact details such as email and phone number.
            skills (list): List of skills the volunteer possesses.
            availability (dict): Availability schedule (e.g., days and hours available).
            location (str): Geographic location of the volunteer.
            health_status (str): Health and fitness status of the volunteer.
            task_preferences (list): List of tasks the volunteer prefers.
            satisfaction_scores (dict): Feedback or satisfaction ratings from previous tasks.
        """
        self.volunteers[volunteer_id] = {
            "name": name,
            "contact_info": contact_info,
            "skills": skills,
            "availability": availability,
            "location": location,
            "health_status": health_status,
            "task_preferences": task_preferences,
            "satisfaction_scores": satisfaction_scores,
            "assigned_tasks": []
        }
      
    def create_roster(self, required_skills):
        """
        Creates a roster of volunteers who match the required skills and are available.

        Args:
            required_skills (list): List of skills needed for a task.

        Returns:
            list: A list of volunteers available for task assignments.
        """
        available_volunteers = []
        for volunteer_id, volunteer_data in self.volunteers.items():
            if all(skill in volunteer_data["skills"] for skill in required_skills) and any(volunteer_data["availability"].values()):
                available_volunteers.append(volunteer_id)
        return available_volunteers
    
    def assign_task(self, volunteer_id, task_details):
        """
        Assigns a task to a volunteer if they are available.

        Args:
            volunteer_id (str): The volunteer to assign.
            task_details (dict): Task description, location, etc.

        Returns:
            str: Confirmation message.
        """
        if volunteer_id not in self.volunteers:
            return f"Volunteer {volunteer_id} not found."

        volunteer = self.volunteers[volunteer_id]

        # Check if volunteer is already assigned a task
        if volunteer["assigned_tasks"]:
            return f"{volunteer['name']} is already assigned a task."

        # Assign the task
        task_id = f"task_{len(volunteer['assigned_tasks']) + 1}"
        volunteer["assigned_tasks"].append(task_details)

        return f"Assigned task to {volunteer['name']}: {task_details['description']}"
        
    def complete_task(self, volunteer_id):
        """
        Marks the volunteer's active task as complete.

        Args:
            volunteer_id (str): The volunteer who completed their task.

        Returns:
            str: Confirmation message.
        """
        if volunteer_id not in self.volunteers:
            return f"Volunteer {volunteer_id} not found."

        volunteer = self.volunteers[volunteer_id]

        if not volunteer["assigned_tasks"]:
            return f"{volunteer['name']} has no active tasks."

        completed_task = volunteer["assigned_tasks"].pop(0)
        return f"{volunteer['name']} completed task: {completed_task['description']}"
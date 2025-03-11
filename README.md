# SAR Volunteer Coordination Agent

# Modifications

## Insights You Gained

- **Understanding of Volunteer Management**: Through the process of developing this agent, I gained deeper insight into the complexity of managing volunteer data, including their skills, availability, and preferences. Tracking volunteers' tasks and availability in a dynamic environment like SAR operations requires careful planning and thoughtful data management.

- **Challenges of Task Assignment and Availability**: Managing task assignment dynamically, while ensuring no conflicts or duplications, was a challenge. I realized that a real-time system would require advanced scheduling and conflict resolution logic, which isn't fully implemented yet but is part of future plans.

- **Importance of Tracking Volunteer Hours**: One significant realization was the need to track volunteer hours worked, especially in a SAR setting. This data is essential for managing volunteer workload, ensuring fair distribution of tasks, and generating performance reports.

- **Value of Flexibility in Data Management**: The process highlighted the importance of allowing volunteer data to be updated after it has been added to the system. Volunteers may change their availability, skills, or health status, so a system that can adapt to these changes is critical for effective management.

## Modifications You Made

- **Volunteer Information Update**: A new method was added to the `KnowledgeBase` class to allow for the updating of existing volunteer information. This enables the system to accommodate changes in volunteer availability, skills, or other attributes after their initial entry into the system. The new method ensures that volunteer data remains accurate and up-to-date.

    ```python
    def update_volunteer(self, volunteer_id, updated_info):
        if volunteer_id in self.volunteers:
            self.volunteers[volunteer_id].update(updated_info)
            return f"Volunteer {volunteer_id} updated successfully."
        return f"Volunteer {volunteer_id} not found."
    ```

- **Volunteer Hours Tracking**: A mechanism was introduced to track the hours worked by each volunteer. This allows the system to store and report on the total number of hours a volunteer has worked. The tracking is done through the `hours_worked` attribute, and methods were added to update and retrieve this data.

    ```python
    def add_hours_worked(self, volunteer_id, hours):
        if volunteer_id in self.volunteers:
            self.volunteers[volunteer_id]["hours_worked"] = self.volunteers[volunteer_id].get("hours_worked", 0) + hours
            return f"{hours} hours added to {volunteer_id}'s record."
        return f"Volunteer {volunteer_id} not found."
    ```

- **Report Generation**: A report generation feature was added that compiles volunteer hours worked and other relevant information into a readable format. This feature can be used for performance evaluation and resource planning.

    ```python
    def generate_report(self):
        report = {}
        for volunteer_id, volunteer_data in self.volunteers.items():
            report[volunteer_id] = volunteer_data.get("hours_worked", 0)
        return report
    ```

- **Status Tracking Integration**: The `VolunteerCoordinatorAgent` class was modified to integrate the status tracking functionality. This allows the agent to track its current mission status and update it dynamically. This feature helps in monitoring the operational state of the coordination agent.

    ```python
    def update_status(self, status):
        self.mission_status = status
        return {"status": "updated", "new_status": status}
    ```

---

## Overview
The **SAR Volunteer Coordination Agent** is designed to manage volunteer resources in Search and Rescue (SAR) operations. It utilizes a **Knowledge Base** to maintain volunteer data, create rosters based on required skills, assign tasks, and track volunteer availability.

## Features
- **Volunteer Management**: Add and store volunteer details, including skills, availability, task preferences, and hours worked.
- **Roster Generation**: Create lists of available volunteers based on required skills.
- **Task Assignment**: Assign tasks to volunteers based on their availability and skillset.
- **Status Tracking**: Update and retrieve the mission status of the volunteer coordination agent.
- **Volunteer Hours Tracking**: Track volunteer hours worked and generate reports based on that data.
- **Data Updates**: Update volunteer details, such as skills, availability, and task preferences.

## Components

### 1. KnowledgeBase Class
The `KnowledgeBase` stores volunteer data and provides functions to:
- **Add Volunteers**: Store contact info, skills, availability, task preferences, and hours worked.
- **Update Volunteer Information**: Update existing volunteer details such as skills, availability, and task preferences.
- **Create Rosters**: Generate lists of available volunteers based on required skills.
- **Assign Tasks**: Allocate tasks to volunteers if they are available.
- **Complete Tasks**: Mark tasks as completed when volunteers finish assignments.
- **Track Hours Worked**: Track and store the number of hours worked by each volunteer.
- **Generate Reports**: Generate reports of volunteers and their hours worked.

### 2. VolunteerCoordinatorAgent Class
The `VolunteerCoordinatorAgent` extends `SARBaseAgent` and handles volunteer coordination tasks:
- **Processes Requests**: Handles messages to create rosters, add volunteers, and retrieve volunteer information.
- **Manages Knowledge Base**: Uses `KnowledgeBase` to store and retrieve data.
- **Tracks Status**: Updates and retrieves the mission status of the agent.

## Limitations
- **Lack of Validation**: The current implementation does not rigorously check for task duplication or conflicts when assigning tasks. Future improvements should introduce better validation mechanisms.
- **Minimal Exception Handling**: There are minimal safeguards for handling unexpected input or missing data.

## Usage
1. **Initialize the Agent**:
    ```python
    from sar_project.agents.volunteer_coordinator_agent import VolunteerCoordinatorAgent
    agent = VolunteerCoordinatorAgent()
    ```

2. **Add a Volunteer**:
    ```python
    message = {
        "action": "add_volunteer",
        "volunteer_data": {
            "volunteer_id": "vol1",
            "name": "John Doe",
            "contact_info": {"email": "johndoe@example.com", "phone": "123-456-7890"},
            "skills": ["First Aid", "CPR"],
            "availability": {"Mon": True, "Tue": False},
            "location": "City A",
            "health_status": "Good",
            "task_preferences": ["Medical Support"],
            "satisfaction_scores": {"task1": 5, "task2": 4}
        }
    }
    agent.process_request(message)
    ```

3. **Create a Roster**:
    ```python
    roster = agent.process_request({"action": "create_roster", "required_skills": ["First Aid"]})
    print(roster)
    ```

4. **Retrieve Volunteer Information**:
    ```python
    volunteer_info = agent.process_request({"action": "get_volunteer_info", "volunteer_id": "vol1"})
    print(volunteer_info)
    ```

## Testing
The functionality of the **VolunteerCoordinatorAgent** is tested using `pytest`:


- **Test Initialization**: Ensures agent properties are correctly set.
- **Test Adding Volunteers**: Verifies if volunteer data is stored correctly.
- **Test Updating Volunteers**: Verifies if volunteer data can be updated successfully.
- **Test Roster Creation**: Ensures volunteers are properly selected based on required skills.
- **Test Report Generation**: Verifies volunteer hours are tracked and reports are generated correctly.


### Run Tests
To execute tests, run:
```bash
pytest tests/
```

---
This agent streamlines SAR volunteer coordination, ensuring efficient resource management and task allocation.


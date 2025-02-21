# SAR Volunteer Coordination Agent

## Overview
The **SAR Volunteer Coordination Agent** is designed to manage volunteer resources in Search and Rescue (SAR) operations. It utilizes a **Knowledge Base** to maintain volunteer data, create rosters based on required skills, assign tasks, and track volunteer availability.

## Features
- **Volunteer Management**: Add and store volunteer details, including skills, availability, and task preferences.
- **Roster Generation**: Create lists of available volunteers matching required skills.
- **Task Assignment**: Assign tasks to volunteers based on their availability.
- **Status Tracking**: Update and retrieve the mission status of the volunteer coordination agent.

## Components

### 1. KnowledgeBase Class
The `KnowledgeBase` stores volunteer data and provides functions to:
- **Add Volunteers**: Store contact info, skills, availability, and task preferences.
- **Create Rosters**: Generate lists of available volunteers based on required skills.
- **Assign Tasks**: Allocate tasks to volunteers if they are available.
- **Complete Tasks**: Mark tasks as completed when volunteers finish assignments.

### 2. VolunteerCoordinatorAgent Class
The `VolunteerCoordinatorAgent` extends `SARBaseAgent` and handles volunteer coordination tasks:
- **Processes Requests**: Handles messages to create rosters, add volunteers, and retrieve volunteer information.
- **Manages Knowledge Base**: Uses `KnowledgeBase` to store and retrieve data.
- **Tracks Status**: Updates and retrieves the mission status of the agent.

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
- **Test Roster Creation**: Ensures volunteers are properly selected based on required skills.

### Run Tests
To execute tests, run:
```bash
pytest tests/
```

## Future Enhancements
- **Automated Task Scheduling**: Improve task assignments based on real-time availability.
- **Volunteer Feedback System**: Implement a system for volunteers to provide feedback on task experiences.
- **Integration with External Databases**: Sync volunteer data with external sources for real-time updates.

---
This agent streamlines SAR volunteer coordination, ensuring efficient resource management and task allocation.


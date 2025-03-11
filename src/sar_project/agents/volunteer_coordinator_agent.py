from sar_project.agents.base_agent import SARBaseAgent
from sar_project.knowledge import KnowledgeBase

class VolunteerCoordinatorAgent(SARBaseAgent):
    def __init__(self, name="volunteer_coordinator", knowledge_base=None):
        super().__init__(
            name=name,
            role="Volunteer Coordinator",
            system_message="""You manage volunteer resources for SAR operations. Your responsibilities include:
            - Creating rosters based on required skills
            - Managing volunteer availability
            - Generating time-sensitive updates on volunteer status"""
        )
        self.kb = knowledge_base or KnowledgeBase()  # Use existing KB or initialize one
        self.mission_status = "standby"  # Initial status

    def process_request(self, message):
        """Handles volunteer coordination requests."""
        action = message.get("action")

        if action == "create_roster":
            return self.kb.create_roster(message.get("required_skills", []))
        elif action == "add_volunteer":
            return self.kb.add_volunteer(**message.get("volunteer_data", {}))
        elif action == "get_volunteer_info":
            return self.kb.volunteers.get(message.get("volunteer_id"), {"error": "Volunteer not found"})
        elif action == "update_volunteer_info":
            return self.update_volunteer_info(message.get("volunteer_id"), message.get("updated_data"))
        elif action == "track_hours":
            return self.track_hours(message.get("volunteer_id"), message.get("hours"))
        elif action == "generate_report":
            return self.generate_report()
        else:
            return {"error": "Unknown request type"}

    def update_volunteer_info(self, volunteer_id, updated_data):
        """Update existing volunteer information."""
        if volunteer_id in self.kb.volunteers:
            self.kb.volunteers[volunteer_id].update(updated_data)
            return {"status": "updated", "volunteer_id": volunteer_id}
        return {"error": "Volunteer not found"}

    def track_hours(self, volunteer_id, hours):
        """Track volunteer hours worked."""
        if volunteer_id in self.kb.volunteers:
            if 'hours_worked' not in self.kb.volunteers[volunteer_id]:
                self.kb.volunteers[volunteer_id]['hours_worked'] = 0
            self.kb.volunteers[volunteer_id]['hours_worked'] += hours
            return {"status": "updated", "volunteer_id": volunteer_id, "hours_worked": self.kb.volunteers[volunteer_id]['hours_worked']}
        return {"error": "Volunteer not found"}

    def generate_report(self):
        """Generate a report of all volunteers and their hours."""
        report = []
        for volunteer_id, data in self.kb.volunteers.items():
            report.append({
                "volunteer_id": volunteer_id,
                "name": data.get('name', 'N/A'),
                "skills": data.get('skills', []),
                "hours_worked": data.get('hours_worked', 0),
                "availability": data.get('availability', {}),
                "task_preferences": data.get('task_preferences', [])
            })
        return report

    def update_status(self, status):
        """Update agent's mission status"""
        self.mission_status = status
        return {"status": "updated", "new_status": status}
    
    def get_status(self):
        """Return current status"""
        return self.mission_status

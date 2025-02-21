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

    def process_request(self, message):
        """Handles volunteer coordination requests."""
        action = message.get("action")

        if action == "create_roster":
            return self.kb.create_roster(message.get("required_skills", []))
        elif action == "add_volunteer":
            return self.kb.add_volunteer(**message.get("volunteer_data", {}))
        elif action == "get_volunteer_info":
            return self.kb.volunteers.get(message.get("volunteer_id"), {"error": "Volunteer not found"})
        else:
            return {"error": "Unknown request type"}
    
    def update_status(self, status):
        """Update agent's mission status"""
        self.mission_status = status
        return {"status": "updated", "new_status": status}
    
    def get_status(self):
        """Return current status"""
        return self.mission_status
    
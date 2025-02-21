import pytest
from sar_project.agents.volunteer_coordinator_agent import VolunteerCoordinatorAgent

class TestVolunteerAgent:
    @pytest.fixture
    def agent(self):
        return VolunteerCoordinatorAgent()
    
    def test_initialization(self, agent):
        assert agent.name == "volunteer"
        assert agent.role == "Volunteer"
        assert agent.mission_status == "standby"
    
    # Test add volunteer
    def test_process_request(self, agent):
        message = {
            "action": "add_volunteer",
            "volunteer_data": {
                "volunteer_id": "test_id",
                "name": "Test Volunteer",
                "contact_info": {"email": "", "phone": ""},
                "skills": ["First Aid", "CPR"],
                "availability": {"Mon": True, "Tue": False},
                "location": "Test City",
                "health_status": "Good",
                "task_preferences": ["Medical Support"],
                "satisfaction_scores": {"task1": 5, "task2": 4}
            }
        }
        response = agent.process_request(message)
        assert agent.kb.volunteers["test_id"] == message["volunteer_data"]
    
    # Test create roster
    def test_create_roster(self, agent):
        agent.kb.add_volunteer(
            volunteer_id="volunteer1",
            name="Volunteer 1",
            contact_info={"email": "", "phone": ""},
            skills=["First Aid", "CPR"],
            availability={"Mon": True, "Tue": False},
            location="Test City",
            health_status="Good",
            task_preferences=["Medical Support"],
            satisfaction_scores={"task1": 5, "task2": 4}
        )
        agent.kb.add_volunteer(
            volunteer_id="volunteer2",
            name="Volunteer 2",
            contact_info={"email": "", "phone": ""},
            skills=["First Aid", "Search & Rescue"],
            availability={"Mon": True, "Tue": True},
            location="Test City",
            health_status="Good",
            task_preferences=["Medical Support", "Search Operations"],
            satisfaction_scores={"task1": 4, "task2": 3}
        )
        roster = agent.kb.create_roster(["First Aid"])
        assert "volunteer1" in roster
        assert "volunteer2" in roster
    

        
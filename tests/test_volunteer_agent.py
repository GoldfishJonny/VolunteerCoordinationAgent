import pytest
from sar_project.agents.volunteer_coordinator_agent import VolunteerCoordinatorAgent

class TestVolunteerAgent:
    @pytest.fixture
    def agent(self):
        return VolunteerCoordinatorAgent()

    def test_initialization(self, agent):
        assert agent.name == "volunteer_coordinator"
        assert agent.role == "Volunteer Coordinator"
        assert agent.mission_status == "standby"

    def test_process_request_add_volunteer(self, agent):
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
        print(agent.kb.volunteers['test_id'])
        assert agent.kb.volunteers["test_id"] == {
            'assigned_tasks': [],
            'availability': {'Mon': True, 'Tue': False},
            'contact_info': {'email': '', 'phone': ''},
            'health_status': 'Good',
            'location': 'Test City',
            'name': 'Test Volunteer',
            'satisfaction_scores': {'task1': 5, 'task2': 4},
            'skills': ['First Aid', 'CPR'],
            'task_preferences': ['Medical Support'],
            'hours_worked': 0  # New field for hours worked
        }

    def test_process_request_update_volunteer_info(self, agent):
        agent.kb.add_volunteer(
            volunteer_id="volunteer1",
            name="Volunteer 1",
            contact_info={"email": "", "phone": ""},
            skills=["First Aid"],
            availability={"Mon": True},
            location="Test City",
            health_status="Good",
            task_preferences=["Medical Support"],
            satisfaction_scores={"task1": 5}
        )

        updated_data = {
            "skills": ["First Aid", "CPR"],
            "availability": {"Mon": True, "Tue": False}
        }

        message = {
            "action": "update_volunteer_info",
            "volunteer_id": "volunteer1",
            "updated_data": updated_data
        }

        response = agent.process_request(message)
        assert response["status"] == "updated"
        assert agent.kb.volunteers["volunteer1"]["skills"] == ["First Aid", "CPR"]
        assert agent.kb.volunteers["volunteer1"]["availability"] == {"Mon": True, "Tue": False}

    def test_process_request_track_hours(self, agent):
        message = {
            "action": "track_hours",
            "volunteer_id": "volunteer1",
            "hours": 5
        }
        agent.kb.add_volunteer(
            volunteer_id="volunteer1",
            name="Volunteer 1",
            contact_info={"email": "", "phone": ""},
            skills=["First Aid"],
            availability={"Mon": True},
            location="Test City",
            health_status="Good",
            task_preferences=["Medical Support"],
            satisfaction_scores={"task1": 5}
        )
        response = agent.process_request(message)
        assert response["status"] == "updated"
        assert agent.kb.volunteers["volunteer1"]["hours_worked"] == 5

    def test_generate_report(self, agent):
        agent.kb.add_volunteer(
            volunteer_id="volunteer1",
            name="Volunteer 1",
            contact_info={"email": "", "phone": ""},
            skills=["First Aid"],
            availability={"Mon": True},
            location="Test City",
            health_status="Good",
            task_preferences=["Medical Support"],
            satisfaction_scores={"task1": 5},
            hours_worked=10
        )

        report = agent.process_request({"action": "generate_report"})
        assert len(report) == 1
        assert report[0]["volunteer_id"] == "volunteer1"
        assert report[0]["hours_worked"] == 10

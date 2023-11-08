from AdvancedChatbot import AdvancedChatbot

class SoftwareManagementChatbot:
    def __init__(self):
        self.advanced_chatbot = AdvancedChatbot()
        self.projects = {}
        self.users = {}
        self.current_user = None

    def handle_message(self, message):
        message = message.lower()

        if self.current_user is None:
            if "login" in message:
                self.current_user = "your_user_id"  # Replace with the actual user ID
                return "You've been logged in. How can I assist you?"
            else:
                return "Please log in first."

        if "create project" in message:
            return self.handle_create_project()

        if "manage project" in message:
            return self.handle_manage_project(message)

        if "show projects" in message:
            return self.show_projects()

        if "logout" in message:
            self.current_user = None
            return "You've been logged out. Have a great day!"

        return self.advanced_chatbot.get_response(message)  # Use AdvancedChatbot for default responses

    def handle_create_project(self):
        project_name = input("Enter project name: ")
        self.projects[project_name] = {
            "tasks": [],
            "code_quality": [],
            "details": {}
            # Add more project details based on your requirements
        }
        return f"Project '{project_name}' created successfully."

    def handle_manage_project(self, message):
        project_name = input("Enter project name: ")
        if project_name in self.projects:
            project = self.projects[project_name]

            if "add task" in message:
                task_name = input("Enter task name: ")
                project["tasks"].append(task_name)
                return f"Task '{task_name}' added to the project."

            if "analyze code quality" in message:
                code_quality_report = input("Enter code quality report: ")
                project["code_quality"].append(code_quality_report)
                return "Code quality analysis recorded."

            if "show project details" in message:
                return f"Project Details: {project['details']}"

        else:
            return "Project not found. Please create the project first."

    def show_projects(self):
        project_list = ", ".join(self.projects.keys())
        if project_list:
            return f"Projects: {project_list}"
        else:
            return "No projects found."

if __name__ == "__main__":
    software_chatbot = SoftwareManagementChatbot()

    print("Welcome to the Software Management Chatbot!")

    while True:
        user_input = input("User: ")
        if user_input == "goodbye":
            break

        response = software_chatbot.handle_message(user_input)
        print("Chatbot:", response)
while True:
    user_input = input("User: ")
    if user_input == "goodbye":
        print("Goodbye!")
        break  # Exit the program

    response = software_chatbot.handle_message(user_input)
    print("Chatbot:", response)

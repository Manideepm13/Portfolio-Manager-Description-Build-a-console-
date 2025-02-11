import tkinter as tk
from tkinter import filedialog, messagebox
import os

class DesignProject:
    def __init__(self, name, description, feedback, image_path):
        self.name = name
        self.description = description
        self.feedback = feedback
        self.image_path = image_path

    def __str__(self):
        return f"Project: {self.name}\nDescription: {self.description}\nClient Feedback: {self.feedback}\nImage Path: {self.image_path}"

class PortfolioManager:
    def __init__(self):
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)
        messagebox.showinfo("Success", "Project added successfully!")

    def view_portfolio(self):
        if not self.projects:
            return "No projects in portfolio."
        portfolio = ""
        for idx, project in enumerate(self.projects):
            portfolio += f"{idx + 1}. {project.name}\nDescription: {project.description}\nClient Feedback: {project.feedback}\nImage Path: {project.image_path}\n\n"
        return portfolio

    def get_project_images(self):
        image_paths = ""
        for project in self.projects:
            image_paths += f"{project.name}: {project.image_path}\n"
        return image_paths if image_paths else "No images available."

class PortfolioApp(tk.Tk):
    def __init__(self, portfolio_manager):
        super().__init__()
        self.portfolio_manager = portfolio_manager
        self.title("Design Portfolio Manager")
        self.geometry("600x500")

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Design Portfolio Manager", font=("Arial", 18))
        self.title_label.pack(pady=20)

        self.view_button = tk.Button(self, text="View Portfolio", command=self.view_portfolio)
        self.view_button.pack(pady=10)

        self.add_button = tk.Button(self, text="Add Project", command=self.add_project_window)
        self.add_button.pack(pady=10)

        self.display_area = tk.Text(self, width=70, height=10)
        self.display_area.pack(pady=20)
        
    def add_project_window(self):
        add_window = tk.Toplevel(self)
        add_window.title("Add New Project")
        add_window.geometry("500x400")

        tk.Label(add_window, text="Project Name").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack(pady=5)

        tk.Label(add_window, text="Description").pack(pady=5)
        description_entry = tk.Entry(add_window)
        description_entry.pack(pady=5)

        tk.Label(add_window, text="Client Feedback").pack(pady=5)
        feedback_entry = tk.Entry(add_window)
        feedback_entry.pack(pady=5)

        tk.Label(add_window, text="Image File Path (optional)").pack(pady=5)
        image_entry = tk.Entry(add_window)
        image_entry.pack(pady=5)

        def save_project():
            name = name_entry.get()
            description = description_entry.get()
            feedback = feedback_entry.get()
            image_path = image_entry.get()

            if name and description and feedback:
                project = DesignProject(name, description, feedback, image_path)
                self.portfolio_manager.add_project(project)
                self.update_display()
                add_window.destroy()
            else:
                messagebox.showerror("Error", "Please fill in all required fields.")

        tk.Button(add_window, text="Save Project", command=save_project).pack(pady=10)

    def view_portfolio(self):
        portfolio = self.portfolio_manager.view_portfolio()
        self.display_area.delete(1.0, tk.END)
        self.display_area.insert(tk.END, portfolio)

    def update_display(self):
        self.display_area.delete(1.0, tk.END)
        portfolio = self.portfolio_manager.view_portfolio()
        self.display_area.insert(tk.END, portfolio)

if __name__ == "__main__":
    portfolio_manager = PortfolioManager()
    app = PortfolioApp(portfolio_manager)
    app.mainloop()

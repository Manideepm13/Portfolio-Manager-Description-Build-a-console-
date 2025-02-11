# Design Portfolio Manager

This project is a console-based portfolio manager for designers. It allows users to add and view their design projects, including project details such as name, description, images (represented in file paths or ASCII format), and client feedback. The system is designed to help designers organize and showcase their work through a simple user interface.

Project Structure

Design_Portfolio_Manager/

├── main.py

├── portfolio_manager.py

├── portfolio_data.json

├── gui.py

├── README.md

└── images/

Key Features

    Add Projects: Collect and store details about your design projects.
    
    View Portfolio: Display all design projects in a clear, organized manner.
    
    Manage Data: CRUD operations (Create, Read, Update, Delete) to manage design projects.
    
    Image Support: Link project images by file path for visualization.
    
    Client Feedback: Include feedback from clients to highlight project success.

    File Descriptions
    
 main.py

    Purpose: The main Python script that runs the application. It handles the backend functionality, such as collecting input from users, storing project details, and displaying the portfolio.

 Run the Python script
```
    python app.py
   ```

Software Requirements

To run this project, you will need the following software installed on your system:

    Python 3.x: The application is built with Python 3. Make sure you have it installed. You can download it from python.org.
    
    Tkinter: For the GUI, Tkinter (Python's standard GUI library) is used. Tkinter is included in Python by default, so no additional installation is required.

 How to Use
 
Running the Application
---
    Add Projects:
        Run the main.py script or use the Tkinter-based GUI from gui.py to add new projects.
        Provide the project name, description, client feedback, and image file paths (if applicable).

    View Portfolio:
        You can view all added design projects by running the script and displaying them on the console or through the Tkinter GUI.

    Update and Delete Projects:
        Use the application to modify or remove projects from your portfolio as needed.

    Image Support:
        When adding projects, you can provide a file path to images that represent the project (e.g., design screenshots). The images can be stored in the images/ folder.

   ---


   

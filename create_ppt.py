from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# Create presentation
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Define colors
DARK_BLUE = RGBColor(0, 51, 102)
LIGHT_BLUE = RGBColor(0, 102, 204)
ACCENT_COLOR = RGBColor(255, 153, 0)

def add_title_slide(prs, title, subtitle):
    slide_layout = prs.slide_layouts[6]  # Blank layout
    slide = prs.slides.add_slide(slide_layout)
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(12.333), Inches(1.5))
    title_frame = title_box.text_frame
    title_frame.text = title
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(54)
    title_para.font.bold = True
    title_para.font.color.rgb = DARK_BLUE
    title_para.alignment = PP_ALIGN.CENTER
    
    # Subtitle
    subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(12.333), Inches(1))
    subtitle_frame = subtitle_box.text_frame
    subtitle_frame.text = subtitle
    subtitle_para = subtitle_frame.paragraphs[0]
    subtitle_para.font.size = Pt(28)
    subtitle_para.font.color.rgb = LIGHT_BLUE
    subtitle_para.alignment = PP_ALIGN.CENTER
    
    return slide

def add_content_slide(prs, title, bullets):
    slide_layout = prs.slide_layouts[6]  # Blank layout
    slide = prs.slides.add_slide(slide_layout)
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12.333), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = title
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(36)
    title_para.font.bold = True
    title_para.font.color.rgb = DARK_BLUE
    
    # Content
    content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.3), Inches(12.333), Inches(5.5))
    content_frame = content_box.text_frame
    content_frame.word_wrap = True
    
    for i, bullet in enumerate(bullets):
        if i == 0:
            p = content_frame.paragraphs[0]
        else:
            p = content_frame.add_paragraph()
        p.text = "• " + bullet
        p.font.size = Pt(24)
        p.font.color.rgb = RGBColor(50, 50, 50)
        p.space_before = Pt(12)
    
    return slide

def add_two_column_slide(prs, title, left_title, left_bullets, right_title, right_bullets):
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12.333), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = title
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(36)
    title_para.font.bold = True
    title_para.font.color.rgb = DARK_BLUE
    
    # Left Column Title
    left_title_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.3), Inches(6), Inches(0.5))
    left_title_frame = left_title_box.text_frame
    left_title_frame.text = left_title
    left_title_para = left_title_frame.paragraphs[0]
    left_title_para.font.size = Pt(24)
    left_title_para.font.bold = True
    left_title_para.font.color.rgb = LIGHT_BLUE
    
    # Left Column Content
    left_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.9), Inches(6), Inches(5))
    left_frame = left_box.text_frame
    left_frame.word_wrap = True
    
    for i, bullet in enumerate(left_bullets):
        if i == 0:
            p = left_frame.paragraphs[0]
        else:
            p = left_frame.add_paragraph()
        p.text = "• " + bullet
        p.font.size = Pt(20)
        p.font.color.rgb = RGBColor(50, 50, 50)
        p.space_before = Pt(8)
    
    # Right Column Title
    right_title_box = slide.shapes.add_textbox(Inches(6.8), Inches(1.3), Inches(6), Inches(0.5))
    right_title_frame = right_title_box.text_frame
    right_title_frame.text = right_title
    right_title_para = right_title_frame.paragraphs[0]
    right_title_para.font.size = Pt(24)
    right_title_para.font.bold = True
    right_title_para.font.color.rgb = LIGHT_BLUE
    
    # Right Column Content
    right_box = slide.shapes.add_textbox(Inches(6.8), Inches(1.9), Inches(6), Inches(5))
    right_frame = right_box.text_frame
    right_frame.word_wrap = True
    
    for i, bullet in enumerate(right_bullets):
        if i == 0:
            p = right_frame.paragraphs[0]
        else:
            p = right_frame.add_paragraph()
        p.text = "• " + bullet
        p.font.size = Pt(20)
        p.font.color.rgb = RGBColor(50, 50, 50)
        p.space_before = Pt(8)
    
    return slide

# ==================== SLIDE 1: Title Slide ====================
add_title_slide(prs, 
    "MERN Stack Todo Application",
    "Internship Project Report\nDepartment of Computer Science & Engineering\nAcademic Year 2025-2026")

# ==================== SLIDE 2: Internship Overview ====================
add_content_slide(prs, "Internship Overview", [
    "Organization: [Your Company Name]",
    "Duration: [Start Date] - [End Date]",
    "Role: Full Stack Web Developer Intern",
    "Project: MERN Stack Todo Application",
    "Mentor: [Mentor's Name]",
    "Key Learning Objectives:",
    "  - Master MERN stack development",
    "  - Understand RESTful API design",
    "  - Implement authentication & authorization",
    "  - Work with version control (Git)",
    "  - Follow agile development practices"
])

# ==================== SLIDE 3: Project Overview ====================
add_content_slide(prs, "Project Overview", [
    "Project Name: MERN Stack Todo Application",
    "Type: Full-Stack Web Application",
    "Objective: Develop a task management system with user authentication",
    "Core Features:",
    "  - User Registration & Login",
    "  - Create, Read, Update, Delete (CRUD) operations",
    "  - JWT-based authentication",
    "  - Password hashing with bcryptjs",
    "  - Responsive UI design",
    "  - Data isolation for user privacy"
])

# ==================== SLIDE 4: Technology Stack ====================
add_two_column_slide(prs, "Technology Stack",
    "Frontend",
    [
        "React.js 19.2.5",
        "React DOM",
        "Axios (HTTP client)",
        "CSS3 (styling)",
        "Create React App"
    ],
    "Backend",
    [
        "Node.js",
        "Express.js 5.2.1",
        "MongoDB (Database)",
        "Mongoose ODM",
        "JWT (Authentication)"
    ])

# ==================== SLIDE 5: Architecture ====================
add_content_slide(prs, "System Architecture", [
    "Client-Server Architecture",
    "Frontend: React.js SPA communicating via RESTful APIs",
    "Backend: Express.js server handling HTTP requests",
    "Database: MongoDB with Mongoose ODM",
    "Authentication: JWT tokens with bcryptjs password hashing",
    "Data Flow: User → React UI → Axios → Express API → MongoDB",
    "Security: Protected routes requiring valid JWT token"
])

# ==================== SLIDE 6: Database Schema ====================
add_two_column_slide(prs, "Database Schema",
    "User Model",
    [
        "name: String (required)",
        "email: String (required, unique)",
        "password: String (hashed)",
        "date: Date (default: now)"
    ],
    "Todo Model",
    [
        "user: ObjectId (ref: User)",
        "title: String (required)",
        "description: String (optional)",
        "completed: Boolean (default: false)",
        "date: Date (default: now)"
    ])

# ==================== SLIDE 7: API Endpoints ====================
add_content_slide(prs, "API Endpoints", [
    "Authentication Routes (/api/auth):",
    "  - POST /api/auth/register - User registration",
    "  - POST /api/auth/login - User login (returns JWT)",
    "",
    "Todo Routes (/api/todos) - Protected with JWT:",
    "  - GET /api/todos - Get all user's todos",
    "  - POST /api/todos - Create new todo",
    "  - PUT /api/todos/:id - Update todo",
    "  - DELETE /api/todos/:id - Delete todo",
    "",
    "All protected routes require Authorization header with JWT"
])

# ==================== SLIDE 8: Key Features Implemented ====================
add_content_slide(prs, "Key Features Implemented", [
    "User Authentication:",
    "  - Secure registration with password hashing",
    "  - Login with JWT token generation",
    "  - Token validation on protected routes",
    "",
    "Todo Management:",
    "  - Add new tasks with title & description",
    "  - View all tasks in organized list",
    "  - Mark tasks as complete/incomplete",
    "  - Edit existing tasks",
    "  - Delete unwanted tasks",
    "",
    "Security:",
    "  - bcryptjs for password hashing",
    "  - JWT for session management",
    "  - User-specific data isolation"
])

# ==================== SLIDE 9: Internship Learning ====================
add_content_slide(prs, "Internship Learning & Experience", [
    "Technical Skills Acquired:",
    "  - MERN Stack (MongoDB, Express, React, Node.js)",
    "  - RESTful API design and implementation",
    "  - JWT authentication and security best practices",
    "  - MongoDB database design and queries",
    "  - React component architecture",
    "",
    "Professional Development:",
    "  - Code version control with Git",
    "  - Problem-solving and debugging",
    "  - Documentation and code comments",
    "  - Time management and project planning",
    "  - Communication with team members"
])

# ==================== SLIDE 10: Challenges & Solutions ====================
add_content_slide(prs, "Challenges Faced & Solutions", [
    "Challenge 1: JWT Token Management",
    "  - Solution: Implemented token storage in localStorage",
    "",
    "Challenge 2: MongoDB Connection Issues",
    "  - Solution: Added proper error handling and retry logic",
    "",
    "Challenge 3: CORS Configuration",
    "  - Solution: Configured CORS middleware properly",
    "",
    "Challenge 4: Data Isolation Between Users",
    "  - Solution: Added user ID reference in todo schema",
    "",
    "Challenge 5: Responsive UI Design",
    "  - Solution: Used CSS media queries for different screen sizes"
])

# ==================== SLIDE 11: Project Structure ====================
add_content_slide(prs, "Project Structure", [
    "Backend (./backend):",
    "  - server.js - Main server entry point",
    "  - config/db.js - MongoDB connection",
    "  - models/ - User.js, Todo.js (Mongoose schemas)",
    "  - routes/ - auth.js, todos.js (API routes)",
    "  - middleware/auth.js - JWT verification",
    "",
    "Frontend (./frontend):",
    "  - src/App.js - Main React component",
    "  - src/App.css - Styling",
    "  - src/index.js - React DOM rendering",
    "  - public/index.html - HTML template"
])

# ==================== SLIDE 12: Future Enhancements ====================
add_content_slide(prs, "Future Enhancements", [
    "Planned Features:",
    "  - Add due dates and reminders for tasks",
    "  - Implement categories/tags for todos",
    "  - Add sub-tasks (checklist items)",
    "  - Drag and drop task reordering",
    "  - Dark mode theme support",
    "",
    "Technical Improvements:",
    "  - Add input validation and sanitization",
    "  - Implement rate limiting for API",
    "  - Add unit and integration tests",
    "  - Set up CI/CD pipeline",
    "  - Deploy to cloud (Heroku/AWS)"
])

# ==================== SLIDE 13: Conclusion ====================
add_content_slide(prs, "Conclusion", [
    "Project Summary:",
    "  - Successfully developed a fully functional MERN stack application",
    "  - Implemented secure authentication with JWT and bcryptjs",
    "  - Created RESTful APIs for CRUD operations",
    "  - Built responsive UI with React.js",
    "",
    "Internship Outcome:",
    "  - Gained hands-on experience with modern web technologies",
    "  - Improved coding skills and best practices",
    "  - Learned software development lifecycle",
    "  - Enhanced problem-solving abilities",
    "",
    "Thank You! Questions?"
])

# ==================== SLIDE 14: Thank You ====================
add_title_slide(prs, 
    "Thank You",
    "Questions?\n\nContact: [Your Email]\nLinkedIn: [Your LinkedIn Profile]")

# Save the presentation
prs.save('MERN_Todo_App_Internship_Presentation.pptx')
print("Presentation created successfully: MERN_Todo_App_Internship_Presentation.pptx")
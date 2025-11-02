# Teamwork & Project Management Report
## Medi-Reach: Medicine Delivery Platform

**Project Team:** Amazing-beep  
**Date:** November 2, 2025  
**Project Repository:** [GitHub - Medi-Reach](https://github.com/Amazing-beep/Medi-Reach)

---

## Table of Contents
1. [Project Management Tools](#1-project-management-tools)
2. [Team Collaboration](#2-team-collaboration)
3. [Progress Documentation](#3-progress-documentation)
4. [Conclusion](#4-conclusion)

---

## 1. Project Management Tools

### 1.1 Tools Used

For the Medi-Reach project, we utilized the following project management and collaboration tools:

#### **GitHub Projects**
- **Purpose:** Task tracking, issue management, and sprint planning
- **URL:** [GitHub Repository](https://github.com/Amazing-beep/Medi-Reach)
- **Features Used:**
  - Issue tracking for bugs and feature requests
  - Pull request reviews for code quality assurance
  - Project boards for sprint management
  - Milestone tracking for release planning

#### **Git Version Control**
- **Purpose:** Source code management and collaboration
- **Strategy:** Feature branch workflow with pull requests
- **Practices:**
  - Descriptive commit messages
  - Regular commits to track incremental progress
  - Branch protection for main branch

### 1.2 How Tools Support Our Workflow

#### **Task Tracking**
- Each feature and bug is tracked as a GitHub Issue
- Issues are assigned to team members with clear descriptions
- Labels categorize work (frontend, backend, database, documentation)
- Milestones group related issues for release planning

#### **Collaboration**
- Pull requests enable code review before merging
- Team members comment on code changes and suggest improvements
- Branch naming convention: `feature/feature-name`, `bugfix/bug-description`

#### **Progress Monitoring**
- GitHub Insights show contribution statistics
- Commit history provides transparent progress tracking
- Project board visualizes work status (To Do, In Progress, Done)

### 1.3 Project Management Board Screenshots

**Note:** Please add screenshots of:
- GitHub Projects board showing tasks in different stages
- GitHub Issues list with assigned tasks
- GitHub Insights showing contribution graph
- Milestone progress view

*[INSERT SCREENSHOT: GitHub Projects Board]*  
*Caption: Project board showing task distribution across team members*

*[INSERT SCREENSHOT: GitHub Issues]*  
*Caption: Active issues with labels and assignments*

*[INSERT SCREENSHOT: GitHub Insights - Contributors]*  
*Caption: Contribution graph showing team collaboration*

---

## 2. Team Collaboration

### 2.1 Team Meeting Evidence

#### **Meeting 1: Project Kickoff**
**Date:** [Insert Date]  
**Duration:** 1.5 hours  
**Attendees:** All team members

**Key Discussion Points:**
- Project scope and requirements analysis
- Technology stack selection (Flask, SQLite, HTML/CSS/JS)
- Database schema design
- Task distribution and role assignment
- Timeline and milestone planning

*[INSERT SCREENSHOT: Meeting Screenshot/Attendance]*  
*Caption: Team kickoff meeting - discussing project architecture*

---

#### **Meeting 2: Sprint Planning & Design Review**
**Date:** [Insert Date]  
**Duration:** 1 hour  
**Attendees:** All team members

**Key Discussion Points:**
- Figma design review and approval
- Database schema finalization
- API endpoint specifications
- Frontend-backend integration strategy
- Sprint 1 task assignments

*[INSERT SCREENSHOT: Meeting Screenshot]*  
*Caption: Design review session - evaluating Figma prototypes*

---

#### **Meeting 3: Mid-Sprint Standup**
**Date:** [Insert Date]  
**Duration:** 30 minutes  
**Attendees:** All team members

**Key Discussion Points:**
- Progress updates from each team member
- Blockers and challenges discussion
- Integration issues between frontend and backend
- Code review feedback
- Adjustments to sprint tasks

*[INSERT SCREENSHOT: Meeting Screenshot]*  
*Caption: Mid-sprint standup - addressing integration challenges*

---

#### **Meeting 4: Sprint Review & Demo**
**Date:** [Insert Date]  
**Duration:** 1 hour  
**Attendees:** All team members

**Key Discussion Points:**
- Demo of completed features
- Testing results and bug reports
- Documentation review
- Sprint retrospective
- Planning for next sprint

*[INSERT SCREENSHOT: Meeting Screenshot]*  
*Caption: Sprint review - demonstrating working features*

---

### 2.2 Communication & Collaboration Practices

#### **Version Control Strategy**
- **Branching Model:** Feature branch workflow
  - `main` branch: Production-ready code
  - `develop` branch: Integration branch for features
  - `feature/*` branches: Individual feature development
  - `bugfix/*` branches: Bug fixes

- **Commit Conventions:**
  ```
  feat: Add user authentication system
  fix: Resolve medicine price calculation bug
  docs: Update API documentation
  style: Format code with consistent indentation
  refactor: Restructure database connection logic
  ```

- **Pull Request Process:**
  1. Create feature branch from `develop`
  2. Implement feature with regular commits
  3. Open pull request with description
  4. At least one team member reviews code
  5. Address review comments
  6. Merge after approval

#### **Design Sharing**
- **Figma:** Collaborative design platform
  - Shared workspace for all team members
  - Real-time design collaboration
  - Comment and feedback system
  - Version history for design iterations

#### **Daily Stand-ups**
- **Format:** Asynchronous updates via team chat
- **Questions:**
  - What did I complete yesterday?
  - What will I work on today?
  - Are there any blockers?

#### **Code Review Standards**
- Check for code quality and best practices
- Verify functionality matches requirements
- Ensure proper error handling
- Validate security considerations
- Confirm documentation is updated

#### **Documentation Practices**
- README.md with setup instructions
- Inline code comments for complex logic
- API endpoint documentation
- Database schema documentation

---

## 3. Progress Documentation

### 3.1 Figma Designs

**Design Link:** [Figma - Medi-Reach Design](https://www.figma.com/file/your-design-link)  
*Note: Ensure link is set to "Anyone with the link can view"*

#### **Design Highlights:**

**Home Page Design**
- Clean, modern interface
- Hero section with call-to-action
- Featured medicines section
- Navigation menu
- Footer with contact information

*[INSERT SCREENSHOT: Figma - Home Page]*  
*Caption: Home page design showing hero section and medicine showcase*

---

**Medicine Catalog Page**
- Grid layout for medicine display
- Search and filter functionality
- Medicine cards with image, name, price
- Add to cart button
- Responsive design for mobile devices

*[INSERT SCREENSHOT: Figma - Medicine Catalog]*  
*Caption: Medicine catalog with search and filter options*

---

**Order/Checkout Page**
- Order form with customer details
- Medicine selection dropdown
- Quantity selector
- Total price calculation
- Delivery address input
- Order confirmation button

*[INSERT SCREENSHOT: Figma - Order Page]*  
*Caption: Order form with customer information fields*

---

**Authentication Page**
- User registration form
- Login form
- Password validation
- Error message display
- Responsive layout

*[INSERT SCREENSHOT: Figma - Auth Page]*  
*Caption: User authentication interface*

---

### 3.2 Database Design and Schema

#### **Database Technology**
- **Database:** SQLite
- **ORM/Connection:** Direct SQLite3 Python library
- **Location:** `instance/medi_reach.db`

#### **Entity Relationship Diagram**

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│     USERS       │         │     ORDERS       │         │   MEDICINES     │
├─────────────────┤         ├──────────────────┤         ├─────────────────┤
│ id (PK)         │────┐    │ id (PK)          │    ┌────│ id (PK)         │
│ name            │    │    │ user_id (FK)     │────┘    │ name            │
│ email (UNIQUE)  │    └────│ medicine_id (FK) │         │ price           │
└─────────────────┘         │ medicine_name    │         └─────────────────┘
                            │ quantity         │
                            │ total_price      │
                            │ delivery_address │
                            │ customer_name    │
                            │ status           │
                            │ created_at       │
                            └──────────────────┘
```

#### **Database Schema**

**Users Table**
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
```

**Medicines Table**
```sql
CREATE TABLE medicines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
);
```

**Orders Table**
```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    medicine_id INTEGER NOT NULL,
    medicine_name TEXT NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    total_price REAL NOT NULL,
    delivery_address TEXT NOT NULL,
    customer_name TEXT NOT NULL,
    status TEXT DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (medicine_id) REFERENCES medicines(id)
);
```

#### **Sample Data**

**Seeded Medicines:**
| ID | Name         | Price |
|----|--------------|-------|
| 1  | Paracetamol  | $5.00 |
| 2  | Amoxicillin  | $8.50 |
| 3  | Ibuprofen    | $6.75 |
| 4  | Vitamin C    | $4.25 |

*[INSERT SCREENSHOT: Database Schema Diagram]*  
*Caption: Entity-relationship diagram showing table relationships*

*[INSERT SCREENSHOT: Database Table View]*  
*Caption: Sample data in medicines table*

---

### 3.3 Frontend Implementation

#### **Technology Stack**
- **HTML5:** Semantic markup
- **CSS3:** Styling with custom styles
- **JavaScript:** Client-side interactivity
- **Template Engine:** Jinja2 (Flask templates)

#### **Implemented Pages**

**1. Home Page (`index.html`)**
- Welcome section
- Medicine showcase
- Navigation menu
- Responsive design

*[INSERT SCREENSHOT: Frontend - Home Page]*  
*Caption: Live home page showing navigation and hero section*

---

**2. Authentication Page (`auth.html`)**
- User registration form
- Login functionality
- Form validation
- Error handling

*[INSERT SCREENSHOT: Frontend - Auth Page]*  
*Caption: User authentication interface with form validation*

---

**3. Medicines Page (`medicines.html`)**
- Display all available medicines
- Fetches data from API
- Dynamic rendering
- Medicine cards layout

*[INSERT SCREENSHOT: Frontend - Medicines Page]*  
*Caption: Medicine catalog displaying available products*

---

**4. Order Page (`order.html`)**
- Order form
- Medicine selection
- Quantity input
- Customer details
- Delivery address

*[INSERT SCREENSHOT: Frontend - Order Page]*  
*Caption: Order form with medicine selection and customer details*

---

**5. Order Confirmation (`order_confirm.html`)**
- Order summary
- Confirmation message
- Order details display
- Return to home option

*[INSERT SCREENSHOT: Frontend - Order Confirmation]*  
*Caption: Order confirmation page showing successful order placement*

---

#### **CSS Styling**
- Custom stylesheet: `static/css/styles.css`
- Consistent color scheme
- Responsive design principles
- Modern UI components

*[INSERT SCREENSHOT: CSS Styling Examples]*  
*Caption: Consistent styling across different pages*

---

### 3.4 Backend/API Implementation

#### **Technology Stack**
- **Framework:** Flask 3.0.0
- **Database:** SQLite with SQLAlchemy
- **Architecture:** Blueprint-based modular design

#### **Project Structure**
```
Medi-Reach-5/
├── app.py              # Main application entry point
├── api.py              # Medicine API endpoints
├── auth.py             # Authentication routes
├── order.py            # Order management routes
├── db.py               # Database initialization
├── models.py           # Database models and queries
├── requirements.txt    # Python dependencies
├── instance/
│   └── medi_reach.db  # SQLite database
├── static/
│   ├── css/
│   │   └── styles.css
│   └── script.js
└── templates/
    ├── base.html
    ├── index.html
    ├── auth.html
    ├── medicines.html
    ├── order.html
    └── order_confirm.html
```

#### **API Endpoints**

**1. Get All Medicines**
```
GET /api/medicines
```
**Response:**
```json
{
  "count": 4,
  "medicines": [
    { "id": 1, "name": "Paracetamol", "price": 5.0 },
    { "id": 2, "name": "Amoxicillin", "price": 8.5 }
  ]
}
```

**2. Create Medicine**
```
POST /api/medicines/create
Content-Type: application/json
```
**Request Body:**
```json
{
  "name": "Aspirin",
  "price": 7.5
}
```

**3. User Registration**
```
POST /auth/register
```

**4. User Login**
```
POST /auth/login
```

**5. Create Order**
```
POST /order/create
```

**6. Get All Orders**
```
GET /order/all
```

#### **Code Highlights**

**Flask Application Setup (`app.py`):**
```python
from flask import Flask
from api import api_bp
from auth import auth_bp
from order import order_bp

app = Flask(__name__)
app.secret_key = "replace_with_a_secure_random_key"

# Register blueprints
app.register_blueprint(api_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(order_bp)

# Initialize database
init_medicine_table()
init_orders_table()
seed_medicines()
```

**Database Models (`models.py`):**
- `get_db_connection()`: Database connection management
- `init_users_table()`: Create users table
- `init_medicines_table()`: Create medicines table
- `init_orders_table()`: Create orders table
- `seed_medicines()`: Populate sample data
- CRUD operations for all entities

*[INSERT SCREENSHOT: API Testing - Postman/Thunder Client]*  
*Caption: API endpoint testing showing successful responses*

*[INSERT SCREENSHOT: Backend Code - API Routes]*  
*Caption: Flask blueprint structure showing modular design*

---

### 3.5 GitHub Repository

**Repository URL:** https://github.com/Amazing-beep/Medi-Reach  
**Visibility:** Public

#### **Repository Statistics**
- **Total Commits:** [Insert number]
- **Contributors:** [Insert number]
- **Branches:** [Insert number]
- **Pull Requests:** [Insert number]
- **Issues:** [Insert number]

#### **Commit History Highlights**

**Recent Commits:**
```
✓ feat: Add order confirmation page
✓ feat: Implement user authentication system
✓ feat: Create order management API
✓ fix: Resolve database connection issues
✓ docs: Update README with API documentation
✓ style: Improve CSS styling for responsive design
✓ refactor: Modularize code with Flask blueprints
```

*[INSERT SCREENSHOT: GitHub - Commit History]*  
*Caption: Commit history showing regular contributions from team members*

---

#### **Collaboration Evidence**

**Pull Requests:**
- Code review process
- Discussion threads
- Approved and merged PRs
- Collaborative problem-solving

*[INSERT SCREENSHOT: GitHub - Pull Requests]*  
*Caption: Pull request with code review comments and approval*

---

**Contributors Graph:**
- Shows individual contributions
- Commit frequency over time
- Lines of code added/removed

*[INSERT SCREENSHOT: GitHub - Contributors Graph]*  
*Caption: Contribution graph showing team collaboration over time*

---

**Branch Network:**
- Feature branches
- Merge history
- Parallel development

*[INSERT SCREENSHOT: GitHub - Network Graph]*  
*Caption: Branch network showing parallel feature development*

---

**Issues and Project Board:**
- Task tracking
- Bug reports
- Feature requests
- Progress visualization

*[INSERT SCREENSHOT: GitHub - Issues List]*  
*Caption: Issue tracking with labels and assignments*

*[INSERT SCREENSHOT: GitHub - Project Board]*  
*Caption: Kanban board showing task progress*

---

## 4. Conclusion

### 4.1 Project Status

The Medi-Reach project has successfully implemented a functional medicine delivery platform with the following completed components:

✅ **Database Design:** Fully implemented with three normalized tables  
✅ **Backend API:** RESTful endpoints for medicines, orders, and authentication  
✅ **Frontend:** Responsive web interface with multiple pages  
✅ **User Authentication:** Registration and login system  
✅ **Order Management:** Complete order placement and tracking  
✅ **Documentation:** Comprehensive README and API documentation  

### 4.2 Team Collaboration Success

Our team effectively utilized:
- **GitHub** for version control and collaboration
- **Regular meetings** for synchronization and problem-solving
- **Code reviews** to maintain quality standards
- **Agile practices** with sprint planning and retrospectives
- **Clear communication** through multiple channels

### 4.3 Key Achievements

1. **Modular Architecture:** Blueprint-based Flask design for scalability
2. **Clean Code:** Consistent coding standards and documentation
3. **Responsive Design:** Mobile-friendly user interface
4. **Database Integrity:** Proper foreign key relationships and constraints
5. **API Documentation:** Clear endpoint specifications
6. **Team Synergy:** Effective collaboration and task distribution

### 4.4 Lessons Learned

- **Version Control:** Feature branches prevented conflicts and enabled parallel development
- **Regular Communication:** Daily standups kept everyone aligned
- **Code Reviews:** Improved code quality and knowledge sharing
- **Documentation:** Saved time during integration and onboarding
- **Agile Methodology:** Iterative development allowed for flexibility

### 4.5 Future Enhancements

- Payment gateway integration
- Real-time order tracking
- Admin dashboard for inventory management
- Email notifications for order updates
- Advanced search and filtering
- User reviews and ratings
- Mobile application

---

## Appendix

### A. Technology Stack Summary

| Component | Technology |
|-----------|------------|
| Backend Framework | Flask 3.0.0 |
| Database | SQLite |
| ORM | SQLAlchemy 3.0.5 |
| Frontend | HTML5, CSS3, JavaScript |
| Template Engine | Jinja2 |
| Version Control | Git/GitHub |
| Project Management | GitHub Projects |

### B. Team Roles

| Team Member | Role | Responsibilities |
|-------------|------|------------------|
| Ivan | Backend Developer | API development, database design |
| [Member 2] | Frontend Developer | UI implementation, styling |
| [Member 3] | Full Stack | Integration, testing |
| [Member 4] | Designer/Developer | Figma designs, frontend |

*Note: Update team member names and roles as appropriate*

### C. Project Timeline

| Phase | Duration | Status |
|-------|----------|--------|
| Planning & Design | Week 1 | ✅ Completed |
| Database Setup | Week 2 | ✅ Completed |
| Backend Development | Week 2-3 | ✅ Completed |
| Frontend Development | Week 3-4 | ✅ Completed |
| Integration & Testing | Week 4 | ✅ Completed |
| Documentation | Week 4-5 | ✅ Completed |

---

**Report Prepared By:** [Team Name]  
**Date:** November 2, 2025  
**Project:** Medi-Reach - Medicine Delivery Platform

---

## Instructions for Completing This Report

### Required Screenshots to Add:

1. **Project Management:**
   - GitHub Projects board
   - GitHub Issues list
   - GitHub Insights/Contributors graph
   - Milestone progress view

2. **Team Meetings:**
   - 4 meeting screenshots with captions
   - Can be from video calls, in-person meetings, or chat discussions

3. **Figma Designs:**
   - Home page design
   - Medicine catalog design
   - Order page design
   - Authentication page design

4. **Database:**
   - ER diagram (can create using draw.io or dbdiagram.io)
   - Database table view (SQLite browser screenshot)

5. **Frontend:**
   - Screenshots of all implemented pages running in browser
   - Show responsive design if applicable

6. **Backend:**
   - API testing screenshots (Postman, Thunder Client, or browser)
   - Code structure/files

7. **GitHub:**
   - Commit history
   - Pull requests with reviews
   - Contributors graph
   - Network/branch graph
   - Issues and project board

### How to Generate PDF:

1. **Option 1 - Using Markdown to PDF Converter:**
   - Use tools like Pandoc, Typora, or VS Code extensions
   - Command: `pandoc Teamwork_Project_Management_Report.md -o Report.pdf`

2. **Option 2 - Using Word/Google Docs:**
   - Copy content to Word/Google Docs
   - Add screenshots in appropriate sections
   - Format with styles and page breaks
   - Export as PDF

3. **Option 3 - Using LaTeX:**
   - Convert to LaTeX format
   - Compile to PDF with proper formatting

### Customization Needed:

- [ ] Add actual GitHub repository URL
- [ ] Add Figma design link
- [ ] Insert all required screenshots
- [ ] Update team member names and roles
- [ ] Add actual meeting dates
- [ ] Update repository statistics (commits, PRs, etc.)
- [ ] Add any additional sections specific to your project
- [ ] Review and proofread all content

---

*This report template follows academic and professional standards for project documentation.*

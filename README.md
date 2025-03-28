# HackNCState2024
# SocioLawgy - A platform to connect clients to lawyers to represent them

Participated in Hack NC State and worked towards building a web app named SocioLawgy, that helps underprivileged communities to connect with lawyers. In addition to helping clients view various case proceedings, the web app maintains anonymity while applying for their cases.


### 1. **Defining the Core Features**
- **Basic User Registration:** Enable lawyers and clients to create accounts with just essential details (name, email, and password).
- **Simple Lawyer Verification:** For the hackathon, this can be a placeholder where lawyers can submit any document, without actual verification.
- **Case Posting:** Allow clients to post a brief description of their case.
- **Basic Map Integration:** Implement a simple map showing general locations of lawyers (this could be static mock data for the hackathon).

### 2. **Choosing Tech Stack Quickly**
- **Frontend:** Choose a framework that allows rapid development. React or Vue.js can be great for this, due to their extensive libraries and components.
- **Backend:** Node.js with Express can help you set up a server quickly. Use a simple database like MongoDB for ease of schema design and flexibility.
- **Geolocation API:** For simplicity, use Google Maps API or Leaflet for basic map functionalities.

### 3. **Development Breakdown**
- **First 2 Hours: Setup**
  - Initialize your project, set up your development environment, and create GitHub repositories.
  - Quickly design a basic UI wireframe.
- **Next 5 Hours: Core Feature Development**
  - **2 Hours for User Registration:** Implement frontend and backend for account creation.
  - **1 Hour for Case Posting:** Allow clients to post cases, and save these to your database.
  - **2 Hours for Map Integration:** Display a simple map with hardcoded locations of lawyers.
- **Next 2 Hours: Basic Lawyer Verification**
  - Implement a form for lawyers to upload a document (actual verification can be mocked).
- **Final Hour: Testing and Polishing**
  - Conduct basic testing, fix any glaring issues, and improve the UI if time allows.

### 4. **Preparing Our Presentation**
- **Outline Key Points:** Focus on the problem you're solving, how your app addresses this problem, and the core features you've implemented.
- **Demo:** Prepare to demonstrate the user flow — registering, posting a case, and viewing it on the map.
- **Future Roadmap:** Briefly mention how you would expand this project post-hackathon, including real lawyer verification, enhanced map features, and security enhancements.

<hr>

**Commands to Run SociaLawgy(app.py):**
- Got to the terminal workspace for SociaLawgy
- Command 1: "source build.sh"
- You should see this once the build is successful:
<br>  <img width="300" alt="image" src="https://github.com/Tanmay-Soni/HackNCState_24/assets/73430591/db4a51ad-5df8-4969-8479-576ec4d4988f">
- Command 2: "python app.py"
- A localhost should be established in your terminal, and you could press on it to run SocioLawgy as a webapp

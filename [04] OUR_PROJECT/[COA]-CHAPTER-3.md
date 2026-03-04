3.0 Technical Background

## 3.1 Development

### 3.1.1 Hardware

#### A. Personal Computers and Laptops

The proponents will primarily use personal computers (PCs), desktop computers, mobile devices and laptops for documentation, system design, testing, and development of the proposed project.

### 3.1.2 Software

#### A. Frontend

#### A. 1 RPG Maker MZ

RPG Maker MZ is a game development engine designed for creating 2D role-playing games. It will be used in the core application development to construct the visual environment, manage the database of enemies and items, and script game events. The proponents utilize this engine because its built-in architecture provides a stable framework for RPG mechanics (such as inventory and movement) while allowing for the addition of custom JavaScript plugins to create the "Math Battle System."

#### A. 2 HTML5 / WebGL

HyperText Markup Language 5 (HTML5) is the standard markup language for structuring web content. Web Graphics Library (WebGL) is a JavaScript API for rendering 2D and 3D graphics within web browsers. HTML5 and WebGL will be used in the web-based deployment build of the project. The proponents utilize these technologies to render hardware-accelerated 2D graphics within client web browsers, allowing the game to run on school computers and mobile devices without requiring the user to install native software.

#### A. 3 Cascading Style Sheets (CSS)

Cascading Style Sheets (CSS) is a style-sheet language used to define the visual presentation and layout of HTML documents. CSS will be applied to the web container (index.html) that hosts the game engine. The proponents utilize CSS to handle the scaling of the game canvas across different screen sizes and to position the "Virtual Keypad" overlay, so that the interface remains usable on touch-screen devices.

#### B. Backend

#### B. 1 JavaScript (ES6)

JavaScript (ECMAScript 6) is a programming language used for creating dynamic and interactive content on web pages. JavaScript will serve as the core programming language for developing custom plugins. It will be used in the backend development phase to program the logic of the "Math Battle System," "Level-Based Difficulty System," "Enemy Auto-Scaling System," "Automatic Quest Generation system," and "P2P Multiplayer Framework" because it is the native scripting language of RPG Maker MZ, allowing the proponents to modify default engine functions without requiring additional software.

#### B. 2 Visual Studio Code (VS Code)

Visual Studio Code is an Integrated Development Environment (IDE) developed by Microsoft for writing, debugging, and managing code. It will be the primary IDE used for managing the JavaScript codebase. It will be utilized in the coding phase because its wide range of extensions (such as ESLint and Git integration) simplifies the management of plugin files and supports code quality during the development process.

#### B. 3 Node.js

Node.js is an open-source, server-side runtime environment that executes JavaScript outside of a web browser. It will be utilized during the development phase to run local server environments. Node.js will be used to simulate server-side operations for testing the P2P multiplayer handshake and simulating network delay conditions, so that the connection logic is stable before deploying to the public web.

#### B. 4 PeerJS

PeerJS is a Web Real-Time Communication (WebRTC) wrapper library that simplifies the process of establishing direct browser-to-browser connections. It will be used to implement the Peer-to-Peer (P2P) Multiplayer Framework by managing the generation of unique "Room Codes" and facilitating the data exchange between the host and connected clients. This library establishes direct connections between players without requiring a centralized backend server.

#### C. Multimedia and Asset Development Tools

#### C. 1 GIMP (GNU Image Manipulation Program)

GIMP is a free, open-source raster graphics editor used for image retouching and editing. It will be utilized as the primary graphics editor for the manipulation of game assets. GIMP will be used in the asset creation phase to perform "Hue Shifting" on default enemy sprites because its color manipulation tools allow for the creation of biome-specific enemy variants (e.g., Sand Slime, Magma Slime) from a single base asset.

#### C. 2 Canva

Canva is a web-based graphic design platform that provides templates and drag-and-drop tools for creating visual content. It will be utilized as the primary design tool for creating the *Chronicles of Arithmos* game logo and visual identity materials. during the design phase.

#### C. 3 Draw.io

Draw.io (also known as diagrams.net) is a free, web-based diagramming application used for creating flowcharts, network diagrams, and system architecture visuals. It will be utilized during the documentation and design phases to create the system's technical diagrams, including the Data Flow Diagram (DFD), Use Case Diagram, and system architecture illustrations required for the capstone manuscript.

#### D. Deployment and Runtime Platform

#### D. 1 NW.js (Native Executable Wrapper)

NW.js is an open-source framework that allows HTML5 and JavaScript applications to run as native desktop programs. It will serve as the core runtime environment for the PC desktop deployment. NW.js will be used to package the HTML5/JavaScript game engine into a standalone executable file (.exe) for Windows because this wrapper gives the application direct access to the local file system for save data persistence, allowing the application to run offline.

#### D. 2 Google Chrome / Microsoft Edge

Google Chrome and Microsoft Edge are Chromium-based web browsers that support modern web standards including HTML5, WebGL, and WebRTC. These browsers will function as the primary runtime environments for the web-based deployment. They will be used in the testing phase to verify the WebGL rendering performance and the responsiveness of the "Virtual Keypad" overlay because they represent the standard browsing environment for the target audience accessing the game via the web

#### D. 3 GitHub

GitHub is a cloud-based platform for hosting and managing source code repositories using the Git version control system. It serves as the central repository for the *Chronicles of Arithmos* project source code during the development phase. The platform manages version control and facilitates collaboration among the proponents by storing all historical iterations of the game files to prevent data loss.

#### D. 4 Git

Git is a distributed version control system that tracks changes in source code during software development. The proponents use Git during the development phase to record modifications to the codebase. It allows the proponents to push updated code from local machines to the GitHub repository.

#### D. 5 Vercel

Vercel is a cloud-based deployment and hosting platform designed for frontend web applications. It operates as the staging host for the web-based deployment of *Chronicles of Arithmos* during the development phase, before the proponents acquire a dedicated domain and hosting plan. The platform connects to the GitHub repository to automate the build process of the game and provides a Hypertext Transfer Protocol Secure (HTTPS) environment, which is a requirement for the WebRTC and PeerJS handshake.

#### D. 6 Hostinger

Hostinger is a web hosting service provider that offers domain registration and cloud-based hosting for web applications. It will serve as the production hosting platform for *Chronicles of Arithmos* during the implementation phase, replacing the Vercel staging environment. The proponents will register a .site top-level domain (TLD) through Hostinger to provide the target audience with a dedicated, permanent web address for accessing the deployed game

### 3.1.3 Peopleware

#### A. The Proponents

The proponents consisted of a project manager, a programmer, a UI/UX designer, a tester, and a graphic designer who planned, programmed, and designed the system, respectively, according to the standards agreed upon for the project.  

#### B. Capstone Adviser

 Mr. Jan Nicole B. Apostol provided guidance, clarifications, and recommendations for the project. The adviser guided the proponents through the technicalities and documentation, provided necessary revisions, and verified that the system met the required formatting and quality standards.

### 3.1.4 Network

#### A. Local Area Network (LAN) & Cloud Staging

During the development lifecycle, the proponents will conduct multiplayer testing using two distinct network configurations. First, the peer-to-peer handshake and data synchronization will be validated using multiple personal computers connected to the same local internet connection (LAN/Same Wi-Fi) to verify low-latency performance. Second, the system will be tested with computers connected to different internet networks (WAN) to simulate remote play conditions and verify the stability of the "Room Code" connection over the public internet.

## 3.2 Implementation

### 3.2.1 Hardware

#### A. Personal Computer or Laptop

Users will be required to have a personal computer (PC), desktop, or laptop to install and use *Chronicles of Arithmos*. The minimum hardware requirements, based on the tested configuration, are as follows:

**Table #1 Tested Minimum Hardware Requirements for PC**

| Component | Minimum Requirement |
| :--- | :--- |
| Processor | Intel Core i3-3220 CPU @ 3.30GHz or equivalent |
| Memory | 8.0 GB RAM |
| Graphics | Intel HD Graphics (32 MB VRAM) or better |
| Storage | At least 2 GB of available space (120GB SSD recommended) |
| System Type | 64-bit operating system, x64-based processor |

#### B. Mobile Device (Web Access)

Users who access the application via the web browser deployment will require a mobile device with the following minimum specifications:

**Table #2 Tested Minimum Hardware Requirements For Mobile**

| Component | Minimum Requirement |
| :--- | :--- |
| Processor | MediaTek Dimensity 700 (Octa-core CPU up to 2.2GHz) |
| Memory | 4 GB RAM (supports LPDDR4X) |
| Graphics | Mali-G57 MC2 GPU |
| Display | 6.5" FHD+ DotDisplay (90Hz refresh rate recommended) |
| Storage | 128 GB UFS 2.2 (Minimum 1GB free for browser cache) |

### 3.2.2 Software

#### A. Operating System (OS)

The minimum operating system requirement will be Windows 10 (64-bit) or macOS 10.15 (Catalina). This OS environment is needed because the NW.js runtime wrapper, which powers the game's executable, relies on modern 64-bit system components that are not supported in older versions like Windows 7. For mobile users, Android 10 or iOS 14 will be required because the game's web technologies (WebGL 2.0) depend on updated support found in these mobile operating systems.

#### B. Modern Browsers

Users will be required to use a modern web browser to access the web-deployed version via GitHub Pages. To align with the development environment, the supported browsers will specifically include Chromium-based web browsers such as Google Chrome and Microsoft Edge. These browsers are required because the game's Virtual Numeric Keypad overlay, WebGL rendering, and Peer-to-Peer (P2P) Multiplayer Framework handshake utilize HTML5 and Web Real-Time Communication (WebRTC) standards that are most reliably implemented within these browsers.

### 3.2.3 Peopleware

#### A. Students (Primary End-Users)

Students (Grades 4-6) will serve as the primary operators of the system. They will engage directly with the Math Battle System to solve arithmetic equations, explore the game world, and progress through the narrative. Their interaction will focus on developing calculation speed and accuracy to defeat enemies and clear procedural quests.

#### B. Educators and Guardians (Secondary Users)

Mathematics teachers instructing Grades 4 to 6, along with the parents or guardians of those specific students, will act as secondary users who utilize the application as a supplementary educational tool. These educators will use the software to reinforce classroom arithmetic topics (such as PEMDAS) or to assign specific Training Dummy practice drills. Meanwhile, guardians will utilize the game to support home-based learning, potentially joining via the P2P Multiplayer mode to directly assist the primary learner during difficult combat encounters.

#### C. Gamers (Tertiary Users)

RPG enthusiasts and casual gamers will interact with the system for entertainment purposes. These users will focus on mastering the "Performance-Based Efficacy" mechanics to achieve high-efficiency combat ratings and complete "Omega Tier" endgame challenges, interacting with the system primarily to test cognitive reaction speeds and strategic planning.

### 3.2.4 Network

#### A. Internet Connection

The system requires an active internet connection for the Peer-to-Peer (P2P) multiplayer feature and initial web resource loading. An internet speed of 6 to 10 Mbps is required to maintain gameplay connectivity, synchronize player data, and prevent connection delays during multiplayer sessions.

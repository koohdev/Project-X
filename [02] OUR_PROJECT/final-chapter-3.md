# 3.0 Technical Background

## 3.1 Development

### 3.1.1 Hardware

#### A. Personal Computers and Laptops

The proponents will primarily use personal computers (PCs), desktop computers, mobile devices and laptops for documentation, system design, testing, and development of the proposed project.

### 3.1.2 Software

#### A. Frontend

##### A.1 RPG Maker MZ

RPG Maker MZ is a game development engine designed for creating 2D role-playing games. It will be used in the core application development to construct the visual environment, manage the database of enemies and items, and script game events. The proponents utilize this engine because its built-in architecture provides a framework for RPG mechanics (such as inventory and movement) while allowing for the addition of custom JavaScript plugins to create the "Math Battle System."

##### A.2 HTML5 / WebGL

HyperText Markup Language 5 (HTML5) is the standard markup language for structuring web content. Web Graphics Library (WebGL) is a JavaScript API for rendering 2D and 3D graphics within web browsers. HTML5 and WebGL will run the web version of the proposed project. The proponents will use these tools to display 2D graphics directly on internet browsers. Doing this will allow the game to work easily on mobile phones and school computers. Users will not need to download or install any extra files to play the game.

##### A.3 Cascading Style Sheets (CSS)

Cascading Style Sheets (CSS) is a style sheet language used to set the visual look and layout of HTML documents and is always partnered up with JavaScript. CSS will be used as it allows the proponents to resize the game window across different screen sizes. It will also place the Virtual Keypad overlay in the exact right spot.

#### B. Backend

##### B.1 JavaScript (ES6)

JavaScript (ECMAScript 6) is a programming language used for creating dynamic and interactive content on web pages and is the native scripting language of RPG Maker MZ. JavaScript will be used as it allows the proponents to make custom plugins for the Math Battle System, Level Based Difficulty System, Enemy Auto Scaling System, Automatic Quest Generation system, and P2P Multiplayer Framework.

##### B.2 Visual Studio Code (v1.111)

Visual Studio Code is the project’s main coding hub. Built by Microsoft, the proponents will use it to write game scripts, specifically managing the JavaScript codebase.

##### B.3 Node.js (v25.8.1)

Node.js is an open-source, server-side runtime environment that executes JavaScript outside of a web browser. It will be used during the development phase to run local server environments. Node.js will be used to simulate server-side operations for testing the P2P multiplayer handshake so that the connection logic is stable before deploying to the public web.

##### B.4 PeerJS (v1.5.5)

PeerJS is a Web Real-Time Communication (WebRTC) wrapper library that simplifies the process of establishing direct browser-to-browser connections. It will be used to implement the Peer-to-Peer (P2P) Multiplayer Framework by managing the generation of unique "Room Codes" and facilitating the data exchange between the host and connected clients. This library establishes direct connections between players without requiring a centralized backend server.

#### C. Multimedia and Asset Development Tools

##### C.1 GIMP (GNU Image Manipulation Program)

GIMP is a free, open-source raster graphics editor used for image retouching and editing. It will be utilized as the primary graphics editor for the manipulation of game assets. GIMP will be used in the asset creation phase to perform "Hue Shifting" on default enemy sprites because its color manipulation tools allow for the creation of biome-specific enemy variants (e.g., Sand Slime, Magma Slime) from a single base asset.

##### C.2 Canva

Canva is a web-based graphic design platform that provides templates and drag-and-drop tools for creating visual content. It will be utilized as the primary design tool for creating the Chronicles of Arithmos game logo and visual identity materials during the design phase.

##### C.3 Draw.io

Draw.io, also known as diagrams.net, is a free, web-based diagramming application used for creating flowcharts, diagrams, and system architecture visuals. Draw.io will be used to create fundamental diagrams for the documentation of the system, which includes the Functional Decomposition Diagrams and Fishbone Diagram.

#### D. Deployment and Runtime Platform

##### D.1 NW.js (Native Executable Wrapper)

NW.js is an open source framework that allows HTML5 and JavaScript applications to run as native desktop programs. It will act as the main program to run the PC version. The proponents will use NW.js to pack the web game files into one executable file (.exe) for Windows. This wrapper gives the application direct access to local folders to store save files. Because of this, the game can run completely offline.

##### D.2 Google Chrome / Microsoft Edge

Google Chrome version 145 and Microsoft Edge version 145 are Chromium based web browsers. They run modern web tools like HTML5, WebGL, and WebRTC. These specific browser versions will act as the main programs to run the web based version of the project.

##### D.3 GitHub

GitHub is the cloud hub for Chronicles of Arithmos files and JavaScript scripts and is always partnered up with Git, since Git tracks every single code change. Proponents work on ATB timer files together without ruining each other's progress. If an update breaks the math logic, the proponents return to a past version since the history stays.

##### D.4 Git

Git is a version control system where developers can track changes in their code during software making. The proponents use Git while building the game to save edits to the code. This tool lets the proponents send updated files from their own computers straight to the GitHub repository.

##### D.5 Vercel

Vercel is the project’s temporary web host. The proponents will use it to test the game online before committing to a paid domain. Since it syncs directly with GitHub, every code update goes live automatically. Most importantly, it provides the HTTPS security required for the game’s P2P multiplayer (WebRTC and PeerJS) to connect.

##### D.6 Hostinger

Hostinger is a web hosting service that offers domains and cloud-based hosting for web apps. It will act as the final live host for the game when it launches. This service will replace the Vercel testing setup during the final release.

### 3.1.3 Peopleware

#### A. The Proponents

The proponents consisted of a project manager, a programmer, a UI/UX designer, a tester, and a graphic designer. Each person executed specific tasks to complete the system according to the agreed standards. The project manager oversaw the overall development schedule and guided the team workflow. The programmer wrote the game scripts. The UI/UX designer planned the visual layouts. The tester conducted the multiplayer network checks and recorded software bugs during the trials. Finally, the graphic designer created assets including the game logo.

#### B. Capstone Adviser

Mr. Jan Nicole B. Apostol provided guidance, clarifications, and recommendations for the project. The adviser guided the proponents through technicalities and documentation, provided necessary revisions, and verified that the system met the required formatting and quality standards.

### 3.1.4 Network

#### A. Local Area Network (LAN) & Cloud Staging

The proponents will test the multiplayer mode using two different network setups during development. First, the team will check the peer-to-peer connection and game data sync by connecting multiple computers to the same Local Area Network or Wi-Fi to make sure the game runs without lag. Next, the proponents will test the game using computers on completely different networks to observe how the system handles a Wide Area Network (WAN). This secondary test will prove that the Room Code connection stays stable over the public internet.

## 3.2 Implementation

### 3.2.1 Hardware

#### A. Personal Computer or Laptop

Users need a personal computer desktop or laptop to download, install, and play the main application of Chronicles of Arithmos. These devices process the local game files and allow the player to control the game using a keyboard and a mouse.

#### B. Mobile Device

Users need a mobile phone or tablet running Android or iOS to open a web browser and play the online version of the game. These devices connect to the internet to load the game pages and allow the player to interact with the screen using touch controls.

### 3.2.2 Software

#### A. Operating System (OS)

The game requires Windows 10 64-bit or higher. The NW.js wrapper depends on 64-bit architecture to function [9]. Older systems cannot run this. Mobile devices need Android 10 or iOS 14 at a minimum. These versions are needed to fully support WebGL 2.0 rules [10], which power the 2D visuals of the game.

#### B. Modern Browsers

Players will need a modern web browser to play. The proponents recommend Google Chrome or Microsoft Edge. These browsers run the WebGL graphics and Virtual Keypad of the game very well. These Chromium based browsers also support WebRTC protocols needed for P2P multiplayer.

### 3.2.3 Peopleware

#### A. Young Learners and General Users

Primary school students between 9 and 12 years old will act as the primary players of the game. However, the system accommodates all possible users regardless of age. Children below 9 years old can play the game using early difficulty stages to learn basic addition and subtraction. Older students and individuals above 12 years old can also play the game for casual entertainment or to refresh their mental calculation speed. These learners will use the battle system to solve math problems while they explore different biomes such as the tundra biome and finish the main story. By playing, all users can practice their math skills and improve calculation speed.

### 3.2.4 Network

#### A. Internet Connection

The system requires a stable internet connection to function properly for multiplayer and web versions. A minimum of 5 to 10 Mbps internet speed will be needed for multiplayer mode or to load web files on the web application version.

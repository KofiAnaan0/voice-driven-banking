# Voice-Driven Banking via Large Acoustic Models (LAMs)

## Introduction
Globally, an estimated 1 to 1.5 billion individuals in rural and underserved communities lack basic digital skills. This significantly limits their ability to perform online financial transactions. Many financial institutions offer digital banking platforms, yet these services remain inaccessible due to literacy barriers and the unavailability of banking facilities in remote areas.

To bridge this gap, this open-source project leverages AI to enable financial transactions through voice commands in native languages and dialects, providing an inclusive banking experience for marginalized populations.

## Objectives
### Technical Objectives
- Develop and deploy Large Acoustic Models (LAMs) for regional languages and accents.
- Integrate Natural Language Processing (NLP) for intent recognition.
- Implement voice biometrics for secure authentication.

### Business Objectives
- Expand access to digital banking services, particularly in underserved areas.
- Improve customer engagement through automation.
- Reduce operational costs associated with traditional banking methods.

### Social Impact
- Empower non-literate users by providing a seamless, voice-driven banking experience.
- Enhance financial inclusion and digital literacy in marginalized communities.

## Tech Stack
**Front-End:**
- HTML, CSS (Bootstrap), JavaScript

**Back-End:**
- Python (Django)

**AI Integrations:**
- **Whisper** – Automatic speech recognition and transcription
- **Mistral 7B** – Open-source Large Language Model (LLM) for processing user queries
- **Playwright** – Browser automation for executing financial transactions
- **OpenVoice** – Text-to-speech for responses in local dialects

## Project Design
Find the detailed explanation of the project design [here](#).

## Product Architecture
Find the detailed explanation of the project architecture in this [link](#).

## Project Demo

## Contributions
This is an open-source initiative. Contributions to the Figma design or codebase are highly encouraged. If you wish to contribute:
- Submit a Pull Request (PR) on GitHub.
- Email: [santosisadru@gmail.com](mailto:santosisadru@gmail.com) for inquiries.

## Installation Guide
### For Windows:
1. Open the terminal & navigate to the folder where you want to clone:
   ```sh
   cd path/to/your/folder
   ```
2. Run the Git Clone Command:
   ```sh
   git clone https://github.com/username/repository.git
   ```
3. Open the Cloned Project in VS Code:
   ```sh
   cd repository
   code .
   ```
4. Install Dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Configure the Database:
   - The project uses SQLite, so no extra setup is needed.
   - If you want PostgreSQL or MySQL, configure the `DATABASES` setting in `settings.py`.
6. Run migrations:
   ```sh
   python manage.py migrate
   ```
7. Run the Development Server:
   ```sh
   python manage.py runserver
   ```
   Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
8. Load Static Files (Optional):
   ```sh
   python manage.py collectstatic
   ```
   Then restart the server.

## Conclusion
The **Voice-Driven Banking via LAMs** project aims to simplify banking for rural and underserved communities by eliminating literacy and technical barriers through AI-powered voice interactions. This initiative enhances financial inclusion, making digital banking truly accessible to everyone.

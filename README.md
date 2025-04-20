# ZFaceMe

**ZFaceMe** is a real-time video calling web application built with **Django** on the backend and **HTML, CSS, and JavaScript** on the frontend. It leverages **WebSockets** for establishing signaling connections and **WebRTC** for peer-to-peer video and audio communication.

## 🚀 Features

- 🔐 User-friendly interface for initiating and receiving video calls
- 📡 WebSocket-based signaling for real-time connection setup
- 🎥 High-quality video and audio powered by WebRTC
- 💻 Built with Django, offering a robust backend framework
- 🖥️ Responsive and clean frontend using HTML, CSS, and JavaScript

## 🧰 Tech Stack

| Layer         | Technology               |
|---------------|--------------------------|
| Backend       | Django                   |
| Frontend      | HTML, CSS, JavaScript    |
| Real-time Comm| WebSocket (signaling)    |
| Media Stream  | WebRTC                   |

## 📷 How It Works

1. **Signaling Phase**:
   - Users connect to a WebSocket server.
   - Signaling data (offer/answer) is exchanged.

2. **WebRTC Connection**:
   - Peer-to-peer media connection is established.
   - Audio and video streams flow directly between clients.

3. **Video Call UI**:
   - Clean and intuitive interface to start and end calls.
   - Dynamic video rendering using JavaScript DOM manipulation.

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8+
- Virtualenv (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MrLionByte/ZFaceMe.git
   cd ZFaceMe
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations and start the server**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Open in browser**
   - Visit: `http://127.0.0.1:8000` in your browser.

## 🔧 Project Structure

```
ZFaceMe/
│
├── zfaceme/            # Django project files
├── videoapp/           # Core app handling video logic
│   ├── templates/
│   ├── static/
│   └── views.py
├── manage.py
└── requirements.txt
```

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

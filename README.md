# 🚀 Docker + Flask App

This is a simple **Flask web application** containerized with **Docker** and deployed on an **EC2 instance**.

---

## 📂 Project Structure

docker-flask-app/
│-- app.py
│-- requirements.txt
│-- Dockerfile


---

## ⚡ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/DevopsbyLalit/docker-flask-app.git
   cd docker-flask-app

2 Build Docker image

   docker build -t flask-app .

3 Run the container

  docker run -d -p 5000:5000 flask-app

4 Access the app

  Open browser and go to 👉 http://localhost:5000
  
🌐 Deployed on AWS EC2

App is containerized using Docker and running on an Amazon EC2 Instance.

🛠️ Tech Stack

Python (Flask)

Docker

AWS EC2

GitHub

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

👤 Author

Lalit Kumar (DevopsbyLalit)
🔗 GitHub
 | LinkedIn

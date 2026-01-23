# AI Powered Worker Productivity Dashboard

## GitHub Repository
https://github.com/Abhra-deep/Ai-powered-worker-productivity-dashboard

---

## Web Application Link
- **Backend (Deployed):** https://ai-powered-worker-productivity-dashboard-nhn0.onrender.com
- **API Docs:** https://ai-powered-worker-productivity-dashboard-nhn0.onrender.com/docs
- **Frontend (Local):** http://localhost:5173  

---

## Architecture Overview
AI CCTV Cameras  
→ JSON Events  
→ FastAPI Backend  
→ SQLite Database  
→ React Dashboard  

AI cameras generate structured events.  
The backend ingests and stores these events, computes productivity metrics, and exposes REST APIs.  
The frontend fetches these metrics and displays them in a dashboard.

---

## Database Schema

### Events
| Field | Description |
|------|------------|
| timestamp | Event timestamp |
| worker_id | Worker reference |
| workstation_id | Workstation reference |
| event_type | working / idle / absent / product_count |
| confidence | AI model confidence |
| count | Units produced (product_count only) |

---

## Metric Definitions

### Worker Level
- **Total Active Time:** count of `working` events  
- **Total Idle Time:** count of `idle` events  
- **Utilization:**  
  `working / (working + idle)`
- **Total Units Produced:** sum of `product_count`  
- **Units per Hour:** total units / active events  

### Factory Level
- **Total Productive Time:** sum of all working events  
- **Total Production Count:** sum of all `product_count` values  
- **Average Utilization:** productive / total events  

---

## Assumptions and Trade-offs

### Assumptions
- Events represent fixed time slices  
- AI-generated events are trusted  
- One worker per workstation per event  

### Trade-offs
- Event-count-based time instead of duration-based  
- SQLite used for simplicity  
- No real-time streaming  

---

## Theoretical Questions

### Intermittent Connectivity
Late-arriving events are stored and processed during metric computation.

### Duplicate Events
Events can be deduplicated using:
worker_id + workstation_id + timestamp + event_type


### Out-of-order Timestamps
Events are sorted by timestamp before computing metrics.

### Model Versioning, Drift, Retraining
- Add `model_version` field to events  
- Monitor confidence, idle time, and production trends  
- Retrain when sustained drift is detected  

---

## Running Locally

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
Frontend
cd frontend
npm install
npm run dev
Author
Abhra Deep
GitHub: https://github.com/Abhra-deep


---

## 🚀 Final Steps (VERY IMPORTANT)

Run these commands now:

```bash
git add README.md
git commit -m "Update README with deployed backend link"
git push

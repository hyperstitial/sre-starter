# SRE Starter Runbook
Start: `docker compose up --build -d`
Stop:  `docker compose down`  (or `docker compose stop app`)
Logs:  `docker compose logs -f app|prometheus|grafana`
Dashboards: http://localhost:3000  (“SRE Starter”)
Alerts: http://localhost:9090/alerts (AppDown: `up{job="app"}==0 for 1m`)
Common fix: `docker compose start app`, verify `/healthz`, target UP.

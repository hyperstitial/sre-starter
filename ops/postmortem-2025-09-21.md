# Postmortem: AppDown Chaos Drill
**Date:** $(date +%F)
**Service:** app (Flask)
**Impact:** Requests failed while the app was stopped.
**Detection:** Prometheus target DOWN; Grafana “App health”=0; AppDown alert after 1m.
**Root cause:** Intentional drill.
**Timeline:** stop -> alert ~1m -> start -> recovered.
**Actions:** Added availability alert; set restart policy.
**Follow-ups:** refine alerting; add rollback guard.

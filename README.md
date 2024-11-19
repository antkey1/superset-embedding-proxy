Superset Embedding Proxy
===

Helper for embed superset dashboards via superset-embedded-sdk.

Edit variables in `docker-compose.yaml`.

Start service:

```shell
docker compose up
```

Swagger available at `http://localhost:8000/docs`

Example embedded dashboard in `example.html`. 
Please, edit `SUPERSET_URL`, `SUPERSET_EMBEDDING_PROXY_URL`, `DASHBOARD_ID` as you need.

For production use modify `CORSMiddleware` and add authorization.

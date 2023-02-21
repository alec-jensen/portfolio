import pynecone as pc

config = pc.Config(
    app_name="portfolio",
    api_url="http://0.0.0.0:1444"
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    # bun_path="/app/.bun/bin/bun" # UNCOMMENT WHEN DEPLOYING WITH DOCKER
)

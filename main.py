import uvicorn

if __name__ == "__main__":
    # The server will automatically reload when the code changes (useful for development less for production)
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)

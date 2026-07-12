from fastapi import FastAPI
import httpx
import os

app = FastAPI()
AIPIPE_KEY = os.environ.get("AIPIPE_KEY") # Set this in Render's Environment tab!

@app.post("/v1/extract-invoice")
async def extract_invoice(payload: dict):
    # This sends your data to the AI pipe endpoint
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "YOUR_AIPIPE_API_URL", # The actual URL the pipe expects
            headers={"Authorization": f"Bearer {AIPIPE_KEY}"},
            json={"prompt": f"Extract this invoice: {payload['text']}"}
        )
        return response.json()

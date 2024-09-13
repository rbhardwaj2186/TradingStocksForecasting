from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import matplotlib.pyplot as plt
import os
import uuid
from app.services import StockService

# Initialize FastAPI app
app = FastAPI()

# Mount the static directory for serving images
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up the templates directory
templates = Jinja2Templates(directory="templates")

# Initialize the stock service
stock_service = StockService()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Renders the home page with the form for selecting stock, start/end dates, and forecast type.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/forecast", response_class=HTMLResponse)
async def forecast(
    request: Request,
    stock: str = Form(...),
    start_date: str = Form(...),
    end_date: str = Form(...),
    forecast_type: str = Form(...)
):
    """
    Handles the form submission, generates a forecast graph based on the user's input.
    """
    # Fetch stock data from the service
    try:
        stock_data = stock_service.get_stock_data(stock, start_date, end_date)
    except ValueError as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": str(e),
            "stock": stock,
            "start_date": start_date,
            "end_date": end_date,
            "forecast_type": forecast_type
        })

    # Apply the selected forecast type
    if forecast_type == "3m":
        stock_data['Forecast'] = stock_data['Close'].rolling(window=3).mean()
    elif forecast_type == "6m":
        stock_data['Forecast'] = stock_data['Close'].rolling(window=6).mean()
    elif forecast_type == "exponential_smoothing":
        stock_data['Forecast'] = stock_service.apply_exponential_smoothing(stock_data['Close'])

    # Generate and save the graph
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['Close'], label='Actual Price', color='blue')
    plt.plot(stock_data.index, stock_data['Forecast'], label=f'{forecast_type} Forecast', color='red')
    plt.title(f"{stock} Stock Forecast")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.legend()

    # Generate unique image filename
    image_filename = f"forecast_graph_{uuid.uuid4()}.png"
    image_path = os.path.join("static", image_filename)
    plt.savefig(image_path)
    plt.close()

    # Return the forecast and display the graph
    return templates.TemplateResponse("index.html", {
        "request": request,
        "image_path": image_path,
        "stock": stock,
        "start_date": start_date,
        "end_date": end_date,
        "forecast_type": forecast_type
    })
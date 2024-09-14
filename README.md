# Trading Stock Prediction: Tesla, GM, and Ford

![image](https://github.com/user-attachments/assets/5236a88b-3f6d-491c-b774-68aa34423176)




https://github.com/user-attachments/assets/deb1121a-1e64-41b8-bb51-a0ccea662cd4


This project is a web-based application built using **FastAPI** for stock price forecasting and analysis. The application fetches historical stock data for Tesla (TSLA), Ford (F), and General Motors (GM), and provides visual forecasts based on **3-month Moving Average**, **6-month Moving Average**, and **Exponential Smoothing**. Users can interact with the app through a simple HTML interface and generate dynamic forecast graphs.

## Project Structure


## Project Overview

This project is designed to:
- Fetch and visualize stock data for Tesla, Ford, and General Motors.
- Provide different forecasting methods: **3-month moving average**, **6-month moving average**, and **exponential smoothing**.
- Allow users to specify a date range (from 2020-2024) to analyze stock prices.
- Present results in an interactive, user-friendly HTML interface using **FastAPI** and **Matplotlib** for graphing.

## Forecasting Methods

### 1. **3-month Moving Average (3M)**:
A moving average is a statistical technique that smooths out short-term fluctuations in data to highlight long-term trends. The **3-month moving average** calculates the average stock price over the past 3 months (or any specified window) and forecasts the stock price based on this average.

**Use case**: 
- Helps smooth out short-term noise in stock prices.
- Useful when identifying short-term trends or fluctuations in volatile stocks.

### 2. **6-month Moving Average (6M)**:
The **6-month moving average** uses a wider window than the 3-month moving average, providing a more stable, long-term trend analysis by averaging the stock prices over the last 6 months.

**Use case**:
- Provides a more stable forecast over a longer period.
- Ideal for identifying long-term trends and avoiding short-term price fluctuations.

### 3. **Exponential Smoothing**:
**Exponential smoothing** assigns exponentially decreasing weights to past data points, meaning more recent data points have a greater impact on the forecast. This method is useful for smoothing out volatile stock prices while remaining sensitive to recent price movements.

**Use case**:
- Useful for forecasting stock prices when you want to account for both the overall trend and recent price changes.
- Highly sensitive to recent stock price changes, making it ideal for reactive market forecasting.

## How the Project Works

1. **Stock Data Fetching**:  
   The stock data for Tesla, Ford, and GM is fetched using the **yfinance** library. This data is used as the foundation for all forecasts and visualizations.

2. **User Interface (`index.html`)**:  
   The project provides a simple HTML interface built with **Jinja2** templating. The interface allows users to:
   - Select the stock (Tesla, Ford, or GM).
   - Set the start and end date for the data analysis.
   - Choose the forecast method (3-month moving average, 6-month moving average, or exponential smoothing).
   
   The form submission triggers a forecast generation, which is displayed as a graph using **Matplotlib**.

3. **FastAPI Backend**:
   - **FastAPI** is used to handle HTTP requests, process form submissions, and route the requests to the correct logic for forecasting.
   - The selected stock data is passed through the appropriate forecast model, and a graph is generated based on the user's input.
   - The forecast graph is saved in the `static` directory and displayed back to the user via the HTML interface.

## Usage Instructions

### 1. Installation

First, clone the repository:

```bash
git clone https://github.com/yourusername/TradingStocksForecasting.git
cd TradingStocksForecasting
# Install the dependencies:
pip install -r requirements.txt
#Running the Application 
uvicorn app.main:app --reload  


### Key Sections in the `README.md`:

1. **Overview**: Brief introduction to the project's goal and technologies used.
2. **Project Structure**: A detailed breakdown of the directory structure.
3. **Forecasting Methods**: Explanation of the 3-month, 6-month moving averages, and exponential smoothing, and their use cases.
4. **How the Project Works**: Overview of stock data fetching, the `index.html` user interface, and FastAPI's role in backend routing.
5. **Usage Instructions**: How to install dependencies, run the server, and use the web interface.
6. **Example Output**: A placeholder for an example forecast graph image.
7. **Future Improvements**: Optional section for any future features or improvements.

### What to Do Next:

1. **Save this `README.md` file** in your project's root directory.
2. **Add example graph images** (optional) in the `static` directory and update the link in the README.
3. Commit the `README.md` file to your Git repository and push it to GitHub:

```bash
git add README.md
git commit -m "Added README.md"
git push

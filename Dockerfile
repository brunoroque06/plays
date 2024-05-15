FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY .streamlit .streamlit
COPY data data
COPY pages pages
COPY reportus reportus
COPY Home.py .
ENTRYPOINT ["streamlit", "run"]
CMD ["Home.py", "--browser.gatherUsageStats", "false", "--server.fileWatcherType", "none", "--server.port", "8080"]

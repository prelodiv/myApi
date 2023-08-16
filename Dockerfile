# 
FROM python:3.11
# 
WORKDIR /code
# 
COPY . /code/app
# 
RUN python -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir --upgrade -r ./app/requirements.txt
ENV PYTHONPATH /code/app
# 
# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

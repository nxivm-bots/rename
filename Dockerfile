FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the code to the container
COPY . /app/

# Install dependencies
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    pip install -r requirements.txt

# Run the bot
CMD ["python", "bot.py"]
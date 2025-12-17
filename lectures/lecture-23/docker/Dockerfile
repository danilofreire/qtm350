# Use an official Python runtime as a parent image
FROM python:3

# Install libraries
RUN pip install numpy pandas matplotlib

# Add a script
RUN echo "print('Hello, QTM350!')" > hello.py

# Run the script
CMD ["python", "hello.py"]
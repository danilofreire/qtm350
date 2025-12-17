# Base image
FROM ubuntu:24.04

# Metadata
LABEL version="1.0"
LABEL description="Container with the tools covered in QTM 350"
LABEL maintainer="Danilo Freire <danilo.freire@emory.edu>"
LABEL license="MIT"

# Update and install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends\
    bash=5.2.21-2ubuntu4 \
    git=1:2.43.0-1ubuntu7.3 \
    sqlite3=3.45.1-1ubuntu2 \
    libsqlite3-0=3.45.1-1ubuntu2 \
    python3.12=3.12.3-1ubuntu0.8 \
    python3.12-venv=3.12.3-1ubuntu0.8 \
    python3-pip=24.0+dfsg-1ubuntu1.3 && \ 
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set default shell to Bash
SHELL ["/bin/bash", "-c"]

# Create and activate virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies in virtual environment
RUN pip install httpx==0.27.2 numpy==1.26.4 pandas==2.2.2 \
                jupyterlab==4.3.0 ipykernel==6.29.5 \
                dask==2024.5.0 matplotlib==3.9.2

# Install Quarto
RUN wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.6.37/quarto-1.6.37-linux-arm64.deb && \
    # Install the local deb file (notice the "./" prefix)
    apt-get install -y ./quarto-1.6.37-linux-arm64.deb && \
    rm quarto-1.6.37-linux-arm64.deb && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a directory for saving files
RUN mkdir -p /workspace
WORKDIR /workspace

# Expose port for JupyterLab 
EXPOSE 8888

# Start JupyterLab
CMD . /opt/venv/bin/activate && jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root

# Run the Docker container
# docker build -t qtm350-container .
# docker run -it --rm -p 8888:8888 -v $(pwd):/workspace qtm350-container
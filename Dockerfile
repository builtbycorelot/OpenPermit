FROM mcr.microsoft.com/devcontainers/python:3.11
# Node for frontend tasks (optional)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
 && apt-get install -y nodejs jq \
 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /workspace
COPY . /workspace
RUN make install || true
EXPOSE 5173 8000
CMD ["bash","-lc","make dev || make docs"]

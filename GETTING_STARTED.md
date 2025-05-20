# Getting Started

This guide explains the basic requirements for running the OpenPermit demo and contributing to future development.

## Prerequisites

- **Node.js 18+** – The client demo uses modern JavaScript syntax that targets Node.js version 18 or later. Install it from [nodejs.org](https://nodejs.org/).
- **npm** – Included with Node.js for running simple HTTP servers or installing tooling.

## Running the Demo

1. Clone the repository:
   ```bash
   git clone https://github.com/sheetpros/openpermit.git
   cd openpermit
   ```
2. Serve the `example/` folder using any static server. One option is `npx http-server`:
   ```bash
   npx http-server example
   ```
3. Open `http://localhost:8080/index.html` in your browser. You should see a page with buttons to create nodes, validate them and build crosswalks.

Alternatively you can simply open `example/index.html` directly in a browser without running a server.

## Roadmap and Contribution Ideas

The project is still in an early state. Future work may include:

- Publishing the Node framework as an installable package.
- Adding unit tests and continuous integration scripts.
- Expanding the ontology and sample data under `open-data-layer/`.
- Improving the browser demo with more realistic examples.
- Providing scripts to import real permitting standards and regulations.

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for general guidelines and open an issue to discuss new features.

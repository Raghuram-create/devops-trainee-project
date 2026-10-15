# DevOps Trainee Project — Python Profit Calculator

## Project Overview

This project demonstrates fundamental DevOps practices using a Python profit calculator.

The application calculates profit from revenue and expenses, then classifies the result as:

- **Positive** — revenue is greater than expenses
- **Break-even** — revenue equals expenses
- **Loss** — expenses are greater than revenue

The project includes automated tests, Git version control, GitHub Actions continuous integration (CI), Docker containerization, and Docker Compose.

## Technologies Used

- Python
- pytest
- Git and GitHub
- GitHub Actions
- Docker
- Docker Compose

## Project Structure

```text
devops-trainee-project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .dockerignore
├── .gitignore
├── Dockerfile
├── compose.yaml
├── app.py
├── test_app.py
├── requirements.txt
└── README.md
```

## Run the Application Locally

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Expected output:

```text
{'profit': 1500, 'decision': 'Positive'}
```

## Run Automated Tests

```bash
python -m pytest -v
```

The project includes four tests covering positive profit, break-even, loss, and invalid negative revenue.

## Continuous Integration

A GitHub Actions workflow is configured in `.github/workflows/ci.yml`.

On every push or pull request, the workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs dependencies.
4. Runs automated tests using pytest.

The workflow must pass before the code is considered successfully tested.

## Docker

Build the Docker image:

```bash
docker build -t profit-calculator .
```

Run the application:

```bash
docker run --rm profit-calculator
```

## Docker Compose

Build and run the application:

```bash
docker compose up --build
```

Inspect the container status:

```bash
docker compose ps -a
```

View container logs:

```bash
docker compose logs
```

Remove the Compose-managed container:

```bash
docker compose down
```

The container exits after printing the calculation because this application is a command-line script, not a continuously running web service.

## Basic Troubleshooting

**Docker daemon connection error:** Start Docker Desktop and confirm the Docker Engine is running using `docker info`.

**Tests fail:** Run `python -m pytest -v` and inspect the failed assertions.

**Container exits:** Check `docker compose ps -a` and `docker compose logs`. Exit code `0` is expected for this application.

**GitHub Actions fails:** Open the Actions tab in GitHub, select the failed workflow run, and inspect the failed step's logs.

## Future Improvements

- Add a web API and health-check endpoint.
- Add automated deployment after successful tests.
- Introduce container image scanning.
- Add monitoring and structured application logging.
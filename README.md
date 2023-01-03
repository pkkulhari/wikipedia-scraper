# wikipedia_scraper

A wikipedia scraper to scrape the information from a wikipedia’s country page.

## API Reference

#### Get country info

```http
  GET /api/country_info/${country_name}
```

| Parameter      | Type     | Description  |
| :------------- | :------- | :----------- |
| `country_name` | `string` | **Required** |

## Run Locally

Clone the project

```bash
  git clone https://github.com/pkkulhari/wikipedia-scraper.git
```

Go to the project directory

```bash
  cd wikipedia-scraper
```

Copy `.env.example` to `.env`

```bash
  cp .env.example .env
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```

Now, Server should be listening at http://127.0.0.1:8000

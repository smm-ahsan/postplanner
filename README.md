# PostPlanner

A tiny, dependency-free command line tool that generates a social media
content calendar as a CSV file.

Pick a business niche and a start date, and PostPlanner builds a day-by-day
plan: each day gets a content pillar, a ready-made post idea for that niche,
a suggested format, and a best posting time. Open the CSV in any spreadsheet
app and your week of content is planned in seconds.

## Why

Social media managers and small business owners lose time every week staring
at a blank calendar. The hard part is rarely posting - it is deciding *what*
to post, day after day, without repeating the same kind of content.
PostPlanner solves the structure problem: it rotates seven proven content
pillars (Educate, Behind the scenes, Offer, Social proof, Engage, Product
spotlight, Story) so a feed stays varied, and pairs each pillar with a
concrete idea written for your niche. You personalise the ideas, schedule
them, and get back to running the business.

## Features

- Zero dependencies - pure Python 3 standard library
- Niches: cafe, restaurant, bakery, salon, gym, realestate, general
- Rotates 7 content pillars across the plan so content never feels repetitive
- Niche-specific post ideas for every pillar
- Suggested format per day: Reel, Photo, Carousel or Story
- Suggested best posting time per day
- Plan any number of days, starting from any date
- Outputs a clean CSV (date, day, pillar, idea, format, best_time) and also
  prints the plan in readable form
- Optional seed for repeatable plans

## Install

No installation needed. Clone the repo and run it with Python 3:

```bash
git clone https://github.com/smm-ahsan/postplanner.git
cd postplanner
python3 postplanner.py --help
```

## Usage

```bash
python3 postplanner.py --niche bakery --days 7 --start 2026-11-16
python3 postplanner.py --niche cafe --days 14 --out cafe-plan.csv --seed 5
python3 postplanner.py --niche gym --days 30 --start 2026-12-01 --out december.csv
```

Sample output:

```
2026-11-16 (Monday) - Educate
  Idea:   Explain why sourdough needs a long, slow fermentation
  Format: Reel at 18:00
```

See [examples.md](examples.md) for a full sample run.

## Roadmap

- More niches (clinics, car services, tutors, photographers)
- Multiple ideas per pillar with random selection
- Export to Markdown and HTML as well as CSV
- Holiday and event hooks for Malta and the EU

## Contributing

Issues and pull requests are welcome. If you plan content for a niche that
is missing, open an issue with your business type and the kinds of posts
that work for you, or add an idea bank for it and send a pull request.

## License

MIT - see [LICENSE](LICENSE).

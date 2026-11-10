#!/usr/bin/env python3
"""PostPlanner - generate a social media content calendar as a CSV file.

A tiny, dependency-free tool for small businesses and social media managers.
Pick a niche and a start date, and it builds a day-by-day plan that rotates
content pillars, suggests a post idea, a format and a best posting time.

Usage:
    python3 postplanner.py --niche bakery --days 7 --start 2026-11-16
    python3 postplanner.py --niche cafe --days 14 --out cafe-plan.csv --seed 5
"""

import argparse
import csv
import random
import sys
from datetime import date, timedelta

PILLARS = [
    "Educate",
    "Behind the scenes",
    "Offer",
    "Social proof",
    "Engage",
    "Product spotlight",
    "Story",
]

FORMATS = ["Reel", "Photo", "Carousel", "Story"]

BEST_TIMES = ["07:30", "12:15", "18:00", "19:30", "20:45"]

IDEA_BANK = {
    "cafe": {
        "Educate": "Explain the difference between a flat white and a latte",
        "Behind the scenes": "Film the morning opening routine and first brew of the day",
        "Offer": "Announce a weekday happy hour on all coffees",
        "Social proof": "Share a regular customer's favourite order and their quote",
        "Engage": "Run a this-or-that poll: espresso or cappuccino?",
        "Product spotlight": "Spotlight the house blend beans and where they come from",
        "Story": "Tell the story of how the cafe got its name",
    },
    "restaurant": {
        "Educate": "Share three tips for pairing wine with pasta",
        "Behind the scenes": "Show the chef prepping the signature sauce from scratch",
        "Offer": "Promote a two-course lunch deal for this week only",
        "Social proof": "Repost a five-star review with a photo of the dish mentioned",
        "Engage": "Ask followers: what dish should join the menu next?",
        "Product spotlight": "Spotlight the chef's special with a close-up shot",
        "Story": "Tell how the restaurant started as a family kitchen",
    },
    "bakery": {
        "Educate": "Explain why sourdough needs a long, slow fermentation",
        "Behind the scenes": "Film the ovens being loaded at 5 AM",
        "Offer": "Announce a buy-two-get-one deal on weekend loaves",
        "Social proof": "Share a photo a customer posted of their birthday cake",
        "Engage": "Poll followers: croissant or pain au chocolat?",
        "Product spotlight": "Spotlight the new seasonal pastry with a cross-section shot",
        "Story": "Tell the story behind the recipe that started the bakery",
    },
    "salon": {
        "Educate": "Share three hair care mistakes clients make at home",
        "Behind the scenes": "Show a stylist mixing a colour formula",
        "Offer": "Promote a weekday discount on cuts and styling",
        "Social proof": "Post a before-and-after transformation with the client's permission",
        "Engage": "Ask followers to vote on the next trending colour",
        "Product spotlight": "Spotlight a treatment service and who it is best for",
        "Story": "Tell how the salon's founder fell in love with hairdressing",
    },
    "gym": {
        "Educate": "Demonstrate correct squat form in three steps",
        "Behind the scenes": "Show the coaches setting up for the morning classes",
        "Offer": "Announce a free trial week for new members",
        "Social proof": "Share a member's progress story with their permission",
        "Engage": "Run a challenge: how many push-ups in one minute?",
        "Product spotlight": "Spotlight a class and what a first session looks like",
        "Story": "Tell why the gym was opened and what it stands for",
    },
    "realestate": {
        "Educate": "Explain the hidden costs of buying a first home",
        "Behind the scenes": "Show how a property is prepared before a photo shoot",
        "Offer": "Announce a free valuation day for sellers this month",
        "Social proof": "Share a happy buyer's testimonial and their new front door",
        "Engage": "Ask followers: apartment in the city or house in the suburbs?",
        "Product spotlight": "Spotlight a new listing with a walk-through tour",
        "Story": "Tell the story of the most unusual property you ever sold",
    },
    "general": {
        "Educate": "Share one useful tip your customers keep asking about",
        "Behind the scenes": "Show what a normal working day looks like for your team",
        "Offer": "Announce a limited-time offer and its deadline",
        "Social proof": "Share a customer review you are proud of",
        "Engage": "Ask a question your followers can answer in one word",
        "Product spotlight": "Spotlight your best-selling product or service",
        "Story": "Tell the story of how your business began",
    },
}


def build_plan(niche, days, start, rng):
    ideas = IDEA_BANK[niche]
    formats = list(FORMATS)
    times = list(BEST_TIMES)
    rng.shuffle(formats)
    rng.shuffle(times)
    rows = []
    for i in range(days):
        day_date = start + timedelta(days=i)
        pillar = PILLARS[i % len(PILLARS)]
        rows.append({
            "date": day_date.isoformat(),
            "day": day_date.strftime("%A"),
            "pillar": pillar,
            "idea": ideas[pillar],
            "format": formats[i % len(formats)],
            "best_time": times[i % len(times)],
        })
    return rows


def print_plan(rows):
    for row in rows:
        print("{date} ({day}) - {pillar}".format(**row))
        print("  Idea:   {idea}".format(**row))
        print("  Format: {format} at {best_time}".format(**row))
        print()


def write_csv(rows, out_path):
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=["date", "day", "pillar", "idea", "format", "best_time"]
        )
        writer.writeheader()
        writer.writerows(rows)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate a social media content calendar as a CSV file."
    )
    parser.add_argument("--niche", default="general",
                        choices=sorted(IDEA_BANK.keys()),
                        help="Business niche (default: general)")
    parser.add_argument("--days", type=int, default=7,
                        help="Number of days to plan (default: 7)")
    parser.add_argument("--start", default=None,
                        help="Start date YYYY-MM-DD (default: today)")
    parser.add_argument("--out", default="plan.csv",
                        help="Output CSV file (default: plan.csv)")
    parser.add_argument("--seed", type=int, default=None,
                        help="Random seed, for repeatable output")
    args = parser.parse_args(argv)

    if args.days < 1:
        print("--days must be at least 1", file=sys.stderr)
        return 2

    if args.start:
        try:
            start = date.fromisoformat(args.start)
        except ValueError:
            print("--start must be a date in YYYY-MM-DD format", file=sys.stderr)
            return 2
    else:
        start = date.today()

    rng = random.Random(args.seed)
    rows = build_plan(args.niche, args.days, start, rng)
    write_csv(rows, args.out)
    print_plan(rows)
    print("Plan saved to {}".format(args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())

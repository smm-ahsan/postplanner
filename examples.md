# Examples

Real output from PostPlanner, captured from an actual run.

## Bakery, one week starting Monday 16 November 2026

Command:

```bash
python3 postplanner.py --niche bakery --days 7 --start 2026-11-16 --seed 5 --out example-plan.csv
```

Printed output:

```
2026-11-16 (Monday) - Educate
  Idea:   Explain why sourdough needs a long, slow fermentation
  Format: Reel at 18:00

2026-11-17 (Tuesday) - Behind the scenes
  Idea:   Film the ovens being loaded at 5 AM
  Format: Photo at 19:30

2026-11-18 (Wednesday) - Offer
  Idea:   Announce a buy-two-get-one deal on weekend loaves
  Format: Story at 12:15

2026-11-19 (Thursday) - Social proof
  Idea:   Share a photo a customer posted of their birthday cake
  Format: Carousel at 07:30

2026-11-20 (Friday) - Engage
  Idea:   Poll followers: croissant or pain au chocolat?
  Format: Reel at 20:45

2026-11-21 (Saturday) - Product spotlight
  Idea:   Spotlight the new seasonal pastry with a cross-section shot
  Format: Photo at 18:00

2026-11-22 (Sunday) - Story
  Idea:   Tell the story behind the recipe that started the bakery
  Format: Story at 19:30

Plan saved to example-plan.csv
```

The CSV file written by the same run (`example-plan.csv`):

```csv
date,day,pillar,idea,format,best_time
2026-11-16,Monday,Educate,"Explain why sourdough needs a long, slow fermentation",Reel,18:00
2026-11-17,Tuesday,Behind the scenes,Film the ovens being loaded at 5 AM,Photo,19:30
2026-11-18,Wednesday,Offer,Announce a buy-two-get-one deal on weekend loaves,Story,12:15
2026-11-19,Thursday,Social proof,Share a photo a customer posted of their birthday cake,Carousel,07:30
2026-11-20,Friday,Engage,Poll followers: croissant or pain au chocolat?,Reel,20:45
2026-11-21,Saturday,Product spotlight,Spotlight the new seasonal pastry with a cross-section shot,Photo,18:00
2026-11-22,Sunday,Story,Tell the story behind the recipe that started the bakery,Story,19:30
```

import csv
from collections import defaultdict
from datetime import datetime

# File paths
INPUT_FILE = 'ff_calendar_thisweek.csv'
OUTPUT_FILE = 'ff_usd_calender.csv'


def filter_high_impact_usd_events():
    """
    Filter forex factory calendar for high-impact USD events.
    Creates a cleaned CSV with only the relevant events.
    """
    with open(INPUT_FILE, newline="") as infile, \
            open(OUTPUT_FILE, 'w', newline="") as outfile:

        reader = csv.DictReader(infile)
        fieldnames = ['Date', 'Time', 'Title', 'Country', 'Impact']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        event_count = 0
        for row in reader:
            if row['Country'] == 'USD' and row['Impact'] == 'High':
                writer.writerow({
                    'Date': row['Date'],
                    'Time': row['Time'],
                    'Title': row['Title'],
                    'Country': row['Country'],
                    'Impact': row['Impact']
                })
                event_count += 1

        print(f"✓ Created {OUTPUT_FILE}")
        print(f"✓ Found {event_count} high-impact USD events\n")


def analyze_usd_events():
    """
    Analyze the filtered USD events and provide useful insights.
    """
    events_by_date = defaultdict(list)
    all_events = []

    with open(OUTPUT_FILE, 'r', newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            all_events.append(row)
            events_by_date[row['Date']].append(row)

    # Print analysis
    print("=" * 70)
    print("HIGH-IMPACT USD ECONOMIC EVENTS ANALYSIS")
    print("=" * 70)

    print(f"\nTotal Events: {len(all_events)}")
    print(f"Days with Events: {len(events_by_date)}")

    print("\n" + "-" * 70)
    print("EVENTS BY DATE")
    print("-" * 70)

    for date in sorted(events_by_date.keys()):
        events = events_by_date[date]
        print(f"\n📅 {date} ({len(events)} event{'s' if len(events) > 1 else ''})")

        for event in events:
            print(f"   • {event['Time']:8} | {event['Title']}")

    print("\n" + "=" * 70)


def get_events_for_date(target_date):
    """
    Get all high-impact USD events for a specific date.

    Args:
        target_date: Date string in format 'MM-DD-YYYY'
    """
    events = []

    with open(OUTPUT_FILE, 'r', newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row['Date'] == target_date:
                events.append(row)

    if events:
        print(f"\nEvents for {target_date}:")
        for event in events:
            print(f"  {event['Time']} - {event['Title']}")
    else:
        print(f"\nNo high-impact USD events found for {target_date}")

    return events


def main():
    """Main execution function"""
    # Step 1: Filter and create the USD calendar
    filter_high_impact_usd_events()

    # Step 2: Analyze the filtered data
    analyze_usd_events()

    # Example: Get events for a specific date
    # Uncomment to use:
    # get_events_for_date('02-11-2026')


if __name__ == "__main__":
    main()
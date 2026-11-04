"""Vehicle Service Management System."""

import hashlib
import json
import shutil
from datetime import date

SERVICE_RATES = {
    "Oil Change": 1500,
    "Wheel Alignment": 800,
    "General": 2500,
    "Brake Check": 1200,
}

SERVICE_RECORDS = {}


def add_service(vehicle_no, service_type="General", history=None):
    """Add a service record for a vehicle and update its history."""
    if history is None:
        history = []

    cost = SERVICE_RATES.get(service_type, 0)
    entry = {
        "type": service_type,
        "cost": cost,
        "date": str(date.today()),
    }

    SERVICE_RECORDS.setdefault(vehicle_no, []).append(entry)
    history.append(vehicle_no)
    return history


def cancel_service(vehicle_no, service_type):
    """Cancel a particular service for a vehicle."""
    try:
        jobs = SERVICE_RECORDS[vehicle_no]
    except KeyError:
        print("No records for", vehicle_no)
        return False

    remaining = [
        job for job in jobs if job["type"] != service_type
    ]

    SERVICE_RECORDS[vehicle_no] = remaining
    return len(remaining) < len(jobs)


def get_total_cost(vehicle_no):
    """Calculate the total service cost for a vehicle."""
    total_cost = 0

    for job in SERVICE_RECORDS.get(vehicle_no, []):
        total_cost += job["cost"]

    return total_cost


def job_card_id(vehicle_no):
    """Generate a secure SHA-256-based job card ID."""
    return hashlib.sha256(
        vehicle_no.encode("utf-8")
    ).hexdigest()[:8]


def busiest_vehicle():
    """Find the vehicle with the highest number of service jobs."""
    best = None

    for vehicle, jobs in SERVICE_RECORDS.items():
        if best is None or len(jobs) > len(SERVICE_RECORDS[best]):
            best = vehicle

    return best


def save_records(file_name="services.json"):
    """Save service records to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(SERVICE_RECORDS, file, indent=2)


def load_records(file_name="services.json"):
    """Load service records from a JSON file."""
    with open(file_name, encoding="utf-8") as file:
        return json.load(file)


def backup_records(folder):
    """Copy the service records file to the specified folder."""
    shutil.copy2("services.json", folder)


def main():
    """Run the vehicle service management demonstration."""
    add_service("KA01AB1234", "Oil Change")
    add_service("KA01AB1234", "Wheel Alignment")
    add_service("KA05XY9876")
    add_service("KA03MN4455", "Brake Check")

    cancel_service("KA05XY9876", "Brake Check")
    cancel_service("KA09ZZ0001", "General")
    cancel_service("KA03MN4455", "Brake Check")

    print(
        "Total for KA01AB1234:",
        get_total_cost("KA01AB1234"),
    )
    print(
        "Total for KA05XY9876:",
        get_total_cost("KA05XY9876"),
    )
    print(
        "Job card for KA01AB1234:",
        job_card_id("KA01AB1234"),
    )

    save_records()
    loaded = load_records()

    print(
        "Vehicles on file:",
        len(loaded),
        "| busiest vehicle:",
        busiest_vehicle(),
    )


if __name__ == "__main__":
    main()

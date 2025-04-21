def main():
    push_ups = {
        "exercise": "Push-ups",
        "sets": 4,
        "reps": 30,
        "notes": "Keep your back straight, hands shoulder-width apart."
    }
    
    print(push_ups["exercise"])
    print(push_ups["sets"])
    print(push_ups["reps"])
    print(push_ups["notes"])

    push_ups["sets"] = 5

    notes_value = "Keep your back straight, hands shoulder-width apart."
    del push_ups["notes"]
    push_ups["workout_notes"] = notes_value
    print(push_ups)

    workout_plan = {
        "Push-ups": {
            "sets": 3,
            "reps": 15,
            "notes": "Keep your back straight, hands shoulder-width apart."
        },
        "Squats": {
            "sets": 4,
            "reps": 12,
            "notes": "Go as low as you can while maintaining proper form."
        },
        "Plank": {
            "sets": 3,
            "reps": "Hold for 60 seconds",
            "notes": "Engage your core and keep your body in a straight line."
        },
        "Lunges": {
            "sets": 3,
            "reps": 10,
            "notes": "Each leg. Step forward and lower your body until your front knee is at a 90-degree angle."
        },
        "Bicep Curls": {
            "sets": 3,
            "reps": 12,
            "notes": "Use dumbbells, keep your elbows close to your body."
        }
    }

    print(workout_plan["Lunges"]["notes"])

    for key, value in push_ups.items():
        print(f"{key.upper()}: {value}")
# ensures that the main() function is only executed when the file is run directly
if __name__ == "__main__":
    main()
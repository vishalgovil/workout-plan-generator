from workout import generate_workout_plan

prompt = generate_workout_plan(
    goal="Build muscle",
    experience="Beginner",
    days=3,
    equipment="Home dumbbells",
    limitations="Avoid overhead pressing",
)

print(prompt)
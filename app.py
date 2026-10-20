from workout import generate_workout_plan
import streamlit as st


st.title('Workout Generator')
st.write("create a workout plan for your body")

goal = st.selectbox("Fitness goal",["Build Muscle","Lose fat","Endurance","General fitness"])

experience = st.selectbox("Experience level",["Beginner","Intermediate","Advanced"])

days= st.slider("Number of days per week",min_value=1,max_value=7,value=3)

equipment = st.selectbox("Equipment access",["No equipment","Home dumbbells","Full gym"])

limitations =  st.text_area("Injuries or limitations",placeholder="For example: recent knee surgery")

if st.button("Generate workout plan"):
    try:
        with st.spinner('Generating workout plan...'):
            plan = generate_workout_plan(goal,experience,days,equipment,limitations or "None")
        st.subheader("Your Personalized Workout Plan")
        st.markdown(plan)

        st.download_button(
            label="Download Workout Plan",
            data=plan,
            file_name="workout_plan.md",
            mime="text/markdown"
        )

    except (ValueError,RuntimeError) as e:
        st.error(str(e))


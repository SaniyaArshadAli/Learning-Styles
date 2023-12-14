import streamlit as st
import plotly.graph_objects as go
import webbrowser
def vark_test():
    st.title("Know Your Unique Learning Style with VARK Test")

    # Updated Questions and Options
    # Updated Questions and Options
    questions = [
        "You are helping someone who wants to go to your airport, the center of town, or railway station. You would:",
        "A website has a video showing how to make a special graph. There is a person speaking, some lists and words describing what to do, and some diagrams. You would learn most from:",
        "You are planning a vacation for a group. You want some feedback from them about the plan. You would:",
        "You are going to cook something as a special treat. You would:",
        "A group of tourists want to learn about the parks or wildlife reserves in your area. You would:",
        "You are about to purchase a digital camera or mobile phone. Other than price, what would most influence your decision?",
        "Remember a time when you learned how to do something new. Avoid choosing a physical skill, e.g. riding a bike. You learned best by:",
        "You have a problem with your heart. You would prefer that the doctor:",
        "You want to learn a new program, skill or game on a computer. You would:",
        "I like websites that have:",
        "Other than price, what would most influence your decision to buy a new non-fiction book?",
        "You are using a book, CD or website to learn how to take photos with your new digital camera. You would like to have:",
        "Do you prefer a teacher or a presenter who uses:",
        "You have finished a competition or test and would like some feedback. You would like to have feedback:",
        "You are going to choose food at a restaurant or cafe. You would:",
        "You have to make an important speech at a conference or special occasion. You would:"
]


    options = [
        ["a. Go with her.", "b. Tell her the directions.", "c. Write down the directions.", "d. Draw, or show her a map, or give her a map."],
        ["a. Seeing the diagrams.", "b. Listening.", "c. Reading the words.", "d. Watching the actions."],
        ["a. Describe some of the highlights they will experience.", "b. Use a map to show them the places.", "c. Give them a copy of the printed itinerary.", "d. Phone, text, or email them."],
        ["a. Cook something you know without the need for instructions.", "b. Ask friends for suggestions.", "c. Look on the Internet or in some cookbooks for ideas from the pictures.", "d. Use a good recipe."],
        ["a. Talk about, or arrange a talk for them about parks or wildlife reserves.", "b. Show them maps and internet pictures.", "c. Take them to a park or wildlife reserve and walk with them.", "d. Give them a book or pamphlets about the parks or wildlife reserves."],
        ["a. Trying or testing it.", "b. Reading the details or checking its features online.", "c. It is a modern design and looks good.", "d. The salesperson telling me about its features."],
        ["a. watching a demonstration.", "b. listening to somebody explaining it and asking questions.", "c. diagrams, maps, and charts - visual clues.", "d. written instructions – e.g. a manual or book."],
        ["a. gave you something to read to explain what was wrong.", "b. used a plastic model to show what was wrong.", "c. described what was wrong.", "d. showed you a diagram of what was wrong."],
        ["a. read the written instructions that came with the program.", "b. talk with people who know about the program.", "c. use the controls or keyboard.", "d. follow the diagrams in the book that came with it."],
        ["a. things I can click on, shift or try.", "b. interesting design and visual features.", "c. interesting written descriptions, lists and explanations.", "d. audio channels where I can hear music, radio programs or interviews."],
        ["a. The way it looks is appealing.", "b. Quickly reading parts of it.", "c. A friend talks about it and recommends it.", "d. It has real-life stories, experiences and examples."],
        ["a. a chance to ask questions and talk about the camera and its features.", "b. clear written instructions with lists and bullet points about what to do.", "c. diagrams showing the camera and what each part does.", "d. many examples of good and poor photos and how to improve them."],
        ["a. demonstrations, models or practical sessions.", "b. question and answer, talk, group discussion, or guest speakers.", "c. handouts, books, or readings.", "d. diagrams, charts or graphs."],
        ["a. using examples from what you have done.", "b. using a written description of your results.", "c. from somebody who talks it through with you.", "d. using graphs showing what you had achieved."],
        ["a. choose something that you have had there before.", "b. listen to the waiter or ask friends to recommend choices.", "c. choose from the descriptions in the menu.", "d. look at what others are eating or look at pictures of each dish."],
        ["a. make diagrams or get graphs to help explain things.", "b. write a few key words and practice saying your speech over and over.", "c. write out your speech and learn from reading it over several times.", "d. gather many examples and stories to make the talk real and practical."]
    ]


    # Updated Scoring Chart for Questions 1 to 6
    scoring_chart = {
    "1": {"a": "Kinesthetic", "b": "Auditory", "c": "Reading", "d": "Visual"},
    "2": {"a": "Visual", "b": "Auditory", "c": "Reading", "d": "Kinesthetic"},
    "3": {"a": "Kinesthetic", "b": "Visual", "c": "Reading", "d": "Auditory"},
    "4": {"a": "Kinesthetic", "b": "Auditory", "c": "Visual", "d": "Reading"},
    "5": {"a": "Auditory", "b": "Visual", "c": "Kinesthetic", "d": "Reading"},
    "6": {"a": "Kinesthetic", "b": "Reading", "c": "Visual", "d": "Auditory"},
    "7": {"a": "Kinesthetic", "b": "Auditory", "c": "Visual", "d": "Reading"},
    "8": {"a": "Reading", "b": "Kinesthetic", "c": "Auditory", "d": "Visual"},
    "9": {"a": "Reading", "b": "Auditory", "c": "Kinesthetic", "d": "Visual"},
    "10": {"a": "Kinesthetic", "b": "Visual", "c": "Reading", "d": "Auditory"},
    "11": {"a": "Visual", "b": "Reading", "c": "Auditory", "d": "Kinesthetic"},
    "12": {"a": "Auditory", "b": "Reading", "c": "Visual", "d": "Kinesthetic"},
    "13": {"a": "Kinesthetic", "b": "Auditory", "c": "Reading", "d": "Visual"},
    "14": {"a": "Kinesthetic", "b": "Reading", "c": "Auditory", "d": "Visual"},
    "15": {"a": "Kinesthetic", "b": "Auditory", "c": "Reading", "d": "Visual"},
    "16": {"a": "Visual", "b": "Auditory", "c": "Reading", "d": "Kinesthetic"}
}


    # User Responses
    responses = []

    # Display Questions and Get User Responses
    for i in range(len(questions)):
        st.markdown(f"**{i + 1}. {questions[i]}**")
        selected_option = st.radio(f"Select the most appropriate option for Question {i + 1}:", options[i])
        responses.append(selected_option.split(".")[0].strip().lower())

    # Calculate Results
    scores = calculate_result(responses, scoring_chart)

    # top_two_styles = list(scores.keys())[:1]
    # print(top_two_styles)
    sorted_styles = sorted(scores.items(), key=lambda x: x[1], reverse=True)

# Extract the top two styles
    top_two_styles = [style[0] for style in sorted_styles[:2]]

    print(top_two_styles)
    st.success(f"Your top two VARK learning styles are: **{top_two_styles[0]}** and **{top_two_styles[1]}**")

    # Display Common Pie Chart for All Learning Styles
    # st.info("Learning Style Scores:")
    plot_common_pie_chart(scores, len(responses))
    if st.button("Continue"):
        # st.markdown("[Click here to continue](https://www.example.com)")
        webbrowser.open_new_tab("https://mubeen161.github.io/Assessment/capacity.html")

def calculate_result(responses, scoring_chart):
    scores = {"Auditory": 0, "Visual": 0, "Reading": 0, "Kinesthetic": 0}
    for i, response in enumerate(responses):
        question_number = str(i + 1)
        scores[scoring_chart[question_number][response]] += 1
        print(scores)
    return scores

def plot_common_pie_chart(scores, total_responses):
    labels = list(scores.keys())
    values = [scores[style] / total_responses * 100 for style in labels]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='percent+label')])
    fig.update_layout(showlegend=True, title="Common Learning Style Scores")
    st.plotly_chart(fig)

if __name__ == "__main__":
    vark_test()

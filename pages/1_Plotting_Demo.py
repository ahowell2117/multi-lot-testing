import streamlit as st

import pandas as pd
import streamlit as st
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    #read xls or xlsx
   df=pd.read_excel(uploaded_file)
   st.write("Filename: ", uploaded_file.name)
else:
    st.warning("you need to upload a csv or excel file")

st.write(df)

st.write(df.at[0,'Lot ID'])
st.write(df.at[1,'Lot ID'])
st.write(df.at[2,'Lot ID'])

st.write(df.at[0,'Bobbin ID'])
st.write(df.at[1,'Bobbin ID'])
st.write(df.at[2,'Bobbin ID'])

st.write(df.at[0,'Length (m)'])
st.write(df.at[1,'Length (m)'])
st.write(df.at[2,'Length (m)'])


def tie_fiber(bobbins):
    # Sort bobbins by length in descending order
    bobbins = sorted(bobbins, key=lambda x: x[2], reverse=True)
    
    max_length = 0
    optimal_sequence = []
    min_knots_in_optimal = float('inf')
    unused_bobbins = {}
    trimmed_bobbins = {}

    def helper(curr_length, bobbins_left, knots_used, sequence, used_bobbins, local_trimmed_bobbins={}, used_lots=set()):
        nonlocal max_length, optimal_sequence, min_knots_in_optimal, unused_bobbins, trimmed_bobbins

        if knots_used > min_knots_in_optimal or len(used_lots) > 4:
            return

        if curr_length >= 475:
            if curr_length <= 525:
                if knots_used < min_knots_in_optimal:
                    max_length = curr_length
                    optimal_sequence = sequence[:]
                    min_knots_in_optimal = knots_used

                    # Improved handling of unused and trimmed bobbins
                    for bobbin in bobbins:
                        if bobbin[1] not in used_bobbins:
                            unused_bobbins[bobbin[1]] = (bobbin[0], bobbin[2])
                        elif bobbin[1] in local_trimmed_bobbins:
                            trimmed_length = local_trimmed_bobbins[bobbin[1]][1]  # Access the correct tuple element for trimmed length
                            if trimmed_length > 0:
                                unused_bobbins[bobbin[1]] = (bobbin[0], trimmed_length)

                    trimmed_bobbins = local_trimmed_bobbins.copy()
            return

        for i, bobbin in enumerate(bobbins_left):
            if bobbin[2] < 20 or bobbin[1] in used_bobbins:
                continue

            new_length = curr_length + bobbin[2]
            new_used_bobbins = used_bobbins | {bobbin[1]}
            new_used_lots = used_lots | {bobbin[0]}

            if new_length <= 525:
                new_sequence = sequence + [(bobbin[0], bobbin[1], bobbin[2])]
                helper(new_length, bobbins_left[i + 1:], knots_used + 1, new_sequence, new_used_bobbins, local_trimmed_bobbins, new_used_lots)

            # Improved trimming check
            if curr_length < 475 and bobbin[2] + curr_length > 525:
                trimmed_amount = 525 - curr_length
                if trimmed_amount <= bobbin[2]:  # Ensure the bobbin is long enough for trimming
                    new_sequence = sequence + [(bobbin[0], bobbin[1], trimmed_amount)]
                    new_trimmed_bobbins = local_trimmed_bobbins.copy()
                    new_trimmed_bobbins[bobbin[1]] = (bobbin[0], bobbin[2] - trimmed_amount)
                    helper(525, bobbins_left[i + 1:], knots_used + 1, new_sequence, new_used_bobbins, new_trimmed_bobbins, new_used_lots)

    helper(0, bobbins, 0, [], set(), {}, set())

    unused_bobbins_list = [(v[0], k, v[1]) for k, v in unused_bobbins.items() if v[1] > 0]
    trimmed_bobbins_info = [(v[0], k, v[1]) for k, v in trimmed_bobbins.items()]  # Corrected format for trimmed bobbins

    return max_length, optimal_sequence, min_knots_in_optimal, unused_bobbins_list, trimmed_bobbins_info

def generate_sequence(unused_bobbins):
    max_length, sequence, knots, unused, trimmed = tie_fiber(unused_bobbins)
    return max_length, sequence, knots, unused, trimmed

# Example usage with new bobbin format
#bobbins_lengths = [("Lot 1", "A1", 500)]
bobbins_lengths = [(df.at[0,'Lot ID'], df.at[0,'Bobbin ID'], df.at[0,'Length (m)']), (df.at[1,'Lot ID'], df.at[1,'Bobbin ID'], df.at[1,'Length (m)']), (df.at[2,'Lot ID'], df.at[2,'Bobbin ID'], df.at[2,'Length (m)'])]

original_sum = sum(bobbin[2] for bobbin in bobbins_lengths)  # Calculate the sum of original lengths
total_max_length = 0  # Initialize total maximum length

max_possible_length, sequence, knots, unused, trimmed = tie_fiber(bobbins_lengths)
if max_possible_length == 0:
    st.write("# First Sequence:")
    st.write("No combinations of bobbins can give the target range of 475 - 525 meters.")
else:
    st.write(" # Sequence 1:")
    st.write(f"The longest possible length with a maximum of 4 knots between 475 and 525 meters is: {max_possible_length}")
    st.write(f"The trimmed bobbins and their trimmed amounts (Lot ID, Line ID, Amount to trim from original length): {trimmed}")
    st.write(f"The sequence of lengths being tied together (Lot ID, Line ID, Length): {sequence}")
    st.write(f"The number of knots in the final bobbin: {knots - 1}")
    st.write(f"The unused bobbins with their remaining lengths (Lot ID, Line ID, Length): {unused}")

    total_max_length += max_possible_length  # Update total maximum length
    unused_bobbins = [bobbin for bobbin in unused if bobbin[2] > 0]

    for i in range(1, 4):
        st.write(f"# Sequence {i+1}:")
        max_length, seq, knots, unused, trimmed = generate_sequence(unused_bobbins)
        if max_length == 0:
            st.write(f"No combinations of unused bobbins can give the target range of 475 - 525 meters.")
        else:
            st.write(f"The longest possible length with a maximum of 4 knots between 475 and 525 meters is: {max_length}")
            st.write(f"The trimmed bobbins and their trimmed amounts (Lot ID, Line ID, Amount to trim from original length): {trimmed}")
            st.write(f"The sequence of lengths being tied together (Lot ID, Line ID, Length): {seq}")
            st.write(f"The number of knots in the final bobbin: {knots - 1}")
            st.write(f"The unused bobbins with their remaining lengths (Lot ID, Line ID, Length): {unused}")

            total_max_length += max_length  # Update total maximum length
            unused_bobbins = [bobbin for bobbin in unused if bobbin[2] > 0]

# After all sequences, calculate and print the final summaries
sum_of_unused_lengths = sum(bobbin[2] for bobbin in unused_bobbins)  # Calculate sum of lengths left in unused bobbins
scrapped_length = original_sum - sum_of_unused_lengths  # Calculate total scrapped length
percent_recovered = (scrapped_length / original_sum) * 100  # Calculate percent recovered
st.write("# Summary Information")
st.write(f"\nTotal Sum of Original Lengths: {original_sum}")
st.write(f"Total Maximum Length from All Sequences: {total_max_length}")
st.write(f"Sum of Lengths Left in Unused Bobbin List: {sum_of_unused_lengths}")
st.write(f"Percent of Recovered Length: {percent_recovered:.2f}%")
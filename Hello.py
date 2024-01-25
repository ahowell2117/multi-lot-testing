# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st

###################################################################################################################
st.write("# BOBBIN LENGTH INPUTS:")

col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

with col1:
   st.header("A")
   A1_length = st.number_input('A1',step=1, min_value=0)
   A2_length = st.number_input('A2',step=1, min_value=0)
   A3_length = st.number_input('* A3',step=1, min_value=0)
   A4_length = st.number_input('* A4',step=1, min_value=0)
   A5_length = st.number_input('* A5',step=1, min_value=0)
   A6_length = st.number_input('* A6',step=1, min_value=0)
   A7_length = st.number_input('* A7',step=1, min_value=0)
   A8_length = st.number_input('* A8',step=1, min_value=0)
   A9_length = st.number_input('* A9',step=1, min_value=0)
   A10_length = st.number_input('* A10',step=1, min_value=0)

with col2:
   st.header("B")
   B1_Length = st.number_input('* B1',step=1, min_value=0)
   B2_length = st.number_input('* B2',step=1, min_value=0)
   B3_length = st.number_input('* B3',step=1, min_value=0)
   B4_length = st.number_input('* B4',step=1, min_value=0)
   B5_length = st.number_input('* B5',step=1, min_value=0)
   B6_length = st.number_input('* B6',step=1, min_value=0)
   B7_length = st.number_input('* B7',step=1, min_value=0)
   B8_length = st.number_input('* B8',step=1, min_value=0)
   B9_length = st.number_input('* B9',step=1, min_value=0)
   B10_length = st.number_input('* B10',step=1, min_value=0)

with col3:
   st.header("C")
   C1_Length = st.number_input('* C1',step=1, min_value=0)
   C2_length = st.number_input('* C2',step=1, min_value=0)
   C3_length = st.number_input('* C3',step=1, min_value=0)
   C4_length = st.number_input('* C4',step=1, min_value=0)
   C5_length = st.number_input('* C5',step=1, min_value=0)
   C6_length = st.number_input('* C6',step=1, min_value=0)
   C7_length = st.number_input('* C7',step=1, min_value=0)
   C8_length = st.number_input('* C8',step=1, min_value=0)
   C9_length = st.number_input('* C9',step=1, min_value=0)
   C10_length = st.number_input('* C10',step=1, min_value=0)

with col4:
   st.header("D")
   D1_Length = st.number_input('* D1',step=1, min_value=0)
   D2_length = st.number_input('* D2',step=1, min_value=0)
   D3_length = st.number_input('* D3',step=1, min_value=0)
   D4_length = st.number_input('* D4',step=1, min_value=0)
   D5_length = st.number_input('* D5',step=1, min_value=0)
   D6_length = st.number_input('* D6',step=1, min_value=0)
   D7_length = st.number_input('* D7',step=1, min_value=0)
   D8_length = st.number_input('* D8',step=1, min_value=0)
   D9_length = st.number_input('* D9',step=1, min_value=0)
   D10_length = st.number_input('* D10',step=1, min_value=0)
  
with col5:
   st.header("E")
   E1_Length = st.number_input('* E1',step=1, min_value=0)
   E2_length = st.number_input('* E2',step=1, min_value=0)
   E3_length = st.number_input('* E3',step=1, min_value=0)
   E4_length = st.number_input('* E4',step=1, min_value=0)
   E5_length = st.number_input('* E5',step=1, min_value=0)
   E6_length = st.number_input('* E6',step=1, min_value=0)
   E7_length = st.number_input('* E7',step=1, min_value=0)
   E8_length = st.number_input('* E8',step=1, min_value=0)
   E9_length = st.number_input('* E9',step=1, min_value=0)
   E10_length = st.number_input('* E10',step=1, min_value=0)

with col6:
   st.header("F")
   F1_Length = st.number_input('* F1',step=1, min_value=0)
   F2_length = st.number_input('* F2',step=1, min_value=0)
   F3_length = st.number_input('* F3',step=1, min_value=0)
   F4_length = st.number_input('* F4',step=1, min_value=0)
   F5_length = st.number_input('* F5',step=1, min_value=0)
   F6_length = st.number_input('* F6',step=1, min_value=0)
   F7_length = st.number_input('* F7',step=1, min_value=0)
   F8_length = st.number_input('* F8',step=1, min_value=0)
   F9_length = st.number_input('* F9',step=1, min_value=0)
   F10_length = st.number_input('* F10',step=1, min_value=0)

with col7:
   st.header("G")
   G1_Length = st.number_input('* G1',step=1, min_value=0)
   G2_length = st.number_input('* G2',step=1, min_value=0)
   G3_length = st.number_input('* G3',step=1, min_value=0)
   G4_length = st.number_input('* G4',step=1, min_value=0)
   G5_length = st.number_input('* G5',step=1, min_value=0)
   G6_length = st.number_input('* G6',step=1, min_value=0)
   G7_length = st.number_input('* G7',step=1, min_value=0)
   G8_length = st.number_input('* G8',step=1, min_value=0)
   G9_length = st.number_input('* G9',step=1, min_value=0)
   G10_length = st.number_input('* G10',step=1, min_value=0)

with col8:
   st.header("H")
   H1_Length = st.number_input('* H1',step=1, min_value=0)
   H2_length = st.number_input('* H2',step=1, min_value=0)
   H3_length = st.number_input('* H3',step=1, min_value=0)
   H4_length = st.number_input('* H4',step=1, min_value=0)
   H5_length = st.number_input('* H5',step=1, min_value=0)
   H6_length = st.number_input('* H6',step=1, min_value=0)
   H7_length = st.number_input('* H7',step=1, min_value=0)
   H8_length = st.number_input('* H8',step=1, min_value=0)
   H9_length = st.number_input('* H9',step=1, min_value=0)
   H10_length = st.number_input('* H10',step=1, min_value=0)




###Code to be run
def tie_fiber(bobbins):
    # Sort bobbins by length in descending order
    bobbins = sorted(bobbins, key=lambda x: x[1], reverse=True)
    
    max_length = 0
    optimal_sequence = []
    min_knots_in_optimal = float('inf')
    unused_bobbins = {}
    trimmed_bobbins = {}

    def helper(curr_length, bobbins_left, knots_used, sequence, used_bobbins, local_trimmed_bobbins={}):
        nonlocal max_length, optimal_sequence, min_knots_in_optimal, unused_bobbins, trimmed_bobbins

        if knots_used > min_knots_in_optimal:
            return

        if curr_length >= 475:
            if curr_length <= 525:
                if knots_used < min_knots_in_optimal:
                    max_length = curr_length
                    optimal_sequence = sequence[:]
                    min_knots_in_optimal = knots_used
                    unused_bobbins = {bobbin[0]: bobbin[1] for bobbin in bobbins if bobbin[0] not in used_bobbins}
                    for bobbin, (rem_len, _) in local_trimmed_bobbins.items():
                        unused_bobbins[bobbin] = rem_len
                    trimmed_bobbins = local_trimmed_bobbins.copy()
            return

        for i, bobbin in enumerate(bobbins_left):
            if bobbin[1] < 20 or bobbin[0] in used_bobbins:
                continue

            new_length = curr_length + bobbin[1]
            new_used_bobbins = used_bobbins | {bobbin[0]}
            
            if new_length <= 525:
                new_sequence = sequence + [(bobbin[0], bobbin[1])]
                helper(new_length, bobbins_left[i + 1:], knots_used + 1, new_sequence, new_used_bobbins, local_trimmed_bobbins)

            # Improved trimming check
            if curr_length < 475 and bobbin[1] + curr_length > 525:
                trimmed_amount = 525 - curr_length
                if trimmed_amount <= bobbin[1]:  # Ensure the bobbin is long enough for trimming
                    new_sequence = sequence + [(bobbin[0], trimmed_amount)]
                    new_trimmed_bobbins = local_trimmed_bobbins.copy()
                    new_trimmed_bobbins[bobbin[0]] = (bobbin[1] - trimmed_amount, trimmed_amount)
                    helper(525, bobbins_left[i + 1:], knots_used + 1, new_sequence, new_used_bobbins, new_trimmed_bobbins)

    helper(0, bobbins, 0, [], set())

    unused_bobbins_list = [(k, v) for k, v in unused_bobbins.items() if v > 0]
    trimmed_bobbins_info = [(k, v[1]) for k, v in trimmed_bobbins.items() if v[1] > 0]

    return max_length, optimal_sequence, min_knots_in_optimal, unused_bobbins_list, trimmed_bobbins_info

def generate_sequence(unused_bobbins):
    max_length, sequence, knots, unused, trimmed = tie_fiber(unused_bobbins)
    return max_length, sequence, knots, unused, trimmed

# Example usage
bobbins_lengths = [("A1", A1_length), ("A2", A2_length), ("A3", A3_length), ("A4", A4_length), ("A5", A5_length), ("A6", A6_length), ("A7", A7_length), ("A8", A8_length), ("A9",A9_length),("A10",A10_length), 
                   ("B1",B1_Length), ("B2",B2_length), ("B3", B3_length), ("B4", B4_length), ("B5", B5_length), ("B6", B6_length), ("B7", B7_length), ("B8", B8_length), ("B9",B9_length),("B10",B10_length),
                   ("C1",C1_Length), ("C2",C2_length), ("C3", C3_length), ("C4", C4_length), ("C5", C5_length), ("C6", C6_length), ("C7", C7_length), ("C8", C8_length), ("C9",C9_length),("C10",C10_length),
                   ("D1",D1_Length), ("D2",D2_length), ("D3", D3_length), ("D4", D4_length), ("D5", D5_length), ("D6", D6_length), ("D7", D7_length), ("D8", D8_length), ("D9",D9_length),("D10",D10_length),
                   ("E1",E1_Length), ("E2",E2_length), ("E3", E3_length), ("E4", E4_length), ("E5", E5_length), ("E6", E6_length), ("E7", E7_length), ("E8", E8_length), ("E9",E9_length),("E10",E10_length),
                   ("F1",F1_Length), ("F2",F2_length), ("F3", F3_length), ("F4", F4_length), ("F5", F5_length), ("F6", F6_length), ("F7", F7_length), ("F8", F8_length), ("F9",F9_length),("F10",F10_length),
                   ("G1",G1_Length), ("G2",G2_length), ("G3", G3_length), ("G4", G4_length), ("G5", G5_length), ("G6", G6_length), ("G7", G7_length), ("G8", G8_length), ("G9",G9_length),("G10",G10_length),
                   ("H1",H1_Length), ("H2",H2_length), ("H3", H3_length), ("H4", H4_length), ("H5", H5_length), ("H6", H6_length), ("H7", H7_length), ("H8", H8_length), ("H9",H9_length),("H10",H10_length),]

original_sum = sum(bobbin[1] for bobbin in bobbins_lengths)  # Calculate the sum of original lengths
total_max_length = 0  # Initialize total maximum length

st.write("# PRODUCT BOBBIN MAKEUPS:")

max_possible_length, sequence, knots, unused, trimmed = tie_fiber(bobbins_lengths)
if max_possible_length == 0:
    st.write("\nProduct Bobbin #1")
    st.write("No combinations of bobbins can give the target range of 475 - 525 meters.")
else:
    st.write("# Product Bobbin #1")
    st.write(f"The longest possible length with a maximum of 4 knots between 475 and 525 meters is: {max_possible_length}")
    st.write(f"The trimmed bobbins and their trimmed amounts (ID, Amount to trim from original length): {trimmed}")
    st.write(f"The sequence of lengths being tied together: {sequence}")
    st.write(f"The number of knots in the final bobbin: {knots - 1}")
    st.write(f"The unused bobbins with their remaining lengths: {unused}")

    total_max_length += max_possible_length  # Update total maximum length
    unused_bobbins = [bobbin for bobbin in unused if bobbin[1] > 0]

    for i in range(1, 4):
        st.write(f"\n # Product Bobbin # {i+1}:")
        max_length, seq, knots, unused, trimmed = generate_sequence(unused_bobbins)
        if max_length == 0:
            st.write(f"No combinations of unused bobbins can give the target range of 475 - 525 meters.")
        else:
            st.write(f"The longest possible length with a maximum of 4 knots between 475 and 525 meters is: {max_length}")
            st.write(f"The trimmed bobbins and their trimmed amounts (ID, Amount to trim from original length): {trimmed}")
            st.write(f"The sequence of lengths being tied together: {seq}")
            st.write(f"The number of knots in the final bobbin: {knots - 1}")
            st.write(f"The unused bobbins with their remaining lengths: {unused}")

            total_max_length += max_length  # Update total maximum length
            unused_bobbins = [bobbin for bobbin in unused if bobbin[1] > 0]

# After all sequences, calculate and print the final summaries
sum_of_unused_lengths = sum(bobbin[1] for bobbin in unused_bobbins)  # Calculate sum of lengths left in unused bobbins
scrapped_length = original_sum - sum_of_unused_lengths  # Calculate total scrapped length
percent_recovered = (scrapped_length / original_sum) * 100  # Calculate percent recovered
st.write("# Summary Information")
st.write(f"\nTotal Sum of Original Lengths: {original_sum}")
st.write(f"Total Maximum Length from All Sequences: {total_max_length}")
st.write(f"Sum of Lengths Left in Unused Bobbin List: {sum_of_unused_lengths}")
st.write(f"Percent of Recovered Length: {percent_recovered:.2f}%")

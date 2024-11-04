import streamlit as st
from pyo import *
import os
import re
from random import uniform

# Initialize the server for pyo
s = Server().boot()

# Function to extract integer values from hex code
def extract_integers_from_hex(hex_code):
    numbers = re.findall(r'\d', hex_code)
    return int(''.join(numbers[:2])) if numbers else 0

# Function to determine the range for mrange
def determine_mrange(a):
    if 0 <= a <= 10:
        return (a, 27)
    elif 11 <= a <= 30:
        return (a, 37)
    elif 31 <= a <= 50:
        return (a, 67)
    elif 51 <= a <= 70:
        return (a, 86)
    elif 71 <= a <= 99:
        return (a, 106)
    else:
        return (a, a + 20)

# Streamlit UI
with st.expander(""):
    color = st.color_picker("Pick A Color for your Day🥳", "#00f900")
    st.write("The current color is", color)

# Extract integer values from the hex code
a = extract_integers_from_hex(color)
st.write("Please click the widget above")

# Determine mrange based on a
mrange = determine_mrange(a)
st.write(f"Using mrange = {mrange}")


# Music generation function
def generate_music(mrange):
    s.start()
    wav = SquareTable()
    b = random.randint(50, 1600) * 5  # 生成一个随机整数，范围从 10 到 8000
    c = random.randint(b // 5 + 1, 1600) * 5  # 生成一个随机整数，范围从 b + 5 到 8000
    d = random.randint(c // 5 + 1, 1600) * 5  # 生成一个随机整数，范围从 c + 5 到 8000
    e = random.randint(d // 5 + 1, 1600) * 5  # 生成一个随机整数，范围从 d + 5 到 8000
    env = CosTable([(0,0), (b,1), (c,0.2),(d,0.4),(e,0.2),(8191,0)])
    a = random.randint(2, 24) // 2 * 2
    met = Metro(.125, a).play()
    amp = TrigEnv(met, table=env, mul=.1)
    x1 = random.randint(7, 121)
    pit = TrigXnoiseMidi(met, dist='loopseg', x1=x1, scale=1, mrange=mrange)
    out = Osc(table=wav, freq=pit, mul=amp).out()
    st.write("Playing music...")
    time.sleep(12)
    s.stop()
    st.write("Finished playing music🙇🏻.")



# Button to generate music
if st.button("Generate Music",icon="😃", type="primary"):
    generate_music(mrange)



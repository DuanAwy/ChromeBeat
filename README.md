# ChromaBeat
SD5913

1.Open the python file with 3.10 Interpreter 

2.Open new terminal, choose the root to assignment3_Duan-main\ChromaBeat,then input:streamlit run .\merge_page.py

3.A streamlit app page will pop up

4.plase click the widget with the ▾

5.Then choose the color you like 

6.click the generate buttom

7.you will listen to what is generating base on the Hex Code of the color

In the given code snippet, mrange is a parameter passed to the TrigXnoiseMidi function. The mrange parameter typically stands for "midi range" and is used to specify the range of MIDI note values that the function can generate.

MIDI (Musical Instrument Digital Interface) is a protocol used to communicate musical information between electronic instruments and computers. In MIDI, notes are represented by numbers ranging from 0 to 127, with 60 typically corresponding to middle C.

The mrange parameter is likely a tuple or list of two values, representing the minimum and maximum MIDI note values that the function can generate. For example, mrange=(48, 72) would limit the generated MIDI notes to the range of C3 (48) to C5 (72).

Here's a breakdown of the possible values for mrange:

mrange=(0, 127): This would allow the function to generate any possible MIDI note value. mrange=(48, 72): This would limit the generated MIDI notes to the range of C3 (48) to C5 (72), which is a common range for many instruments. mrange=(60, 60): This would limit the generated MIDI notes to a single note, middle C (60).

import pandas as pd
import zipfile

# Load CSV
df = pd.read_csv("numba_question_bank.csv")

# Create XML content
xml = """<?xml version="1.0" encoding="UTF-8"?>
<questestinterop>
<assessment title="Numba Quiz">
<section>
"""

for i, row in df.iterrows():
    xml += f"""
    <item title="Question {i+1}">
        <presentation>
            <material>
                <mattext>{row['Question']}</mattext>
            </material>
            <response_lid ident="response1">
                <render_choice>
    """

    for opt in ['A', 'B', 'C', 'D']:
        xml += f"""
        <response_label ident="{opt}">
            <material>
                <mattext>{row[f'Option {opt}']}</mattext>
            </material>
        </response_label>
        """

    xml += f"""
                </render_choice>
            </response_lid>
        </presentation>

        <resprocessing>
            <respcondition continue="No">
                <conditionvar>
                    <varequal respident="response1">{row['Correct Answer']}</varequal>
                </conditionvar>
                <setvar action="Set" varname="SCORE">100</setvar>
            </respcondition>
        </resprocessing>
    </item>
    """

xml += """
</section>
</assessment>
</questestinterop>
"""

# Save XML
with open("quiz.xml", "w", encoding="utf-8") as f:
    f.write(xml)

# Create ZIP
with zipfile.ZipFile("numba_qti.zip", "w") as z:
    z.write("quiz.xml")

print("✅ QTI ZIP file created: numba_qti.zip")
